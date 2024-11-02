from flask import Flask, render_template, request, jsonify
import yt_dlp 
from data import Data
import http.client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])

def request_download():
    video_url = request.json['url']
    quality_url = request.json['quality']
    output_url = request.json['output']

    #is_valid_url desabilitado temporariamente, ele não reconhece o vimeo e gera o erro 'URL inválida'

    #if(is_valid_url(video_url)):
    #    currentData = Data(video_url, quality_url, output_url)
    #elif(video_url == ""):
    #    return jsonify({"status": "error", "message": "Insira uma URL para fazer o download"}), 400
    #else:
    #    return jsonify({"status": "error", "message": "URL inválida!"}), 400

    currentData = Data(video_url, quality_url, output_url)

    try:
        currentData.extract_data()
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
