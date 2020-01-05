import PySimpleGUI as sg
import youtube_dl

# Saving the YouTube video as an MP4
def mp4(url, directory):
    ydl_opts = {
    'postprocessors': [{'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',  # one of avi, flv, mkv, mp4, ogg, webm
                      }],
    'outtmpl': directory+'\\%(title)s.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            msg = 'Unable to download video as an MP3 due to the error message above.'
            sg.popup(str(e),msg)

# Saving the Youtube Video as an MP3
def mp3(url, directory):
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': directory+'\\%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except Exception as e:
            msg = 'Unable to download video as an MP3 due to the error message above.'
            sg.popup(str(e),msg)

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter a YouTube URL (https://www.youtube.com/...): '), sg.InputText()],
            [sg.Text('Output Folder: ', size=(8, 1)), sg.Input(), sg.FolderBrowse()],
            [sg.Button('Convert to MP3'),sg.Button('Convert to MP4')] ]

# Create the Window
window = sg.Window("Daniel's YouTube Downloader", layout)

event, values = window.read()
# Event Loop to process "events" and get the "values" of the inputs
# event means the 'Convert to MP3' or 'Convert to MP4' button have been pressed
# value[0] is URL and value[1] is directory
# print('URL:' + url)
# print('Directory:' + directory)
while True:
    event, values = window.read()
    url = values[0]
    directory = values[1]
    if event in (None, 'Exit'):	# if user closes window or presses Exit
        break
    elif event in ('Convert to MP3'): #if the user clicks the "output folder" button
        mp3(url,directory)
    elif event in ('Convert to MP4'):
        mp4(url,directory)
window.close()
