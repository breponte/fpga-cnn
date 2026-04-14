# Progress Log

Status: In Progress \
Last Updated: 2026/04/07

## Abstract
FPGA-accelerated CNN on PYNQ-Z2, leveraging HLS and DMA for pipelined streaming. Project aims to demonstrate AI acceleration on embedded hardware.

## Key Concepts
- FPGA development using Vivado HLS for rapid CNN prototyping
- AXI DMA for PS ↔ PL streaming
- SystemVerilog Optimization of Vivado HLS
- RTL design
- Hardware acceleration for AI/ML
- Resource optimization on constrained hardware

## Reflection
TODO

## Journal

### Iteration #1 - 2026/04/07

**Objectives:**
- Setup environment and gather resources
- Planned outline for project
- Organized repository

**Actions Taken:**
- Installed Vivado 2024.2 and HLS environment
- Setup Python 3.12.3 and downloaded CIFAR-10 dataset
- Prepared PYNQ-Z2 reference manual and Linux DMA drivers for review
- Drafted `~/docs/specifications.md` to outline project goals and workflow
- Organized initial file structure for the repository

**Observations / Issues:**
- Environment setup successful
- No issues encountered

**Results / Metrics:**
- N/A (initial setup iteration)

**Next Steps:**
- Review Linux DMA drivers and PYNQ-Z2 documentation
- Architecture documentation of dataflow and DMA
- Python script for streaming CIFAR-10 image data to an echo HLS module
- HLS Metrics for latency, throughput, and resource utilization

### Iteration #2 - 2026/04/09

**Objectives:**
- Review Linux DMA drivers and PYNQ-Z2 documentation, taking notes to understand the architecture
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)
- Python script for streaming CIFAR-10 image data to an echo HLS module
- HLS Metrics for latency, throughput, and resource utilization

**Actions Taken:**
- Python script for socket communication between a host and client. Able to echo 10 messages between each other. Relevant files: `transmit.py`, `main.py`, `test_client.py`.
- Python script for downloading and extracting CIFAR-10 data. Relevant files: `data_loader.py`
- Add virtual environment and requirements.txt; update .gitignore to ignore these directories/files

**Observations / Issues:**
- None

**Results / Metrics:**
- 10 messages able to echo between a host and client socket on a local machine
- Dataset is loaded into `~/data` programmatically

**Next Steps:**
- Finished Python scripts for streaming loaded CIFAR-10 data from a host socket to a client socket, receiving echoed data
- Client Python script performing CNN on received CIFAR-10 data and sending back to host classification tensor, iterating from echoing
- Review Linux DMA drivers and PYNQ-Z2 documentation, taking notes to understand the architecture
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)

### Iteration #2.1 - 2026/04/13

**Objectives:**
- Finished Python scripts for streaming loaded CIFAR-10 data from a host socket to a client socket, receiving echoed data

**Actions Taken:**
- Preprocessed and formatted CIFAR-10 data

**Observations / Issues:**
- Sending raw bytes is chaotic and poor practice
- Image data cannot be streamed as raw bytes through TCP socket, errors on decoding

**Results / Metrics:**
- N/A

**Next Steps:**
- Research industry approach to sending packet data over TCP
- Define and implement image data packet framing and transmission
- Review Linux DMA drivers and PYNQ-Z2 documentation, taking notes to understand the architecture
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)

<!-- ### Iteration #3 - 2026/04/10

**Objectives:**
- Finished Python scripts for streaming loaded CIFAR-10 data from a host socket to a client socket, receiving echoed data
- Client Python script performing CNN on received CIFAR-10 data and sending back to host classification tensor, iterating from echoing
- Review Linux DMA drivers and PYNQ-Z2 documentation, taking notes to understand the architecture
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)

**Actions Taken:** (what you actually did)  
**Observations / Issues:** (bugs, hardware notes, performance metrics)  
**Results / Metrics:**
(measurable results)
**Next Steps:**
- Placeholder HLS module that echoes back CIFAR-10 data from host socket
- HLS Metrics for latency, throughput, and resource utilization -->

<!-- ### Iteration #X - YYYY/MM/DD

**Objectives:** (what you aimed to do)  
**Actions Taken:** (what you actually did)  
**Observations / Issues:** (bugs, hardware notes, performance metrics)  
**Results / Metrics:**
(measurable results)
**Next Steps:** (planned actions for next session) -->