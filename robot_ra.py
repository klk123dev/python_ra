# CÓDIGO ACTUALIZADO JUNIO 2025
import requests
from telegram import Bot
import time

TOKEN = "8173170619:AAEQBfEH1hlhj47t9VO4k8RTwU0wOa64ZV0"  # 👈 El que te dio @BotFather
CHAT_ID = "5397929116"  # 👈 Envía "Hola" a @RawDataBot para saberlo
RA_URL = "https://es.ra.co/events/2072940"  # 👈 URL de tu evento

bot = Bot(token=TOKEN)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Robot activo 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

while True:
    try:
        # Truco 2025 para evitar bloqueos
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        page = requests.get(RA_URL, headers=headers, timeout=10).text
        
        # Detecta cambios (actualizado para RA 2025)
        if "Ticket sales have ended" not in page.lower() and "agotado" not in page.lower():
            bot.send_message(
                chat_id=CHAT_ID,
                text=f"🚨 ¡ENTRADAS DISPONIBLES! 🎟️\n{RA_URL}"
            )
        time.sleep(10)  # Revisa cada 10 segundos
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(60)
