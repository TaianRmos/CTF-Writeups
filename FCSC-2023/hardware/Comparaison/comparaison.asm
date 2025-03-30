; Initialize R0 to 0, then compare R5 and R6
MOV R0, #0
CMP R5, R6

; If R5 == R6, we jump to end, else we set R0 to 1 because R5 != R6
JZA end
MOV R0,#1

end:
    STP