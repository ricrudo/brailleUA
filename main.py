# -*- coding: utf-8 -*-


"""
MusicXML -> BRF (ASCII braille) usando SOLO music21
Requisitos: pip install music21

Uso:
  python xml_a_brf_music21.py entrada.musicxml salida.brf
"""

import sys
from pathlib import Path
from music21 import converter, braille
import re


pat = re.compile(
    r'^(?:title_(?P<title>[^_]+))?(?:_composer_(?P<composer>[^_]+))?\.(?:mxl|musicxml|xml)$',
    re.IGNORECASE
)

def parse_filename(input_xml: str):
    name = Path(input_xml).name
    m = pat.fullmatch(name)
    if not m:
        return None, None
    return m.group('title') or None, m.group('composer') or None

def add_title_and_composer(output_brf:str, input_xml:str):
    content_brf = Path(output_brf).read_text()
    metadata = parse_filename(input_xml)
    title = metadata[0]
    composer =  metadata[1]
    str_final = ''
    if title:
        str_final += f'{title}\n'
    if composer:
        str_final += f'{composer}\n'
    str_final += content_brf
    Path(output_brf).write_text(str_final, encoding="ascii", errors="replace")

    print(f"Listo: {output_brf} con title {title} y composer {title}")


def musicxml_to_brf(input_xml: str, max_line_len: int = 40):
    # 1) Abrir MusicXML
    s = converter.parse(input_xml)
    
    # debería recopilar los metadatos del mxl, pero al parecer musescore no lo esta guardando
    datos = {}
    for data in dir(s.metadata):
        if isinstance(getattr(s.metadata, data), str):
            datos[data] = getattr(s.metadata, data)
    
    # Limpia el metadata para que solo aparezca la información musical
    s.metadata = None
    
    # 2) Traducir a braille (Unicode) con el motor interno
    #    Puedes usar objectToBraille/scoreToBraille/streamToBraille; aquí uno genérico:
    b_unicode = braille.translate.streamToBraille(
        s,
        maxLineLength=max_line_len,   # ancho de línea típico para BRF
        inPlace=False,                # aplica makeNotation() internamente
    )
    
    input_path = Path(input_xml)
    output_brf = input_path.parent / f"{input_path.stem}.brf"


    # 3) Pasar a ASCII braille (compatible BRF) y guardar .brf
    b_ascii = braille.basic.brailleUnicodeToBrailleAscii(b_unicode)
    output_brf.write_text(b_ascii, encoding="ascii", errors="replace")
    print(f"Listo: {output_brf}")

    add_title_and_composer(output_brf, input_xml)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python xml_a_brf_music21.py entrada.musicxml salida.brf")
        sys.exit(1)
    musicxml_to_brf(sys.argv[1])
