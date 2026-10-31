import sqlite3

conexao = sqlite3.connect("vendas.db")
cursor = conexao.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto TEXT NOT NULL,
        valor REAL NOT NULL,
        data TEXT
    )
''')
conexao.commit()

def cadastrar_venda(produto, valor, data):
    if valor <= 0:
        print(f"Erro: O valor de '{produto}' não pode ser zero ou negativo.")
        return
        
    try:
        cursor.execute("INSERT INTO vendas (produto, valor, data) VALUES (?, ?, ?)", (produto, valor, data))
        conexao.commit()
        print(f"Sucesso: Venda de '{produto}' registrada!")
    except Exception as erro:
        print(f"Deu erro ao salvar no banco: {erro}")

def relatorio_vendas():
    print("\n--- Relatório Geral de Vendas ---")
    cursor.execute("SELECT SUM(valor) FROM vendas")
    total = cursor.fetchone()[0]
    
    total_formatado = total if total else 0.0
    
    print(f"Total faturado: R$ {total_formatado:.2f}")
    print("---------------------------------\n")


cadastrar_venda("Curso de Python", 150.00, "30/10/2026")
cadastrar_venda("Mentoria SQL", 250.00, "30/10/2026")
cadastrar_venda("E-book duvidoso", -50.00, "30/10/2026")

relatorio_vendas()

conexao.close()
