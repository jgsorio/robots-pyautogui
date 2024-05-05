import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1


pyautogui.hotkey('win', 'r')
pyautogui.typewrite('https://www.gabrielcasemiro.com.br/atividade_pyautogui/ \n')

time.sleep(7)

with open('membros.csv') as file:
    next(file)
    for line in file:
        line = line.strip()
        line = line.split(';')
        
        name = line[0]
        sexo = line[1]
        email = line[2]
        telefone = line[3]

        name_location = pyautogui.locateCenterOnScreen('./img_browser/nome.png', confidence=0.8)
        pyautogui.click(name_location)
        pyautogui.typewrite(name)

        email_location = pyautogui.locateCenterOnScreen('./img_browser/email.png', confidence=0.8)
        pyautogui.click(email_location)
        pyautogui.typewrite(email)

        telefone_location = pyautogui.locateCenterOnScreen('./img_browser/telefone.png', confidence=0.8)
        pyautogui.click(telefone_location)
        pyautogui.typewrite(telefone)

        sexo_location = pyautogui.locateCenterOnScreen('./img_browser/sexo.png', confidence=0.8)
        pyautogui.click(sexo_location)

        if sexo == 'Feminino':
            pyautogui.typewrite('f')
            pyautogui.press('enter')
        else:
            pyautogui.typewrite('m')
            pyautogui.press('enter')
        
        enviar = pyautogui.locateCenterOnScreen('./img_browser/botao_cadastrar.png', confidence=0.8)
        pyautogui.click(enviar)

        time.sleep(2)

pyautogui.alert('Processo finalizado!')
