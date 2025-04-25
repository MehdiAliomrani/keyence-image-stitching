# Keyence Image Stitching Automation Tool

This project automates the batch stitching and exporting of fluorescence microscopy images captured by the **Keyence BZ-X800 Analyzer**.

## Background
While working with the Keyence fluorescent microscope to image brain samples, I realized the manual stitching process for each set of images was extremely time-consuming. Since each stitching step required manual clicking and waiting, I developed this Python script to automate the process — saving time and reducing manual errors.

## Features
- Automatically opens and stitches images from each subfolder.
- Batch processes all registered areas (XYs) within a selected main folder.
- Automatically saves and renames the stitched overlays based on the registration area.
- Keeps the Keyence BZ-X800 Analyzer software running if it closes.


## Requirements
- Python 3.x
- `pyautogui`
- `pygetwindow`
- `psutil`
- `opencv-python`
- `numpy`
- `tkinter`

Install required packages:
```bash
pip install pyautogui pygetwindow psutil opencv-python numpy
