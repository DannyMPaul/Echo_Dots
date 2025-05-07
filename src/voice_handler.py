import speech_recognition as sr
import pyttsx3
import time
import keyboard

class VoiceHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
    def listen_for_speech(self):
        """Listen for speech input and return the recognized text"""
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
            
        try:
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

    def speak_text(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def record_morse_input(self):
        """Record morse code input using spacebar (. for short press, - for long press)"""
        morse = []
        key_down_time = 0
        last_input_time = time.time()
        print("Press spacebar for morse input (short press for dot, long press for dash)")
        print("Press ESC to finish input")
        
        while True:
            current_time = time.time()
            
            # Check for letter separation (pause longer than 0.5 seconds)
            if morse and current_time - last_input_time > 1 and morse[-1] != ' ':
                morse.append(' ')
                print(' ', end='', flush=True)
            
            if keyboard.is_pressed('space') and key_down_time == 0:
                key_down_time = current_time
            elif not keyboard.is_pressed('space') and key_down_time > 0:
                duration = current_time - key_down_time
                if duration < 0.2:  # Short press
                    morse.append('.')
                    print('.', end='', flush=True)
                else:  # Long press
                    morse.append('-')
                    print('-', end='', flush=True)
                key_down_time = 0
                last_input_time = current_time
            
            if keyboard.is_pressed('esc'):
                print("\nFinished recording morse code")
                break
                
            time.sleep(0.01)  # Small delay to prevent high CPU usage
            
        return ''.join(morse)