import os


def limpar_terminal() -> None:
    os.system("cls" if os.name == "nt" else "clear")