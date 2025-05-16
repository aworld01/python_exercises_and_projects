# pip install yt_dlp

import yt_dlp

yt_dlp.YoutubeDL({'format': 'best','outtmp1': '%(title)s.%(ext)s'}).download(["https://www.youtube.com/watch?v=HITUI_Lu6FE"])