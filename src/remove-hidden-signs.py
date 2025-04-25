   # -*- coding: utf-8 -*-
import re
import ctypes

def msg(message, title=u"NPP-script"):
    ctypes.windll.user32.MessageBoxW(0, message, title, 0)

msg(u"Script running.", u"Invisible characters")

text = editor.getText()
# List of "invisible" whitespace and control characters
all_invis = ( 
    u'\u00A0'  # NBSP – NO-BREAK SPACE (U+00A0)
    u'\u00AD'  # SHY – SOFT HYPHEN (U+00AD)
    u'\u180E'  # MVS – MONGOLIAN VOWEL SEPARATOR (U+180E)
    u'\u2000'  # EN QUAD – (U+2000)
    u'\u2001'  # EM QUAD – (U+2001)
    u'\u2002'  # EN SPACE – (U+2002)
    u'\u2003'  # EM SPACE – (U+2003)
    u'\u2004'  # THREE-PER-EM SPACE – (U+2004)
    u'\u2005'  # FOUR-PER-EM SPACE – (U+2005)
    u'\u2006'  # SIX-PER-EM SPACE – (U+2006)
    u'\u2007'  # FIGURE SPACE – (U+2007)
    u'\u2008'  # PUNCTUATION SPACE – (U+2008)
    u'\u2009'  # THIN SPACE – (U+2009)
    u'\u200A'  # HAIR SPACE – (U+200A)
    u'\u200B'  # ZWSP – ZERO WIDTH SPACE (U+200B)
    u'\u200C'  # ZWNJ – ZERO WIDTH NON-JOINER (U+200C)
    u'\u200D'  # ZWJ – ZERO WIDTH JOINER (U+200D)
    u'\u200E'  # LRM – LEFT-TO-RIGHT MARK (U+200E)
    u'\u200F'  # RLM – RIGHT-TO-LEFT MARK (U+200F)
    u'\u202A'  # LRE – LEFT-TO-RIGHT EMBEDDING (U+202A)
    u'\u202B'  # RLE – RIGHT-TO-LEFT EMBEDDING (U+202B)
    u'\u202C'  # PDF – POP DIRECTIONAL FORMATTING (U+202C)
    u'\u202D'  # LRO – LEFT-TO-RIGHT OVERRIDE (U+202D)
    u'\u202E'  # RLO – RIGHT-TO-LEFT OVERRIDE (U+202E)
    u'\u205F'  # MMSP – MEDIUM MATHEMATICAL SPACE (U+205F)
    u'\u2060'  # WJ – WORD JOINER (U+2060)
    u'\u2061'  # IP – INVISIBLE FUNCTION APPLICATION (U+2061)
    u'\u2062'  # IT – INVISIBLE TIMES (U+2062)
    u'\u2063'  # FA – INVISIBLE SEPARATOR (U+2063)
    u'\u2064'  # IS – INVISIBLE PLUS (U+2064)
    u'\u2066'  # LRI – LEFT-TO-RIGHT ISOLATE (U+2066)
    u'\u2067'  # RLI – RIGHT-TO-LEFT ISOLATE (U+2067)
    u'\u2068'  # FSI – FIRST STRONG ISOLATE (U+2068)
    u'\u2069'  # PDI – POP DIRECTIONAL ISOLATE (U+2069)
    u'\uFEFF'  # BOM – BYTE ORDER MARK (U+FEFF)
    u'\u3000'  # IDEOGRAPHIC SPACE – (U+3000)
)

regex = u'[' + all_invis + u']'

# Find and count all invisible characters
found = re.findall(regex, text)
found_types = {}

for c in found:
    if c in found_types:
        found_types[c] += 1
    else:
        found_types[c] = 1

# Show summary of found characters
msg(
    u'Found invisible characters: %d\n%s' % (
        len(found),
        "\n".join(u'U+%04X : %d' % (ord(k), v) for (k, v) in found_types.items())
    ),
    u"Summary"
)

# Replace all invisible characters with spaces
new_text = re.sub(regex, u' ', text)
# Simplify multiple spaces into one
new_text = re.sub(u'[ ]{2,}', u' ', new_text)

editor.setText(new_text.encode('utf-8'))

msg(u"Invisible characters have been removed or replaced with spaces!", u"NPP-script")
