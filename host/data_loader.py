import numpy
import time
import tarfile
from pathlib import Path
from urllib.request import urlretrieve
import pickle

start_time = None

def reporthook(block_num, block_size, total_size):
    """
    Report hook progress bar for downloading, argument for urlretrieve
    Args:
        block_num: The index of the block being downloaded
        block_size: The size of the block being downloaded
        total_size: The total size of the download
    """

    global start_time
    
    if start_time is None:
        start_time = time.time()
    
    downloaded = block_num * block_size
    elapsed = time.time() - start_time
    
    # Avoid division issues
    speed = downloaded / elapsed if elapsed > 0 else 0
    
    if total_size > 0:
        percent = downloaded / total_size * 100
        remaining = total_size - downloaded
        eta = remaining / speed if speed > 0 else 0

        for i in range(20):
            if (i < (percent // 5)):
                print("#", end="")
            else:
                print("-", end="")
        print(f"\r{percent:5.1f}% | {downloaded/1e6:.2f}MB "
              f"| {speed/1e6:.2f} MB/s | ETA: {eta:.1f}s | ", end="")
    else:
        # Fallback if size unknown
        print(f"\rDownloaded {downloaded/1e6:.2f}MB "
              f"| {speed/1e6:.2f} MB/s", end="")

def download_dataset():
    """
    Download and extract the CIFAR-10 dataset via website.
    Uses the Python download.
    """

    URL = "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    OUT_DIR = Path("../data")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    archive = OUT_DIR / "cifar-10-python.tar.gz"
    extracted = OUT_DIR / "cifar-10-batches-bin"

    if not archive.is_file():
        print("Downloading...")
        urlretrieve(URL, archive, reporthook)
        print("Done:", archive)

    if not extracted.is_dir():
        print("Extracting...")
        with tarfile.open(archive, "r:gz") as tf:
            tf.extractall(OUT_DIR)
        print("Extract under:", OUT_DIR)
    else:
        print("Dataset already exists")

def unpickle(file):
    """
    Reads the CIFAR-10 data/meta pickle files.
    If a data file, it will load the file into a dictionary as follows:

    data -- a 10000 x 3072 numpy array of uint8s.
        Each row of the array stores a 32 x 32 color image.
        The first 1024 entries contain the red channel values,
        the next 1024 the green, and the final 1024 the blue.
        The image is stored in row-major order, so that the first 32 entries of
        the array are the red channel values of the first row of the image.

    labels -- a list of 10000 numbers in the range 0-9.
        The number at index i indicates the label of the
        ith image in the array data.

    The metadata file will be loaded into a dictionary as follows:
    
    label_names -- a 10-element list which gives meaningful names to the
        numeric labels in the labels array described above.
        For example, label_names[0] == "airplane",
        label_names[1] == "automobile", etc.

    Args:
        file: CIFAR-10 pickle data or metadata to be loaded
    Returns:
        dictionary: Python dictionary of the loaded CIFAR-10 data
    """

    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

if __name__ == "__main__":
    download_dataset()