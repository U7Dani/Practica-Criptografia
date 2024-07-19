from Crypto.Cipher import ChaCha20_Poly1305
import base64

# Clave desde el keystore (32 bytes de longitud)
key = bytes.fromhex('AF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce = b'9Yccn/fSnJJhAt2S'[:12]

# Inicializar el cifrador ChaCha20-Poly1305
cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)

# Texto plano
plaintext = 'KeepCoding te enseña a codificar y a cifrar'.encode('utf-8')

# Cifrar el mensaje
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Codificar el texto cifrado y el tag en base64
ciphertext_b64 = base64.b64encode(ciphertext).decode()
tag_b64 = base64.b64encode(tag).decode()

# Mostrar el texto cifrado y el tag
print('Texto cifrado (base64):', ciphertext_b64)
print('Etiqueta de autenticidad (base64):', tag_b64)

# Código de descifrado
cipher = ChaCha20_Poly1305.new(key=key, nonce=nonce)
ciphertext = base64.b64decode(ciphertext_b64)
tag = base64.b64decode(tag_b64)
plaintext = cipher.decrypt_and_verify(ciphertext, tag)

print('Plaintext:', plaintext.decode('utf-8'))
