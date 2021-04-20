import pyautogui, time

text = str(input('Введите текст спама ') + ' ')
counter = int(input('Введите колличество повторений текста '))
text2 = text * counter
spam = text2.split(' ')
time.sleep(10)

for line in spam:
	pyautogui.typewrite(line)
	pyautogui.press('enter')
