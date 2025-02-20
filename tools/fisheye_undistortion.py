import cv2
import numpy as np
import matplotlib.pyplot as plt

def undistort_fisheye(image_path):
    """
    Fully corrects fisheye distortion using OpenCV with advanced remapping.
    
    Parameters:
    - image_path: Path to the fisheye image.
    
    Returns:
    - Displays the original and fully undistorted image side by side.
    """
    # Load the fisheye image
    fisheye_img = cv2.imread(image_path)

    if fisheye_img is None:
        print("Error: Could not load image.")
        return
    
    # Get image dimensions
    height, width = fisheye_img.shape[:2]

    # Define the camera matrix (assumed values, should be calibrated for best results)
    K = np.array([[width / 1.5, 0, width / 2],  # Focal length in x
                  [0, width / 1.5, height / 2],  # Focal length in y
                  [0, 0, 1]], dtype=np.float32)  # Principal point

    # Adjusted distortion coefficients (tweak for best results)
    D = np.array([-0.5, 0.1, 0.0, 0.0], dtype=np.float32)  # Adjusted for stronger correction

    # Compute new camera matrix with optimized field of view
    new_K = cv2.fisheye.estimateNewCameraMatrixForUndistortRectify(K, D, (width, height), np.eye(3), balance=0.0)

    # Generate undistortion and rectification maps
    map_x, map_y = cv2.initUndistortRectifyMap(K, D, np.eye(3), new_K, (width, height), cv2.CV_32FC1)

    # Apply remapping to correct fisheye distortion
    undistorted_img = cv2.remap(fisheye_img, map_x, map_y, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    # Display the original and undistorted images
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))
    axs[0].imshow(cv2.cvtColor(fisheye_img, cv2.COLOR_BGR2RGB))
    axs[0].set_title("Original Fisheye Image")
    axs[0].axis("off")

    axs[1].imshow(cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2RGB))
    axs[1].set_title("Fully Undistorted Image")
    axs[1].axis("off")

    plt.show()

# Example usage
image_path = "/Users/kaiheng/Documents/python-venv/Image-Processing-Tools/images/Distortion/real_distorted.jpg"
undistort_fisheye(image_path)
