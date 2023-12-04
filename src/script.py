#1. Acessar diretorio
#2. Criar pasta "pasta1" e "pasta2"
#3. Percorrer subpastas do diretório
#3.1 Extrair subpastas .zip
#4. Mover subpastas que contém "pastaY" para a pasta "pasta2"
#5. Mover subpastas que contém "pastaX" para a pasta "pasta1"

import os.path
import zipfile
#from zipfile import ZipFile

#1. Acessar diretorio
try:
    directoryInput = input('Digite o diretorio (nao esqueca de utilizar duas "\\" para separar pastas: ')
    os.chdir(directoryInput)
    print(f'{directoryInput} acessado')

#2. Criar pasta "pasta1" e "pasta2"
    if not os.path.exists(directoryInput + './pasta1'):
        print('Criando pasta .\pasta1...')
        os.makedirs(directoryInput + './pasta1')
        print('Pasta .\pasta1 criada com sucesso!')
    else:
        print('A pasta .\pasta1 ja existe!')
        
    if not os.path.exists(directoryInput + './pasta2'):
        print('Criando pasta .\pasta2...')
        pasta2 = os.makedirs(directoryInput + './pasta2')
        print('Pasta .\pasta2 criada com sucesso!')
    else:
        print('A pasta .\pasta2 ja existe!')
except ValueError:
    print('O caminho informado nao existe')

#3. Percorrer subpastas do diretorio e extrair arquivos .zip
for foldersDate in os.listdir(directoryInput):
    for dirpath, dirnames, filenames in os.walk(foldersDate):
        for arquivo in filenames:
            if arquivo.endswith('.zip'):
                caminho_completo = os.path.join(dirpath, arquivo)
                with zipfile.ZipFile(caminho_completo, 'r') as zip_ref:
                    zip_ref.extractall(dirpath)
                    print(f'Extraindo -> {arquivo}')
   