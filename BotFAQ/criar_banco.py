import sqlite3

# Cria novo banco
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# Cria tabela de respostas
cursor.execute("""
CREATE TABLE IF NOT EXISTS respostas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    palavra_chave TEXT NOT NULL,
    resposta TEXT NOT NULL
)
""")

# Dados iniciais sobre streaming de música 🎵
respostas = [
    ("plano", "Temos três planos: Gratuito, Premium e Família. O Premium remove anúncios e permite baixar músicas."),
    ("assinar", "Para assinar o plano Premium, clique em 'Assinar Agora' na página inicial ou no menu do aplicativo."),
    ("cancelar", "Você pode cancelar sua assinatura a qualquer momento em 'Minha Conta' > 'Assinatura'."),
    ("playlist", "Crie, edite e compartilhe suas playlists na aba 'Minhas Playlists'."),
    ("música", "Use a barra de pesquisa para encontrar suas músicas favoritas."),
]

cursor.executemany("""
INSERT INTO respostas (palavra_chave, resposta)
VALUES (?, ?)
""", respostas)

conn.commit()
conn.close()

print("🎶 Banco de dados criado e populado com sucesso!")
