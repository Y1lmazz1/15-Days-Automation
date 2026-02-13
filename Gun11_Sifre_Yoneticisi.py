import os
from cryptography.fernet import Fernet
from rich.console import Console
from rich.panel import Panel

console = Console()


def anahtar_uret():
    
    anahtar = Fernet.generate_key()
    with open("gizli.key", "wb") as anahtar_dosyasi:
        anahtar_dosyasi.write(anahtar)

def anahtar_yukle():
   
    return open("gizli.key", "rb").read()


def sifre_kaydet():
    site = input("Hangi site/uygulama için? (örn: Instagram): ")
    sifre = input(f"{site} için şifreniz ne olsun?: ")
    
    anahtar = anahtar_yukle()
    f = Fernet(anahtar)
    
    
    sifrelenmis_metin = f.encrypt(sifre.encode())
    
    with open("sifreler.txt", "a") as f_dosya:
        f_dosya.write(f"{site}: {sifrelenmis_metin.decode()}\n")
    
    console.print(f"[bold green]✔ {site} şifresi güvenli bir şekilde kaydedildi![/]")

def sifreleri_listele():
    if not os.path.exists("sifreler.txt"):
        console.print("[red]Henüz kayıtlı bir şifre yok.[/]")
        return

    anahtar = anahtar_yukle()
    f = Fernet(anahtar)
    
    console.print("\n[bold cyan]🔐 KAYITLI ŞİFRELERİNİZ[/]")
    with open("sifreler.txt", "r") as f_dosya:
        for satir in f_dosya:
            site, sifre_kilitli = satir.strip().split(": ")
            
            cozulmus_sifre = f.decrypt(sifre_kilitli.encode()).decode()
            console.print(f"[yellow]{site}:[/] [white]{cozulmus_sifre}[/]")


def main():
    if not os.path.exists("gizli.key"):
        anahtar_uret()
        console.print("[bold yellow]İlk kullanım: Sizin için özel bir güvenlik anahtarı (gizli.key) oluşturuldu![/]")

    while True:
        console.print("\n1- Yeni Şifre Kaydet\n2- Şifrelerimi Gör\n3- Çıkış")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            sifre_kaydet()
        elif secim == "2":
            sifreleri_listele()
        elif secim == "3":
            break

if __name__ == "__main__":
    main()