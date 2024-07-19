import hashlib
from Crypto.Cipher import AES

# Clave AES en hexadecimal
clave_aes = bytes.fromhex('A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72')

# Calcular SHA-256
sha256_hash = hashlib.sha256(clave_aes).digest()

# Tomar los primeros 3 bytes del SHA-256
kcv_sha256 = sha256_hash[:3].hex().upper()
print("KCV(SHA-256):", kcv_sha256)

# Bloque de 16 bytes de ceros
block_of_zeros = bytes(16)

# Crear el cifrador AES en modo ECB
cipher = AES.new(clave_aes, AES.MODE_ECB)

# Cifrar el bloque de ceros
ciphertext = cipher.encrypt(block_of_zeros)

# Tomar los primeros 3 bytes del resultado cifrado
kcv_aes = ciphertext[:3].hex().upper()
print("KCV(AES):", kcv_aes)
