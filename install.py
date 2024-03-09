import argparse
import subprocess

def deploy_pyenv(pyenv_path, install_pkg=False):
    # Liste der Pakete, die installiert werden sollen
    print(f'{pyenv_path} | {install_pkg}')

    # Erstellen Sie ein virtuelles Python-Umgebung (pyenv)
    try:
        subprocess.run(['python', '-m', 'venv', pyenv_path], check=True)
    except:
         print("Allready set up")
    # Aktivieren Sie das erstellte pyenv
    activate_script = f'{pyenv_path}/Scripts/activate'
#    subprocess.run(['cmd', '/K', activate_script], check=True)

    # Installieren Sie alle Pakete in der virtuellen Umgebung
    if install_pkg:
         installPackages()

    print("Deployment abgeschlossen.")

def installPackages():
    packages = [
        'pillow',
        'pyautogui',
        'numpy',
        'pytesseract',
        'PyQt5',
        'keyboard',
        'pywin32',
        'opencv-python'
    ]

    for package in packages:
            print(f"Trying to install {package}")
            subprocess.check_call(['pip', 'install', package])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Skript zum Bereitstellen eines pyenv mit allen benötigten Paketen.")
    parser.add_argument("pyenv_path", type=str, help="Pfad, in dem das pyenv erstellt werden soll")
    parser.add_argument("install_pkg", type=bool, help="tell me if i should istall the packages")
    args = parser.parse_args()

    deploy_pyenv(args.pyenv_path, args.install_pkg)