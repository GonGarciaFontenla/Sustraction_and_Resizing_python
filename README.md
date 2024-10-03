# Image Processing Automation Program

## Overview
This program automates two essential image processing tasks: **background removal** and **image resizing**. It is designed to simplify workflows where these tasks are frequently required, making it an efficient solution for users who need to handle large batches of images.

## Features

1. **Background Removal**  
   The program uses an API powered by neural networks to accurately remove backgrounds from images. It communicates with the [remove.bg API](https://www.remove.bg/api) via the `requests` module to handle the background removal process automatically.

2. **Image Resizing**  
   Once the background is removed, the images are resized to user-specified dimensions using the Python Imaging Library ([PIL](https://pillow.readthedocs.io/)). This makes the images ready for various use cases, such as web publishing, printing, or any other resizing requirements.

3. **Efficient Image Management**  
   The program automatically organizes processed images into appropriate folders and logs API usage for tracking purposes. It uses Python’s standard libraries, such as `os` and `shutil`, for file and folder management, ensuring the entire process runs smoothly.

## Requirements
- Python 3.x
- `requests` library for handling API communication
- `Pillow` (PIL) for image processing
