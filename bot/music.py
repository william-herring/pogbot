from __future__ import unicode_literals
import discord
import youtube_dl


def get_mp3(link):
    src = link

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
        info = ydl.extract_info(link, download=False)
        path = ydl.prepare_filename(info)

    return path.split(".", 1)[0] + ".mp3"