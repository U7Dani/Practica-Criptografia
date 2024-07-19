from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization

# Mensaje a firmar
message = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos.".encode('utf-8')

# Ruta de la clave privada
private_key_path = "C:\\Users\\34652\\Documents\\GitHub\\criptografia\\Practica\\clave-rsa-oaep-priv.pem"

# Leer la clave privada desde el fichero
with open(private_key_path, "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

# Crear la firma usando PKCS#1 v1.5
signature = private_key.sign(
    message,
    padding.PKCS1v15(),
    hashes.SHA256()
)

# Convertir la firma a hexadecimal
signature_hex = signature.hex()
print(f"Firma (PKCS#1 v1.5) en hexadecimal: {signature_hex}")
