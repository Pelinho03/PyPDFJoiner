
# PyPDFJoiner

**PyPDFJoiner** é uma ferramenta simples em Python para juntar múltiplos ficheiros PDF num único documento. Este projeto foi criado com o objetivo de automatizar a tarefa de combinar PDFs, sendo ideal para quem precisa de uma solução rápida e eficiente.

## Funcionalidades
- Junta dois ou mais PDFs num único ficheiro final.
- Ordena automaticamente os PDFs por nome de ficheiro antes de os combinar.
- Interface de linha de comandos simples e fácil de usar.

## Pré-requisitos

Para executar este projeto, vais precisar de:

- Python 3.6 ou superior
- Biblioteca **PyPDF2**

Podes instalar a biblioteca necessária com o seguinte comando:

```bash
pip install PyPDF2
```

## Como utilizar

1. Cria uma pasta chamada `arquivos` no mesmo diretório onde está o script Python.
2. Coloca todos os ficheiros PDF que pretendes combinar dentro da pasta `arquivos`. 
3. O script ordena os ficheiros PDF por nome de forma automática, garantindo que a ordem de junção é a correta.
4. Executa o script com o comando:

```bash
python PyPDFJoiner.py
```

5. O ficheiro resultante será gravado como **'PDF Final.pdf'** no mesmo diretório.

## Exemplo de uso

Imagina que tens três ficheiros na pasta `arquivos`:
- `pdf1.pdf`
- `pdf2.pdf`
- `pdf3.pdf`

Após a execução do script, estes três ficheiros serão combinados e guardados como **'PDF Final.pdf'**.

## Estrutura do Projeto

```bash
|-- PyPDFJoiner
    |-- arquivos
        |-- pdf1.pdf
        |-- pdf2.pdf
        |-- pdf3.pdf
    |-- nome_do_script.py
    |-- PDF Final.pdf
```

## Notas
- Certifica-te de que todos os ficheiros na pasta `arquivos` são PDFs.
- A ordem de junção segue a ordem alfabética dos nomes dos ficheiros.

## Contribuições
Sente-te à vontade para contribuir com melhorias, como suporte para separar páginas ou adicionar mais funcionalidades de manipulação de PDFs. Podes fazer um fork deste projeto e abrir uma pull request com as tuas sugestões.

---
