import os
import time
import pyautogui

def main():
    test_folder = r"S:\OIT\....(path to your source folder)"
     
    # Get a list of files in the "test" folder
    files = os.listdir(test_folder)
    
    for file in files:
        # Open each folder/file in "test"
        os.startfile(os.path.join(test_folder, file))

        # Wait for a short duration (optional)
        time.sleep(8)

        # Run Image_XY01.gci file with BZ_X800 Analyzer Software
        os.startfile(os.path.join(test_folder, file, f"Image_{file}.gci"))

        # Wait for the BZ_X800 Analyzer Software window to appear
        time.sleep(15)  # Adjust the delay as needed

        pyautogui.hotkey('tab')
        time.sleep(1)

        pyautogui.press('right')
        time.sleep(1)

        # Click on the "Load" button using coordinates
        pyautogui.hotkey('shift', 'L')  # Adjust the coordinates as needed

        # Add a delay to ensure the "Uncompressed" page is fully loaded
        time.sleep(260)  # Adjust the delay as needed

        for _ in range(6):
          pyautogui.hotkey('tab')

        pyautogui.press('right')
        time.sleep(1)

        for _ in range(3):
          pyautogui.hotkey('tab')

        time.sleep(1)

        pyautogui.hotkey('enter')

        # Add a delay to ensure the "stitching is done" page is fully loaded/adjust the cordinates based on your screen to save the files in final folder
        time.sleep(350)  # Adjust the delay as needed

        for _ in range(4):
            pyautogui.hotkey('win', 'up')
            time.sleep(2)
            pyautogui.click(100, 97, clicks=2)
            time.sleep(3)
            pyautogui.click(194, 316) 
            time.sleep(2)
            pyautogui.click(1715, 1243)
            time.sleep(2)
            pyautogui.press('enter')
            pyautogui.hotkey('alt', 'f4')
            time.sleep(3)
            pyautogui.press('right')
            time.sleep(2)
            pyautogui.press('enter')
        
        # Closing all windows
        for _ in range(3):
            pyautogui.hotkey('alt', 'f4')
            time.sleep(10)

        # Clean up
        pyautogui.hotkey('alt', 'f4')
        time.sleep(10)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('right')
        time.sleep(1)
        pyautogui.press('enter')

        # Closing all windows
        pyautogui.hotkey('alt', 'f4')
        time.sleep(2)

        
if __name__ == "__main__":
    main()