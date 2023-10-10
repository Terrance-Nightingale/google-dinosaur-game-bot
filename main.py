import time
import keyboard
from mss import mss
from selenium import webdriver

# Constants
# Sets the color to jump at, the target pixel to evaluate, and the game url
URL = "https://elgoog.im/dinosaur-game/"
RANGE = {'top': 600, 'left': 150, 'width': 500, 'height': 200}
TARGET_X = 460
TARGET_Y = 120

# Sets driver configurations
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--guest")

# Opens webpage to dinosaur game
driver = webdriver.Edge(options=options)
driver.maximize_window()
driver.get(URL)
time.sleep(2)

# Starts game
keyboard.press("space")
time.sleep(2)

playing = True
while playing:
    # Set screenshot range.
    with mss() as sct:
        game_state = sct.grab(RANGE)
    # Establish variables
    dino_pxl = game_state.pixel(0, 100)
    cactus_pxl = game_state.pixel(TARGET_X, TARGET_Y)
    bird_pxl = game_state.pixel(TARGET_X, TARGET_Y - 100)
    # Check if cactus/bird is in jumping range
    if cactus_pxl == dino_pxl or bird_pxl == dino_pxl:
        keyboard.press("space")
        time.sleep(0.2)
