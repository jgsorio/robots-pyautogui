from PIL import ImageGrab
import pyautogui

def is_collision(data):
    for i in range(764, 840):
        for j in range(410, 440):
            if data[i, j] < 100:
                pyautogui.keyDown('up')
                return

while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()

    is_collision(data)
