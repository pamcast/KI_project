#Brain Tumor Classification Dataset
#This project uses a dataset of brain tumor images organized into different folders based on tumor types. The dataset was obtained from Kaggle (provide exact link if available).

#Dataset Description
#The dataset contains images of brain tumors with the following classes:

#meningiona
#glioma
#notumor
#pituitary
#The images are organized in a folder structure that is compatible with TensorFlow's image_dataset_from_directory() method.

#How they can set up their own Kaggle API credentials
Create a Kaggle account if they haven't already.
Generate an API token:
Log in to Kaggle.
Visit your account settings: https://www.kaggle.com/account
Scroll to the "API" section and click Create New API Token.
Download the kaggle.json file.
Place the file in the appropriate directory:
Your script expects it at:
C:\Users\pamel\OneDrive\Documentos\Project_management\Kaggle\kaggle.json
They should place their own kaggle.json in their respective path (recommended to keep it private).
Recommendations
Your collaborators must have their own kaggle.json.
They should not use your kaggle.json file for their account.
Adjust your script if needed so each user stores the file in their environment.
Summary
Yes, each person needs their own kaggle.json.
They must place it in the directory specified in your script.
Once they do that, they can run your script to download the dataset.


Load the dataset
import tensorflow as tf

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
#Notes for Classmates
#Make sure your dataset folder structure matches the expected structure.
#Adjust the dataset_path variable if your dataset folder is located elsewhere.
#Install the required packages:
#bash
#Copy
#pip install tensorflow
#You can modify the image_size or other parameters as needed for your specific use case.
