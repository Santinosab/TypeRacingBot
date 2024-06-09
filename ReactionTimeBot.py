import pyautogui
import time
import keyboard
import win32api, win32con

# Click function

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.001)  # Short delay to simulate human-like click
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Main code
def main():
    while not keyboard.is_pressed('q'):
        # Get the RGB value of the pixel at (1420, 400)
        pixel_color = pyautogui.pixel(1420, 400)
        if pixel_color[1] == 219:  # Check if the green component is 219
            click(1420, 400)
if __name__ == "__main__":
    main()