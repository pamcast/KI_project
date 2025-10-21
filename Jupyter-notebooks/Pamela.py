import tensorflow as tf

dataset_path = r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\dataset\extracted'

# Load dataset with labels (automatic if folder structure organized by class)
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset='training',
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset='validation',
    seed=123,
    image_size=(128, 128),
    batch_size=32
)

# Now you can train your model
from tensorflow.keras import layers, models


# Define image dimensions and number of classes
IMG_HEIGHT = 128
IMG_WIDTH = 128
NUM_CLASSES = 4

# Example model
model = models.Sequential([
    layers.Rescaling(1./255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    layers.Conv2D(32, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(NUM_CLASSES, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])