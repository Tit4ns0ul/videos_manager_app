import tkinter as tk
import json

def list_all_videos(videos):
    if not videos:
        output_label.config(text="No videos available.")
    else:
        output = ""
        for index, video in enumerate(videos, start=1):
            output += f"{index}. Name: {video['name']}, Duration: {video['time']}, Link: {video['link']}\n"
        output_label.config(text=output)

def add_video(videos):
    name = name_entry.get()
    time = time_entry.get()
    link = link_entry.get()
    if name and time and link:
        videos.append({'name': name, 'time': time, 'link': link})
        save_data_helper(videos)
        output_label.config(text="Video added successfully!")
    else:
        output_label.config(text="Please enter all the fields.")

def update_video(videos):
    if not videos:
        output_label.config(text="No videos to update.")
        return

    index = index_entry.get()
    name = name_entry.get()
    time = time_entry.get()
    link = link_entry.get()
    try:
        index = int(index) - 1
        if 0 <= index < len(videos):
            videos[index] = {'name': name, 'time': time, 'link': link}
            save_data_helper(videos)
            output_label.config(text="Video updated successfully!")
        else:
            output_label.config(text="Invalid index.")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a number.")

def delete_video(videos):
    if not videos:
        output_label.config(text="No videos to delete.")
        return

    index = index_entry.get()
    try:
        index = int(index) - 1
        if 0 <= index < len(videos):
            del videos[index]
            save_data_helper(videos)
            output_label.config(text="Video deleted successfully!")
        else:
            output_label.config(text="Invalid index.")
    except ValueError:
        output_label.config(text="Invalid input. Please enter a number.")

def load_data():
    try:
        with open('yt.txt', 'r') as file:
            data = json.load(file)
            if not data:
                return []  # Return an empty list if data is empty
            return data
    except FileNotFoundError:
        output_label.config(text="File not found.")
        return []  # Return an empty list if file not found
    except json.JSONDecodeError:
        output_label.config(text="Error: The file contains invalid JSON.")
        return []  # Return an empty list if JSON decode error


def save_data_helper(videos):
    with open('yt.txt', 'w') as file:
        json.dump(videos, file)

def create_playlist(playlists):
    # Add your code here to create a playlist
    pass

def add_to_playlist(videos, playlists):
    # Add your code here to add a video to a playlist
    pass

def remove_from_playlist(playlists):
    # Add your code here to remove a video from a playlist
    pass

# Create a root window object
root = tk.Tk()
root.title("YouTube Video Manager")

# Create a frame for the input fields
input_frame = tk.Frame(root)
input_frame.pack()

# Create labels and entries for the input fields
index_label = tk.Label(input_frame, text="Index:")
index_label.grid(row=0, column=0, padx=5, pady=5)
index_entry = tk.Entry(input_frame)
index_entry.grid(row=0, column=1, padx=5, pady=5)

name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=1, column=1, padx=5, pady=5)

time_label = tk.Label(input_frame, text="Duration:")
time_label.grid(row=2, column=0, padx=5, pady=5)
time_entry = tk.Entry(input_frame)
time_entry.grid(row=2, column=1, padx=5, pady=5)

link_label = tk.Label(input_frame, text="Link:")
link_label.grid(row=3, column=0, padx=5, pady=5)
link_entry = tk.Entry(input_frame)
link_entry.grid(row=3, column=1, padx=5, pady=5)

# Create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create buttons for the operations
list_button = tk.Button(button_frame, text="List videos", command=lambda: list_all_videos(videos))
list_button.grid(row=0, column=0, padx=5, pady=5)

add_button = tk.Button(button_frame, text="Add video", command=lambda: add_video(videos))
add_button.grid(row=0, column=1, padx=5, pady=5)

update_button = tk.Button(button_frame, text="Update video", command=lambda: update_video(videos))
update_button.grid(row=0, column=2, padx=5, pady=5)

delete_button = tk.Button(button_frame, text="Delete video", command=lambda: delete_video(videos))
delete_button.grid(row=0, column=3, padx=5, pady=5)

playlist_button = tk.Button(button_frame, text="Create playlist", command=lambda: create_playlist(playlists))
playlist_button.grid(row=1, column=0, padx=5, pady=5)

add_to_playlist_button = tk.Button(button_frame, text="Add to playlist", command=lambda: add_to_playlist(videos, playlists))
add_to_playlist_button.grid(row=1, column=1, padx=5, pady=5)

remove_from_playlist_button = tk.Button(button_frame, text="Remove from playlist", command=lambda: remove_from_playlist(playlists))
remove_from_playlist_button.grid(row=1, column=2, padx=5, pady=5)

exit_button = tk.Button(button_frame, text="Exit", command=root.destroy)
exit_button.grid(row=1, column=3, padx=5, pady=5)

# Create a label for the output
output_label = tk.Label(root, text="", bg="white", wraplength=500)
output_label.pack()

# Load the data from the file
videos = load_data()
playlists = {}

# Enter the main loop
root.mainloop()
