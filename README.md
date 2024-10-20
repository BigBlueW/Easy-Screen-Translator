# Usage
To use this program directly, you should...

First, open the folder `readyToUseVersion`.

Next, click the `EST.exe`. 

After opened, this application has working in the background.

Then, you are allowed to press `Win+Shift+L` to make a screenshot.

(you must confirm that `Win+Shift+S` is working as universal computers under windows system.)

Select the area you wanna translate. 

And it will popup a window showing a UI of translator.

BTW, since `EST.exe` has no window shown (except the translator), 

I make a `close.bat` that can turn off this program.

# Customize
You are allowed to change

1. default language translated to
2. key to activate the screen translate

via modifying the config.txt in the folder `readyToUseVersion`.

> resultLanguage = zh-TW
> 
> key = win+shift+l

Default config is in `config.txt`. (worked even if `config.txt` is deleted)

Language list is provided in `language_list.txt`.

(Notice: Not all languages are supported.)

# Others
This program is made with __tesseract__. 

It only identified characters of English, Chinese, German, French, Japanese, Korean, and Russian.