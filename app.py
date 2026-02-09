from config import BASE_DIR, CREDENTIALS
from email_service import EmailService
from utils import validate_file, rename_file_flag


class App:

    def __init__(self):
        self.basepath = BASE_DIR
        self.sender = EmailService()

        self.contracts = []

    def navigation(self):
        for modality in self.basepath.iterdir(): # Dispensas, aditivos, inex
            if not modality.is_dir():
                continue

            for process_folder in modality.iterdir(): # 001 - Processo X, 002 - Processo Y
                if not process_folder.is_dir():
                    continue

                enviar_file = process_folder / 'ENVIAR.txt'

                if enviar_file.exists():
                    rename_file_flag(enviar_file)
                    for file in process_folder.iterdir(): # Acessar a pasta e enviar o contrato
                        validated = validate_file(file)
                        if validated:
                            self.contracts.append(validated)

    def run_app(self):
        self.navigation()
        
        try:
            if self.contracts:
                self.sender.format_email(self.contracts)
                self.sender.send_email()
                print('Email enviado.')
        except Exception as e:
            print(f'{e}: Falha ao enviar os contratos.')

if __name__ == '__main__':
    app = App()
    app.run_app()