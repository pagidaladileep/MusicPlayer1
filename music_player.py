import pygame
import os

def init_music_player():
    pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

def load_music_files():
    music_files = []
    for file in os.listdir("music"):
        if file.endswith(".mp3"):
            music_files.append(os.path.join("music", file))
    return music_files

def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    print(f"Now playing: {music_file}")

def display_menu(music_files):
    print("\nAvailable Music:")
    for idx, file in enumerate(music_files):
        print(f"{idx + 1}. {file}")
    
    choice = int(input("Enter the number of the song to play (0 to exit): "))
    
    if choice == 0:
        pygame.mixer.music.stop()
        return False
    elif 1 <= choice <= len(music_files):
        play_music(music_files[choice - 1])
    else:
        print("Invalid choice. Please try again.")
    
    return True

def main():
    init_music_player()
    music_files = load_music_files()

    if not music_files:
        print("No music files found in the 'music' directory.")
        return

    while True:
        if not display_menu(music_files):
            break

if __name__ == "__main__":
    main()
