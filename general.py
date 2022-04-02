from pytube import YouTube

def on_complete(stream, file_path):
    print(stream)
    print(file_path)

def on_progress(stream, chunk, bytes_remaining):
    print(100 - (bytes_remaining / stream.filesize * 100))

video_obj = YouTube(
    'https://www.youtube.com/watch?v=NtzDjNhPZgU', on_complete_callback = on_complete,
    on_progress_callback = on_progress )


#print(video_obj.streams.get_highest_resolution())
#print(video_obj.streams.get_lowest_resolution())
#print(video_obj.streams.get_audio_only())


video_obj.streams.get_highest_resolution().download()
