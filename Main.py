def main():
   idade = int (input("Qual a sua idade?"))

   if idade >= 18:
     print("Entrada liberada")
   elif idade >= 16:
     acom=input("Você estaria com acompanhante?")
     if acom=="sim":
       print("Entrada liberada!")
     else:
       print("Entrada proibida!")
   else:
     print("Entrada negada")



   return 0
main()
