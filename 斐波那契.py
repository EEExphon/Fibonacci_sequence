#   FIBONACCI DIGITS CALCULATING :

#           (N < M < Q)

print("====================FIBONACCI DIGITS====================")
N = 0
M = 0
Q = 0

yu = "start"

while yu != "ELF":
    NUM = int(input("No."))

    for i in range (NUM-1):
        if i == 0:
            Q = 0
        elif i == 1:
            M = 0
            Q = 1
        elif i == 2:
            N = 0
            M = Q
            Q = M+N
        else:
            N = M
            M = Q
            Q = M+N
    print(Q)
    
    N = 0
    M = 1
    Q = 0
    
print("END")
        
    
    
