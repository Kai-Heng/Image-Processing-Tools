# Image Processing Tools

## Overview
**Image Processing Tools** is a collection of Python-based utilities for performing various image calibration and transformation tasks. This project is designed to handle a variety of image formats and distortions, including 360-degree image unwrapping, fisheye image undistortion, and more. The tools leverage OpenCV and NumPy to provide efficient and accurate image processing capabilities.

## Features
- **360-degree Image Unwrapping**: Converts circular panoramic images into flat equirectangular projections.
- **Fisheye Image Undistortion**: Removes distortion from fisheye images to produce rectilinear projections.
- **More tools coming soon**: Additional calibration and enhancement tools will be added as the project evolves.

## Installation
To use these tools, you need to have Python installed along with the required dependencies. You can set up the environment as follows:

```bash
# Clone the repository
git clone https://github.com/yourusername/image-processing-tools.git
cd image-processing-tools

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage

### **1. 360-degree Image Unwrapping**
```python
from tools.unwrap_360 import unwrap_360
unwrap_360("path/to/your/360_image.png")
```

### **2. Fisheye Image Undistortion (In Progress)**
```python
from tools.fisheye_undistort import undistort_fisheye
undistort_fisheye("path/to/your/fisheye_image.png")
```

## Project Structure
```
image-processing-tools/
│── tools/
│   ├── unwrap_360.py  # 360-degree image unwrapping tool
│   ├── fisheye_undistort.py  # Fisheye undistortion tool (In Progress)
│── examples/
│   ├── sample_360.png
│   ├── sample_fisheye.png
│── README.md
│── requirements.txt
│── setup.py
```

## Roadmap
- ✅ **360-degree Image Unwrapping** (Completed)
- 🚧 **Fisheye Image Undistortion** (In Progress)
- ⏳ **Perspective Correction** (Planned)
- ⏳ **Color Calibration and Enhancement** (Planned)

## Contributions
Contributions are welcome! If you'd like to improve an existing tool or add a new one, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or collaborations, reach out via GitHub Issues or email **info@xemtron.com**.

