import psutil
import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def get_size(bytes):
    for unit in ['', 'K', 'M', 'G', 'T']:
        if bytes < 1024: return f"{bytes:.1f}{unit}B"
        bytes /= 1024

def sistem_paneli():

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq().current / 1000
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    battery = psutil.sensors_battery()
    uptime = str(datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())).split('.')[0]

 
    temp = "N/A"
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        for name, entries in temps.items():
            temp = f"{entries[0].current}°C"
            break

 
    table = Table(title="🚀 GELİŞMİŞ SİSTEM ANALİZİ", style="bold white")
    table.add_column("Donanım", style="cyan")
    table.add_column("Detay Bilgi", style="magenta")
    table.add_column("Durum/Yüzde", style="bold yellow")

    table.add_row("İşlemci (CPU)", f"{cpu_freq:.2f} GHz", f"%{cpu_usage}")
    table.add_row("Sıcaklık", "İşlemci Çekirdeği", temp)
    table.add_row("Bellek (RAM)", f"{get_size(ram.used)} / {get_size(ram.total)}", f"%{ram.percent}")
    table.add_row("Depolama (Disk)", f"{get_size(disk.free)} Boş Alan", f"%{disk.percent}")
    table.add_row("Ağ (Network)", f"⬇ {get_size(net.bytes_recv)} | ⬆ {get_size(net.bytes_sent)}", "Aktif")
    table.add_row("Sistem Çalışma", "Açılıştan Beri", uptime)

    if battery:
        pil_ikon = "🔌 Takılı" if battery.power_plugged else "🔋 Deşarj"
        table.add_row("Batarya", pil_ikon, f"%{battery.percent}")

    console.print(Panel(table, expand=False, border_style="green", padding=(1, 2)))

if __name__ == "__main__":
    sistem_paneli()