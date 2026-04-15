# Host

The host transmits data to the FPGA development board via TCP through Ethernet. Image data will be sent according to the following packet framing strategy:

TODO

## configs.yaml

This file contains the configurations of the entire system, for both the host computer and the FPGA development board. The configurations include:

TODO

## data_loader.py

This file contains functions that handle loading/extracting the dataset from the Internet and preprocessing the data. It can be run as a standalone script, but is also included within `main.py`. It will skip if the data is downloaded and extracted.

## main.py

The top-level file that organizes all the host behavior. It downloads the dataset if it isn't already. It then sets up the host's server and waits until the client connects. Once connected, it will send the configuration information for the FPGA and afterwards send the CIFAR-10 image data through the TCP connection. The packet sizing is adjustable in the `configs.yaml` file.

## test_client.py

The testing script that simulates the FPGA development board client locally on the same machine as the host. Its purpose is for prototyping networking before implementing the HLS module.

## transmit.py

This file ontains functions that handle the TCP hosting and send/receive transmission to/from the FPGA development board.

## visualize.py

TODO