from flask import Flask, render_template, request, jsonify
import yt_dlp 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def download_from_url(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': './download/%(title)s.%(ext)s',
        'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        },
        'nocheckcertificate': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/download', methods=['POST'])
def download():
    video_url = request.json['url']
    download_from_url(video_url)
    return jsonify({"status": "sucess", "message": "Vídeo baixado!"})

if __name__ == '__main__':
    app.run(debug=True)
