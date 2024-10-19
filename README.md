# Usage
To use this program directly, you should...

First, unzip the EST.zip (I had to do it, because it had exceed the 100mb limit of github) to the same directory.

Next, click the EST.exe. 

After opened, the program allows you to press `Win+Shift+L` to make a screenshot

(you must confirm that Win+Shift+S is working as universal windows computer.)

Select the area you wanna translate. 

And it will popup a notification showing the result of translator.

(It will also copy the result into you clipboard)

On the other hand, `Win+Shift+;` allows you to translate into English

BTW, since EST.exe has no window shown, I make a close.bat that can turn off this program.

# Customize
You are allowed to change

1. language you wanna translate to 
2. key to activate the screen translate

via modifying the config.txt.

> resultLanguage = zh-TW
> 
> key = win+shift+l
>
> keyEn = win+shift+;

Default config is in config.txt. (worked even if config.txt is deleted)

Language list is provided in language_list.txt.

(Notice: Not all languages are supported.)

# Others
This program is made with __tesseract__. 
It only supports English, Chinese, German, French, Japanese, Korean, Russian, and Spanish.
