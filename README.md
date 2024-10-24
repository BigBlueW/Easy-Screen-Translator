# Usage - readyToUseVersion
To use this program directly, you should...

First, open the folder [readyToUseVersion](readyToUseVersion).

Next, click the [EST.exe](readyToUseVersion/EST.exe). 

After opened, this application has been on standby in the background.

Then, you can press `Win+Shift+L` to make a screenshot.

(you must confirm that `Win+Shift+S` is working as universal computers under windows system.)

Select the area you wanna translate. 

And it will popup a window showing a translator showing both original and translated versions.

Double click on a word you want to learn its definition, and click the button `Search`

to check its definition on Cambridge dictionary.

BTW, since [EST.exe](readyToUseVersion/EST.exe) has no window shown (except the translator), 

I make a [close.bat](readyToUseVersion/close.bat) that can turn off this program.

# Usage - sourceCode
If you wanna do some change in [EST.py](sourceCode/EST.py),

after that, you can do the pyinstaller command in the top of the .py file.

The route path in that command is not full. btw

# Customize
You are allowed to change

1. default language translated to
2. key to activate the screen translate
3. where `search` button takes you
4. which language to identify via tesseract

via modifying the [config.txt](readyToUseVersion/config.txt) in the folder [readyToUseVersion](readyToUseVersion).

> resultLanguage = zh-TW
> 
> key = win+shift+l
> 
> defURL = https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/<word>
> 
> tesseractLangs = eng+chi_tra+fra+ara+deu+jpn+kor+rus+chi_sim

Code for `resultLanguage` is provided in [language_list.txt](readyToUseVersion/language_list.txt).

Notice: Not all languages are supported.

Language code for `tesseractLangs` is provided in [official website](https://tesseract-ocr.github.io/tessdoc/Data-Files.html#:~:text=Data%20Files%20for%20Version%204.00%20(November%2029%2C%202016))

You can also install traineddata to [the folder for readyToUseVersion](readyToUseVersion/_internal/Tesseract-OCR/tessdata)

# example
I used this app to translate the question above into Chinese(Taiwan):
![Image](https://github.com/BigBlueW/Easy-Screen-Translator/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202024-10-24%20190704.png)