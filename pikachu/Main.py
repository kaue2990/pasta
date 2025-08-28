def main():
    notas = [] * 4
    i = 0
    while i < 4:
        notas.append(random.randint(0, 10))
        i += 1
    media = sum(notas) / len(notas)
    print("Notas:", notas)
    print("Média:", media)
    if media >= 6:
        print("Aprovado!")
    else:
        print("Reprovado!")
          
    
    
    
    
    
    
    return 0
main()