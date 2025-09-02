#include <stdio.h>
#include <string.h>

int main() {
    char aa[5];  // buffer pequeno, só cabe 4 caracteres + '\0'

    printf("Digite um texto (máx 4 letras): ");
    gets(aa);  // ⚠ gets NÃO verifica o tamanho da entrada

    printf("Você digitou: %s\n", aa);

    return 0;
}
