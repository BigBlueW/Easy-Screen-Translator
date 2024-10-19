"""
pyinstaller --onefile --add-data "Google_Translate_logo.ico;." --add-data "Tesseract-OCR;Tesseract-OCR" --hidden-import plyer.platforms.win.notification EST.py --noconsole
"""
import pyperclip
from PIL import Image, ImageGrab
import pytesseract
from googletrans import Translator
import keyboard
import plyer
import mouse
import time
import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))

if getattr(sys, 'frozen', False):
    exe_path = sys.argv[0]
else:
    exe_path = os.path.abspath(__file__)
exe_dir = os.path.dirname(exe_path)  
print(f"The executable is located at: {exe_dir}")

config = {}
try:
    with open(os.path.join(exe_dir, "config.txt"), "r") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key_, value = line.split("=", 1)
                config[key_.strip()] = value.strip()
except FileNotFoundError:
    print("Config file not found. Using default settings.")
#config
resultLanguage = config.get("resultLanguage", "zh-TW")
key = config.get("key", "win+shift+l")
#/config

def show_tooltip(msg):
    plyer.notification.notify(
        title="Translating result：",
        message=msg,
        app_icon= os.path.join(base_dir, "Google_Translate_logo.ico")
    )

def process_image_from_clipboard():
    img = ImageGrab.grabclipboard()

    if isinstance(img, Image.Image):
        extracted_text = pytesseract.image_to_string(img)
        extracted_text = extracted_text.replace("\n", "")
        if extracted_text.strip():
            translation = translator.translate(extracted_text, dest=resultLanguage)

            show_tooltip(translation.text)

            pyperclip.copy(translation.text)
        else:
            show_tooltip("No text found in the image.")
    else:
        show_tooltip("No image found in clipboard.")

def take_screenshot():
    keyboard.press_and_release('win+shift+s')
    print("Please do screenshot.")
    while not mouse.is_pressed('left'):
        time.sleep(0.1)

    while mouse.is_pressed('left'):
        time.sleep(0.1)

    print("released")
    time.sleep(0.3)
    process_image_from_clipboard()

def bind_hotkey():
    keyboard.add_hotkey(key, take_screenshot)
    print(f"{key} is set for screenshot.")
    keyboard.wait('esc')

if __name__ == "__main__":
    pytesseract.pytesseract.tesseract_cmd = os.path.join(base_dir, "Tesseract-OCR", "tesseract.exe")
    translator = Translator()
    print(base_dir)
    bind_hotkey()