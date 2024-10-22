# Solution to Clair connu

This challenge is about the XOR operation.

If you don't know, the xor operation has a lot of very interesting properties, especially the fact that you can switch the different variables !

If `a ^ b = c` then `b ^ a = c`,  `a ^ c = b` and `c ^ b = a`.

This means that if `flag ^ key = encrypted`, then `encrypted ^ key = flag`, but also `encrypted ^ flag = key` !

## Decrypt the flag

How do we get flag if we don't have the key ? Well we see from the python script that the key is only 4 bytes long, then it's repeated 20 times.

This is the vulnerability ! Why ? Well because we know how the flag starts: "FCSC", which is exactly 4 letters.

So we xor the encrypted flag with "FCSC", this will give us the 4 bytes of the key, we repeat the key 20 times, then xor the entire encrypted flag with the key !

With that we get our flag: `FCSC{3ebfb1b880d802cb96be0bb256f4239c27971310cdfd1842083fbe16b3a2dcf7}`