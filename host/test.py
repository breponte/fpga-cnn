import torch
model = torch.hub.load("chenyaofo/pytorch-cifar-models", "cifar10_resnet20", pretrained=True)
model.eval()

dummy = torch.randn(1, 3, 32, 32)
with torch.no_grad():
    out = model(dummy)
print(out.shape)  # torch.Size([1, 10])