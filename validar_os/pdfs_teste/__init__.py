from pathlib import Path


DIR_INPLAC = Path(__file__).parent.joinpath('inplac')
OS_INPLAC = [pdf for pdf in DIR_INPLAC.iterdir() if pdf.suffix.lower() == '.pdf']
TXT_INPLAC = [pdf for pdf in DIR_INPLAC.iterdir() if pdf.suffix.lower() == '.txt']
