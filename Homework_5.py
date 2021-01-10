A = int(input("Число А\n"))
B = int(input("Число В\n"))
if A < B:
    while A != B:
        print(A)
        A += 1
    print(B)
else:
    while A != B:
        print(A)
        A -= 1
    print(B)