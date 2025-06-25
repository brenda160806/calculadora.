import pyautogui

pyautogui.hotkey("win", "r") #"hotkey" e para combinar teclas
pyautogui.sleep(1) 
pyautogui.write('calc')
pyautogui.press('enter')
pyautogui.sleep(2)
pyautogui.press('8')
pyautogui.sleep(2)
pyautogui.press('+')
pyautogui.sleep(2)
pyautogui.press('2')
pyautogui.press('=')

print('o calculo foi realizado na calculadora do windows,')
print("confira o historico da calculadora")
S