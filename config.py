import re
import os
from dotenv import load_dotenv
from pathlib import Path


load_dotenv()

CREDENTIALS = {
    'email': os.getenv("email"),
    'senha_app': os.getenv("senha_app"),
    'destino': os.getenv("destino")
}

BASE_DIR = Path(os.getenv("base_dir"))

padrao = r'''
^
(?: (?P<numero>\d+)\.\s* )?     # Número opcional
CONTRATO\s+
(?P<assunto>.+?)\s*            # Assunto
-\s*
(?P<empresa>.+?)               # Empresa
(?:\s+(?P<ano>\d{4}))?          # Ano opcional
$
'''
regex = re.compile(padrao, re.VERBOSE | re.IGNORECASE)