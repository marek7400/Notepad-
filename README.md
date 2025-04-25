Handling (remove) Invisible Characters in Text (Python/Notepad++ script)

WARNING: 	
All invisible characters are replaced with a regular space (U+0020), and then multiple spaces are simplified to a single space. This can have different consequences for text formatting, depending on the original function of the invisible character.

Key takeaways:
The script replaces all invisible characters with regular spaces, regardless of their original function.

If the invisible characters had special formatting functions (such as controlling text direction, preventing line breaks, or special spaces with a specified width), the text may look different after the script runs.

The following characters can be particularly problematic when replacing:

ZWSP (zero width space) - a possible line break location
ZWJ/ZWNJ - used in some languages and emoticons
RTL/LTR text direction signs - important in Arabic and Hebrew

![notepad-remove.jpg](images/notepad-remove.jpg)
![notepad-remove1.jpg](images/notepad-remove1.jpg)
