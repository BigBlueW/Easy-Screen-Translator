# Usage
To use this program directly, you should...

First, open the folder `readyToUseVersion`.

Next, click the `EST.exe`. 

After opened, this application has been on standby in the background.

Then, you can press `Win+Shift+L` to make a screenshot.

(you must confirm that `Win+Shift+S` is working as universal computers under windows system.)

Select the area you wanna translate. 

And it will popup a window showing a translator showing both original and translated versions.

Double click on a word you want to learn its definition, and click the button `Search`

to check its definition on Cambridge dictionary.

BTW, since `EST.exe` has no window shown (except the translator), 

I make a `close.bat` that can turn off this program.

# Customize
You are allowed to change

1. default language translated to
2. key to activate the screen translate
3. where `search` button takes you
4. which language to identify via tesseract

via modifying the config.txt in the folder `readyToUseVersion`.

> resultLanguage = zh-TW
> 
> key = win+shift+l
> 
> defURL = https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/<word>
> 
> tesseractLangs = eng+chi_tra+fra+ara+deu+jpn+kor+rus+chi_sim

Code for `resultLanguage` is provided in `language_list.txt`.

Notice: Not all languages are supported.

Language code for `tesseractLangs` is provided in [official website](https://tesseract-ocr.github.io/tessdoc/Data-Files.html#:~:text=Data%20Files%20for%20Version%204.00%20(November%2029%2C%202016))

You can also install traineddata to [the folder](readyToUseVersion\_internal\Tesseract-OCR\tessdata) or [the folder](sourceCode\Tesseract-OCR\tessdata)