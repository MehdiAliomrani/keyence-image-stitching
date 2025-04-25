import os
import time
import pyautogui
import pygetwindow as gw
import psutil
import tkinter as tk
from tkinter import filedialog
from threading import Thread
import numpy as np
import cv2

# Full path to the software
SOFTWARE_PATH = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\KEYENCE BZ-X800"
WINDOW_TITLE = "BZ-X800 Analyzer"

# Paths to button images
file_button = r"E:\Users\maliomr\Desktop\Ario\Keyence_click\File.jpg"
export_button = r"E:\Users\maliomr\Desktop\Ario\Keyence_click\Export.jpg"
ok_button = r"E:\Users\maliomr\Desktop\Ario\Keyence_click\Ok.jpg"

def select_folder():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory(title="Select the Main Folder Containing Subfolders")

def is_running(process_name):
    for proc in psutil.process_iter(["name"]):
        if process_name.lower() in proc.info["name"].lower():
            return True
    return False

def keep_software_running():
    while True:
        if WINDOW_TITLE not in [w.title for w in gw.getAllWindows()]:
            print(f"{WINDOW_TITLE} is closed! Restarting...")
            os.startfile(SOFTWARE_PATH)
        time.sleep(5)

def find_and_click(image_path, confidence=0.8):
    screen = pyautogui.screenshot()
    screen = np.array(screen)
    template = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    if template is None:
        print(f"Error: Could not load image {image_path}. Check the file path.")
        return False
    
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= confidence:
        center_x = max_loc[0] + template.shape[1] // 2
        center_y = max_loc[1] + template.shape[0] // 2
        pyautogui.click(center_x, center_y)
        print(f"Clicked on {image_path} at ({center_x}, {center_y})")
        return True
    else:
        print(f"Could not find {image_path} on the screen.")
        return False

def wait_for_process_to_complete(timeout=600):
    print("Waiting for one of the 'Image Stitch' windows to close...")
    start_time = time.time()

    while time.time() - start_time < timeout:
        windows = [w for w in gw.getWindowsWithTitle("Image Stitch")]
        if len(windows) >= 2:
            print("Two 'Image Stitch' windows detected. Monitoring for closure...")
            break
        time.sleep(2)

    while time.time() - start_time < timeout:
        windows = [w for w in gw.getWindowsWithTitle("Image Stitch")]
        if len(windows) < 2:
            print("✅ One 'Image Stitch' window has closed. Assuming process is complete.")
            return True
        time.sleep(2)

    print("⚠ Timeout reached. Assuming stitching process is complete.")
    return False

def wait_for_wideview_windows(count=4, timeout=200):
    print(f"Waiting for {count} Wide Image Viewer windows to open...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        windows = [w for w in gw.getWindowsWithTitle("BZ-X800 Wide Image Viewer")]
        if len(windows) >= count:
            print(f"✅ {count} Wide Image Viewer windows detected.")
            return windows
        time.sleep(4)

    print(f"⚠ Timeout reached. Proceeding with available windows: {len(windows)}.")
    return gw.getWindowsWithTitle("BZ-X800 Wide Image Viewer")

def save_file(stitched_folder, filename):
    print(f"Saving file as: {filename} in {stitched_folder}")
    time.sleep(2)
    
    pyautogui.hotkey("alt", "d")
    pyautogui.write(stitched_folder)
    pyautogui.press("enter")
    time.sleep(1)

    pyautogui.press('tab', presses=6, interval=0.1)
    pyautogui.write(filename)
    pyautogui.press('tab', presses=3, interval=0.1)
    pyautogui.press("enter")
    

    pyautogui.hotkey("alt", "f4")
    pyautogui.hotkey("right")
    pyautogui.press("enter")
    

def close_wideview_windows():
    windows = gw.getWindowsWithTitle("BZ-X800 Wide Image Viewer")
    for window in windows:
        print(f"Closing: {window.title}")
        window.close()
        time.sleep(2)
        pyautogui.press("right")  
        pyautogui.press("enter")  
        time.sleep(1)  
    print("✅ All Wide Image Viewer windows closed!")

def close_all():
        pyautogui.press("tab")  
        pyautogui.press("right")  
        pyautogui.press("enter")  
        time.sleep(1) 
        pyautogui.press('tab', presses=3, interval=0.1)
        pyautogui.hotkey('enter')
        print("✅ All Wide Image Viewer windows closed!")

def close_all_except_BZX800():
    # Get all open windows
    all_windows = gw.getWindowsWithTitle("")  # List all open windows

    # Iterate through all windows
    for window in all_windows:
        # Skip BZX800 Analyzer and any windows related to "Stitch" or "Load"
        if "BZ-X800 Analyzer" not in window.title and ("Stitch" in window.title or "Load" in window.title):
            try:
                print(f"Closing window: {window.title}")
                window.activate()  # Bring the window to the foreground
                time.sleep(0.5)  # Wait a bit for window focus
                window.close()  # Try to close the window
                time.sleep(2)  # Give time for the window to close
            except Exception as e:
                print(f"Failed to close {window.title}: {e}")
        else:
            print(f"Skipping window: {window.title}")  # Skip BZX800 and windows unrelated to Stitch or Load


def process_images(main_folder):
    if not main_folder:
        print("No folder selected. Exiting.")
        return
    
    stitched_folder = os.path.join(main_folder, "Stitched_Outputs")
    os.makedirs(stitched_folder, exist_ok=True)

    if not is_running("BZ-X800_Analyzer.exe"):
        print("Starting BZ-X800 Analyzer...")
        os.startfile(SOFTWARE_PATH)
        time.sleep(10)

    subfolders = [f for f in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, f))]

    for subfolder in subfolders:
        folder_path = os.path.join(main_folder, subfolder)
        gci_file = next((f for f in os.listdir(folder_path) if f.endswith(".gci")), None)

        if not gci_file:
            print(f"No .gci file found in {subfolder}, skipping.")
            continue

        print(f"\n📂 Processing folder: {subfolder}")
        os.startfile(os.path.join(folder_path, gci_file))
        time.sleep(2)

        pyautogui.press('tab', presses=4, interval=0.1)
        pyautogui.hotkey('right')
        pyautogui.hotkey('shift', 'L')
       

        wait_for_process_to_complete()

         # ✅ Click "First" and "Second" buttons only once per XY
        if not os.path.exists(os.path.join(stitched_folder, f"Stitched_Image_{subfolder}_1.tif")):
            print("Clicking 'First' and 'Second' buttons for this XY...")
            pyautogui.press('tab', presses=6)
            pyautogui.hotkey('right')
            pyautogui.press('tab', presses=3)
            pyautogui.hotkey('enter')

        wideview_windows = wait_for_wideview_windows(count=4)

        for i, window in enumerate(wideview_windows[:4]):
            print(f"\n🚀 Processing Image {i + 1} from Wide Image Viewer...\n")
            window.activate()
            pyautogui.hotkey('win', 'up')  # Maximize window
           

            # Click on File button
            find_and_click(file_button)
            

            # Click on Export button
            find_and_click(export_button)
     

            # Click on OK button
            find_and_click(ok_button)
           

            filename = f"Stitched_Image_{subfolder}_{i + 1}.tif"
            save_file(stitched_folder, filename)

        close_wideview_windows()
        close_all()
        close_all_except_BZX800()

if __name__ == "__main__":
    main_folder = select_folder()
    monitor_thread = Thread(target=keep_software_running, daemon=True)
    monitor_thread.start()
    process_images(main_folder)
