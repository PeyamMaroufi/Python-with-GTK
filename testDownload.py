from __future__ import unicode_literals
import youtube_dl
ydl_opts = {}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    x = ydl.extract_info('http://www.youtube.com/watch?v=BaW_jenozKc', download =False)
    formats = x.get('formats',[x])
    print(x['format'])
    for f in formats:
        x = f['format']

        print(x[5:])
        if(x[6:8]=='au'):
            print(f['ext'])
            print(f['quality'])



options={
    'format': 'bestaudio',
    'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])