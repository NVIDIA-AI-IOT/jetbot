ARG BASE_IMAGE=jetbot-base:jp44
FROM ${BASE_IMAGE}

RUN python3 -c "import torchvision; \
                model = torchvision.models.alexnet(pretrained=True); \
                model = torchvision.models.squeezenet1_1(pretrained=True); \
                model = torchvision.models.resnet18(pretrained=True); \
                model = torchvision.models.resnet34(pretrained=True)"
