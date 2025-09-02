def main():

    num = int (input("Digite um número: "))

    i = 2

    while num != i and num > 1:
        if num % i == 0:
            break 
        i += i
    
    if num == i:
        print("O número ", num, " é primo")
    else:
        print("O número ", num, " não é primo")

    return 0
main()