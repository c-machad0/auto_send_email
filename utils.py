from pathlib import Path
from config import regex

def validate_file(file: Path):
    if not file.is_file():
        return None

    if not file.suffix.lower() == '.pdf':
        return None
    
    if not regex.fullmatch(file.stem):
        return None
    
    return file

def rename_file_flag(file: Path):
    file.rename(file.with_name('ENVIADO.txt'))

