# FPGA Accelerated Convolutional Neural Network on CIFAR-10 Data

## Project Overview

The goal of this project is to implement a hardware-accelerated Convolutional Neural Network (CNN) on the PYNQ-Z2 FPGA development board. The project will leverage AXI DMA for streaming data between the Processing System (PS) and Programmable Logic (PL), demonstrating end-to-end AI acceleration on embedded hardware.

The components of this project include host scripts for data streaming to and from the FPGA development board, HLS/SystemVerilog program for handling CNN, and DMA transferring of data on the FPGA board.

This project is an exploratory project and is not intended for industry use. Hence, this code is free to be redistributed and used.

For more details on the project overview, see [project specifications](./docs/SPECIFICATIONS.md) in the [docs](./docs) folder.

## File Structure

### data

[CIFAR-10 data](https://www.cs.toronto.edu/~kriz/cifar.html) input for the convolutional neural network.

The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

### docs

Documentation for the repository, including project specifications, architecture design, and change log.

### hls_kernel

Prototype HLS code for the convolutional neural network kernel with testbench to verify correctness and performance metrics.

### host

Python/C++ scripts running on host PC which handles the data streaming to and from the FPGA development board. Additionally includes the DMA transfer simulation script for prototyping without the physical board.

### rtl

RTL code translated from HLS to allow for more control and optimization of the kernel program.

## How to Use

### Setup

First, create a Python virtual environment and download the dependencies. Run the following command to set up a virtual environment, activate it, and download dependencies (ensure running in root directory):

```
# create virtual environment
python -m venv .venv

# bash
source .venv/bin/activate
# Windows CMD
.venv\Scripts\activate

# download dependencies
pip install -r requirements.txt
```

## Contributors

- Brandon Reponte

## Citations

This project uses the [CIFAR-10](https://www.cs.toronto.edu/~kriz/cifar.html) dataset. Please cite:
> Krizhevsky, A. (2009). *Learning multiple layers of features from tiny images* (Technical Report). University of Toronto.