from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
from morse_utils import text_to_morse, morse_to_text
from braille_utils import text_to_braille

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.get_json()
        if not data or 'text' not in data or 'direction' not in data:
            return jsonify({'error': 'Invalid request data'}), 400
            
        text = data['text'].strip()
        direction = data['direction']
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
            
        if direction == 'to_morse':
            result = text_to_morse(text)
        elif direction == 'to_braille':
            result = text_to_braille(text)
        else:  # to_text
            result = morse_to_text(text)
            
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)