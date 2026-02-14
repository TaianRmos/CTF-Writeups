import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256

# Load encrypted data
with open("FCSC-2022/crypto/Hamac/output.txt", "r") as f:
    data = json.load(f)

# Extract IV and ciphertext
iv = bytes.fromhex(data["iv"])
c = bytes.fromhex(data["c"])

# Load the password list (rockyou.txt)
with open("FCSC-2022/crypto/Hamac/rockyou.txt", "r", encoding="latin-1") as f:
    passwords = f.read().splitlines()

# Try each password
for password in passwords:
    password = password.encode()  # Convert to bytes
    key = SHA256.new(password).digest()  # Generate AES key

    # Attempt decryption
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        plaintext = unpad(cipher.decrypt(c), 16)
        
        # If successful, print the password and plaintext
        # print(f"[+] Found password: {password.decode()}")
        print("Decrypted content:", plaintext.decode())
        break  # Stop once we find the correct password
    except (ValueError, UnicodeDecodeError):
        pass  # Ignore incorrect passwords

print("[-] Brute force finished.")
