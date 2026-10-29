plaintext= input("Enter plain text")

ciphertext= plaintext[::-1]
decrypt= ciphertext[::-1]

print("Encrypted text:",ciphertext)
print("Decrypted text:",decrypt)