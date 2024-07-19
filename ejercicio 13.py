import ed25519

# Cargar la clave privada desde el archivo
with open('ed25519-priv', 'rb') as f:
    privKey = ed25519.SigningKey(f.read())

# Cargar la clave pública desde el archivo
with open('ed25519-publ', 'rb') as f:
    pubKey = ed25519.VerifyingKey(f.read())

# Mensaje a firmar (codificado en UTF-8)
msg = "El equipo está preparado para seguir con el proceso, necesitaremos más recursos.".encode('utf-8')

# Firmar el mensaje
signature = privKey.sign(msg)
print("Firma Generada (64 bytes):", signature.hex())

# Verificar la firma
try:
    pubKey.verify(signature, msg)
    print("La firma es válida")
except ed25519.BadSignatureError:
    print("Firma inválida")
