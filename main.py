import tkinter as tk
import pygame

from PIL import ImageTk, Image

from Interface import Interface

AUDIO_DIR = "data"


def main():
    Interface(audio_path=AUDIO_DIR)


def run():
    # initialize Tkinter object
    root = tk.Tk()

    # name it
    root.title("MP3 Player")
    # set the initial size
    root.geometry("500x400")

    # create the control frame
    controls_frame = tk.Frame(root)
    controls_frame.pack()

    song_box = tk.Listbox(root, bg="black", fg="green", width=60)
    song_box.pack(pady=20)

    # images for icons
    back_button_image = ImageTk.PhotoImage(Image.open("data/image_data/previous.png").resize((25, 25)))
    next_button_image = ImageTk.PhotoImage(Image.open("data/image_data/next.png").resize((25, 25)))
    play_button_image = ImageTk.PhotoImage(Image.open("data/image_data/play.png").resize((25, 25)))
    pause_button_image = ImageTk.PhotoImage(Image.open("data/image_data/pause.png").resize((25, 25)))
    stop_button_image = ImageTk.PhotoImage(Image.open("data/image_data/stop.png").resize((25, 25)))
    # next_button_image = tk.PhotoImage(file="data/image_data/next.png")
    # play_button_image = tk.PhotoImage(file="data/image_data/play.png")
    # pause_button_image = tk.PhotoImage(file="data/image_data/pause.png")
    # stop_button_image = tk.PhotoImage(file="data/image_data/stop.png")

    # create player control buttons
    # Next song
    next_button = tk.Button(controls_frame,
                            image=next_button_image,
                            borderwidth=0)
    # Previous song
    back_button = tk.Button(controls_frame,
                            image=back_button_image,
                            borderwidth=0)
    # Start
    play_button = tk.Button(controls_frame,
                            image=play_button_image,
                            borderwidth=0)
    # Pause
    pause_button = tk.Button(controls_frame,
                             image=pause_button_image,
                             borderwidth=0)
    # Stop
    stop_button = tk.Button(controls_frame,
                            image=stop_button_image,
                            borderwidth=0)

    # Position the buttons
    next_button.grid(row=0, column=0)
    back_button.grid(row=0, column=1)
    play_button.grid(row=0, column=2)
    pause_button.grid(row=0, column=3)
    stop_button.grid(row=0, column=4)

    # start the GUI
    root.mainloop()




# def main():
#     # enable mixer capabilities
#     pygame.mixer.init()
#
#     # initialize Tkinter object
#     root = tk.Tk()
#     # name it
#     root.title("MP4 Player")
#     # set the initial size
#     root.geometry("500x400")
#
#     # images for icons
#     back_button_image = tk.PhotoImage(file="data/image_data/previous.png")
#     next_button_image = tk.PhotoImage(file="data/image_data/next.png")
#     play_button_image = tk.PhotoImage(file="data/image_data/play.png")
#     pause_button_image = tk.PhotoImage(file="data/image_data/pause.png")
#     stop_button_image = tk.PhotoImage(file="data/image_data/stop.png")
#
#     # create the control frame
#     controls_frame = tk.Frame(root)
#     controls_frame.pack()
#
#     # create player control buttons
#     # Next song
#     next_button = tk.Button(controls_frame,
#                             image=next_button_image,
#                             borderwidth=0)
#     # Previous song
#     back_button = tk.Button(controls_frame,
#                             image=back_button_image,
#                             borderwidth=0)
#     # Start
#     play_button = tk.Button(controls_frame,
#                             image=play_button_image,
#                             borderwidth=0)
#     # Pause
#     pause_button = tk.Button(controls_frame,
#                              image=pause_button_image,
#                              borderwidth=0)
#     # Stop
#     stop_button = tk.Button(controls_frame,
#                             image=stop_button_image,
#                             borderwidth=0)
#
#     # Position the buttons
#     next_button.grid()
#     back_button.grid()
#     play_button.grid()
#     pause_button.grid()
#     stop_button.grid()
#
#     # song selection menu
#     song_box = tk.Listbox(root, bg="black", fg="green", width=60)
#     song_box.pack(pady=20)
#
#     button_play = tk.Button(root, text="play",
#                             font=("Helvetica", 12),
#                             command=play)
#     button_stop = tk.Button(root, text="stop",
#                             font=("Helvetica", 12),
#                             command=stop)
#     button_play.pack(pady=20)
#     button_stop.pack(pady=20)
#
#     root.mainloop()
#
#
# def stop():
#     pygame.mixer.music.stop()
#
#
# def play():
#     pygame.mixer.music.load("data/house_lo.mp3")
#     pygame.mixer.music.play(loops=0)


if __name__ == '__main__':
    main()
