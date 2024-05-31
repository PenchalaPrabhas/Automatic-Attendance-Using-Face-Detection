import hashlib
import csv
def hash_string(input_string):
    
    hash_object = hashlib.sha256()
    
    hash_object.update(input_string.encode('utf-8'))
    
    hashed_string = hash_object.hexdigest()
    return hashed_string

def check_passcode(input_passcode):
    with open('codes.csv', 'r') as file:
        reader = csv.reader(file)
        passcodes = [row[0] for row in reader]
        if input_passcode in passcodes:
            print("Match found for passcode:", input_passcode)
            return True
        else:
            print("No match found for passcode:", input_passcode)
            return False

def main(string1):
    strings=hash_string(string1)
    m=check_passcode(strings)
    return m
