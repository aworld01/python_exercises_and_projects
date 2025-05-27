import torch

#print("GPU Available:", torch.cuda.is_available())
print("GPU Name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")

#nvidia-smi: to check gpu capability


#device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
#print("Using device:", device)


"""
conda uninstall pytorch torchvision torchaudio# This removes PyTorch and its related packages.
conda list | grep pytorch: conda list | grep pytorch
conda clean --all: If you want to clean up unused dependencies

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
"""