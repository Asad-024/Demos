plaintext = input("Enter the plaintext: ")

#Reverse the plaintext to ciphertext by reversing the string
ciphertext = plaintext[::-1]

#Reverse the ciphertext to get back the plaintext
decrypted_text = ciphertext[::-1]

print("Ciphertext: ", ciphertext)
print("Decrypted text: ", decrypted_text)