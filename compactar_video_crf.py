import subprocess
import os
import sys

# Caminho fixo do ffmpeg
ffmpeg_path = r"C:\ffmpeg-7.1\bin\ffmpeg.exe"

def compactar_video_maximo(input_path, output_path=None, crf=23, preset="slow"):
    if not os.path.isfile(input_path):
        print("❌ Arquivo não encontrado:", input_path)
        return

    if output_path is None:
        nome, ext = os.path.splitext(input_path)
        output_path = f"{nome}_compactado{ext}"

    # Comando para compressão máxima mantendo boa qualidade
    cmd = [
        ffmpeg_path, "-i", input_path,
        "-c:v", "libx264",
        "-crf", str(crf),               # Quanto menor, mais qualidade. Recomendo entre 18 e 28.
        "-preset", preset,             # veryslow, slow, medium, etc.
        "-c:a", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        output_path
    ]

    print(f"🔄 Compactando: {input_path}")
    print(f"🎯 CRF: {crf} | Preset: {preset}")
    subprocess.run(cmd)
    print(f"✅ Vídeo salvo em: {output_path}")

# Execução via terminal
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python compactar_video_crf.py caminho\\do\\video.mp4")
    else:
        caminho = sys.argv[1]
        compactar_video_maximo(caminho)
