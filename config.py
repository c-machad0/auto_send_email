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

read_pattern = r'''
^
(?: (?P<numero>\d+)\.\s* )?     # Número opcional
CONTRATO\s+
(?P<assunto>.+?)\s*            # Assunto
-\s*
(?P<empresa>.+?)               # Empresa
(?:\s+(?P<ano>\d{4}))?          # Ano opcional
$
'''
regex_read = re.compile(read_pattern, re.VERBOSE | re.IGNORECASE)

sent_pattern = r'''
^
(?: (?P<numero>\d{1,2})\.\s* )?   # Número opcional
CONTRATO\s+
(?P<assunto>.+?)\s*              # Assunto
-\s*
(?P<empresa>.+?)\s*              # Empresa
\s*\[ENVIADO\]                   # Literal [ENVIADO]
\.pdf
$
'''

regex_sent = re.compile(sent_pattern, re.VERBOSE | re.IGNORECASE)