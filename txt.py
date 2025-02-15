# Sadə Caesar şifrəsi ilə mətn faylını şifrələyən və şifrəsini açan 
# Python proqramı yazın.
# encrypt_file(input_file, output_file, shift) funksiyası yaradın. 
# Bu funksiya mətn faylını oxuyur, Caesar şifrəsi ilə şifrələyir 
# (hər simvolu shift dəyəri qədər dəyişdirir) və şifrələnmiş məzmunu 
# yeni fayla yazır.
# decrypt_file(input_file, output_file, shift) funksiyası yaradın. Bu 
# funksiya şifrələnmiş faylı oxuyur, şifrəsini açır və açılmış məzmunu 
# yeni fayla yazır.
# Faylı şifrələyib sonra şifrəsini açaraq orijinal məzmunun bərpa 
# olunduğunu yoxlayın.
# ord() və chr() built in funksiyalarından istifadə edin
# https://docs.python.org/3/library/functions.html#ord
# https://docs.python.org/3/library/functions.html#chr
# Output:
# encrypt_file('secret.txt', 'encrypted.txt', 3)
# decrypt_file('encrypted.txt', 'decrypted.txt', 3)
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  
            new_char = chr(ord(char) + shift)  
            result += new_char
        else:
            result += char  
    return result

def encrypt_file(input_file, output_file, shift):
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    encrypted_content = caesar_cipher(content, shift)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(encrypted_content)

def decrypt_file(input_file, output_file, shift):
    encrypt_file(input_file, output_file, -shift) 


with open("secret.txt", "w", encoding="utf-8") as f:
    f.write("Salam, dünya!")

encrypt_file("secret.txt", "encrypted.txt", 3)
decrypt_file("encrypted.txt", "decrypted.txt", 3)
with open("secret.txt", "r", encoding="utf-8") as f:
    original = f.read()

with open("decrypted.txt", "r", encoding="utf-8") as f:
    decrypted = f.read()

print("Şifrələmə və deşifrələmə uğurludur:", original == decrypted)
