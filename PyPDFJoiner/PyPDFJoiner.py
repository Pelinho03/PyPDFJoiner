import PyPDF2  # Importa a biblioteca PyPDF2 para manipulação de PDFs
import os  # Importa a biblioteca os para interagir com o sistema de ficheiros

# Cria um objeto de merger (união) de PDFs da biblioteca PyPDF2
merger = PyPDF2.PdfMerger()

# Obtém a lista de ficheiros da pasta 'arquivos' (onde estão os PDFs) e guarda na variável lista_arquivos
lista_arquivos = os.listdir('arquivos')

# Ordena a lista de ficheiros em ordem alfabética (neste caso, pdf1, pdf2, pdf3)
lista_arquivos.sort()

# Exibe no terminal a lista de ficheiros encontrados para conferência
print(lista_arquivos)

# Percorre cada ficheiro da lista
for arquivo in lista_arquivos:
    # Verifica se o ficheiro é um PDF (se contém '.pdf' no nome)
    if '.pdf' in arquivo:
        # Junta o PDF ao objeto merger, usando o caminho completo para cada ficheiro
        merger.append(f'arquivos/{arquivo}')

# Após unir todos os PDFs, escreve o resultado no ficheiro 'PDF Final.pdf'
merger.write('PDF Final.pdf')
