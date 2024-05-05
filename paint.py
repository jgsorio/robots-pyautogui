import pyautogui

# pyautogui.displayMousePosition()

# clicar no menu iniciar
pyautogui.moveTo(x=787, y=1056, duration=2)
pyautogui.click()

# # pesquisar paint
pyautogui.write("paint", interval=0.8)

# #clicar no app paint
pyautogui.moveTo(578, 341, 2)
pyautogui.click()

pyautogui.moveTo(744, 578, 2)

distance = 200

while distance > 0:
    pyautogui.dragRel(distance, 0, 0.5, button="left")
    distance = distance - 5
    pyautogui.dragRel(0, distance, 0.5, button="left")
    pyautogui.dragRel(-distance, 0, 0.5, button="left")
    distance = distance - 5
    pyautogui.dragRel(0, -distance, 0.5, button="left")



