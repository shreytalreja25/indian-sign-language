import cv2
import numpy as np
# from tensorflow.keras.applications import VGG16
from tensorflow.python.keras. import VGG16
from tensorflow.keras.models import Model

# Load pre-trained VGG16 model + higher level layers
base_model = VGG16(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_pool').output)

def extract_features(frames):
    preprocessed_frames = np.array([preprocess_frame(frame) for frame in frames])
    features = model.predict(preprocessed_frames)
    return features

def preprocess_frame(frame):
    frame = cv2.resize(frame, (224, 224))
    frame = frame / 255.0
    return frame
