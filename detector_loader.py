from utils import *


# class ObjectDetectorController:
#     def __init__(self):
#         self.device = torch.device(
#             "cuda" if torch.cuda.is_available() else "cpu")
#         self.model = detection.fasterrcnn_resnet50_fpn(
#             weights_backbone=torchvision.models.ResNet50_Weights.DEFAULT,
#             progress=True,
#             num_classes=91,
#             pretrained_backbone=True).to(self.device)
#         self.model.eval()

#     def get_predictions(self, image):
#         image = process_for_object_detection(image)
#         image = image.to(self.device)
#         detections = self.model(image)[0]
#         return detections
