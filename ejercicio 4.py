import base64
import json

jwt_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c3VhcmlvIjoiRG9uIFBlcGl0byBkZSBsb3MgUGFsb3RlcyIsInJvbGUiOiJBZG1pbiIsImlhdCI6MTY2NzkzNTMzMyJ9.krgBkzCBQ5WZ8JnzHuRvmnAZdg4ZMeRNv2CIAOD1HRI"

# Separar las tres partes del JWT
header_b64, payload_b64, signature_b64 = jwt_token.split('.')

# Asegúrate de que el payload tenga un padding correcto
missing_padding = len(payload_b64) % 4
if missing_padding != 0:
    payload_b64 += '=' * (4 - missing_padding)

# Decodificación Base64 del payload
try:
    body = base64.b64decode(payload_b64)
    print("Decodificación Base64 exitosa")
    print("Contenido binario:", body)

    # Convertir a cadena y corregir el JSON
    body_str = body.decode('utf-8')
    body_str = body_str.replace(',"iat":1667935333"}', ',"iat":1667935333}')
    
    # Intentar decodificar como JSON
    try:
        body_decoded = json.loads(body_str)
        print("Decodificación JSON exitosa")
        print(body_decoded)
    except json.JSONDecodeError as e:
        print(f"Error de decodificación JSON: {e}")
except (ValueError, Exception) as e:
    print(f"Error decoding JWT body: {e}")
