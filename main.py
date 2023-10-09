import time
import pyautogui
from PIL import Image
# TODO 1. Grab image
# TODO 2. When certain pixels are grey, press Space to jump

# Sets the color to jump at
JUMP_COLOR = (83, 83, 83)
TARGET = (365, 680)


screenWidth, screenHeight = pyautogui.screenshot().size
print(screenWidth, screenHeight)

playing = True
while playing:
    game_state = pyautogui.screenshot().getpixel(TARGET)
    if game_state == JUMP_COLOR:
        print("Jump!")
# with Image.open("Game.png") as game_state:
#     game_state.show()
#     evaluating = True
#     while evaluating:
#         x, y = pyautogui.position()
#         r, g, b = pyautogui.pixel(x, y)
#         print(x, y)
#         print(r, g, b)
#         time.sleep(2)
