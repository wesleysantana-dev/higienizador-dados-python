Higienizador de dados de vendas

Script em Python que registra vendas em um banco SQLite (`vendas.db`) e recusa registros inválidos.

---O que faz ---
- Cria a tabela `vendas` se ela não existir
- Recusa vendas com valor zero ou negativo
- Salva as vendas válidas no banco
- Gera um relatório com o total faturado

--- Como rodar ---
python higienizador.py
