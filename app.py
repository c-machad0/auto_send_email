from config import BASE_DIR
from email_service import EmailService
from utils import validate_file, rename_sent_file


class App:

    def __init__(self):
        self.basepath = BASE_DIR
        self.sender = EmailService()

        self.contracts = []

    def navigation(self):
        files_to_rename = []

        for modality in self.basepath.iterdir(): # Dispensas, aditivos, inex
            if not modality.is_dir():
                continue

            for process_folder in modality.iterdir(): # 001 - Processo X, 002 - Processo Y
                if not process_folder.is_dir():
                    continue

                for file in process_folder.iterdir(): # Acessar a pasta e enviar o contrato
                    if validate_file(file):
                        self.contracts.append(file)
                        files_to_rename.append(file)

        
        return files_to_rename


    def run_app(self):
        files_to_rename = self.navigation()

        try:
            if self.contracts:
                self.sender.format_email(self.contracts)
                self.sender.send_email()

                for file in files_to_rename:
                    rename_sent_file(file)
                    
                print('Email enviado.')
        except Exception as e:
            print(f'{e}: Falha ao enviar os contratos.')

if __name__ == '__main__':
    app = App()
    app.run_app()