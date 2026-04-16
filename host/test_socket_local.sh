#!/usr/bin/env bash
set -euo pipefail

# Run both local endpoints in WSL to validate host-client socket flow.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

main_pid=""

if [[ -f "${REPO_ROOT}/.venv/bin/activate" ]]; then
  # Use project virtualenv so numpy and other deps are available.
  # shellcheck disable=SC1091
  source "${REPO_ROOT}/.venv/bin/activate"
fi

cleanup() {
  if [[ -n "${main_pid}" ]] && kill -0 "${main_pid}" 2>/dev/null; then
    kill "${main_pid}" 2>/dev/null || true
    wait "${main_pid}" 2>/dev/null || true
  fi
}

trap cleanup EXIT INT TERM

echo "Starting main.py (server) ..."
python3 "${SCRIPT_DIR}/main.py" &
main_pid=$!
echo "main.py PID: ${main_pid}"

# Give server a moment to bind before client connect attempt.
sleep 1

echo "Starting test_client.py (client) ..."
python3 "${SCRIPT_DIR}/test_client.py"
client_exit=${PIPESTATUS[0]}

# main.py should complete quickly after echo loop; wait to surface exit status.
if kill -0 "${main_pid}" 2>/dev/null; then
  wait "${main_pid}"
fi
main_exit=$?

echo "main.py exit code: ${main_exit}"
echo "test_client.py exit code: ${client_exit}"

if [[ ${main_exit} -ne 0 || ${client_exit} -ne 0 ]]; then
  echo "Socket local test FAILED"
  exit 1
fi

echo "Socket local test EXECUTED"
