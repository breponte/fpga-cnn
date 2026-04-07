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

<!-- ### Iteration #X - YYYY/MM/DD

**Objectives:** (what you aimed to do)  
**Actions Taken:** (what you actually did)  
**Observations / Issues:** (bugs, hardware notes, performance metrics)  
**Results / Metrics:**
(measurable results)
**Next Steps:** (planned actions for next session) -->