# Solution to Comparaison

This was my first time ever to write any form of assembly program, and I have to admit I didn't really understand how to interact with the Python code at first.

Let's break down the solution:

### 1. Write the assembly code

We want to compare the registers R5 and R6, then set R0 to 1 if R5 and R6 are different, or to 0 if they're equal.

If you have to write the code in an `.asm` file, in my case I called it `comparaison.asm`:

```asm
; Initialize R0 to 0, then compare R5 and R6
MOV R0, #0
CMP R5, R6

; If R5 == R6, we jump to end, else we set R0 to 1 because R5 != R6
JZA end
MOV R0,#1

end:
    STP
```

In this program, I initialize the value of R0 to 0, then I do the comparison. The result of this comparison is not stored, but it sets a special flag, in this case the Zero flag.

We can then do the comparison between R5 and R6 using `CMP`.

After that, we use `JZA` which jumps to a part of the code if the Zero is active (JZA: Jump Zero Active). If R5 is equal to R6, the Zero flag will be active, so we skip the line below and directly go to the end label which stops the program.

If R5 is different from R6, the Zero flag is not active, so we go through the line `MOV R0, #1`, which sets R0 to 1, then we stop the program.

With this, we should have everything we need to get the flag !

### 2. Transform the assembly into hexadecimal

We need to transform our assembly code into hexadecimal format using the python code give. We use this command: `python assembly.py comparaison.asm`. It just starts the `assembly.py` file with the argument `comparaison.asm`.

The program should give you a hexadecimal string as an output, in my case it was `80000000066588000007800000011400`.

### 3. Get the flag

Then, we can start the docker using `docker compose up`, open another terminal, connect to the container using `nc localhost 4000` and give our hexadecimal code.

You should be rewarded with the flag: `FCSC{6b7b0a69935108a38e58dfcb4efc857973efdc18b9db81ab9de047d3b9100b98}`