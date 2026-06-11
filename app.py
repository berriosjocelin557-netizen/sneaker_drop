from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# --- CONFIGURACIÓN ---
INVENTARIO = 5
# Aquí pegarás los datos de tu bot de Telegram en el Paso 2:
TELEGRAM_TOKEN = '8748113402:AAFDe75qG4PsUStcIWtO4mSBxDPiKAYRGSU'
CHAT_ID = 'TU_CHAT_ID_AQUI'

def enviar_alerta_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={'chat_id': CHAT_ID, 'text': mensaje})

@app.route('/')
def index():
    return render_template('index.html', inventario=INVENTARIO)

@app.route('/comprar', methods=['POST'])
def comprar():
    global INVENTARIO
    if INVENTARIO > 0:
        INVENTARIO -= 1
        enviar_alerta_telegram(f"🚨 ¡NUEVA COMPRA en Sneaker Drop! Quedan {INVENTARIO} pares disponibles.")
        return jsonify({'success': True, 'inventario': INVENTARIO})
    else:
        return jsonify({'success': False, 'mensaje': 'Agotado'})

if __name__ == '__main__':
    app.run(debug=True)