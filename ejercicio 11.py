from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from binascii import unhexlify

# Texto cifrado en hexadecimal proporcionado
ciphertext_hex = (
    "b72e6fd48155f565dd2684df3ffa8746d649b11f0ed4637fc4c99d18283b32e1"
    "709b30c96b4a8a20d5dbc639e9d83a53681e6d96f76a0e4c279f0dffa76a329d"
    "04e3d3d4ad629793eb00cc76d10fc00475eb76bfbc1273303882609957c4c0ae"
    "2c4f5ba670a4126f2f14a9f4b6f41aa2edba01b4bd586624659fca82f5b49701"
    "86502de8624071be78ccef573d896b8eac86f5d43ca7b10b59be4acf8f8e0498"
    "a455da04f67d3f98b4cd907f27639f4b1df3c50e05d5bf63768088226e2a9177"
    "485c54f72407fdf358fe64479677d8296ad38c6f177ea7cb74927651cf24b01d"
    "ee27895d4f05fb5c161957845cd1b5848ed64ed3b03722b21a526a6e447cb8ee"
)

# Convertir de hexadecimal a bytes
ciphertext_bytes = unhexlify(ciphertext_hex)

# Leer la clave privada desde el fichero
with open("C:\\Users\\34652\\Documents\\GitHub\\criptografia\\Practica\\clave-rsa-oaep-priv.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(key_file.read(), password=None)

# Desencriptar el texto cifrado
plaintext = private_key.decrypt(
    ciphertext_bytes,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Texto desencriptado:", plaintext)

# Leer la clave pública desde el fichero
with open("C:\\Users\\34652\\Documents\\GitHub\\criptografia\\Practica\\clave-rsa-oaep-publ.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(key_file.read())

# Volver a encriptar el texto desencriptado
ciphertext_new = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Nuevo texto cifrado (hex):", ciphertext_new.hex())
