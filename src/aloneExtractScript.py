from zipfile import ZipFile

try:
    z = ZipFile('logs.zip', 'r')
    z.extractall()
    z.close()
except:
    print('Arquivo nao encontrado')