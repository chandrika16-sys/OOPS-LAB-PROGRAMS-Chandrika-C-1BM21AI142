def encrypt(text,shift):
  encrypted_text = ""  
  for i in range(len(text)):  
     char = text[i]  
     if (char.isupper()):  
        encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)  
     else:  
        encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)  
  return encrypted_text  

def decrypt(encrypted_text,shift):
  return encrypt(encrypted_text,-shift)

text="Hello, My name is Chandrika"
shift=3

encrypted_text=encrypt(text,shift)
print("Encrypted_text:",encrypted_text)
decrypted_text=decrypt(encrypted_text,shift)
print("Decrypted text:",decrypted_text)
