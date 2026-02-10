import smtplib
from email.message import EmailMessage
from rich.console import Console

console = Console()

def mail_gonder():
    gonderen_mail = "gonderen_mail"
    uygulama_sifresi = "uygulama_sifresi"  
    alici_mail = input("📧 Alıcı e-posta adresini girin: ")
    
    msg = EmailMessage()
    msg['Subject'] = "Python Otomasyon Testi 🚀"
    msg['From'] = gonderen_mail
    msg['To'] = alici_mail
    msg.set_content("Selam! Bu mesaj 8. Gün Python otomasyonu ile otomatik olarak gönderilmiştir. Harika gidiyoruz!")

    try:
        console.print("[yellow]Mail gönderiliyor...[/]")
        

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(gonderen_mail, uygulama_sifresi)
            smtp.send_message(msg)
            
        console.print("[bold green]✅ E-posta başarıyla gönderildi![/]")
        
    except Exception as e:
        console.print(f"[bold red]Hata oluştu:[/] {e}")

if __name__ == "__main__":
    mail_gonder()