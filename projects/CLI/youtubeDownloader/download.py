# pip install yt_dlp

import yt_dlp

l1 = "https://www.youtube.com/shorts/dJFXhyzd2yY"
l2 = "https://www.youtube.com/watch?v=eksZLqnUes8"

yt_dlp.YoutubeDL({'format': 'best','outtmp1': '%(title)s.%(ext)s'}).download([l2])



#yt-dlp "https://www.youtube.com/watch?v=eksZLqnUes8"

