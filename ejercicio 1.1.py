clave_fija = "B1EF2ACFE2BAEEFF"
clave_properties_prod = "B98A15BA31AEBB3F"

# Convertir las claves a bytes
clave_fija_bytes = bytes.fromhex(clave_fija)
clave_properties_prod_bytes = bytes.fromhex(clave_properties_prod)

# Calcular la clave en memoria mediante XOR
clave_memoria_bytes = bytes(a ^ b for a, b in zip(clave_fija_bytes, clave_properties_prod_bytes))

# Convertir la clave en memoria a hexadecimal
clave_memoria = clave_memoria_bytes.hex().upper()
print(f"Clave en memoria: {clave_memoria}")
