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

## Outstanding Objectives

- [ ] draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)
- [x] ~~Python scripts for streaming loaded CIFAR-10 data from a host socket to a client socket, receiving echoed data~~
- [ ] Client Python script performing CNN on received CIFAR-10 data and sending back to host classification tensor, iterating from echoing
- [ ] Echo HLS module with AXI DMA IP
- [ ] HLS Metrics for latency, throughput, and resource utilization
- [ ] Review Linux DMA drivers, taking notes to understand the architecture
- [ ] Review PYNQ-Z2 documentation, taking notes to understand the architecture


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

### Iteration #2.2 - 2026/04/16

**Objectives:**
- Research industry approach to sending packet data over TCP
- Define and implement image data packet framing and transmission
- Review Linux DMA drivers and PYNQ-Z2 documentation, taking notes to understand the architecture
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)

**Actions Taken:**
- Researched common implementations of sending packet data over TCP
- Implemented host-client echo of all CIFAR-10 image data with configurability of data transmission

**Observations / Issues:**
- Because the architecture is built around CIFAR-10 data which consists of 50000 images of size 3\*32\*32, we can manage without custom packet framing because both the host and client implicitly agree on the size of the data being communicated

**Results / Metrics:**
Roundtrip times based on number of images read as a minibatch from stream per recv() call.
- 1 image per recv(): 481.337 ms (5-trial average), 488.736 ms (median)
- 2 image per recv(): 390.990 ms (5-trial average), 389.131 ms (median)
- 3 image per recv(): 695.159 ms (5-trial average), 347.948 ms (median)
- 4 image per recv(): 300.575 ms (5-trial average), 293.748 ms (median)
- 5 image per recv(): 294.872 ms (5-trial average), 290.756 ms (median)

**Next Steps:**
- Review Linux DMA drivers and PYNQ-Z2 documentation, taking notes to understand the architecture
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)
- Client Python script performing CNN on received CIFAR-10 data and sending back to host classification tensor, iterating from echoing

### Iteration #2.3 - 2026/04/20

**Objectives:**
- draw.io architecture diagrams for dataflow (host -> board PS -> AXI DMA -> board PL -> AXI DMA -> board PS -> host) and DMA (how the DMA is implemented)
- Client Python script performing CNN on received CIFAR-10 data and sending back to host classification tensor, iterating from echoing

**Actions Taken:**
- Redefined objectives by postponing research of Linux DMA for when DMA implementation is being worked on; for now the AXI DMA IP will be used for simplicity and proof of concept

**Observations / Issues:** (bugs, hardware notes, performance metrics)  
**Results / Metrics:**
(measurable results)
**Next Steps:** (planned actions for next session)

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