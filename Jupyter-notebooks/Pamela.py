import tensorflow as tf

dataset_path = r'path/to/your/extracted/dataset'

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
model.fit(train_ds, validation_data=val_ds, epochs=10)