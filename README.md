# Usage - readyToUseVersion
To use this program directly, you should...

First, open the folder [readyToUseVersion](readyToUseVersion).

Next, click the [EST.exe](readyToUseVersion/EST.exe). 

After opened, this application has been on standby in the background.

Then, you can press `Win+Shift+L(default shortcut key)` to make a screenshot.

(you must confirm that `Win+Shift+S` is working as universal computers under windows system.)

Select the area you wanna translate. 

And it will popup a window showing a translator showing both original and translated versions.

Double click on a word you want to learn its definition, and click the button `Search`

to check its definition on Cambridge dictionary.

BTW, since [EST.exe](readyToUseVersion/EST.exe) has no window shown (except the translator), 

To close EST.exe, you can close it in `task manager` or enter `taskkill /IM EST.exe /F` in `win+R`.

Or, you can double click on [EST.exe](readyToUseVersion/EST.exe), then it'll be closed.

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

# example
eg1: I used this app to translate the question above into Chinese(Taiwan):
![Image](https://github.com/BigBlueW/Easy-Screen-Translator/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-24%20190704.png)