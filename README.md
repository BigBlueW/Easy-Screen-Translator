# Usage
To use this program directly, you should...

First, open the folder `readyToUseVersion`.

Next, click the `EST.exe`. 

After opened, this application has been on standby in the background.

Then, you can press `Win+Shift+L` to make a screenshot.

(you must confirm that `Win+Shift+S` is working as universal computers under windows system.)

Select the area you wanna translate. 

And it will popup a window showing a translator showing both original and translated versions.

Double click on a word you want to learn its definition, and click the button "Search" 

to check its definition on Cambridge dictionary.

BTW, since `EST.exe` has no window shown (except the translator), 

I make a `close.bat` that can turn off this program.

# Customize
You are allowed to change

1. default language translated to
2. key to activate the screen translate
3. where "search" button takes you

via modifying the config.txt in the folder `readyToUseVersion`.

> resultLanguage = zh-TW
> 
> key = win+shift+l
> 
> defURL = https://dictionary.cambridge.org/zht/%E8%A9%9E%E5%85%B8/%E8%8B%B1%E8%AA%9E/<word>

# Others
This program is made with __tesseract__. 

It only identified characters of English, Chinese, German, French, Japanese, Korean, and Russian.

Default config is in `config.txt`. (worked even if `config.txt` is deleted)

Language list is provided in `language_list.txt`.

Notice: Not all languages are supported.