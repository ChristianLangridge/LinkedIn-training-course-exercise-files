import json 
import os
# The file name that will be passed to this function is 10_04_challenge_art.txt

def encodeFile(filename,newFilename):
    with open(filename, 'r') as f:
        content = f.read()
        encoded_content = content.replace("),(", ",")
        f.close
    with open(newFilename, 'w') as f:
       f.write(encoded_content)
       print(f"Encoded content written to {newFilename}")
       f.close


def decodeFile(newFilename):
    with open(newFilename, 'r') as f:
        content = f.read()
        decoded_content = content.replace("),(", ",")
    return decoded_content 


print(encodeFile('10_04_challenge_art.txt','10_04_challenge_art_encoded.txt'))

print(decodeFile('10_04_challenge_art_encoded.txt'))


original_filesize = os.path.getsize("10_04_challenge_art.txt")
print(f'Original file size: {original_filesize} ')
encoded = encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

new_filesize = os.path.getsize("10_04_challenge_art.encoded.txt")
print(f'New file size: {new_filesize}')
decoded = decodeFile('10_04_challenge_art_encoded.txt')