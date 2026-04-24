# Project Plan: FPGA-Accelerated CNN on PYNQ-Z2
Project Owner: Brandon Reponte \
Start Date: April 2026 \
Target Completion: June–July 2026 \
Tools & Hardware: Vivado 2024.2, Python 3.12.3, CIFAR-10 dataset, PYNQ-Z2 (planned acquisition)

## Project Overview
The goal of this project is to implement a hardware-accelerated Convolutional Neural Network (CNN) on the PYNQ-Z2 FPGA development board. The project will leverage AXI DMA for streaming data between the Processing System (PS) and Programmable Logic (PL), demonstrating end-to-end AI acceleration on embedded hardware.
Before the board is available, the project will use Vivado HLS simulations to prototype the CNN and emulate DMA transfers using host-side Python code.

Primary Objectives:
- Build host-side Python scripts to transfer and receive data from the FPGA board.
- Build a CNN kernel in Vivado HLS and simulate data input, convolution, data output, and latency/throughput metrics.
- Implement host-side Python scripts to emulate DMA streaming for pre-board simulation.
- Optimize kernel for pipelining, throughput, and resource utilization.
- Deploy the kernel on PYNQ-Z2 using real AXI DMA once the board arrives.
- Measure and document performance metrics and resource usage.

Key Deliverables:
- Functional HLS CNN simulation with emulated DMA transfers.
- Python host scripts for data streaming.
- Optimized RTL kernel ready for PYNQ-Z2 deployment.
- Full performance report: cycles, latency, throughput, resource utilization.
- Diagram of PS ↔ PL DMA dataflow pipeline.

## Tools and Resources
| Resource | Purpose |
|----------|---------|
| Vivado 2024.2 | HLS prototyping, RTL synthesis, bitstream generation, block design |
| Python 3.12.3 | Host simulation of DMA transfers and tensor preprocessing |
| CIFAR-10 dataset | Input data for CNN validation and testing |
| Linux xilinx_dma.c / dmaengine.h / dmaengine.c |Reference for understanding Linux DMA engine |
| PYNQ-Z2 Board | Hardware deployment of CNN with real AXI DMA (post-arrival) |

Reference Materials:
PYNQ-Z2 board documentation: [PYNQ Docs](https://pynq.readthedocs.io/en/latest/getting_started/pynq_z2_setup.html) \
Digilent PYNQ-Z2 Reference Manual PDF: [Reference Manual](https://dpoauwgwqsy2x.cloudfront.net/Download/PYNQ_Z2_User_Manual_v1.1.pdf)
PYNQ-Z2 purchase: [Newark listing](https://www.newark.com/tul-corporation/1m1-m000127dvb/tul-pynq-z2-basic-kit/dp/69AC1754?cjdata=MXxOfDB8WXww&CMP=AFF-CJ-100876641-Evergreen+Link+for+Newark&source=CJ&cjevent=d227076532a311f183af02360a1eba8e&loyaltysignal=0)

## Project Phases
### Phase 0: Preparation / Setup (1 week)

- Install Vivado and HLS environment.
- Set up Python for host simulation.
- Gather datasets and Linux DMA reference files.
- Review PYNQ-Z2 specifications and constraints.

Deliverables: Ready-to-go development environment.

### Phase 1: HLS CNN Prototype (2 weeks)
- Implement a small CNN in HLS (1–2 convolution layers, optional FC layer).
- Create a testbench to simulate input tensors and capture output.
- Instrument HLS for latency, throughput, and resource utilization.
- Document dataflow and DMA-like streaming architecture.

Deliverables: Functional HLS CNN simulation, performance metrics, and dataflow diagrams.

### Phase 2: Host-Side DMA Simulation (1 week)
- Implement Python host scripts to emulate DMA transfers.
- Introduce buffer/FIFO simulation for streaming input/output.
- Benchmark simulated throughput and latency.
- Validate accuracy and precision with CIFAR-10 inputs.

Deliverables: Complete host-kernel simulation pipeline with metrics.

### Phase 3: Optimization & RTL Preparation (1 week)
- Optimize kernel: pipelining, loop unrolling, buffer adjustments.
- Convert critical areas from HLS to SystemVerilog.
- Convert data streaming scripts from Python to C++.
- Verify correctness of RTL simulation against HLS simulation.

Deliverables: Optimized RTL kernel ready for PYNQ-Z2 deployment.

### Phase 4: Board Deployment (1–2 weeks)
- Deploy kernel on PYNQ-Z2, generate bitstream.
- Integrate real AXI DMA for PS ↔ PL transfers.
- Run CNN inference with real inputs and capture outputs.
- Measure throughput, latency, and FPGA resource usage.

Deliverables: Fully working hardware CNN accelerator with performance report.

### Phase 5: Final Touches
- Add additional CNN layers or fully connected layers to improve accuracy and precision.
- Quantize weights for INT8 computation to improve latency, throughput, and resource utilization.
- Implement pipelined streaming for batch inference to improve throughput and resource utilization.
- Prepare polished GitHub repo / project writeup for portfolio or interviews.

