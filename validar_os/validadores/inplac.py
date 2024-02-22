"""
inplac.py
"""
from validar_os.pdfs_teste import OS_INPLAC
from validar_os.validadores.utils import generate_texts_from_image_pdf


ID_ESPESSURA = 'Espessura do Clichê: '
ID_CAMADA = 'Impressão'
ID_FECHAMENTO = 'Fechamento de Cilindro: '
ID_COD_BARRAS = 'Código de Barras: '


def scan_lines(text: str) -> dict:
    result = {}

    lines = text.splitlines()
    for line in lines:
        if line.startswith(ID_CAMADA):
            if 'interna' in line.lower():
                result['camada'] = 'interna'
            elif 'externa' in line.lower():
                result['camada'] = 'externa'

        if line.startswith(ID_ESPESSURA):
            if '1,14' in line:
                result['espessura'] = 1.14
            elif '2,84' in line:
                result['espessura'] = 2.84

        if line.startswith(ID_FECHAMENTO):
            fechamento = line[len(ID_FECHAMENTO):]
            try:
                fechamento = fechamento.replace(',', '.')
                fechamento = float(fechamento)
            except ValueError:
                fechamento = None
            if fechamento:
                result['fechamento'] = fechamento

        if line.startswith(ID_COD_BARRAS):
            cod_barras = line[len(ID_COD_BARRAS):]
            if cod_barras:
                result['cod_barras'] = cod_barras

    return result


if __name__ == '__main__':
    for arquivo in OS_INPLAC:
        print(f'Verificando {arquivo.name}...')
        texto = generate_texts_from_image_pdf(arquivo)
        print(scan_lines(texto))
