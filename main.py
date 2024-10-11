import yt_dlp,os,sys,colorlog,logging
from pathlib import Path

log_colors = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    log_colors=log_colors
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

file_handler = logging.FileHandler("video_downloader.log")
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.basicConfig(
    level=logging.INFO,
    handlers=[handler, file_handler]
)

logger = logging.getLogger()

DOWNLOAD_DIR = Path("downloads")
DOWNLOAD_DIR.mkdir(exist_ok=True)

def ffmpeg():
    if not Path('C:/ffmpeg').exists():
        logger.error("FFMPEG IS NOT FOUND, DOWNLOAD AND PUT THE PATH !!!")
        sys.exit(1)

def download_video(video_url):
    ffmpeg()

    ydl_opts = {
        'ffmpeg_location': 'C:/ffmpeg',
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': str(DOWNLOAD_DIR / '%(title)s.%(ext)s'),
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        },
        'noplaylist': True,
        'retries': 5,
        'fragment_retries': 5,
        'quiet': True,
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info(f"Starting download: {video_url}")
            ydl.download([video_url])
            logger.info(f"Download completed for: {video_url}")
    except yt_dlp.utils.DownloadError as e:
        logger.error(f"{e}")
    except Exception as e:
        logger.error(f"{e}")

def checkurl(url):
    if not url.startswith("http"):
        logger.error("Please provide a valid YouTube URL.")
        return False
    return True

def main():
    print("-----------------------------------------------")
    logger.info("YouTube Video Downloader started.")
    print("-----------------------------------------------")
    while True:
        url = input("Enter the YouTube video URL and 'exit' to stop :::> ")
        if url.lower() == 'exit':
            logger.info("Good Bye 🙋‍♂️.")
            break
        if not checkurl(url):
            continue
        
        download_video(url)
        print("Download completed, Thank you.")
        logger.info("Waiting for next URL input...")

if __name__ == "__main__":
    main()


# Created By ujjwalsrivastava
