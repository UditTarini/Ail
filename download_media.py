import pafy, pyglet
import urllib.request
from urllib.parse import *
from bs4 import BeautifulSoup
import youtube_dl
import html5lib
import main
from pydub import AudioSegment

 
lst = []
dict = {}
dict_names = {}
playlist = []    
def url_search( search_string, max_search):

        textToSearch = search_string
        query = urllib.parse.quote(textToSearch)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html5lib')
        i = 1
        for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
            if len(dict) < max_search:
                dict[i] = 'https://www.youtube.com' + vid['href']
                i += 1
            else:
                break

def get_search_items( max_search):

        if dict != {}:
            i = 1
            for url in dict.values():
                try:
                    info = pafy.new(url)
                    dict_names[i] = info.title
                    print("{0}. {1}".format(i, info.title))
                    i += 1

                except ValueError:
                    pass

def play_media( num):
        url = dict[int(num)]
        info = pafy.new(url)
        # audio = info.m4astreams[-1]
        audio = info.getbestaudio(preftype="mp3")
        song_name = info.title+'.mp3'
        audio.download(filepath=song_name, quiet=True)

        AudioSegment.converter = "path to ffmpeg file"
        song = AudioSegment.from_mp3("song.mp3")
        song.export("Taylor Swift Lover.wav", format="wav")

        song = pyglet.resource.media(song_name)
        print("Playing: {0}.".format(dict_names[int(num)]))

        song.play()
        pyglet.app.run()
        stop = ''
        while True:
            stop = input('Type "s" to stop; "p" to pause; "" to play; : ')
            if stop == 's':
                song.pause()
                break
            elif stop == 'p':
                song.pause()
            elif stop == '':
                song.play()
            elif stop == 'r':
                # player.queue(song)
                # player.play()
                print('Replaying: {0}'.format(dict_names[int(num)]))

def download_video( num):
        url = dict[int(num)]
        info = pafy.new(url)
        audio = info.getbestvideo(preftype="mp4")
        song_name = dict_names[int(num)]
        print("Downloading: {0}.".format(dict_names[int(num)]))
        print(song_name)
        main.ail("Enter where you want to save")
        song_name = input("Filename (Enter if as it is): ")
        # file_name = song_name[:11] + '.m4a'
        filename = song_name
        if song_name == '':
            main.ail("downloading started you can press enter to check progress")
            audio.download()
            main.ail("video downloaded")
            main.command()

        else:
            main.ail("downloading started you can press enter to know progress")
            audio.download(filepath=filename,quiet=False)
            main.ail("video downloaded")
            main.command()


def download_song(num):
    url = dict[int(num)]
    info = pafy.new(url)
    audio = info.getbestaudio()
    song_name = dict_names[int(num)]
    print("Downloading: {0}.".format(dict_names[int(num)]))
    print(song_name)
    main.ail("Enter where you want to save")
    song_name = input("Filename (Enter if as it is): ")
    # file_name = song_name[:11] + '.m4a'
    filename = song_name 
    if song_name == '':
        main.ail("downloading started you can press enter to check progress")
        audio.download()
        main.ail("song downloaded")
        main.command()
    else:
        main.ail("downloading started you can press enter to check progress")
        audio.download(filepath=filename, quiet=False)
        main.ail("downloaded")
        main.command()

def add_playlist( search_query):
        url = url_search(search_query, max_search=1)
        playlist.append(url)


def initYT_Video():
        
        search = ''
        while search != 'q':

            main.ail('Okay sir please Enter the title or enter q to quit:')
            search = input("Youtube Search or enter q to quit:\n")


            old_search = search
            max_search = 5

            if search == 'q':
                main.ail("What else can i do for you...")
                main.command()

            if search != 'q':
                main.ail("Fetching videos available on youtube:")
                print('\nFetching for: {0} on youtube:'.format(search.title()))
                url_search(search, max_search)
                get_search_items(max_search)
                main.ail("Enter the video number you want to download")
                number = input('Input video number: ')
                download_video(number)



def initYT_Song():
    search = ''
    while search != 'q':

        main.ail('Okay sir Enter the title or enter q to quit:')
        search = input("Youtube Search or enter q to quit:\n")
        old_search = search
        max_search = 4

        if search == 'q':
            main.ail("What else can i do for you...")
            main.command()
        main.ail("please choose your option...")
        download = input('1. Play Live Music\n2. Download Mp3 from Youtube.\n')
        if search != 'q' and (download == '1' or download == ''):
            main.ail("Fetching videos available on youtube:")
            print('\nFetching for: {0} on youtube.'.format(search.title()))
            url_search(search, max_search)
            get_search_items(max_search)
            song_number = input('Input song number: ')
            play_media(song_number)
        elif download == '2':
            main.ail("Fetching videos available on youtube:")
            print('\nFetching for: {0} on youtube:'.format(search.title()))
            url_search(search, max_search)
            get_search_items(max_search)
            main.ail("Enter the song number you want to download")
            song_number = input('Input song number: ')
            download_song(song_number)
