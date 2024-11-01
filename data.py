import yt_dlp 

class Data:
    def __init__(self, url, quality, output):
        self.url = url
        self.quality = quality
        self.output = output

    def extract_data(self):
        ydl_opts = {
            'format': self.quality if self.output != 'mp3' else 'bestaudio[ext=m4a]/mp4', #check if the request is audio or video
            'outtmpl': './download/%(title)s.%(ext)s',
            'concurrent_fragment_downloads': 10, 
            'cachedir': False,
            'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
            },
            'nocheckcertificate': True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': self.output, 
            }],

        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url])
