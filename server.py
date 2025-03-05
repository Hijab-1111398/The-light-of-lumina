from flask import Flask, request, jsonify
import pygame

app = Flask(__name__)

# Initialize Pygame mixer
pygame.mixer.init()

# Function to play audio
def play_audio(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        return {"status": "success", "message": f"Playing: {file_path}"}
    except pygame.error as e:
        return {"status": "error", "message": str(e)}

@app.route('/play-audio', methods=['POST'])
def play_audio_endpoint():
    data = request.json
    file_path = data.get('file_path', '')
    if not file_path:
        return jsonify({"status": "error", "message": "File path not provided"}), 400

    response = play_audio(file_path)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
