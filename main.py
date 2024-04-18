import os
from pytube import YouTube
import time

def create_folder_if_not_exists(folder_path):
    """Function to create folder if it doesn't exist"""
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    except Exception as e:
        print(f"Error creating folder: {e}")

def on_progress(stream, chunk, bytes_remaining):
    """Callback function to show download progress"""
    try:
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent = (bytes_downloaded / total_size) * 100
        print("\r" + "▌" * int(percent) + " " * (100 - int(percent)) + " {}%".format(int(percent)), end='')
    except Exception as e:
        print(f"Error in progress callback: {e}")

def download_video(vid_url, resolution='720p'):
    """Function to download video"""
    try:
        yt = YouTube(vid_url, on_progress_callback=on_progress)
        print('Title:', yt.title)
        video = yt.streams.filter(res=resolution).first()
        if video:
            print('Video size:', video.filesize_mb, 'MB')
            start = time.time()
            create_folder_if_not_exists('video')
            video.download('video')
            end = time.time()
            file_size = video.filesize_mb
            status = "Complete"
        else:
            status = "Failed"
            start = 0.0
            end = 0.0
            file_size = 0.0
    except Exception as e:
        print(f"Error downloading video: {e}")
        status = "Failed"
        start = 0.0
        end = 0.0
        file_size = 0.0
    return status, start, end, file_size

def download_audio(vid_url):
    """Function to download audio"""
    try:
        yt = YouTube(vid_url, on_progress_callback=on_progress)
        print('Title:', yt.title)
        audio = yt.streams.get_audio_only()
        if audio:
            print('Audio size:', audio.filesize_mb, 'MB')
            start = time.time()
            create_folder_if_not_exists('audio')
            audio.download('audio')
            end = time.time()
            file_size = audio.filesize_mb
            status = "Complete"
        else:
            status = "Failed"
            start = 0.0
            end = 0.0
            file_size = 0.0
    except Exception as e:
        print(f"Error downloading audio: {e}")
        status = "Failed"
        start = 0.0
        end = 0.0
        file_size = 0.0
    return status, start, end, file_size

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    controler = 1
    while(controler==1):
        try:
            vid_url = input("Enter the video URL: ")
            valid_format = False
            while not valid_format:
                vid_format = input("Choose the format:\n1. Video (MP4)\n2. Audio (MP3)\nEnter the format number: ")
                if vid_format in ['1', '2']:
                    valid_format = True
                else:
                    print("Invalid format number. Please enter '1' for Video (MP4) or '2' for Audio (MP3).")

            if vid_format == '1':
                resolution = input("Choose the resolution:\n1. 720p\n2. 480p\n3. 360p\nEnter the resolution number: ")
                resolutions = {1: '720p', 2: '480p', 3: '360p'}
                resolution_choice = resolutions.get(int(resolution), '720p')
                status, start, end, file_size = download_video(vid_url, resolution_choice)
            elif vid_format == '2':
                status, start, end, file_size = download_audio(vid_url)

            if status == "Complete":
                print(f'\nDownload {status} in {(end - start):0.2f} seconds at {file_size / (end - start):0.2f} MB/s')
            else:
                print("\nDownload failed.")
            controler = int(input("Do you want to download one more if yes press 1 or if no then press 0: "))
        except Exception as e:
            print(f"Error in main loop: {e}")
    else:
        print("Thank you for Using my software. Developed by Tarak Rahman")