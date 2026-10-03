import time
import pyautogui
import os
import shutil


pyautogui.press('win')
time.sleep(2)
pyautogui.write('google', interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('win', 'up')
time.sleep(2)
pyautogui.write(
    'https://dados.turismo.gov.br/dataset/chegada-de-turistas-internacionais', interval=0.2)
time.sleep(2)
pyautogui.press('enter')
time.sleep(60)
pyautogui.press('end')
time.sleep(10)
pyautogui.click(1467, 526)
time.sleep(2)
pyautogui.click(1493, 598)
time.sleep(15)
pyautogui.hotkey('ctrl', 'f4')
time.sleep(5)

arquivo = r"C:\Users\Lucas\Downloads\base_chegadas_2026_acum_08_agosto.csv"
pasta_destino = r"C:\Users\Lucas\Desktop\Projeto BI + RPA\Dados"

destino = os.path.join(pasta_destino, "base_chegadas_2026_acum_08_agosto.csv")

shutil.copy2(arquivo, destino)

pyautogui.press('win')
time.sleep(2)
pyautogui.write('PowerBi', interval=0.1)
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(411, 758)
time.sleep(20)
pyautogui.click(747, 93)
time.sleep(15)
