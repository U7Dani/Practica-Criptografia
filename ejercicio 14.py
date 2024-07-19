from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from binascii import unhexlify, hexlify

# Clave maestra obtenida del keystore (proporcionada)
master_key_hex = 'A2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72'
master_key = unhexlify(master_key_hex)

# Identificador de dispositivo (salt)
salt_hex = 'e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3'
salt = unhexlify(salt_hex)

# Crear el objeto HKDF
hkdf = HKDF(
    algorithm=hashes.SHA512(),
    length=32,  # Longitud de la clave AES (256 bits = 32 bytes)
    salt=salt,
    info=None,
    backend=default_backend()
)

# Derivar la nueva clave
new_key = hkdf.derive(master_key)

# Imprimir la nueva clave en hexadecimal
new_key_hex = hexlify(new_key).decode('utf-8')
print(f"Clave diversificada (AES-256) en hexadecimal: {new_key_hex}")
