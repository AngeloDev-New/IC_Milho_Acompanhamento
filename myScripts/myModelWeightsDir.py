from weedsgalore_main.src.nets import deeplabv3plus_resnet50
import torch
import torch.nn as nn
def Model(num_classes = 3,
          in_channels = 3):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    net = deeplabv3plus_resnet50(num_classes = num_classes)
    net = net.to(device)
    net.backbone.conv1 = nn.Conv2d(in_channels, net.backbone.conv1.out_channels, kernel_size=7, stride=2, padding=3, bias=False, device=device)

    return net