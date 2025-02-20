import cv2
import numpy as np
import os
from datetime import datetime

def open_cv_unwrap(file_path):
    """Unwrap a circular image into a strip image using OpenCV."""
    circle_image = cv2.imread(file_path, cv2.IMREAD_COLOR)
    
    if circle_image is None:
        print("Error: Could not load image.")
        return
    
    # height, width, _ = circle_image.shape

    # strip_height = height * 2
    # strip_width = width * 4

    # strip_image = np.zeros((strip_height, strip_width, 3), dtype=np.uint8)

    # for x in range(strip_height):
    #     for y in range(strip_width):
    #         angle = (y / strip_width) * 2 * np.pi
    #         normalized_x = x / strip_height
    #         radius = int((normalized_x - 0.5) * height * 0.8 + height / 2)

    #         circle_y = int(radius * np.cos(angle) + width / 2)
    #         circle_x = int(radius * np.sin(angle) + height / 2)

    #         if 0 <= circle_y < width and 0 <= circle_x < height:
    #             strip_image[x, y] = circle_image[circle_x, circle_y]

    # flipped_image = cv2.flip(strip_image, 0)

    # Get image dimensions
    height, width, _ = circle_image.shape
    center_x, center_y = width // 2, height // 2
    max_radius = min(center_x, center_y)

    # Define output strip dimensions
    strip_height = height  # Keep original height
    strip_width = width * 2  # Expand width to capture full 360 degrees

    # Create an empty strip image
    strip_image = np.zeros((strip_height, strip_width, 3), dtype=np.uint8)

    # Unwrap the circular image
    for x in range(strip_height):
        for y in range(strip_width):
            angle = (y / strip_width) * 2 * np.pi  # Convert to radians
            normalized_x = x / strip_height
            radius = int(normalized_x * max_radius)  # Adjust radius scaling

            circle_x = int(center_x + radius * np.cos(angle))
            circle_y = int(center_y + radius * np.sin(angle))

            if 0 <= circle_x < width and 0 <= circle_y < height:
                strip_image[x, y] = circle_image[circle_y, circle_x]

    # Flip the image vertically
    flipped_image = cv2.flip(strip_image, 0)

    # Define save directory
    save_dir = "/Users/kaiheng/Documents/python-venv/Image-Processing-Tools/Images/Circular_Unwrap"
    os.makedirs(save_dir, exist_ok=True)  # Ensure directory exists

    # Extract filename from the input file path
    filename = os.path.basename(file_path)  # Get filename with extension
    filename_no_ext = os.path.splitext(filename)[0]  # Remove extension

    unwrapped_path = os.path.join(save_dir, f"{filename_no_ext}.png")

    cv2.imwrite(unwrapped_path, flipped_image)
    print(f"Unwrapped image saved at: {unwrapped_path}")


open_cv_unwrap("/Users/kaiheng/Documents/python-venv/Image-Processing-Tools/Images/Circular/real_360.webp")