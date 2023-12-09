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
            self.executa_comando(f'git clone {repositorio}')
            self.log(f"INFO: INSTALADO | {repositorio}")
        self.log(f"INFO: LISTA DE REPOSITORIOS CONCLUIDA", "yellow")

    def login(self):
        self.executa_comando(f'git config --global credential.helper store && echo -e "https://{self.usuario}:{self.senha}@github.com" > ~/.git-credentials')
        self.log(f"INFO: USUARIO {self.usuario} AUTENTICADO", "yellow")

    def executa_comando(self, comando):
        try:
            return subprocess.run(comando, capture_output = True, text = True, check = True).stdout.strip() 
        except subprocess.CalledProcessError as e:
            self.log("ERROR: FALHA NA EXECUCAO DO COMANDO", "red")
            return e.stderr.strip()
        
    def log(self, mensagem, tipo = "green"):
        Console().log(mensagem, style = f"bold black on {tipo}")


if __name__ == "__main__":
    Git(usuario, senha).clona_repositorios(repositorios)
