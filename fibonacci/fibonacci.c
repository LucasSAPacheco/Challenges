#include <stdio.h>
#include <stdlib.h>

int fibonacci(int number)
{
    int k = 0, soma = 0, aux = 0, aux2 = 1;
    while (soma < number){
        soma = aux + aux2;
        aux = aux2;
        aux2 = soma;
        k += 1;
        if (soma == number){
            printf("This Number is a Fibonacci Number\n");
            return (0);
        }
    }
    if (soma > number){
        printf("This Number is not a Fibonacci Number\n");
        return (1);
    }
    return (0);
}

int main(int argc, char *argv[]){
    fibonacci(atoi(argv[1]));
    return 0;
}