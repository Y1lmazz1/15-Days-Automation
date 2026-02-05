import requests
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def doviz_cek():

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    
    try:
        response = requests.get(url)
        data = response.json()
        rates = data["rates"]
     
        usd_tl = rates["TRY"]
        eur_tl = usd_tl / rates["EUR"]
        gbp_tl = usd_tl / rates["GBP"]

        table = Table(title="💰 CANLI DÖVİZ KURLARI", style="bold green")
        table.add_column("Döviz Cinsi", style="cyan")
        table.add_column("Fiyat (TL)", justify="right", style="yellow")

        table.add_row("Dolar (USD)", f"{usd_tl:.2f} ₺")
        table.add_row("Euro (EUR)", f"{eur_tl:.2f} ₺")
        table.add_row("Sterlin (GBP)", f"{gbp_tl:.2f} ₺")

        console.print(Panel(table, expand=False, border_style="blue"))
        
    except Exception as e:
        console.print(f"[bold red]Hata oluştu:[/] {e}")

if __name__ == "__main__":
    doviz_cek()