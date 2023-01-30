from torchvision import models
import torch.nn as nn
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

import torch
import torchvision.transforms as T
from torchvision.io import read_image


class Predictor():

    def __init__(self):
        super().__init__()
        device = torch.device('mps')
        model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        model.fc = torch.nn.Linear(512, 2)
        model.load_state_dict(torch.load('automator.pth', map_location=device))
        model.to(device)
