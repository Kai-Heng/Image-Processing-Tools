import cv2
import numpy as np
import matplotlib.pyplot as plt

def advanced_undistort(image_path, checkerboard_size=(7, 7)):
    """
    Detects and corrects distortion in a checkerboard image using OpenCV with enhanced optimization.
    
    Parameters:
    - image_path: Path to the distorted checkerboard image.
    - checkerboard_size: Tuple (cols, rows) defining the number of inner corners of the checkerboard.
    
    Returns:
    - Displays the original and undistorted image side by side with improved accuracy.
    """
    # Load the image
    distorted_img = cv2.imread(image_path)
    
    if distorted_img is None:
        print("Error: Could not load image.")
        return
    
    gray = cv2.cvtColor(distorted_img, cv2.COLOR_BGR2GRAY)

    # Prepare object points (3D points in real-world space)
    objp = np.zeros((checkerboard_size[0] * checkerboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:checkerboard_size[0], 0:checkerboard_size[1]].T.reshape(-1, 2)

    # Arrays to store object points and image points
    objpoints = []  # 3D points in real-world space
    imgpoints = []  # 2D points in image plane

    # Find the checkerboard corners with increased accuracy
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    ret, corners = cv2.findChessboardCorners(gray, checkerboard_size, None)

    if ret:
        # Refine corner detection
        corners_refined = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        objpoints.append(objp)
        imgpoints.append(corners_refined)

        # Perform camera calibration with optimized parameters
        ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
            objpoints, imgpoints, gray.shape[::-1], None, None, flags=cv2.CALIB_RATIONAL_MODEL
        )

        # Optimizing the undistortion process using `initUndistortRectifyMap`
        new_camera_matrix, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, dist_coeffs, gray.shape[::-1], 1, gray.shape[::-1])
        mapx, mapy = cv2.initUndistortRectifyMap(camera_matrix, dist_coeffs, None, new_camera_matrix, gray.shape[::-1], cv2.CV_16SC2)

        undistorted_img = cv2.remap(distorted_img, mapx, mapy, interpolation=cv2.INTER_LINEAR)

        # Crop the image to remove black edges
        x, y, w, h = roi
        undistorted_img = undistorted_img[y:y+h, x:x+w]

        # Show original and undistorted images
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        axs[0].imshow(cv2.cvtColor(distorted_img, cv2.COLOR_BGR2RGB))
        axs[0].set_title("Distorted Image")
        axs[0].axis("off")

        axs[1].imshow(cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2RGB))
        axs[1].set_title("Undistorted Image (Improved)")
        axs[1].axis("off")

        plt.show()
    else:
        print("Checkerboard corners not detected. Try a different image or adjust checkerboard size.")

# Example usage
image_path = "/Users/kaiheng/Documents/python-venv/Image-Processing-Tools/Images/Distortion/barrel_distortion_1.jpg"  # Upload a checkerboard calibration image
advanced_undistort(image_path, checkerboard_size=(7, 7))

