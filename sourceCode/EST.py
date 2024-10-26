#pyinstaller --noconfirm --onedir --windowed --hidden-import plyer.platforms.win.notification --add-data "sourceCode\config.txt;." --add-data "sourceCode\Google_Translate_logo.ico;." --add-data "sourceCode\Tesseract-OCR;Tesseract-OCR/" --add-data "AppData\Local\Programs\Python\Python310\Lib\site-packages\customtkinter;customtkinter/"  "sourceCode\EST.py" --noconsole

import customtkinter as ctk
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
import plyer
import psutil

def tooltip(msg):
    plyer.notification.notify(
        title="EST",
        message=msg,
    )
    
#setup
try:
    if (sum(1 for i in psutil.process_iter() if i.name() == "EST.exe") >= 2): 
        tooltip("EST.exe has been closed.")
        time.sleep(.5)
        os.system("taskkill /IM EST.exe /F")
        sys.exit()
except:
    pass

extracted_text:str = ""
translation_text:str = ""
img = ImageGrab.grabclipboard()
translator = Translator()
base_dir:str = os.path.dirname(os.path.abspath(__file__))
exe_dir:str = os.path.dirname(sys.argv[0] if getattr(sys, 'frozen', False) else os.path.abspath(__file__))  
pytesseract.pytesseract.tesseract_cmd = os.path.join(base_dir, "Tesseract-OCR", "tesseract.exe")
languages = {
    "🌍Detect language": "auto",
    "🇺🇸English": "en",
    "🇹🇼中文 (臺灣)": "zh-TW",
    "🇨🇳中文 (中国)": "zh-CN",
    "🇫🇷Français": "fr",
    "🇩🇪Deutsch": "de",
    "🇯🇵日本語": "ja",
    "🇰🇷한국어": "ko",
    "🇷🇺Русский": "ru",
}
#/

#config
config = {}
try:
    with open(os.path.join(exe_dir, "config.txt"), "r") as f:
        for line in f:
            if line.strip() and not line.startswith("#"):
                key_, value = line.split("=", 1)
                config[key_.strip()] = value.strip()
except FileNotFoundError:
    tooltip("Config file not found. Using default settings.")

resultLanguage:str = config.get("resultLanguage", "zh-TW")
key:str = config.get("key", "win+shift+l")
defURL:str = config.get("defURL", "https://dictionary.cambridge.org/dictionary/english/<word>")
tesseractLangs:str = config.get("tesseractLangs", "eng+chi_tra+fra+ara+deu+jpn+kor+rus+chi_sim")
#/

tooltip("EST is now ready to work.")

def keyMethod():
    global extracted_text, translation_text, img
    extracted_text = ""
    translation_text = ""

    sendMethod = "Image"
    keyboard.press_and_release('win+shift+s')
    while True:
        if not mouse.is_pressed('left'):
            if keyboard.is_pressed("esc"):
                sendMethod = "Text"
                break
            else:
                time.sleep(0.001)
        elif mouse.is_pressed('left'):
            while mouse.is_pressed('left'):
                time.sleep(0.1)
            break
    if sendMethod == "Image":
        imgReceived = False
        for x in range(10): 
            # it often passes in one time; however, sometimes it doesn't. So try ten times here.
            try:
                time.sleep(0.3)
                img = ImageGrab.grabclipboard()
                imgReceived = True
                break
            except:
                pass
        if imgReceived and isinstance(img, Image.Image):
            extracted_text = pytesseract.image_to_string(img,lang=tesseractLangs)
            extracted_text = extracted_text.replace("\n", " ").replace("|", "I") # tesseract always misidentify I into |. that's why
            if extracted_text.strip():
                translation_text = translator.translate(extracted_text, dest=resultLanguage).text
            else:
                tooltip("No text found in the image.")
        else:
            tooltip("No image found in clipboard or image cannot be opened.")
            sendMethod = "Text2" # if no image found, use text to translate

    if sendMethod == "Text" or sendMethod == "Text2":  
            extracted_text = pyperclip.paste()
            if extracted_text.strip():
                translation_text = translator.translate(extracted_text, dest=resultLanguage).text
            else:
                if sendMethod == "Text": tooltip("No text found in clipboard.")
                else: tooltip("No image found in clipboard or image cannot be opened.")

    open_translation_window()
def open_translation_window():
    global extracted_text, translation_text
    
    def searchOnInternet():
        def searchOnInternet2():
            words = pyperclip.paste().replace("\n", "").replace(" ", "")
            webbrowser.open(defURL.replace("<word>", words))
        keyboard.press_and_release('ctrl+c')
        app.after(100, searchOnInternet2)

    def translateText():
        extracted_text = input_box.get("1.0", ctk.END)
        
        if extracted_text.strip():
            translation_text = translator.translate(extracted_text, dest=(languages[dest_lang_combo.get()])).text
            output_box.delete("1.0", ctk.END)
            output_box.insert(ctk.END, translation_text)
        else:
            output_box.delete("1.0", ctk.END)
            output_box.insert(ctk.END, "Please enter text to translate")

    def app_destroy(self):
        # check if nothing is on focus then destroy. Without this we cannot focus on another element in the app
        focused_widget = app.focus_get()
        
        if focused_widget is None:
            app.destroy()

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
    src_lang_combo.grid(row=0, column=0, padx=10, pady=10)
    
    dest_lang_combo = ctk.CTkComboBox(app, width=250, height=20, values=[x for x in list(languages.keys()) if x not in ["🌍Detect language"]], state="readonly")
    dest_lang_combo.set(list(languages.keys())[list(languages.values()).index(resultLanguage)])
    dest_lang_combo.grid(row=0, column=1, padx=10, pady=10)
    
    input_box = ctk.CTkTextbox(app, width=250, height=125, wrap="word", font=("default", 20))
    input_box.grid(row=1, column=0, padx=10, pady=10)
    
    output_box = ctk.CTkTextbox(app, width=250, height=125, wrap="word", font=("default", 20))
    output_box.grid(row=1, column=1, padx=10, pady=10)
    
    difinition_button = ctk.CTkButton(app, width=250, text="Search", command=searchOnInternet)
    difinition_button.grid(row=2, column=0, padx=10, pady=10)#.place(x=50,y=222)
    
    translate_button = ctk.CTkButton(app, width=250, text="Translate", command=translateText)
    translate_button.grid(row=2, column=1, padx=10, pady=10)#.place(x=350,y=222)
    
    input_box.delete("1.0", ctk.END)
    input_box.insert(ctk.END, extracted_text)
    
    output_box.delete("1.0", ctk.END)
    output_box.insert(ctk.END, translation_text)
    
    app.after(500, lambda: app.bind("<FocusOut>", app_destroy))
    input_box.focus_set()
    app.mainloop()
keyboard.add_hotkey(key, keyMethod)
keyboard.wait()