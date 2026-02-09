from pathlib import Path
from config import regex_read, regex_sent

def validate_file(file: Path) -> bool:
    return (
        file.is_file()
        and file.suffix.lower() == '.pdf'
        and regex_read.fullmatch(file.stem)
    )


def rename_sent_file(file: Path):
    filename = file.stem

    if regex_read.fullmatch(filename) and '[ENVIADO]' not in filename:
        new_filename = f'{filename} [ENVIADO]{file.suffix}'
        file.rename(file.with_name(new_filename))


