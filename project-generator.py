import subprocess


def lendo_entradas():
    local = input("Digite o local que deseja criar o projeto Angular: ")
    nome_do_projeto = input("Digite o nome do projeto:")
    print(local, nome_do_projeto)
    criar_projeto(local, nome_do_projeto)

def  criar_projeto(local, nome_do_projeto):
    comando = "ng new " + nome_do_projeto
    localAlterar = "cd "
    print(comando)
    subprocess.run('cd ')
    subprocess.run('echo testado')



if __name__ == '__main__':
    lendo_entradas()