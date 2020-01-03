import youtube_dl

# Saving the YouTube video as an MP4
def mp4(url, directory):
    ydl_opts = {
    'postprocessors': [{'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',  # one of avi, flv, mkv, mp4, ogg, webm
                      }],
    'outtmpl': 'C:\\Users\\%USERNAME%\\'+directory+'\\%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception:
            print('\nUnable to download video as an MP4 due to the error message above.')

# Saving the Youtube Video as an MP3
def mp3(url, directory):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'C:\\Users\\%USERNAME%\\'+directory+'\\%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception:
            print('\nUnable to download video as an MP3 due to the error message above.')

def prompt():
    # Determining the YouTube Video
    link = input('Enter the URL of a Youtube video you would like to download: ')

    # Determining Directory
    directory = input('Downloads (1), Documents (2), or Desktop (3)? You can enter 1-3 or type the name of the folder: ')

    # Determining which directory to save the file in:
    if (directory == 'Downloads') or (directory == 'downloads') or (directory == '1'):
        directory = 'Downloads'
    elif (directory == 'Documents') or (directory == 'documents') or (directory == '2'):
        directory = 'Documents'
    else:
        directory = 'Desktop'

    # Determining Filetype 
    filetype = input('Would you like an MP3 or an MP4?: ')
    print()

    # Determining which filetype to save the file as:
    if (filetype == 'MP4') or (filetype == 'mp4'):
        mp4(link, directory)
    elif (filetype == 'MP3') or (filetype == 'mp3'):
        mp3(link, directory)
    else:
        print('Filetype not understood. Please restart the program and type either "MP3" or "MP4".')


if __name__ == "__main__":
    prompt()