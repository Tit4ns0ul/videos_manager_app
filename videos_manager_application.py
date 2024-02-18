import json

def list_all_videos(videos):
    if not videos:
        print("No videos available.")
    else:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. Name: {video['name']}, Duration: {video['time']}, Link: {video['link']}")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video duration (e.g., 10:30 for 10 minutes 30 seconds): ")
    link = input("Paste video URL link: ")
    videos.append({'name': name, 'time': time, 'link': link})
    save_data_helper(videos)

def update_video(videos):
    if not videos:
        print("No videos to update.")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the index of the video you want to update: ")) - 1
        if 0 <= index < len(videos):
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video duration: ")
            link = input("Enter the updated video link: ")
            videos[index] = {'name': name, 'time': time, 'link': link}
            save_data_helper(videos)
            print("Video updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_video(videos):
    if not videos:
        print("No videos to delete.")
        return

    list_all_videos(videos)
    try:
        index = int(input("Enter the index of the video you want to delete: ")) - 1
        if 0 <= index < len(videos):
            del videos[index]
            save_data_helper(videos)
            print("Video deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def load_data():
    try:
        with open('yt.txt', 'r') as file:
            data = json.load(file)
            if not data:
                return []  # Return an empty list if data is empty
            return data
    except FileNotFoundError:
        print("File not found.")
        return []  # Return an empty list if file not found
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
        return []  # Return an empty list if JSON decode error


def save_data_helper(videos):
    with open('yt.txt', 'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()
    playlists = {}

    print("Contents of videos list:", videos)  # Add this line to inspect the contents of the videos list

    while True:
        print("\nYoutube Video Manager")
        print("1. List favorite videos")
        print("2. Add a YouTube video")
        print("3. Update a YouTube video")
        print("4. Delete a YouTube video")
        print("5. Create a Playlist")
        print("6. Add a Video to Playlist")
        print("7. Remove a Video from Playlist")
        print("8. Exit the app")

        choice = input('Enter your choice: ')
        print("Choice selected:", choice)

        match choice:
            case '1':
                print("Listing all videos...")
                list_all_videos(videos)

            case '2':
                print("Adding a video...")
                add_video(videos)

            case '3':
                print("Updating a video...")
                update_video(videos)

            case '4':
                print("Deleting a video...")
                delete_video(videos)

            case '5':
                print("Creating a playlist...")
                create_playlist(playlists)

            case '6':
                print("Adding a video to playlist...")
                add_to_playlist(videos, playlists)

            case '7':
                print("Removing a video from playlist...")
                remove_from_playlist(playlists)

            case '8':
                print("Exiting the app. Goodbye!")
                break

            case _:
                print("Invalid choice. Please enter a number from 1 to 8.")

def create_playlist(playlists):
    name = input("Enter playlist name: ")
    playlists[name] = []

def add_to_playlist(videos, playlists):
    list_all_videos(videos)
    playlist_name = input("Enter the name of the playlist: ")
    if playlist_name not in playlists:
        print("Playlist not found.")
        return
    try:
        index = int(input("Enter the index of the video you want to add to the playlist: ")) - 1
        if 0 <= index < len(videos):
            playlists[playlist_name].append(videos[index])
            print("Video added to the playlist successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def remove_from_playlist(playlists):
    playlist_name = input("Enter the name of the playlist: ")
    if playlist_name not in playlists:
        print("Playlist not found.")
        return
    list_playlist_videos(playlists, playlist_name)
    try:
        index = int(input("Enter the index of the video you want to remove from the playlist: ")) - 1
        if 0 <= index < len(playlists[playlist_name]):
            del playlists[playlist_name][index]
            print("Video removed from the playlist successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def list_playlist_videos(playlists, playlist_name):
    if not playlists[playlist_name]:
        print("No videos in this playlist.")
    else:
        for index, video in enumerate(playlists[playlist_name], start=1):
            print(f"{index}. Name: {video['name']}, Duration: {video['time']}, Link: {video['link']}")

if __name__ == "__main__":
    main()
