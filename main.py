import time
import pyautogui
from selenium import webdriver
from PIL import Image
# TODO 1. Grab image
# TODO 2. When certain pixels are grey, press Space to jump

# Constants
# Sets the color to jump at, the target pixel to evaluate, and the game url
URL = "https://elgoog.im/dinosaur-game/"
JUMP_COLOR = (83, 83, 83)
TARGET_X = 580
TARGET_Y = 700

# Sets driver configurations
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

# Opens webpage to dinosaur game
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get(URL)
time.sleep(3)

# Starts game
pyautogui.press("space")

playing = True
while playing:
    game_state_1 = pyautogui.pixel(TARGET_X, TARGET_Y)
    game_state_2 = pyautogui.pixel(TARGET_X, TARGET_Y - 100)
    if game_state_1 == JUMP_COLOR or game_state_2 == JUMP_COLOR:
        pyautogui.press("space")
