from pathlib import Path
from smtplib import SMTP
from email.message import EmailMessage

from config import regex, BASE_DIR, CREDENTIALS

basepath = BASE_DIR


def validate_file(file: Path):
    if not file.is_file():
        return None

    if not file.suffix.lower() == '.pdf':
        return None
    
    if not regex.fullmatch(file.stem):
        return None
    
    return file

def send_email(files):
    msg = EmailMessage()
    msg['From'] = CREDENTIALS['email']
    msg['To'] = CREDENTIALS['destino']
    msg['Subject'] = 'Envio de contrato'
    msg.set_content("""Olá,

            Segue em anexo o contrato assinado.

            Atenciosamente,
            Prefeitura Municipal
            """)

    for file in files:
        with file.open('rb') as f:
            msg.add_attachment(
                f.read(),
                maintype='application',
                subtype='pdf',
                filename=file.name
            )

    with SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(
            CREDENTIALS['email'], 
            CREDENTIALS['senha_app']
            )
        server.send_message(msg)

contracts = []

for modality in basepath.iterdir(): # Dispensas, aditivos, inex
    if not modality.is_dir():
        continue

    for process_folder in modality.iterdir(): # 001 - Processo X, 002 - Processo Y
        if not process_folder.is_dir():
            continue

        enviar_file = process_folder / 'ENVIAR.txt'

        if enviar_file.exists():
            for file in process_folder.iterdir(): # Acessar a pasta e enviar o contrato
                validated = validate_file(file)
                if validated:
                    contracts.append(validated)

try:
    if contracts:
        send_email(contracts)
        print('Email enviado.')
except Exception:
    print(f'Falha ao enviar os contratos.')