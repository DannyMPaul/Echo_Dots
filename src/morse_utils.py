MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': ' '
}

# Create reverse mapping for morse to text conversion
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Convert text to Morse code"""
    morse = []
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse.append(MORSE_CODE_DICT[char])
    return ' '.join(morse)

def morse_to_text(morse):
    """Convert Morse code to text"""
    text = []
    morse_chars = morse.split(' ')
    for char in morse_chars:
        if char in REVERSE_MORSE_DICT:
            text.append(REVERSE_MORSE_DICT[char])
        elif char == '':  # Handle word spaces (multiple spaces between words)
            if text and text[-1] != ' ':
                text.append(' ')
    return ''.join(text)