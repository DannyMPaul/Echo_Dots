"""
Braille translation utilities using Unicode Braille patterns
"""

BRAILLE_DICT = {
    'A': '⠁', 'B': '⠃', 'C': '⠉', 'D': '⠙', 'E': '⠑',
    'F': '⠋', 'G': '⠛', 'H': '⠓', 'I': '⠊', 'J': '⠚',
    'K': '⠅', 'L': '⠇', 'M': '⠍', 'N': '⠝', 'O': '⠕',
    'P': '⠏', 'Q': '⠟', 'R': '⠗', 'S': '⠎', 'T': '⠞',
    'U': '⠥', 'V': '⠧', 'W': '⠺', 'X': '⠭', 'Y': '⠽',
    'Z': '⠵', ' ': ' ',
    '0': '⠼⠚', '1': '⠼⠁', '2': '⠼⠃', '3': '⠼⠉', '4': '⠼⠙',
    '5': '⠼⠑', '6': '⠼⠋', '7': '⠼⠛', '8': '⠼⠓', '9': '⠼⠊',
    ',': '⠂', ';': '⠆', ':': '⠒', '.': '⠲', '!': '⠖', '?': '⠦',
    '"': '⠦', '(': '⠐⠣', ')': '⠐⠜', '/': '⠌'
}

def text_to_braille(text):
    """Convert text to Braille Unicode characters"""
    braille = []
    for char in text.upper():
        if char in BRAILLE_DICT:
            braille.append(BRAILLE_DICT[char])
    return ''.join(braille)