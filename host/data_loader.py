import numpy
import time
import tarfile
from pathlib import Path
from urllib.request import urlretrieve

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

def download_targz():
    """
    Download and extract the CIFAR-10 dataset binary via website.
    """

    URL = "https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz"
    OUT_DIR = Path("../data")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    archive = OUT_DIR / "cifar-10-binary.tar.gz"
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



if __name__ == "__main__":
    download_targz()