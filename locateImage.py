import pyautogui
import time

try:
    pyautogui.moveTo(790, 1048, duration=1)
    pyautogui.click()
    pyautogui.write("calc", interval=0.1)
    pyautogui.press("enter")
    time.sleep(3)

    locale4 = pyautogui.locateCenterOnScreen('./images/print_4.png', grayscale=True, confidence=0.8)
    pyautogui.moveTo(locale4[0], locale4[1], duration=1)
    pyautogui.click()

    plus = pyautogui.locateCenterOnScreen('./images/plus.png', grayscale=True, confidence=0.8)
    pyautogui.moveTo(plus[0], plus[1], duration=1)
    pyautogui.click()

    locale5 = pyautogui.locateCenterOnScreen('./images/print_5.png', grayscale=True, confidence=0.8)
    pyautogui.moveTo(locale5[0], locale5[1], duration=1)
    pyautogui.click()

    equals = pyautogui.locateCenterOnScreen('./images/equal_button.png', grayscale=True, confidence=0.8)
    pyautogui.moveTo(equals[0], equals[1], duration=1)
    pyautogui.click()

except:
    print('Not found')
