# Usage

## Screenshot to translate
To use this program, you should make sure you have downloaded Tesseract-OCR and placed it like this [Tesseract-OCR](/sourceCode/Tesseract-OCR).

That folder should contains tessdata, tesseract.exe, and so on.

In the beginning, run this script: ```python EST.py```

After opened, this application has been on standby in the background.

Then, you can press `Win+Shift+L(default shortcut key)` to make a screenshot.

(you must confirm that `Win+Shift+S` is working as universal computers under windows system.)

Select the area you wanna translate. 

And it will popup a window showing a translator showing both original and translated versions.

## Copy to translate
To use the method, you should copy texts into your clipboard,

then press `Win+Shift+L(default shortcut key)` and `esc`. 

Eventually, the source text will be copied from the clipboard simply.

## Definition
In the windows of `Easy Screen Translator`, double click on a word you want to learn its definition, 

and clicking the button `Search` will lead you to check its definition on Cambridge dictionary.

## Translate
In the windows of `Easy Screen Translator`, press what you want to translate on the left side. 

And the result will provide on the right side.

# Change
I deleted the `readyToUseVersion` and only kept [sourceCode](/sourceCode) 

for the reason that Tesseract-OCR is not a part of my code.

You are supposed to use pyinstaller to make yourself a readyToUseVersion.

Code for pyinstaller is provided in the first line of EST.py.

# Customize
You are allowed to change

1. default language translated to
2. key to activate the screen translate
3. where `search` button takes you
4. which language to identify via tesseract

through modifying the [config.txt](sourceCode/config.txt) present below.

> resultLanguage = zh-TW
> 
> key = win+shift+l
> 
> defURL = https://dictionary.cambridge.org/dictionary/english/<word>
> 
> tesseractLangs = eng+chi_tra+fra+ara+deu+jpn+kor+rus+chi_sim

Code for `resultLanguage` is provided in [language_list.txt](sourceCode/language_list.txt).

Notice: Not all languages are supported.

Language code for `tesseractLangs` is provided in its [official website](https://tesseract-ocr.github.io/tessdoc/Data-Files.html#:~:text=Data%20Files%20for%20Version%204.00%20(November%2029%2C%202016))

# Problem
When using this, you should know these:

1. Task manager will make hotkey forbidden, which represents that you should turn off task manager if not using it.

# Example
eg1: I used this app to translate the question above into Chinese(Taiwan):
![Image](https://github.com/BigBlueW/Easy-Screen-Translator/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-24%20190704.png)
