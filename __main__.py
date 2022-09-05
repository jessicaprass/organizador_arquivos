import os
import shutil

#Função cria pastas
def cria_pastas():
    #verifica se existe pastas
    if not os.path.exists('documentos'):
        os.mkdir('documentos')

    if not os.path.exists('planilhas'):
        os.mkdir('planilhas')

#Função move arquivos
def move_arquivos():
    arquivos = os.listdir()
    #Percorrendo lista arquivos
    for arquivo in arquivos:
        if ".doc" in arquivo:
            shutil.move(arquivo, "documentos")
        if ".xls" in arquivo:
            shutil.move(arquivo, "planilhas")


#Executa
if __name__ == "__main__":
    cria_pastas()
    move_arquivos()
