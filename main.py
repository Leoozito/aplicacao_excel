import openpyxl
# Pegar dados do Excel
arquivo_excel =  openpyxl.load_workbook("IC-Accounts-Payable-Ledger-Template-Updated-57129_PT.xlsx")
dados = arquivo_excel.active

total_linhas = dados.max_row
total_colunas = dados.max_column

# Percorra as linhas e colunas preenchidas com dados
for linha in range(1, total_linhas + 1):
    for coluna in range(1, total_colunas + 1):
        celula = dados.cell(row=linha, column=coluna)
        valor = celula.value
        if valor is not None:
            print(f"Célula na linha {linha}, coluna {coluna}: {valor}")




# Digitaliza os dados em um relatorio

# Fazer o calculo dos dados

# Fazer um relatorio dos dados  
 
# Salvar o arquivo relatorio

# Colocar no Excel o caminho salvo