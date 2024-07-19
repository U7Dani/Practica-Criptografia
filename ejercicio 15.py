from Crypto.Cipher import AES
from binascii import unhexlify, hexlify

def clean_tr31_block(block):
    # Remover todos los caracteres no hexadecimales
    cleaned_block = ''.join(c for c in block if c in '0123456789ABCDEFabcdef')
    # Asegurar que la longitud es par
    if len(cleaned_block) % 2 != 0:
        cleaned_block = '0' + cleaned_block
    return cleaned_block

def pad_data(data, block_size):
    padding_len = block_size - (len(data) % block_size)
    return data + b'\x00' * padding_len

def unwrap_tr31_block(tr31_block, kek):
    # Limpiar el bloque TR31
    tr31_block = clean_tr31_block(tr31_block)
    
    # Decodificar el bloque TR31 y la KEK (Key Encryption Key)
    tr31_block_bytes = unhexlify(tr31_block)
    kek_bytes = unhexlify(kek)

    # Ajustar la longitud del bloque TR31 para que sea múltiplo de 16 bytes
    tr31_block_bytes = pad_data(tr31_block_bytes, 16)

    # Crear el objeto de cifrado AES en modo ECB
    cipher = AES.new(kek_bytes, AES.MODE_ECB)

    # Decifrar el bloque TR31
    unwrapped_key = cipher.decrypt(tr31_block_bytes)

    return unwrapped_key

# Datos proporcionados
tr31_block = 'D0144D0AB00S000042766B9265B2DF93AE6E29B58135B77A2F616C8D515ACDBE6A5626F79FA7B4071E9EE1423C6D7970FA2B965D18B23922B5B2E5657495E03CD857FD37018E111B'
kek = 'A1A10101010101010101010101010102'

# Desempaquetar el bloque TR31
unwrapped_key = unwrap_tr31_block(tr31_block, kek)

# Imprimir la clave desenrollada en hexadecimal
print(f"Clave desenrollada: {hexlify(unwrapped_key).decode('utf-8')}")
