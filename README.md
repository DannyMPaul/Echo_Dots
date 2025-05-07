# Morse Code Translator

A Python-based Morse code translator that supports:

- Text to Morse code conversion
- Morse code to text conversion
- Voice input and output
- Interactive Morse code input using spacebar (short press for dot, long press for dash)

## Requirements

- Python 3.x
- Required packages listed in `requirements.txt`

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the translator from the src directory:

```
python morse_translator.py
```

### Features

1. Text/Voice to Morse Code:

   - Type text or use voice input
   - Get Morse code output

2. Morse Code to Text/Voice:

   - Input Morse code using keyboard (spacebar method) or type dots and dashes
   - Get text output and voice pronunciation

### Keyboard Input Method

- Short spacebar press (< 0.2s) = dot (.)
- Long spacebar press (≥ 0.2s) = dash (-)
- Press ESC to finish input

## Future Enhancements

- Braille language support (coming soon)
- Additional input methods
- Support for more special characters
