from Crypto.Util.strxor import strxor

encrypted = bytearray.fromhex("d91b7023e46b4602f93a1202a7601304a7681103fd611502fa684102ad6d1506ab6a1059fc6a1459a8691051af3b4706fb691b54ad681b53f93a4651a93a1001ad3c4006a825")
begining = "FCSC".encode() # We know the flag starts with FCSC

key = strxor(begining, encrypted[:len(begining)]) # Xor the FCSC with the beginning of the encrypted flag to retreive the key
print(key)

key = key * 20

flag = strxor(encrypted, key[:len(encrypted)]) # Xor the encrypted flag with the key to retreive the flag
print(flag.decode())

# FCSC{3ebfb1b880d802cb96be0bb256f4239c27971310cdfd1842083fbe16b3a2dcf7}