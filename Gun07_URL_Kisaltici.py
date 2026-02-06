import pyshorteners
from rich.console import Console
from rich.panel import Panel

console = Console()

def link_kisalt():
    long_url = input("Kısaltmak istediğiniz uzun URL'yi yapıştırın: ")
    
    try:
        
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        
       
        cikti = (
            f"[bold cyan]Orijinal:[/] {long_url}\n"
            f"[bold green]Kısaltılmış:[/] [link={short_url}]{short_url}[/link]"
        )
        
        console.print(Panel(cikti, title="🔗 URL KISALTICI SONUCU", expand=False, border_style="magenta"))
        
    except Exception as e:
        console.print(f"[bold red]Bir hata oluştu:[/] {e}")

if __name__ == "__main__":
    link_kisalt()