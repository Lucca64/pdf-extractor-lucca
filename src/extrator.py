import argparse
from pypdf import PdfReader

def extrair_texto(caminho_pdf, paginas_selecionadas=None):
    try:
        reader = PdfReader(caminho_pdf)
        texto_final = ""
        
        # Se não houver filtro, pega todas as páginas
        if not paginas_selecionadas:
            paginas = range(len(reader.pages))
        else:
            # Transforma "1,3" em lista de índices [0, 2]
            paginas = [int(p.strip()) - 1 for p in paginas_selecionadas.split(',')]

        for i in paginas:
            if 0 <= i < len(reader.pages):
                texto_final += f"\n--- PÁGINA {i+1} ---\n"
                texto_final += reader.pages[i].extract_text()
            else:
                print(f"Aviso: Página {i+1} está fora do intervalo.")

        if reader.is_encrypted:
            return "Erro: O arquivo está protegido por senha."
        if len(reader.pages) == 0:
            return "Erro: O PDF está vazio ou sem texto extraível."
        
        return texto_final

    except Exception as e:
        return f"Erro: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrator de PDF DocuMaster")
    parser.add_argument("--input", required=True, help="Caminho do PDF")
    parser.add_argument("--pages", help="Páginas (ex: 1,3,5)")
    
    args = parser.parse_args()
    resultado = extrair_texto(args.input, args.pages)
    print(resultado)
