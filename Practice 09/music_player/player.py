import pygame
import os


class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        self.playlist = [
            "music/track1.wav",
            "music/track2.wav"
        ]

        self.current_index = 0
        self.is_playing = False
        self.is_paused = False

    def load_track(self):
        track_path = self.playlist[self.current_index]
        pygame.mixer.music.load(track_path)

    def play(self):
        if not self.is_playing:
            self.load_track()
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused = False
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False

    def next_track(self):
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False

    def previous_track(self):
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True
        self.is_paused = False

    def get_current_track_name(self):
        return os.path.basename(self.playlist[self.current_index])

    def get_position(self):
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms < 0:
            return 0
        return pos_ms // 1000