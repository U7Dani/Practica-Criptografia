import hmac
import hashlib

# Clave HMAC-SHA256 desde el keystore
key = bytes.fromhex('A212A51C997E1B4DF08D55967641B0677CA31E049E672A4B06B618AA4D5826EB')

# Texto a hashear
mensaje = "Siempre existe más de una forma de hacerlo, y más de una solución válida."

# Crear el objeto HMAC usando SHA256
hmac_obj = hmac.new(key, mensaje.encode('utf-8'), hashlib.sha256)

# Obtener el HMAC en formato hexadecimal
hmac_result = hmac_obj.hexdigest()
print("HMAC-SHA256:", hmac_result)
