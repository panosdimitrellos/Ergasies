import sys

file = open(sys.argv[1], "r")
prg = file.read()
file.close()

prgPos = 0
mem = [0]
memPos = 0

while prgPos < len(prg):
    if prg[prgPos] == ">":
        memPos += 1
        if len(mem) <= memPos:
            mem.append(0)
            
    elif prg[prgPos] == "<":
        memPos -= 1
        if memPos < 0:
            print "Error: Moved off tape!" 
            sys.exit(0)
        
    elif prg[prgPos] == "+":
        mem[memPos] += 1
        if mem[memPos] >= 255:
            mem[memPos] = 0
        
    elif prg[prgPos] == "-":
        mem[memPos] -= 1
        if mem[memPos] <= -1:
            mem[memPos] = 255
        
    elif prg[prgPos] == ".":
        print chr(mem[memPos]), 
        
    elif prg[prgPos] == ",":
        inp = input("Input requested: ")
        mem[memPos] = ord( inp[0] )
        
    elif prg[prgPos] == "[":
        if mem[memPos] == 0:
            countOpened = 0
            prgPos += 1
            while prgPos < len(prg):
                if prg[prgPos] == "]" and countOpened == 0:
                    break
                elif prg[prgPos] == "[":
                    countOpened += 1
                elif prg[prgPos] == "]":
                    countOpened -= 1
                prgPos += 1
                
    elif prg[prgPos] == "]":
        if mem[memPos] != 0:
            countClosed = 0
            prgPos -= 1
            while prgPos >= 0:
                if prg[prgPos] == "[" and countClosed == 0:
                    break
                elif prg[prgPos] == "]":
                    countClosed += 1
                elif prg[prgPos] == "[":
                    countClosed -= 1
                prgPos -= 1

    prgPos += 1
    
print("")
