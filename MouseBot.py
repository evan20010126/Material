import pyautogui

# while(True):
#     x = pyautogui.position()
#     print(x)

# while(True):
x, y = pyautogui.position()
print(x)
print(y)
# pyautogui.dragRel(300, 20)
# pyautogui.click()
# pyautogui.click(x=1564, y=45)
# pyautogui.doubleClick()

# pyautogui.moveTo(100, 200, 2)
# pyautogui.dragTo(300, 400, 2, button="left")

# pyautogui.press('left') #<-
# pyautogui.press('enter')
# pyautogui.press('ctrl')
# pyautogui.hotkey('ctrl', 'c')

# pyautogui.PAUSE = 2  # 1 instruction/ 2s
# pyautogui.keyDown('alt')  # hold
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.press('tab')
# pyautogui.keyUp('alt')  # release

# pyautogui.write('hello python !', interval=0.3)


# draw a picture
# distance = 160
# while distance > 0:
#     pyautogui.drag(distance, 0, duration=0.5)
#     distance -= 5
#     pyautogui.drag(0, distance, duration=0.5)
#     pyautogui.drag(-distance, 0, duration=0.5)
#     distance -= 5
#     pyautogui.drag(0, -distance, duration=0.5)
