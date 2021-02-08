import time
import argparse

from encryption import Encryption
from decryption import Decryption


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-fin', type=str, dest='source_file', help='Path to source file')
    parser.add_argument('-fout', type=str, dest='target_file', help='Path to target file')
    parser.add_argument('-type', type=int, dest='type', required=False, help='0 - encryption, 1 - decryption')
    parser.add_argument('-shift', type=int, dest='shift', required=False, default=0, help='Value of shifting')
    parser.add_argument('-train', type=str, dest='train_file', required=False, help='Path to train file for decryption')
    parser.add_argument('-decryption-method', type=int, dest='method', required=False, default=0, help='0 - conformity, 1 - shift')
    args = parser.parse_args()
    
    if args.type == 0:
        encryption = Encryption()
        start = time.time()
        encryption.encrypt(args.source_file, args.target_file, args.shift)
        end = time.time()
        print(f'Runtime of the encryption is {round(end - start, 2)}')
    elif args.type == 1:
        decryption = Decryption()

        if args.method == 0:
            start = time.time()
            conformity: dict = decryption.conformity(args.source_file, args.train_file)
            decryption.conformity_decrypt(args.source_file, args.train_file, args.target_file)
            end = time.time()
            print(f'Dictionary conformity is:\n {conformity}')
            print(f'Runtime of the encryption is {round(end - start, 2)}')
        elif args.method == 1:
            start = time.time()
            shift: int = decryption.shift_predict(args.source_file, args.train_file)
            decryption.shift_decrypt(args.source_file, args.train_file, args.target_file)
            end = time.time()
            print(f'Predict shift is {shift}.')
            print(f'Runtime of the encryption is {round(end - start, 2)}')
        else:
            raise Exception('Selected decryption type does not support.')    
    else:
        raise Exception('Selected type orientation does not support.')
