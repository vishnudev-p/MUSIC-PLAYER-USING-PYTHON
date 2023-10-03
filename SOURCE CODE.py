import pygame
import os
import tkinter as tk
from tkinter import Listbox

class MusicPlayer:

    def __init__(self, root):
        self.root = root
        root.geometry('250x400')
        root.title('iPod-inspired Music Player')
        root.configure(bg='#282828')

        pygame.init()
        pygame.mixer.init()

        self.track = tk.StringVar()
        self.status = tk.StringVar()

        # iPod Screen Frame
        screenframe = tk.LabelFrame(root, bg="#0A0A0A", bd=5)
        screenframe.place(relx=0.5, rely=0.2, relwidth=0.8, relheight=0.6, anchor="n")

        # Track Info
        songtrack = tk.Label(screenframe, textvariable=self.track, font=("Arial", 12, "bold"), bg="#0A0A0A", fg="#FFFFFF")
        songtrack.pack(pady=10)

        # Track Status
        trackstatus = tk.Label(screenframe, textvariable=self.status, font=("Arial", 10), bg="#0A0A0A", fg="#FFFFFF")
        trackstatus.pack(pady=10)

        # Listbox for songs
        self.playlist = Listbox(screenframe, bg="#333333", fg="#FFFFFF", bd=0, font=("Arial", 10))
        self.playlist.pack(fill=tk.BOTH, pady=20, padx=10)

        # Populate the Listbox
        for song in list_songs('C:\\Users\\HP\\Desktop\\MUSIC PLAYER USING PYTHON\\MUSICS'):
            self.playlist.insert(tk.END, song)

        # Control buttons
        frame_controls = tk.LabelFrame(root, bg="#282828")
        frame_controls.place(relx=0.5, rely=0.85, relwidth=0.8, relheight=0.1, anchor="n")

        # Without images, using text buttons
        play_button = tk.Button(frame_controls, text="Play", command=self.play_song, bg="#0A0A0A", fg="#FFFFFF")
        play_button.grid(row=0, column=1, padx=5)
        
        stop_button = tk.Button(frame_controls, text="Stop", command=self.stop_song, bg="#0A0A0A", fg="#FFFFFF")
        stop_button.grid(row=0, column=2, padx=5)
        
        pause_button = tk.Button(frame_controls, text="Pause", command=self.pause_unpause_song, bg="#0A0A0A", fg="#FFFFFF")
        pause_button.grid(row=0, column=3, padx=5)
        
        prev_button = tk.Button(frame_controls, text="Prev", command=self.prev_song, bg="#0A0A0A", fg="#FFFFFF")
        prev_button.grid(row=0, column=0, padx=5)
        
        next_button = tk.Button(frame_controls, text="Next", command=self.next_song, bg="#0A0A0A", fg="#FFFFFF")
        next_button.grid(row=0, column=4, padx=5)

    def play_song(self):
        selected_song = self.playlist.get(tk.ACTIVE)
        pygame.mixer.music.load(os.path.join('C:\\Users\\HP\\Desktop\\MUSIC PLAYER USING PYTHON\\MUSICS', selected_song))
        pygame.mixer.music.play()
        self.track.set(selected_song)
        self.status.set("Playing")

    def stop_song(self):
        pygame.mixer.music.stop()
        self.status.set("Stopped")

    def pause_unpause_song(self):
        if pygame.mixer.music.get_busy():
            if pygame.mixer.music.get_pos() == -1:
                pygame.mixer.music.unpause()
                self.status.set("Playing")
            else:
                pygame.mixer.music.pause()
                self.status.set("Paused")

    def next_song(self):
        # Find the index of the currently selected song and try to play the next one.
        next_one = self.playlist.curselection()[0] + 1
        if next_one < self.playlist.size():
            self.playlist.selection_clear(0, tk.END)
            self.playlist.activate(next_one)
            self.playlist.selection_set(next_one)
            self.play_song()

    def prev_song(self):
        # Find the index of the currently selected song and try to play the previous one.
        prev_one = self.playlist.curselection()[0] - 1
        if prev_one >= 0:
            self.playlist.selection_clear(0, tk.END)
            self.playlist.activate(prev_one)
            self.playlist.selection_set(prev_one)
            self.play_song()

def list_songs(directory):
    return [song for song in os.listdir(directory) if song.endswith(('.mp3', '.wav'))]

root = tk.Tk()
MusicPlayer(root)
root.mainloop()
