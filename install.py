import argparse
import subprocess

def deploy_pyenv(pyenv_path):
    # Liste der Pakete, die installiert werden sollen
    packages = [
        'pyautogui',
        'numpy',
        'PIL',
        'json',
        'pytesseract',
        'queue',
        'PyQt5'
    ]

    # Erstellen Sie ein virtuelles Python-Umgebung (pyenv)
    subprocess.run(['python', '-m', 'venv', pyenv_path], check=True)

    # Aktivieren Sie das erstellte pyenv
    activate_script = f'{pyenv_path}/Scripts/activate'
    subprocess.run(['cmd', '/K', activate_script], check=True)

    # Installieren Sie alle Pakete in der virtuellen Umgebung
    for package in packages:
        subprocess.run(['pip', 'install', package], check=True)

    print("Deployment abgeschlossen.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skript zum Bereitstellen eines pyenv mit allen benötigten Paketen.")
    parser.add_argument("pyenv_path", type=str, help="Pfad, in dem das pyenv erstellt werden soll")
    args = parser.parse_args()

    deploy_pyenv(args.pyenv_path)