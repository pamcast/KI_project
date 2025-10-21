import os

# Set the environment variable if your kaggle.json is not in the default location
os.environ['KAGGLE_CONFIG_DIR'] = r"C:\Users\pamel\OneDrive\Documentos\Project_management\Kaggle"

# Now, invoke the Kaggle API to download the dataset
dataset_path = "masoudnickparvar/brain-tumor-mri-dataset"

# Download the dataset
import subprocess
subprocess.run(["kaggle", "datasets", "download", "-d", dataset_path, "-p", "./dataset"])

# Unzip the dataset if needed
import zipfile

zip_file = "./dataset/brain-tumor-mri-dataset.zip"
extract_folder = "./dataset/extracted"
with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_folder)

print("Dataset downloaded and extracted at:", os.path.abspath(extract_folder))

