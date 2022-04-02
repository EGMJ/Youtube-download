from pytube import YouTube
from colorama import init, Fore


def on_complete(stream, filepath):
    print('download complete')
    print(filepath)

def on_progress(stream, chunk, bytes_remaining ):
    progress_str = f'{round( 100 - (bytes_remaining / stream.filesize * 100),2)}%'
    print(progress_str)

init()
#link = input('Youtube link: ')
link = 'https://www.youtube.com/watch?v=3_CpaZfn-mI'
video_obj = YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

# video information
print(Fore.RED + f'title: \033[39m {video_obj.title}')
print(Fore.RED + f'length: \033[39m {(video_obj.length / 60.2)} minutes ')
print(Fore.RED + f'views: \033[39m {(video_obj.views / 1000000)} milion' )
print(Fore.RED + f'author: \033[39m n {video_obj.author}')

# download

print(Fore.RED + 'download:' +
    Fore.GREEN + '(b)est \033[39m| ' +
    Fore.YELLOW + '(w)orst \033[39m| ' +
    Fore.BLUE + '(a)udio \033[39m| (e)xit')
    
download_choice = input('Choice: ')
#
#match download_choice:
#    case 'b':
#        video_obj.streams.get_highest_resolution().download(r'\home\egmj\Projects\youtube-download')
#    case 'w':
#        video_obj.streams.get_worst_resolution().download(r'\home\egmj\Projects\youtube-download')
#    case 'a':
#        video_obj.streams.get_audio_only().download(r'\home\egmj\Projects\youtube-download')
#
if download_choice == 'b':
    video_obj.streams.get_highest_resolution().download(r'/home/egmj/Projects/youtube-download')
elif download_choice == 'w':
    video_obj.streams.get_lowest_resolution().download(r'/home/egmj/Projects/youtube-download')
elif download_choice == 'a':
    video_obj.streams.get_audio_only().download(r'/home/egmj/Projects/youtube-download')
elif download_choice == 'e':
    quit()
