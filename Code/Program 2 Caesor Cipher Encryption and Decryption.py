def encrypt(text,key):
    result = ""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text,key):
    result=""
    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
            else:
                result += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        else:
            result += ch
    return result

plaintext = input("Enter the plaintext: ")
key = int(input("Enter the key (shift value): "))

encrypted_text = encrypt(plaintext,key)
decrypted_text = decrypt(encrypted_text,key)

print("Encrypted text: ", encrypted_text)
print("Decrypted text: ", decrypted_text)