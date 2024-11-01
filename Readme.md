# VIDEO-DOWNLOADER
Olá! Esse é um downloader de videos do youtube e algumas outras plataformas, **VIDEO-DOWNLOADER** é desenvolvido utilizando **Flask** no python em seu backend e **Javascript, html e css** em seu front-end. Este é meu primeiro projeto envolvendo python como backend e utilizando os meus conhecimentos de front-end, então muitas coisas estão ainda em melhorias e outras podem não funcionar tão bem

# Init

O **video-downloader** utiliza a versão 3.12.6 e sua ferramenta **venv**
A seguir o passo a passo para inicializar o projeto e desfruta-lo
 - 1. Clone o repositório e abra o console na pasta do projeto.
 - 2. No console digite **python -m venv venv**, para instalar o **venv**
 - 3. Ainda no console digite **venv\scripts\activate** para iniciar o **venv** e logo em seguida ira aparecer em verde o nome **venv** antes da linha do diretório
 - 4. Para inicializar o programa, escreva **python app.py** e acesse o ip fornecido no terminal

## Dependencies

Para o programa funcionar, deve-se instalar o **Flask** e o **yt-dlp** no projeto ao inicializar o **venv**
 - 1. Use o comando **pip install Flask** para instalar o Flask dentro da pasta venv
 - 2. Use o comando **pip install yt-dlp** para instalar a lib yt-dlp responsável pelo núcleo do projeto

## FFmpeg

O **video-downloader** utiliza a ferramenta FFmpeg para converter o arquivo solicitado na saída escolhida pelo usuário, como por exemplo: **MP4**, **WEBM** ou **AVI**
A seguir o passo a passo para baixa-lo

### Windows
 - 1. Baixe o [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip) através do repositório oficial no [github](https://github.com/BtbN/FFmpeg-Builds/releases)
 - 2. Extraia a pasta no diretório **C:\**
 - 3. Renomeie a pasta para ffmpeg e abra as variáveis de ambiente do windows
 - 4. Adicione ao path a seguinte linha **C:\ffmpeg\bin** e reinicie a IDE
 
 Pronto, agora é só desfrutar e baixar seus videos favorítos e ou suas musicas preferidas 😉