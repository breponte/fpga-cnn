# Data

This folder contains the [CIFAR-10 image data](https://www.cs.toronto.edu/~kriz/cifar.html) to be used for the convolutional neural network.

According to the official distributors of the CIFAR-10 dataset:

```
The CIFAR-10 dataset consists of 60000 32x32 colour images in 10 classes, with 6000 images per class. There are 50000 training images and 10000 test images.

The dataset is divided into five training batches and one test batch, each with 10000 images. The test batch contains exactly 1000 randomly-selected images from each class. The training batches contain the remaining images in random order, but some training batches may contain more images from one class than another. Between them, the training batches contain exactly 5000 images from each class.

The classes are completely mutually exclusive. There is no overlap between automobiles and trucks. "Automobile" includes sedans, SUVs, things of that sort. "Truck" includes only big trucks. Neither includes pickup trucks.
```

The data is not stored within this repository. The dataset must be downloaded on the local machine. The `data_loader.py` contains methods for downloading and extracting the CIFAR-10 dataset via URL.

For more details on the dataset used, visit https://www.cs.toronto.edu/~kriz/cifar.html.

## Dataset Organization

There are 5 training batches, `data_batch_x` for an arbitrary `x`, and one test batch, `test_batch`. The `batches.meta` outlines the 10 classes within the dataset:
- airplane
- automobile
- bird
- cat
- deer
- dog
- frog
- horse
- ship
- truck

