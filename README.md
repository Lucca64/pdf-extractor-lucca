# 📄 PDF Extractor - DocuMaster Solutions

Projeto desenvolvido para a Avaliação Final de Assistente Técnico. Esta ferramenta automatiza a extração de texto de arquivos PDF, permitindo selecionar páginas específicas.

## 🛠️ Tecnologias
- Python 3.14
- Biblioteca `pypdf`

## 🚀 Como Executar
1. Instale a biblioteca necessária:
   `pip install pypdf`

2. Execute o extrator passando o caminho do arquivo:
   `python src/extrator.py --input seu_arquivo.pdf`

3. Para extrair páginas específicas (ex: 1 e 3):
   `python src/extrator.py --input seu_arquivo.pdf --pages 1,3`

## 📦 Requisitos Funcionais
- [x] Extração total de texto.
- [x] Filtro por páginas específicas.
- [x] Tratamento de erros (PDF com senha ou vazio).
