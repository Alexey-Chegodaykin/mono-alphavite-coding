from typing import List
from settings import ALPHAVITE


class Decryption:
    def __init__(self, encoding='windows-1251'):
        self._upper_alphavite: List[str] = [char.upper() for char in ALPHAVITE]
        self._lower_alphavite: List[str] = [char.lower() for char in ALPHAVITE]
        self._encoding: str = encoding

    def _max_shift_frequency(self, shifts: List[int]) -> int:
        shifts_dictionary: dict = {shift: 0 for shift in set(shifts)}

        for shift in shifts:
            if shift in shifts_dictionary.keys():
                shifts_dictionary[shift] += 1
            else:
                continue

        return max(shifts_dictionary, key=shifts_dictionary.get)

    def _shift_char(self, alphavite_list: List, char: str, shift: int) -> str:
        alphavite_len: int = len(alphavite_list)

        while True:
            for ind, elem in enumerate(alphavite_list):
                if elem == char:
                    return alphavite_list[(ind + shift) % alphavite_len]
                else:
                    continue
    
    def _frequency_chars(self, source_file: str) -> dict:
        alphavite: List[str] = self._upper_alphavite + self._lower_alphavite
        count_chars: dict = {key: 0 for key in alphavite}
    
        with open(source_file, 'r', encoding=self._encoding) as fin:
            data: str = fin.read()

            for char in data:
                if char in count_chars.keys():
                    count_chars[char] += 1
                else:
                    continue
        fin.close()

        total_count_chars: int = sum(count_chars.values())

        if not total_count_chars:
            raise Exception('Target chars is not found.')
        else:
            frequency_chars: dict = {key: value / total_count_chars for key, value in count_chars.items()} 

            return {key: value for key, value in sorted(frequency_chars.items(), 
                    key=lambda item: item[1], reverse=True)}

    def conformity(self, encrypt_file: str, train_file: str) -> dict:
        train_frequency: dict = self._frequency_chars(train_file)
        encrypt_frequency: dict = self._frequency_chars(encrypt_file)
        conformity_dictionary: dict = {encrypt_char: train_char for encrypt_char, train_char 
                                       in zip(encrypt_frequency.keys(), train_frequency.keys())}

        return conformity_dictionary

    def _shift_value(self, alphavite_list: List[str], encrypt_char: str, train_char: str) -> int:
        alphavite_len: int = len(alphavite_list)

        while True:
            if (encrypt_char or train_char) not in alphavite_list:
                raise Exception('Invalid char values.')
            elif encrypt_char == train_char:
                return 0 
            else:   
                for ind, elem in enumerate(alphavite_list):
                    if elem == encrypt_char:
                        encrypt_char_ind: int = ind
                    elif elem == train_char:
                        train_char_ind: int = ind
                    else:
                        continue

                return (encrypt_char_ind - train_char_ind) % alphavite_len
                    
    def shift_predict(self, encrypt_file: str, train_file: str) -> int:
        conformity: dict = self.conformity(encrypt_file, train_file)
        shifts: List[int] = []

        for encrypt_char, train_char in conformity.items():
            if encrypt_char.isupper() and train_char.isupper():
                shift: int = self._shift_value(self._upper_alphavite, encrypt_char, train_char)
                shifts.append(shift)
            elif encrypt_char.islower() and train_char.islower():
                shift: int = self._shift_value(self._lower_alphavite, encrypt_char, train_char)
                shifts.append(shift)
            else:
                continue

        return self._max_shift_frequency(shifts)
    
    def _decrypt_conformity_stream(self, encrypt_file: str, train_file: str) -> str:
        decrypt_stream: str = ''
        conformity: dict = self.conformity(encrypt_file, train_file)

        with open(encrypt_file, 'r', encoding=self._encoding) as fin:
            encrypt_data: str = fin.read()

            for char in encrypt_data:
                if char in (self._upper_alphavite + self._lower_alphavite):
                    decrypt_stream += conformity[char]
                else:
                    decrypt_stream += char
            
            fin.close()

        return decrypt_stream

    def _decrypt_shift_stream(self, encrypt_file: str, train_file: str) -> str:
        decrypt_stream: str = ''
        shifting: int = self.shift_predict(encrypt_file, train_file)

        with open(encrypt_file, 'r', encoding=self._encoding) as fin:
            encrypt_data: str = fin.read()

            for char in encrypt_data:
                if char.isupper() and (char in self._upper_alphavite):
                    decrypt_stream += self._shift_char(self._upper_alphavite, char, -shifting)
                elif char.islower() and (char in self._lower_alphavite):
                    decrypt_stream += self._shift_char(self._lower_alphavite, char, -shifting)
                else:
                    decrypt_stream += char
            fin.close()
        
        return decrypt_stream

    def _write_decrypt_stream(self, decrypt_file: str, decrypt_stream: str):
        with open(decrypt_file, 'w', encoding=self._encoding) as fout:
            fout.write(decrypt_stream)
            fout.close()

    def conformity_decrypt(self, encrypt_file: str, train_file: str, decrypt_file: str):
        decrypt_stream: str = self._decrypt_conformity_stream(encrypt_file, train_file)
        self._write_decrypt_stream(decrypt_file, decrypt_stream)
        print(f'Decryption completed successfully.')
    
    def shift_decrypt(self, encrypt_file: str, train_file: str, decrypt_file: str):
        decrypt_stream: str = self._decrypt_shift_stream(encrypt_file, train_file)
        self._write_decrypt_stream(decrypt_file, decrypt_stream)
        print(f'Decryption completed successfully.')
