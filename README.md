# 🎥 Compactador Inteligente de Vídeo com FFmpeg

Este script Python usa o poder do **FFmpeg 7.1** para **reduzir drasticamente o tamanho de arquivos de vídeo**, mantendo uma **alta qualidade visual**. Ele é ideal para quem deseja otimizar vídeos para envio por e-mail, upload em sites, armazenamento ou visualização rápida.

---

## 🚀 Funcionalidades

- ✅ Compressão automática usando o codec H.264 (`libx264`)
- ✅ Redução significativa de tamanho com qualidade visivelmente mantida
- ✅ Suporte para qualquer tipo de vídeo (MP4, AVI, MOV etc.)
- ✅ Geração automática do vídeo compactado com o sufixo `_compactado`
- ✅ Compatível com Windows (usa caminho fixo do FFmpeg)

---

## 🛠️ Pré-requisitos

- **Python 3.6+**
- **FFmpeg 7.1** (ou versão similar)

---

## 📦 Instalação do FFmpeg no Windows

1. Baixe o FFmpeg em: https://www.gyan.dev/ffmpeg/builds/
2. Extraia os arquivos para `C:\ffmpeg-7.1`
3. Certifique-se de que os arquivos `ffmpeg.exe` e `ffprobe.exe` estão dentro de `C:\ffmpeg-7.1\bin`

---

## 🧠 Como funciona

O script utiliza a opção `-crf` (Constant Rate Factor) do FFmpeg, onde:
- **CRF 18** = máxima qualidade (maior tamanho)
- **CRF 23** = equilíbrio ideal (recomendado)
- **CRF 28** = qualidade menor, mas vídeo muito leve

O valor padrão utilizado é `crf=23` com `preset=slow`.

---

## 💻 Como usar

### 1. Coloque o vídeo e o script na mesma pasta

### 2. Execute pelo terminal (CMD ou PowerShell):

```bash
python compactar_video_crf.py "C:\Users\IgorDev\Videos\meu_video.mp4"
```

> Isso vai gerar um novo arquivo chamado: `meu_video_compactado.mp4`

---

## 🧪 Exemplo real

```bash
python compactar_video_crf.py "C:\Videos\Aula01.mp4"
```

Resultado:

- Tamanho original: **120 MB**
- Tamanho final: **28 MB**
- Qualidade: **quase idêntica**

---

## 🔧 Personalização

Quer ajustar a qualidade? Edite o script e altere esta linha:

```python
compactar_video_maximo(caminho, crf=23)
```

Exemplo para maior compressão:

```python
compactar_video_maximo(caminho, crf=26)
```

---

## 📁 Estrutura do projeto

```
.
├── compactar_video_crf.py      # Script principal
└── README.md                   # Este arquivo
```

---

## 📜 Licença

Este projeto é de código aberto, sob a licença MIT.

---

## 👨‍💻 Autor

**Igor Justino Rodrigues**
