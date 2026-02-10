import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table

console = Console()

def haberleri_kazı():

    url = "https://shiftdelete.net/teknoloji-haberleri" 
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    
    try:
        console.print(f"[yellow]{url}[/] sitesine bağlanılıyor...\n")
        response = requests.get(url, headers=headers)
        
        # Siteyi başarılı bir şekilde okuduk mu? (200 OK)
        if response.status_code != 200:
            console.print(f"[red]Siteye ulaşılamadı. Durum Kodu: {response.status_code}[/]")
            return

        soup = BeautifulSoup(response.content, "html.parser")

        haberler = soup.select("h3 a") 

        table = Table(title="📰 GÜNCEL TEKNOLOJİ HABERLERİ", style="bold green")
        table.add_column("No", justify="center", style="cyan")
        table.add_column("Haber Başlığı", style="white")

        sayac = 0
        for haber in haberler:
            metin = haber.get_text().strip()
            if len(metin) > 15:
                sayac += 1
                table.add_row(str(sayac), metin)
            
            if sayac == 15: break

        if sayac == 0:
            console.print("[red]Hala haber bulunamadı. Lütfen internet bağlantını kontrol et.[/]")
        else:
            console.print(table)
        
    except Exception as e:
        console.print(f"[bold red]Hata oluştu:[/] {e}")

if __name__ == "__main__":
    haberleri_kazı()