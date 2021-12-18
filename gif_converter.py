# 2021 Krzysztof Budek

import tkinter as tk
import imageio
import os

from tkinter.font import Font
from tkinter import filedialog, Text

clips = []

def choose_a_clip():
    for widget in list_frame.winfo_children():
        widget.destroy()

    if len(clips) < 8:
        file = filedialog.askopenfilename(initialdir="/", title="Select a clip",
                                                        filetypes = (("video", "*.mp4 *.webm"), ("all files", "*.*")))

        if file:
            if not file in clips:
                # add clip to a list
                clips.append(file)
            else:
                # display error - video already in list
                tk.messagebox.showwarning(title='Error', message="That video is already on a list.")

    else:
        tk.messagebox.showwarning(title='Error', message="You can't add more than 8 videos at once.")

    for clip in clips:
        name = os.path.basename(clip)
        label = tk.Label(list_frame, text=name, bg="#CCAFA5", font=fut13)
        label.pack()
        print("*")

def clear_clips():
    for widget in list_frame.winfo_children():
        widget.destroy()

    clips.clear()

    for clip in clips:
        name = os.path.basename(clip)
        label = tk.Label(list_frame, text=name, bg="#CCAFA5", font=fut13)
        label.pack()

def gif_maker(file_path, target_format):
    output_path = os.path.splitext(file_path)[0] + target_format

    read_video = imageio.get_reader(file_path)
    fps = read_video.get_meta_data()['fps']
    writer = imageio.get_writer(output_path, fps=fps)

    for frame in read_video:
        writer.append_data(frame)

    writer.close()

def convert_to_gifs():
    target_format = '.gif'

    if clips:
        for clip in clips:
            gif_maker(clip, target_format)
        tk.messagebox.showinfo(title='Conversion successful', message='All videos have been successfuly converted to gifs.')
        clear_clips()
    else:
        tk.messagebox.showwarning(title='Error', message="You haven't selected any videos yet.")

# create window
root = tk.Tk()
root.title("GIF Converter")

# fonts
fut14 = Font(family="Futura", size=14)
fut16 = Font(family="Futura", size=16)
fut13 = Font(family="Futura", size=13)
fut20 = Font(family="Times New Roman", size=62)

# window width, height and color
canvas = tk.Canvas(root, height=600, width=800, bg="#EDE7DC")
canvas.pack()

# header frame
frame1 = tk.Frame(root, bg="#647C90")
frame1.place(relwidth=1, relheight=0.2)

# header text frame
frame1_header = tk.Label(frame1, text='GIF CONVERTER', font=fut20, bg="#647C90")
frame1_header.place(relwidth=0.9, relx=0.05, rely=0.05)

# frame for holding list of videos
list_frame_holder = tk.Frame(root, bg="#CCAFA5")
list_frame_holder.place(relwidth=0.3, relheight=0.5, rely=0.3, relx=0.05)

# frame with actual list of videos
list_frame = tk.Frame(list_frame_holder, bg="#CCAFA5")
list_frame.place(relwidth=0.9, relheight=0.6, rely=0.15, relx=0.05)

# label FILES
lab = tk.Label(list_frame_holder, text='FILES', bg="#CCAFA5", font=fut14)
lab.pack(pady=0.15, ipady=10)

# frame containing buttons
frame2 = tk.Frame(root, bg="#DCD2CC")
frame2.place(relwidth=0.55, relheight=0.5, relx=0.4, rely=0.3)

# buttons
add_video_button = tk.Button(frame2, text="Add Video", height=10, padx=10, pady=5, fg="black", bg="#FBEEAC", font=fut14, command = choose_a_clip)
add_video_button.pack(side='right', padx=10)

convert_to_gif = tk.Button(frame2, text="Convert all to gif", height=10, padx=10, pady=5, fg="black", bg="#FBEEAC", font=fut14, command = convert_to_gifs)
convert_to_gif.pack(side='right', padx=10)

clear = tk.Button(frame2, text="Clear", height=10, padx=10, pady=5, fg="black", bg="#FBEEAC", font=fut14, command = clear_clips)
clear.pack(side='right', padx=10)

# mainloop
root.mainloop()


