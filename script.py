from pathlib import Path
import hashlib

k = bytes.fromhex("e14bca49fe44ac76")

in_f = Path("Real.dll")
out_f = Path("Real_decrypted.dll")

d = in_f.read_bytes()

decrypted = bytes(
    b ^ k[i % len(k)]
    for i, b in enumerate(d)
)

out_f.write_bytes(decrypted)

print("encrypted SHA 256:", hashlib.sha256(d).hexdigest())
print("decrypted SHA 256:", hashlib.sha256(decrypted).hexdigest())