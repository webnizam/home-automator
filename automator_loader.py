
import torch
from torchvision import models
import torch.nn.functional as F
from utils import *


class AutomatorModel:
    def __init__(self):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = models.resnet18(pretrained=True)
        self.model.fc = torch.nn.Linear(512, 2)
        self.model.load_state_dict(torch.load(
            'automator.pth', map_location=device))
        self.model.to(device)
        self.model.eval()

    def predict_class(self, image):
        preprocessed = preprocess(image)
        output = self.model(preprocessed)
        output = F.softmax(output, dim=1).detach().cpu().numpy().flatten()
        category_index = output.argmax()
        return category_index
