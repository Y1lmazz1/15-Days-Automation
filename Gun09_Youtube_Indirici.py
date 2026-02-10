import yt_dlp
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import os

console = Console()

def video_indir():
    link = input("📥 YouTube linkini yapıştırın: ")

    table = Table(title="🎥 İndirme Seçenekleri", style="bold cyan")
    table.add_column("No", justify="center")
    table.add_column("Kalite / Format", style="magenta")
    table.add_row("1", "En Yüksek Kalite (Best)")
    table.add_row("2", "1080p (Full HD)")
    table.add_row("3", "720p (HD)")
    table.add_row("4", "480p (SD)")
    table.add_row("5", "Sadece Ses (MP3)")
    
    console.print(table)
    secim = input("\nSeçiminiz (1-5): ")


    kayit_yolu = os.path.expanduser("~/Desktop/Indirilen_Medya")
    if not os.path.exists(kayit_yolu):
        os.makedirs(kayit_yolu)

    format_dict = {
        "1": "bestvideo+bestaudio/best",
        "2": "bestvideo[height<=1080]+bestaudio/best[height<=1080]",
        "3": "bestvideo[height<=720]+bestaudio/best[height<=720]",
        "4": "bestvideo[height<=480]+bestaudio/best[height<=480]",
        "5": "bestaudio/best"
    }

    ydl_opts = {
        'format': format_dict.get(secim, "best"),
        'outtmpl': f'{kayit_yolu}/%(title)s.%(ext)s',
        'quiet': False,
        'no_warnings': True,
    }

  
    if secim == "5":
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        console.print("[yellow]Video inceleniyor ve indirme başlıyor...[/]")
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
            
        console.print(Panel(f"[bold green]✅ İşlem Başarıyla Tamamlandı![/]\n[white]Dosya şuraya kaydedildi: {kayit_yolu}[/]", border_style="green"))
        
    except Exception as e:
        console.print(f"[bold red]Bir hata oluştu:[/] {e}")

if __name__ == "__main__":
    video_indir()