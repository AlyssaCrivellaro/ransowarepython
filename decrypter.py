import os
import pyaes

## abrir o arquivo que sera criptografado

file_name = 'teste.txt.ransomwaretroll'
file = open(file_name. 'rb')
file_data = file.read()
file.close()

## chave de descriptografia

key = b'testeransomware'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado

os.remove(file_name)

## criar um novo arquivo descriptografado

new_file = 'teste.txt'
new_file = open (f'{new_file}', 'wb')
new_file.write(decript_data)
new_file.close
