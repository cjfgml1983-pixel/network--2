import yt_dlp
import os

def download_video():
    print("\n" + "="*50)
    print("      고성능 유튜브 다운로더 (Powered by yt-dlp)")
    print("="*50)
    
    url = input("\n다운로드할 유튜브 주소(URL)를 입력하세요: ").strip()
    if not url:
        print("URL이 입력되지 않았습니다.")
        return

    print("\n1. 고화질 영상 다운로드 (MP4)")
    print("2. 오디오만 추출 (MP3)")
    choice = input("\n원하는 작업 번호를 선택하세요 (1 또는 2): ").strip()

    # 저장 폴더 설정
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    
    ydl_opts = {
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    if choice == '2':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })
        print("\n오디오 추출을 시작합니다...")
    else:
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        })
        print("\n고화질 영상 다운로드를 시작합니다...")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n✅ 다운로드 완료! 저장 위치: {download_path}")
    except Exception as e:
        print(f"\n❌ 오류 발생: {str(e)}")

if __name__ == "__main__":
    download_video()
