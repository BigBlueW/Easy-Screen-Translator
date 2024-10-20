#pyinstaller --noconfirm --onedir --windowed --add-data "C:\Users\Badon\OneDrive\桌面\EST\config.txt;." --add-data "C:\Users\Badon\OneDrive\桌面\EST\Google_Translate_logo.ico;." --add-data "C:\Users\Badon\OneDrive\桌面\EST\Tesseract-OCR;Tesseract-OCR/" --add-data "C:\Users\Badon\AppData\Local\Programs\Python\Python310\Lib\site-packages\customtkinter;customtkinter/"  "C:\Users\Badon\OneDrive\桌面\EST\EST.py" --noconsole

import customtkinter as ctk
import tkinter as tk
from googletrans import Translator
import keyboard
from PIL import Image, ImageGrab
import pytesseract
import mouse
import time
import os
import sys
import pyperclip
import webbrowser

#setup
extracted_text = ""
translation_text = ""
img = ImageGrab.grabclipboard()
translator = Translator()
base_dir = os.path.dirname(os.path.abspath(__file__))
if getattr(sys, 'frozen', False):
    exe_path = sys.argv[0]
else:
    exe_path = os.path.abspath(__file__)
exe_dir = os.path.dirname(exe_path)  
pytesseract.pytesseract.tesseract_cmd = os.path.join(base_dir, "Tesseract-OCR", "tesseract.exe")

languages = {
    "🌍Detect language": "DL",
    "🇺🇸English": "en",
    "🇹🇼中文 (臺灣)": "zh-tw",
    "🇨🇳中文 (中国)": "zh-cn",
    "🇫🇷Français": "fr",
    "🇩🇪Deutsch": "de",
    "🇯🇵日本語": "ja",
    "🇰🇷한국어": "ko",
    "🇷🇺Русский": "ru",
}

setuped = False
#/

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
#/

def keyMethod():
    global extracted_text, translation_text, img

    extracted_text = ""
    translation_text = ""
    keyboard.press_and_release('win+shift+s')
    while not mouse.is_pressed('left'):
        time.sleep(0.1)
    while mouse.is_pressed('left'):
        time.sleep(0.1)
    time.sleep(0.3)
    img = ImageGrab.grabclipboard()

    if isinstance(img, Image.Image):
        extracted_text = pytesseract.image_to_string(img,lang="eng+chi_tra+fra+ara+deu+jpn+kor+rus+chi_sim")
        extracted_text = extracted_text.replace("\n", " ")
        if extracted_text.strip():
            translation = translator.translate(extracted_text, dest=resultLanguage)
            translation_text = translation.text
        else:
            print("No text found in the image.")
    else:
        print("No image found in clipboard.")
    open_translation_window()

def open_translation_window():
    global extracted_text, translation_text

    # def againButtonOnClick():
    #     app.destroy()
    #     keyMethod()
    
    def searchOnInternet():
        def searchOnInternet2():
            words = pyperclip.paste().replace("\n", "").replace(" ", "")
            webbrowser.open(f"https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/{words}")
        keyboard.press_and_release('ctrl+c')
        app.after(100, searchOnInternet2)

    def translate_text():
        input_text = input_box.get("1.0", tk.END)
        src_lang = languages[src_lang_combo.get()]
        dest_lang = languages[dest_lang_combo.get()]
        
        if input_text.strip():
            if(src_lang=="DL"):
                translated = translator.translate(input_text, dest=dest_lang)
            else:
                translated = translator.translate(input_text, src=src_lang, dest=dest_lang)
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, translated.text)
        else:
            output_box.delete("1.0", tk.END)
            output_box.insert(tk.END, "Please enter text to translate")

    def check_focus():
        if app.focus_get() is None:
            app.destroy()
        else:
            app.after(500, check_focus)

    app = ctk.CTk()
    app.title("Easy Screen Translator")
    app.geometry("535x300")
    app.iconbitmap(os.path.join(base_dir, "Google_Translate_logo.ico"))
    app.resizable(False, False)

    app.lift()
    app.attributes('-topmost', True)
    app.after_idle(app.attributes, '-topmost', False)
    app.focus_force()

    app.eval('tk::PlaceWindow . center')

    src_lang_combo = ctk.CTkComboBox(app, width=250, height=20, values=list(languages.keys()), state="readonly")
    src_lang_combo.set("🌍Detect language")
    src_lang_combo.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

    dest_lang_combo = ctk.CTkComboBox(app, width=250, height=20, values=[x for x in list(languages.keys()) if x not in ["Detect language"]], state="readonly")
    dest_lang_combo.set(list(languages.keys())[list(languages.values()).index(resultLanguage.lower())])
    dest_lang_combo.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

    input_box = ctk.CTkTextbox(app, width=250, height=125, wrap="word")
    input_box.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W+tk.E)

    output_box = ctk.CTkTextbox(app, width=250, height=125, wrap="word")
    output_box.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W+tk.E)

    difinition_button = ctk.CTkButton(app, text="Cambridge", command=searchOnInternet)
    difinition_button.place(x=50,y=222)
    translate_button = ctk.CTkButton(app, text="Translate", command=translate_text)
    translate_button.place(x=350,y=222)

    input_box.delete("1.0", tk.END)
    input_box.insert(tk.END, extracted_text)
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, translation_text)

    app.after(500, check_focus)

    app.mainloop()
keyboard.add_hotkey(key, keyMethod)
keyboard.wait()