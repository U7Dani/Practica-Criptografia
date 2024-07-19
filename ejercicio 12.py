from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import b64encode

# Datos proporcionados
key = bytes.fromhex("E2CFF885901B3449E9C448BA5B948A8C4EE322152B3F1ACFA0148FB3A426DB74")
nonce = b"9Yccn/f5nJJhAt2S"  # Debe ser exactamente 12 bytes para AES/GCM
plaintext = "He descubierto el error y no volveré a hacerlo mal".encode('utf-8')

# Crear el cifrador AES-GCM
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
encryptor = cipher.encryptor()

# Cifrar el texto
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Obtener el tag (etiqueta de autenticación)
tag = encryptor.tag

# Convertir el texto cifrado y el tag a hexadecimal y base64
ciphertext_hex = ciphertext.hex()
tag_hex = tag.hex()
ciphertext_base64 = b64encode(ciphertext).decode('utf-8')
tag_base64 = b64encode(tag).decode('utf-8')

# Mostrar resultados
print(f"Texto cifrado (hex): {ciphertext_hex}")
print(f"Tag (hex): {tag_hex}")
print(f"Texto cifrado (base64): {ciphertext_base64}")
print(f"Tag (base64): {tag_base64}")
