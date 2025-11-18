from flask import Flask, request, jsonify, render_template
import sqlite3
import unicodedata
from difflib import SequenceMatcher

app = Flask(__name__)

# --- Função para remover acentos ---
def remover_acentos(txt):
    return ''.join(c for c in unicodedata.normalize('NFD', txt) if unicodedata.category(c) != 'Mn')

# --- Função para buscar resposta no banco com similaridade ---
def buscar_resposta(pergunta):
    pergunta_limpa = remover_acentos(pergunta.lower().strip())

    conn = sqlite3.connect("banco.db")
    cursor = conn.cursor()
    cursor.execute("SELECT palavra_chave, resposta FROM respostas")
    resultados = cursor.fetchall()
    conn.close()

    melhor_resposta = None
    maior_similaridade = 0.0

    for chave, resposta in resultados:
        chave_limpa = remover_acentos(chave.lower())
        similaridade = SequenceMatcher(None, pergunta_limpa, chave_limpa).ratio()

        if similaridade > maior_similaridade:
            maior_similaridade = similaridade
            melhor_resposta = resposta

    if maior_similaridade >= 0.6:
        return melhor_resposta

    return None

# --- Rota principal ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Rota de perguntas ---
@app.route('/perguntar', methods=['POST'])
def perguntar():
    data = request.get_json()
    pergunta = data.get('mensagem', '').strip()

    resposta = buscar_resposta(pergunta)

    if not resposta:
        resposta = "❓ Não encontrei nada sobre isso. Tente palavras como: música, plano, artista, baixar, etc."

    return jsonify({"resposta": resposta})

# --- Executar app ---
if __name__ == '__main__':
    app.run(debug=True)
