from smtplib import SMTP
from email.message import EmailMessage


from config import CREDENTIALS


class EmailService:
    def __init__(self):
        self.email_from = CREDENTIALS['email']
        self.email_to = CREDENTIALS['destino']
        self.password_app = CREDENTIALS['senha_app']

    def format_email(self, files: list):
        self.msg = EmailMessage()
        self.msg['From'] = self.email_from
        self.msg['To'] = self.email_to
        self.msg['Subject'] = 'Envio de contrato'
        self.msg.set_content("""Olá,

                Segue em anexo o(s) contrato(s) feitos no dia de hoje.

                Atenciosamente,
                Christian - Departamento de Licitações e Contratos
                """)

        for file in files:
            with file.open('rb') as f:
                self.msg.add_attachment(
                    f.read(),
                    maintype='application',
                    subtype='pdf',
                    filename=file.name
                )


    def send_email(self):
        with SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(
                self.email_from, 
                self.password_app,
                )
            server.send_message(self.msg)