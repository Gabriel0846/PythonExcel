import openpyxl

# Carrega arquivo
book = openpyxl.load_workbook('Planilha de Compras.xlsx')

# seleciona uma pagina
frutas_page = book['Frutas']

#imprimi os dados de cada linha
for rows in frutas_page.iter_rows(min_row=2, max_row=5):
    for cell in rows:
        if cell.value == 'Banana':
            cell.value = 'Fruta 1'

# salvar as alterações
book.save('Planilha de Compras v2.xlsx')