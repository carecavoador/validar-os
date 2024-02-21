import pytesseract
from pypdf import PdfReader
from PIL import Image
from icecream import ic

from validar_os.pdfs_teste import OS_INPLAC


reader = PdfReader(OS_INPLAC)

page = reader.pages[0]
text = page.extract_text()


if text:
    ic(text)
else:
    print('Nenhum texto encontrado.')
    text = pytesseract.image_to_string(Image.open(OS_INPLAC))
