# Claves en hexadecimal
clave_fija = "B1EF2ACFE2BAEEFF"
clave_final = "91BA13BA21AABB12"

# Convertir las claves a bytes
clave_fija_bytes = bytes.fromhex(clave_fija)
clave_final_bytes = bytes.fromhex(clave_final)

# Calcular la clave en properties mediante XOR
clave_properties_bytes = bytes(a ^ b for a, b in zip(clave_fija_bytes, clave_final_bytes))

# Convertir la clave en properties a hexadecimal
clave_properties = clave_properties_bytes.hex().upper()
print(f"Clave properties: {clave_properties}")
