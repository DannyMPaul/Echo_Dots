from morse_utils import text_to_morse, morse_to_text
from voice_handler import VoiceHandler

class MorseTranslator:
    def __init__(self):
        self.voice_handler = VoiceHandler()

    def text_input_to_morse(self, text=None):
        """Convert text input to morse code"""
        if text is None:
            # Get voice input if no text is provided
            text = self.voice_handler.listen_for_speech()
            if text is None:
                return None
            print(f"Recognized text: {text}")
        
        morse = text_to_morse(text)
        print(f"Morse code: {morse}")
        return morse

    def morse_input_to_text(self, morse=None):
        """Convert morse code to text"""
        if morse is None:
            # Get morse input using spacebar if no morse code is provided
            morse = self.voice_handler.record_morse_input()
        
        text = morse_to_text(morse)
        print(f"Decoded text: {text}")
        self.voice_handler.speak_text(text)  # Speak the decoded text
        return text

def main():
    translator = MorseTranslator()
    
    while True:
        print("\nMorse Code Translator")
        print("1. English to Morse Code")
        print("2. Morse Code to English")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            use_voice = input("Use voice input? (y/n): ").lower() == 'y'
            if use_voice:
                translator.text_input_to_morse()
            else:
                text = input("Enter text to convert: ")
                translator.text_input_to_morse(text)
        
        elif choice == '2':
            use_keyboard = input("Use spacebar input? (y/n): ").lower() == 'y'
            if use_keyboard:
                translator.morse_input_to_text()
            else:
                morse = input("Enter morse code (use . and - separated by spaces): ")
                translator.morse_input_to_text(morse)
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()