from pytube import YouTube


yt = local = url = None

v = '0.0.1' #VERSÃO DO APP
#url https://www.youtube.com/watch?v=h-S3W5vIfEg

def progress():
    print('/')


def getURL():
    global yt
    url = input('Insert URL >')
    yt = YouTube(f'{url}', on_progress_callback=progress())
    print(str(yt.title))
    location()

def location():
    global local
    print(r'ex: C:\Users\UserName\Desktop')
    local = input('Insert path >')

    download()

def download():
    print('downloading...')
    yt = YouTube(f'{url}', on_progress_callback=progress())
    yt.streams.get_by_itag(18).download(local)


#print(str(yt.title))
#print(str(yt.thumbnail_url))
#print(str(yt.streams.filter(file_extension='mp4')))
#yt.streams.get_by_itag(18).download(r'C:\Users\Christian\Desktop')
#print(f'v{v}')"""
