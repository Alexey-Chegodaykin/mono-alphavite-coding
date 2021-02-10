from typing import List
from settings import ALPHAVITE


class Encryption:
    def __init__(self, encoding='windows-1251'):
        self._upper_alphavite: List[str] = [char.upper() for char in ALPHAVITE]
        self._lower_alphavite: List[str] = [char.lower() for char in ALPHAVITE]
        self._encoding: str = encoding
    
    def _shift_char(self, alphavite_list: List, char: str, shift: int) -> str:
        alphavite_len: int = len(alphavite_list)

        while True:
            for ind, elem in enumerate(alphavite_list):
                if elem == char:
                    return alphavite_list[(ind + shift) % alphavite_len]
                else:
                    continue
    
    def _compute_encrypt_stream(self, source_file: str, shifting: int) -> str:
        encrypt_stream: str = ''

        with open(source_file, 'r', encoding=self._encoding) as fin:
            source_data: str = fin.read()

            for char in source_data:
                if char.isupper() and (char in self._upper_alphavite):
                    encrypt_stream += self._shift_char(self._upper_alphavite, char, shifting)
                elif char.islower() and (char in self._lower_alphavite):
                    encrypt_stream += self._shift_char(self._lower_alphavite, char, shifting)
                else:
                    encrypt_stream += char
            fin.close()
        
        return encrypt_stream

    def _write_encrypt_stream(self, encrypt_file: str, encrypt_stream: str):
        with open(encrypt_file, 'w', encoding=self._encoding) as fout:
            fout.write(encrypt_stream)
            fout.close()

    def encrypt(self, source_file: str, encrypt_file: str, shifting: int):
        encrypt_stream: str = self._compute_encrypt_stream(source_file, shifting)
        self._write_encrypt_stream(encrypt_file, encrypt_stream)
        print(f'Caesar encryption with shift {shifting} completed successfully.')
