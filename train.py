import os
import kagglehub
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator

path_original = kagglehub.dataset_download("uraninjo/augmented-alzheimer-mri-dataset")
path = os.path.join(path_original, "AugmentedAlzheimerDataset")

IMG_SIZE = (128, 128)
BATCH_SIZE = 32

datagen = ImageDataGenerator(
    rescale = 1./255,
    validation_split = 0.19
)


