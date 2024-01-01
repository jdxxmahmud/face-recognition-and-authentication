---

# Face Recognition and Authentication Project

This project involves setting up an environment for face recognition and authentication. Follow these steps to set up your environment and get started.

## Environment Setup

### Step 1: Create a Conda Environment
Create a Conda environment to manage dependencies and isolate your project.

```bash
conda create -n fr_env python=3.9
conda activate fr_env
```

### Step 2: Install Basic Libraries and Tools
Install the necessary libraries and tools before the face recognition library.

```bash
pip install --upgrade pip setuptools wheel
pip install cmake
```

### Step 3: Install Visual C++ Build Tools (Windows Only)
For Windows users, install the Visual C++ Build Tools from the [Microsoft website](https://visualstudio.microsoft.com/visual-cpp-build-tools/).

### Step 4: Set Up `zlibwapi.dll` (Windows Only)
For 64-bit Windows systems:

- Download `zlibwapi.dll` from a trusted source.
- Extract and paste the DLL into `C:\Windows\System32`.

### Step 5: Install OpenCV
Now install OpenCV.

```bash
pip install opencv-python
```

### Step 6: Install the face_recognition Library
Finally, install the `face_recognition` library.

```bash
pip install face_recognition
```

## Project Configuration

### Uploading Images
For face recognition, upload your images:

- Create a folder named `images` inside `face_recog_and_auth`.
- Upload your images to `\face_recog_and_auth\images`.


## Getting Started

With these setup instructions, your environment should be ready for running the face recognition and authentication project.

---
