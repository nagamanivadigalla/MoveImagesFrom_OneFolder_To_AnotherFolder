import shutil
import os

source_folder = "code/Images"
destination_folder = "code/AppleImages"
image_filename = "Ios_Img.png"  # Change this to the actual image file name

# Construct the full paths for the source and destination
source_path = os.path.join(source_folder, image_filename)
destination_path = os.path.join(destination_folder, image_filename)

# Use the shutil.move() function to move the file
shutil.move(source_path, destination_path)

print(f"Image '{image_filename}' moved from '{source_folder}' to '{destination_folder}'.")
