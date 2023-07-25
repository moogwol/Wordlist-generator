# Wordlist-generator
Creates a wordlist based on a seed phrase given by the user for use in a password cracker such as John the Ripper

# Usage
This will output a plain text file; \<seed word\>.txt with the number of mutations specified

`python ./wordlist_generator.py <seed word> <number>`

## Example
This will generate 100 mutations based on the word 'secretpassword'.

`python ./wordlist_generator.py 'secretpassword' 100'`
