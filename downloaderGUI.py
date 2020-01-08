import PySimpleGUI as sg
import youtube_dl

# Method used to save the Youtube Video as an MP4
def mp4(url, directory):
    ydl_opts = {
    'postprocessors': [{'key': 'FFmpegVideoConvertor',
                        'preferedformat': 'mp4',  # one of avi, flv, mkv, mp4, ogg, webm
                      }],
    'outtmpl': directory+'\\%(title)s.%(ext)s',                                             # Using given directory + name of youtube video as 
    }                                                                                       # output destination
    
    # Obtaining YouTube Video's Information (mainly the title of the video for the popup after a successful download)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)
    
    # Downloading the Video as an MP4
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:                                                                                # Error handling 
            ydl.download([url])
            sg.popup("The YouTube video you requested was downloaded successfully to the following location: ",directory+'/'+video_title+'.mp4')
        except Exception as e:                                                              # popup displaying error message
            msg = 'Unable to download video as an MP4 due to the error message above.'
            sg.popup(str(e),msg)

# Method used to save the Youtube Video as an MP3
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

    # Obtaining YouTube Video's Information (mainly the title of the video for the popup after a successful download)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', None)

    # Downloading the Video as an MP3
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:                                                                                # Error handling 
            ydl.download([url])
            sg.popup("The YouTube video you requested was downloaded successfully to the following location: ",directory+'/'+video_title+'.mp3')
        except Exception as e:                                                              # popup displaying error message
            msg = 'Unable to download video as an MP3 due to the error message above.'
            sg.popup(str(e),msg)

sg.theme('DarkBrown4')	# Adding a touch of color using PySimpleGUI's built-in Themes

# All the stuff inside the GUI window. 
# Each list is a row, each entry in each list is a column. 
layout = [  [sg.Text('Enter a YouTube URL (https://www.youtube.com/...):  '), sg.InputText()],      # First Row (Enter URL)
            [sg.Text('Export to Output Folder: ', size=(39, 1)), sg.Input(), sg.FolderBrowse()],    # Second Row (Output Folder textbox + browse button)
            [sg.Button('Convert to MP3'),sg.Button('Convert to MP4')] ]                             # Third Row (Convert to MP3/MP4 buttons)

# Create the GUI Window
window = sg.Window("Daniel's YouTube Downloader", layout)

while True:
    # Obtaining the URL and directory information from URL in a loop
    global url, directory
    event, values = window.read()
    url = values[0]
    directory = values[1]

    if event in (None, 'Exit'):	# if user closes window or presses Exit
        break
    elif event in ('Convert to MP3'): # if the user clicks the "Convert to MP3" button
        mp3(url,directory)
    elif event in ('Convert to MP4'): # if the user clicks the "Convert to MP4" button
        mp4(url,directory)
window.close()
