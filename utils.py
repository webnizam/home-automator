import torch
import torchvision.transforms as transforms
import torch.nn.functional as F
import cv2
import PIL.Image

mean = torch.Tensor([0.485, 0.456, 0.406]).cuda(
) if torch.cuda.is_available() else torch.Tensor([0.485, 0.456, 0.406]).cpu()
std = torch.Tensor([0.229, 0.224, 0.225]).cuda() if torch.cuda.is_available(
) else torch.Tensor([0.229, 0.224, 0.225]).cpu()


def preprocess(image):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    image = cv2.resize(image, (224, 224))
    image = PIL.Image.fromarray(image)
    image = transforms.functional.to_tensor(image).to(device)
    image.sub_(mean[:, None, None]).div_(std[:, None, None])
    return image[None, ...]
