import sys


def main():
    # https://www.pythonforbeginners.com/system/python-sys-argv
    if len(sys.argv) < 3:
        # https://en.wikipedia.org/wiki/Standard_streams#Standard_error_(stderr)
        return sys.stderr("Verifique os argumentos")
    
    print("deu bom")
