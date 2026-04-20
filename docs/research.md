# Research

## Direct Memory Access (General)

A microcontroller that manages bus traffic and allows for other meaningful work to be done outside of transferring memory. It must know the type of memory operation being executed, the device address, the memory address, and the size of the memory block to transfer.

This piece of hardware is useful for avoiding back and forth trips with data. For example, a CPU loads memory from an I/O device and brings the memory into the CPU cache, then stores the loaded memory into the physical memory. A DMA avoids monopolizing the bus twice and instead brings the requested memory directly from the I/O device to the physical memory, without requiring the CPU to be the middleman.

The DMA cooperates, and avoids contention with the CPU by requesting the bus from the CPU. This is called cycle stealing:
1. DMA requests bus monopoloy
2. CPU disconnects (tri-stating the bus with a value of 'Z')
3. DMA takes over the bus

Some DMA architectures include:
- Personal DMA for a given device
- Master DMA that manages a device bus

[Reference](https://www.youtube.com/watch?v=M16l_ymlfcs) used.

## Linux DMA drivers

Note: pivoted from studying `dmaengine` due to the file's broad scope and complexity. Instead of approaching through files first, approaching through functionality first.

### Functionality Notes: [Provider](https://github.com/torvalds/linux/blob/master/Documentation/driver-api/dmaengine/provider.rst), [Client](https://github.com/torvalds/linux/blob/master/Documentation/driver-api/dmaengine/client.rst)

### [linux/drivers/dma/virt-dma.h](https://github.com/torvalds/linux/blob/master/drivers/dma/virt-dma.h)


### [linux/drivers/dma/virt-dma.c](https://github.com/torvalds/linux/blob/master/drivers/dma/virt-dma.c)



## PYNQ-Z2

### [Documentation](https://pynq.readthedocs.io/en/latest/getting_started/pynq_z2_setup.html)



### [Reference Manual](https://dpoauwgwqsy2x.cloudfront.net/Download/PYNQ_Z2_User_Manual_v1.1.pdf)

