import torch
import numpy as np

rng = np.random.default_rng()

model = torch.hub.load("chenyaofo/pytorch-cifar-models", "cifar10_resnet20", pretrained=True)
model.eval()

dummy = rng.random((1, 3, 32, 32))
dummy = torch.from_numpy(dummy).float()
with torch.no_grad():
    out = model(dummy)
print(out.shape)  # torch.Size([1, 10])