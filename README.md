# Keyence Microscope Image Stitching Script

This repository contains a Python script that automates the stitching of images captured with a Keyence microscope using the BZ_X800 Analyzer Software. The script uses the `pyautogui` library to simulate user interactions, streamlining the stitching process.

---

## Features

- Automates the opening of image folders and `.gci` files.
- Simulates key presses and mouse clicks for the stitching workflow in the BZ_X800 Analyzer Software.
- Customizable delays to adapt to different system setups.
- Automatically stitches images and saves the channels and overlays in the specified folder.

---

## Prerequisites

- Keyence **BZ_X800 Analyzer Software** installed on your system.
- A Windows operating system (required for `pyautogui` operations).
- Python 3.7 or later.

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/MehdiAliomrani/keyence-image-stitching.git
   ```
2. Navigate to the project directory:
   ```bash
   cd keyence-image-stitching
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Update the `test_folder` variable in `stitch_images.py` to point to the directory containing your images.
2. Open a terminal and navigate to the project directory.
3. Run the script:
   ```bash
   python stitch_images.py
   ```

**Important Notes:**
- Ensure all images to be stitched are organized in subfolders within the `test_folder`.
- The script uses pre-configured delays (`time.sleep`) and mouse/keyboard actions tailored for the Keyence BZ_X800 Analyzer Software. Adjust these as needed for your setup.

---

## Example

Here’s how the folder structure should look:
```
Captured slides/
├── XY01/
│   ├── Image_XY01.gci
├── XY02/
│   ├── Image_XY02.gci
```

The script will:
1. Open each folder.
2. Process the `.gci` files using the BZ_X800 software.
3. Automate the stitching process through key presses and mouse clicks.
4. Save all channels and overlays to the specified folder.

---

## Known Issues

- The script relies on hardcoded mouse coordinates. If your screen resolution or software layout differs, adjust the coordinates in the script.
- Ensure the Keyence BZ_X800 software is running and in focus when the script starts.

---

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to submit an issue or a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).


---

## Acknowledgments

Thanks to the [Ghashghaei Lab](https://ghashghaeilab.ncsu.edu/) for supporting this work.
