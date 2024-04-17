"""
converted all the png images to jpg images in my picture folder using python
"""
import os
from PIL import Image

# Change the directory to the folder containing PNG images
os.chdir(r"C:\Users\asus\Pictures\image")

# Loop through each file in the directory
for f in os.listdir():
    # Check if the file is a PNG image
    if f.lower().endswith('.png'):
        # Open the PNG image using full path, eg: current directory\filename
        img_path = os.path.join(os.getcwd(), f)
        img = Image.open(img_path) 
        
        # Convert the image to RGB mode if it's not already
        if img.mode != "RGB":
            img = img.convert('RGB')
        
        # Define the output filename with JPG extension
        jpg_filename = os.path.splitext(f)[0] + ".jpg"
        
        # Save the image as a JPG file with a different filename
        img.save(jpg_filename, "JPEG")
        print(f"Converted {f} to {jpg_filename}")


