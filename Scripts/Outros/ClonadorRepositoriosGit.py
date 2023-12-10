import subprocess
from rich.console import Console

usuario = ""
senha = ""

repositorios = [
    "https://github.com/kaiquesouzasantos/java-maratona-programacao-cps.git",
    "https://github.com/kaiquesouzasantos/estudos-especializacao-java.git"
]

class Git:
    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha
        self.login()

    def clona_repositorios(self, repositorios):
        for repositorio in repositorios:
           self.clona_repositorio(repositorio)
        self.log(f"INFO: CLONAGEM DA LISTA DE REPOSITORIOS CONCLUIDA", "blue")

    def clona_repositorio(self, repositorio):
        try:
            self.executa_comando(f'git clone {repositorio}')
            self.log(f"INFO: INSTALADO | {repositorio}")
        except subprocess.CalledProcessError as e:
            self.log("ERROR: FALHA NA CLONAGEM DO REPOSITORIO", "red")

    def login(self):
        try:
            self.executa_comando(f'git config --global credential.helper store && echo -e "https://{self.usuario}:{self.senha}@github.com" > ~/.git-credentials')
            self.log(f"INFO: USUARIO {self.usuario} AUTENTICADO", "purple")
        except subprocess.CalledProcessError as e:
            self.log("ERROR: FALHA NA AUTENTICACAO DO USUARIO", "red")

    def executa_comando(self, comando):
        return subprocess.run(comando, capture_output = True, text = True, check = True).stdout.strip()
    
    def log(self, mensagem, tipo = "green"):
        Console().log(mensagem, style = f"bold black on {tipo}")

if __name__ == "__main__":
    Git(usuario, senha).clona_repositorios(repositorios)
