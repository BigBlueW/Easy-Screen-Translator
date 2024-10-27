# Usage - readyToUseVersion

## Screenshot to translate
To use this program directly, you can...

In the beginning, open [EST.exe](readyToUseVersion/EST.exe). 

And you are supposed to add [EST.exe](readyToUseVersion/EST.exe) in the whitelist of McAfee or so on

to make sure the program will not be forbidden.

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
In the `Easy Screen Translator`, double click on a word you want to learn its definition, 

and clicking the button `Search` will lead you to check its definition on Cambridge dictionary.

## Translate
In the `Easy Screen Translator`, press what you want to translate left. 

And the result will provide on the right.

## Other
Since [EST.exe](readyToUseVersion/EST.exe) has no window shown (except the translator), 

To close EST.exe, you can close it in `task manager` or enter `taskkill /IM EST.exe /F` in `win+R`.

Or, you can double click on [EST.exe](readyToUseVersion/EST.exe) again, then it'll be closed.

# Usage - sourceCode
If you wanna do some change in [EST.py](sourceCode/EST.py),

after done, you can do the pyinstaller command in the top of the .py file.

The route path in that command is not full. btw

# Customize
You are allowed to change

1. default language translated to
2. key to activate the screen translate
3. where `search` button takes you
4. which language to identify via tesseract

through modifying the [config.txt](readyToUseVersion/config.txt) as below.

> resultLanguage = zh-TW
> 
> key = win+shift+l
> 
> defURL = https://dictionary.cambridge.org/dictionary/english/<word>
> 
> tesseractLangs = eng+chi_tra+fra+ara+deu+jpn+kor+rus+chi_sim

Code for `resultLanguage` is provided in [language_list.txt](readyToUseVersion/language_list.txt).

Notice: Not all languages are supported.

Language code for `tesseractLangs` is provided in its [official website](https://tesseract-ocr.github.io/tessdoc/Data-Files.html#:~:text=Data%20Files%20for%20Version%204.00%20(November%2029%2C%202016))

You can also install traineddata to [the folder](readyToUseVersion/_internal/Tesseract-OCR/tessdata) for `readyToUseVersion`

# Problem
When using this, you should know these:

1. Task manager will make hotkey forbidden, which represents that you should turn off task manager if not using it.

# Example
eg1: I used this app to translate the question above into Chinese(Taiwan):
![Image](https://github.com/BigBlueW/Easy-Screen-Translator/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-24%20190704.png)