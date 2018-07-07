import pyaes

key = "1234567891234567"

iv = "InitializationVe"
# aes = pyaes.AESModeOfOperationCBC(key, iv = iv)

ciphertext = ''
encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
for line in file('google-10000-english.txt'):
#    print(line)
    ciphertext += encrypter.feed(line)


ciphertext += encrypter.feed()


print(ciphertext)
decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key, iv))
decrypted = decrypter.feed(ciphertext[:len(ciphertext) / 2])
decrypted += decrypter.feed(ciphertext[len(ciphertext) / 2:])
decrypted += decrypter.feed()



print file('google.txt').read() == decrypted

