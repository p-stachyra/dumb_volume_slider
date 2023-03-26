# global imports
import os
import pygame
import tkinter as tk
import tkinter.filedialog
import sys

from PIL import ImageTk, Image


class Interface:
    def __init__(self, audio_path):
        # initialize mixer from PyGame
        pygame.mixer.init()

        # set the default directory for opening MP3 files
        self.audio_path = audio_path

        # checks for application data availability
        try:
            image_names = os.listdir("data/image_data")
            # these button image names are expected to be found.
            for img_name in ["previous.png", "next.png", "play.png", "pause.png", "stop.png"]:
                if img_name not in image_names:
                    sys.exit("Could not find application images.")
        except FileNotFoundError:
            sys.exit("The application data folder could not be found. The application cannot work properly.")

        # initialize Tkinter object
        self.root = tk.Tk()

        # name it
        self.root.title("MP3 Player")
        # set the initial size
        self.root.geometry("500x400")

        # create the master frame
        self.master_frame = tk.Frame(self.root, padx=5, pady=10, bg="yellow")
        self.master_frame.pack(pady=20)

        # create the song box frame
        self.song_box = tk.Listbox(self.master_frame, bg="black", fg="green", width=60)
        self.song_box.grid(row=0, column=0)

        # create the control frame
        self.controls_frame = tk.Frame(self.master_frame, pady=25, bg="blue")
        self.controls_frame.grid(row=1, column=0)

        # create the volume frame
        self.volume_frame = tk.LabelFrame(self.master_frame,
                                          fg="white",
                                          bg="blue",
                                          highlightcolor="yellow",
                                          padx=5,
                                          pady=5)
        self.volume_frame.grid(row=3, column=0)

        # manage the slider
        self.volume_slider = tk.Scale(self.volume_frame, from_=0, to=1,
                                      resolution=0.1,
                                      activebackground="green",
                                      orient=tk.HORIZONTAL,
                                      command=self.volume, length=125)
        self.volume_slider.pack()

        # images for icons
        back_button_image = ImageTk.PhotoImage(Image.open("data/image_data/previous.png").resize((25, 25)))
        next_button_image = ImageTk.PhotoImage(Image.open("data/image_data/next.png").resize((25, 25)))
        play_button_image = ImageTk.PhotoImage(Image.open("data/image_data/play.png").resize((25, 25)))
        pause_button_image = ImageTk.PhotoImage(Image.open("data/image_data/pause.png").resize((25, 25)))
        stop_button_image = ImageTk.PhotoImage(Image.open("data/image_data/stop.png").resize((25, 25)))

        # create player control buttons
        # Next song
        next_button = tk.Button(self.controls_frame,
                                image=next_button_image,
                                borderwidth=0,
                                command=self.next_song)
        # Previous song
        back_button = tk.Button(self.controls_frame,
                                image=back_button_image,
                                borderwidth=0,
                                command=self.previous_song)
        # Start
        play_button = tk.Button(self.controls_frame,
                                image=play_button_image,
                                borderwidth=0,
                                command=self.play)
        # Pause
        pause_button = tk.Button(self.controls_frame,
                                 image=pause_button_image,
                                 borderwidth=0,
                                 command=self.pause)
        # Stop
        stop_button = tk.Button(self.controls_frame,
                                image=stop_button_image,
                                borderwidth=0,
                                command=self.stop)

        # Position the buttons
        next_button.grid(row=0, column=0, padx=10)
        back_button.grid(row=0, column=1, padx=10)
        play_button.grid(row=0, column=2, padx=10)
        pause_button.grid(row=0, column=3, padx=10)
        stop_button.grid(row=0, column=4, padx=10)

        # menu functionality
        mymenu = tk.Menu(self.root)
        self.root.config(menu=mymenu)
        add_song_menu = tk.Menu(mymenu)
        mymenu.add_cascade(label="Add Songs", menu=add_song_menu)
        add_song_menu.add_command(label="Add a song to the playlist ...", command=self.add_song)

        # variables for state
        self.is_paused = False

        # start the GUI
        self.root.mainloop()

    @staticmethod
    def stop():
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            print("LOGGED: %s" % e)

    def play(self):
        try:
            song = self.song_box.get(tk.ACTIVE)
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
        except Exception as e:
            print("LOGGED: %s" % e)

    def pause(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
        else:
            pygame.mixer.music.unpause()
            self.is_paused = False

    def next_song(self):
        # current song
        current = self.song_box.curselection()
        # next one's index
        try:
            next_s = int(current[0]) + 1
            song = self.song_box.get(next_s)
            # play the next one
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            # reset the bar
            self.song_box.selection_clear(0, tk.END)
            self.song_box.activate(next_s)
            self.song_box.selection_set(next_s, last=None)
        # the case that there are no other songs : idle behavior
        except Exception as e:
            print("LOGGED: %s." % e)
            pass

    def previous_song(self):
        # current song
        current = self.song_box.curselection()
        # previous one's index
        try:
            next_s = int(current[0]) - 1
            song = self.song_box.get(next_s)
            # play the previous one
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(loops=0)
            # reset the bar
            self.song_box.selection_clear(0, tk.END)
            self.song_box.activate(next_s)
            self.song_box.selection_set(next_s, last=None)
        # the case that there are no other songs : idle behavior
        except Exception as e:
            print("LOGGED: %s." % e)
            pass

    def add_song(self):
        song = tkinter.filedialog.askopenfile(initialdir=self.audio_path, title="Select file",
                                              filetypes=([("mp3 Files", "*.mp3")]))
        if song is None:
            pass
        else:
            self.song_box.insert(tk.END, song.name)

    def volume(self, position):
        pygame.mixer.music.set_volume(self.volume_slider.get())
