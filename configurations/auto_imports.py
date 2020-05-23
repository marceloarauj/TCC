import subprocess
import sys

def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m","pip","install","matplotlib"])
        subprocess.check_call([sys.executable, "-m","pip","install","opencv-python"])
        subprocess.check_call([sys.executable, "-m","pip","install","numpy"])
        subprocess.check_call([sys.executable, "-m","pip","install","--upgrade","https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl"])
    except:
        print('Erro na importacao dos modulos')
