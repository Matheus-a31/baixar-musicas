import subprocess
import os
import dotenv


dotenv.load_dotenv()

def baixar_playlist(url):
    caminho_env = os.getenv("caminho", "")
    
    if caminho_env.startswith("\\"):
        caminho_base = "C:" + caminho_env
    else:
        caminho_base = caminho_env or "musicas"
        
    caminho_saida = os.path.join(caminho_base, "%(playlist_title)s", "%(title)s.%(ext)s")

    comando = [
        "yt-dlp",
        "-x",
        "--audio-format", "mp3",
        "--audio-quality", "0",
        "--embed-metadata",
        "--embed-thumbnail",
        "--ffmpeg-location", rf"C:{caminho_env}ffmpeg-8.0.1-essentials_build\ffmpeg-8.0.1-essentials_build\bin",
        "-o", caminho_saida,
        url
    ]

    subprocess.run(comando, check=True)
