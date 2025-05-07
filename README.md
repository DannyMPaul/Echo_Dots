# Morse & Braille Translator

A modern web application that translates between text, Morse code, and Braille with support for both desktop and mobile devices.

## Features

### Text to Morse Code

- Convert any text to Morse code
- Automatic vibration feedback on mobile devices
- "Play Morse Pattern" button to feel the pattern through vibration
- Support for letters, numbers, and common punctuation

### Morse Code to Text

Multiple input methods:

- Tap/hold button: Quick tap for dot (.), long press for dash (-)
- Manual buttons: Separate buttons for dot, dash, and space
- Direct typing: Type dots (.) and dashes (-) manually
- Haptic feedback on mobile devices

### Text to Braille

- Convert text to Unicode Braille patterns
- Support for letters, numbers, and punctuation marks
- Optimized display with proper spacing and sizing

### Progressive Web App (PWA) Features

- Works offline
- Installable on mobile devices
- Responsive design for all screen sizes
- Dark/Light theme support
- Add to home screen functionality

## Requirements

- Python 3.x
- Required packages listed in `requirements.txt`
- Modern web browser with JavaScript enabled

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

1. Start the Flask server:
   ```
   cd src
   python app.py
   ```
2. Access the application:
   - Desktop: Open `http://localhost:5000` in your browser
   - Mobile: Connect to the same network as the server and visit `http://<server-ip>:5000`

### Mobile Features

- Haptic feedback for Morse code input/output
- Touch-optimized interface
- Installable as a standalone app
- Works offline once installed

### Keyboard Shortcuts

- Enter: Translate input
- Space: Add space in Morse code input
- Tap/Hold: Generate Morse code dots and dashes

## Timing Reference

- Dot (.) = Short press/vibration (200ms)
- Dash (-) = Long press/vibration (500ms)
- Symbol gap = 200ms
- Letter gap = 500ms
- Word gap = 1000ms

## Future Enhancements

- Enhanced Braille support with additional patterns
- Voice input/output improvements
- Support for more special characters
- Additional language support
