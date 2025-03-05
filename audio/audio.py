import pygame
import sys

# Initialize Pygame mixer
pygame.mixer.init()

# Function to play audio
def play_audio(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Playing: {file_path}")
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except pygame.error as e:
        print(f"Error playing {file_path}: {e}")

# Command-line interface
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python play_audio.py <audio_file_path>")
        sys.exit(1)

    audio_file = sys.argv[1]
    play_audio(audio_file)
