import enum
import cv2
from .jpeg_encoder import JpegEncoder


_ENCODER = JpegEncoder(width=224, height=224, fps=21)


def bgr8_to_jpeg(value):
    return _ENCODER.encode(value)


def bgr8_to_jpeg_legacy(value, quality=75):
    return bytes(cv2.imencode('.jpg', value)[1])