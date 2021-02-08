# Cryptographic mono-alphavite coding and data frequency cryptanalysis

## Purpose

1. Caesar cipher text encoding.
2. Frequency analysis of encoded text.

## Input Data

Any text file.

## Output Data

Encrypted or decrypted file.

## Algorithm

### Encrypt

1. An arbitrary Caesar shift is used for encryption. 
2. Only the characters of the Russian alphabet are used. 
3. Characters other than those of the Russian alphabet remain unchanged.
4. Punctuation marks, numbers, spaces also remain unchanged. 
5. An uppercase character is encoded by an uppercase character, a lowercase character by a lowercase character.

### Decrypt

1. A training file is used to form the frequency dictionary. 
2. Decoding involves two approaches. 
2.1 Decoding according to the conformity of the frequency dictionaries of the encoded and training files.
2.2 Decoding using the shift predicted from the frequency dictionaries of the encoded and training files.

## Get Started

### Prerequisites

To run the project, you need to have Python 3.7+.

### Installation

1. Clone the repo:

```git clone https://github.com/Alexey-Chegodaykin/mono-alphavite-coding.git```

### Usage

#### Encrypt

```python main.py -fin SOURCE -fout TARGET -shift SHIFT -type 0```

* SOURCE - File path for encrypting.
* TARGET - The path to the encrypting result file.
* SHIFT - Shift the alphabet.

#### Decrypt

```python main.py -fin SOURCE -fout TARGET -type 1 -train TRAIN -decryption-method METHOD```

* SOURCE - File path for decrypting.
* TARGET - The path to the decrypting result file.
* TRAIN - File path for calculating frequence of characters.
* METHOD - Decryption method (0 - Dictionary of conformity, 1 - Shift Prediction).
