import pyaes
#
key = "1234567891234567"
#
iv = "InitializationVe"
# # aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
#
# ciphertext = ''
# encrypter = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(key, iv))
# for line in file('google-10000-english.txt'):
# #    print(line)
#     ciphertext += encrypter.feed(line)
#
#
# ciphertext += encrypter.feed()
#
#
# print(ciphertext)
# decrypter = pyaes.Decrypter(pyaes.AESModeOfOperationCBC(key, iv))
# decrypted = decrypter.feed(ciphertext[:len(ciphertext) / 2])
# decrypted += decrypter.feed(ciphertext[len(ciphertext) / 2:])
# decrypted += decrypter.feed()
#
#
#
# print file('google-10000-english.txt').read() == decrypted

aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
plaintext = "TextMustBe16Byte"
ciphertext = aes.encrypt(plaintext)

# '\xd6:\x18\xe6\xb1\xb3\xc3\xdc\x87\xdf\xa7|\x08{k\xb6'
print repr(ciphertext)


# The cipher-block chaining mode of operation maintains state, so
# decryption requires a new instance be created
aes = pyaes.AESModeOfOperationCBC(key, iv = iv)
decrypted = aes.decrypt(ciphertext)

# True
print decrypted == plaintext