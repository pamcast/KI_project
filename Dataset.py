import os
from PIL import Image
import shutil

def process_and_save_images(folder_paths, output_folder, target_size=(256, 256), quality=85):
    """
    Resize and compress images from multiple folders, then save them to a new directory.

    Args:
        folder_paths (list): List of folder paths to load images from.
        output_folder (str): Directory to save processed images.
        target_size (tuple): Size to resize images to (width, height).
        quality (int): Compression quality for JPEG (1-95).

    Returns:
        list: Paths of saved processed images.
    """
    saved_image_paths = []

    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for folder_path in folder_paths:
        for filename in os.listdir(folder_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                img_path = os.path.join(folder_path, filename)
                try:
                    with Image.open(img_path) as img:
                        # Resize image
                        img = img.resize(target_size)
                        # Save compressed image in output folder
                        new_filename = os.path.splitext(filename)[0] + "_compressed.jpg"
                        save_path = os.path.join(output_folder, new_filename)
                        img.save(save_path, "JPEG", quality=quality)
                        saved_image_paths.append(save_path)
                except Exception as e:
                    print(f"Error processing {img_path}: {e}")
    return saved_image_paths

# Example folder paths for training and testing
train_paths = [
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Training\meningioma',
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Training\notumor',
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Training\glioma',
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Training\pituitary'
]

test_paths = [
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Testing\meningioma_testing',
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Testing\notumor_testing',
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Testing\glioma_testing',
    r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Testing\pituitary_testing'
]

# Output directories for processed images
train_output_dir = r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Processed\train'
test_output_dir = r'C:\Users\pamel\OneDrive\Documentos\GitHub\KI_project\Processed\test'

# Process and save training images
train_images = process_and_save_images(train_paths, train_output_dir, target_size=(256, 256), quality=85)
print(f"Processed {len(train_images)} training images.")

# Process and save testing images
test_images = process_and_save_images(test_paths, test_output_dir, target_size=(256, 256), quality=85)
print(f"Processed {len(test_images)} testing images.")