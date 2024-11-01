from flask import Flask, render_template, request, jsonify
import yt_dlp 
from data import Data
import http.client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def extract_data(url, quality, output):
    ydl_opts = {
        'format': quality if output != 'mp3' else 'bestaudio[ext=m4a]/mp4', #check if the request is audio or video
        'outtmpl': './download/%(title)s.%(ext)s',
        'concurrent_fragment_downloads': 10, 
        'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
        },
        'nocheckcertificate': True,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': output, 
        }],

    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

@app.route('/download', methods=['POST'])

def request_download():
    #get data from request.json
    video_url = request.json['url']
    quality_url = request.json['quality']
    output_url = request.json['output']

    #create url object
    if(is_valid_url(video_url)):
        currentData = Data(video_url, quality_url, output_url)
    elif(video_url == ""):
        return jsonify({"status": "error", "message": "Insira uma URL para fazer o download"}), 400
    else:
        return jsonify({"status": "error", "message": "URL inválida!"}), 400

    try:
        extract_data(currentData.url, currentData.quality, currentData.output)
        return jsonify({"status": "success", "message": "Vídeo baixado!"})
    except:
        return jsonify({"status": "error", "message": "Erro ao baixar arquivo!"}), 500

def is_valid_url(url):
    try:
        http.client.HTTPConnection(url)
        True
    except:
        return False

if __name__ == '__main__':
    app.run(debug=True)
