import sqlite3

# Conectar ao banco existente
conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

# Limpa tabela
cursor.execute("DELETE FROM respostas")

# Novas respostas
respostas_musica = [
    ("oi", "Olá! Eu sou o FleekBot. Me diga uma palavra-chave como plano, suporte, login ou musica e eu te ajudo."),
    ("ola", "Olá! Eu sou o FleekBot. Me diga uma palavra-chave como plano, suporte, login ou musica e eu te ajudo."),
    ("boa tarde", "Olá! Eu sou o FleekBot. Me diga uma palavra-chave como plano, suporte, login ou musica e eu te ajudo."),
    ("boa noite", "Olá! Eu sou o FleekBot. Me diga uma palavra-chave como plano, suporte, login ou musica e eu te ajudo."),
    ("bom dia", "Olá! Eu sou o FleekBot. Me diga uma palavra-chave como plano, suporte, login ou musica e eu te ajudo."),
    ("plano", "Temos três planos: Gratuito, Premium e Família."),
    ("assinar", "Para assinar o Premium, vá até 'Assinar Agora'."),
    ("cancelar", "Você pode cancelar em Minha Conta > Assinatura."),
    ("playlist", "Crie e gerencie suas playlists em Minhas Playlists."),
    ("musica", "Busque por músicas usando a barra de pesquisa."),
    ("artista", "Pesquise artistas na aba Explorar."),
    ("album", "Veja todos os álbuns de um artista na página dele."),
    ("baixar", "Premium permite baixar músicas e ouvir offline."),
    ("download", "Downloads são exclusivos para assinantes Premium."),
    ("dispositivo", "Plano Família permite até 4 dispositivos."),
    ("favorito", "Use o botão de favoritar para salvar músicas."),
    ("ouvir", "Clique em Tocar para ouvir imediatamente."),
    ("letra", "Ative letras nas Configurações."),
    ("conta", "Gerencie sua conta em Minha Conta."),
    ("pagamento", "Aceitamos cartão, boleto e PIX."),
    ("familia", "O plano Família tem 4 perfis independentes."),
    ("suporte", "Fale com suporte: fleek.suporte@gmail.com"),
    ("problema", "Reinicie o app ou faça login novamente."),
    ("login", "Se não conseguir entrar, use 'Esqueci minha senha'."),
    ("senha", "Altere sua senha em Minha Conta."),
    ("site", "Nosso site funciona em desktop e mobile."),
    ("offline", "Premium permite ativar modo offline."),
    ("explorar", "Veja tendencias e lançamentos em Explorar."),
    ("genero", "Filtre músicas por gênero."),
]

cursor.executemany("""
INSERT INTO respostas (palavra_chave, resposta)
VALUES (?, ?)
""", respostas_musica)

conn.commit()
conn.close()

print("🎧 Banco de dados atualizado com sucesso!")
