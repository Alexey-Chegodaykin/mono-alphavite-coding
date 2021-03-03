python main.py -fin 'oneday.txt' -fout 'oneday-encrypt.txt' -shift 3 -type 0
python main.py -fin 'oneday-encrypt.txt' -fout 'oneday-decrypt-conformity.txt' -type 1 -train 'dreamshed.txt' -decryption-method 0
python main.py -fin 'oneday-encrypt.txt' -fout 'oneday-decrypt-shift.txt' -type 1 -train 'dreamshed.txt' -decryption-method 1