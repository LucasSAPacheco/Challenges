#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *rev_str(char *str){
    char *rev = NULL;
    int i = 0;
    int j = 0;

    rev = malloc(sizeof(char) * strlen(str));
    if (!rev)
        return NULL;
    i = strlen(str) - 1;
    while (i >= 0){
        rev[j] = str[i];
        i--;
        j++;
    }
    rev[j] = '\0';
    return (rev);
}

int main(void){
    char *str = NULL;

    str = rev_str("Desafio Concluido!");
    printf("%s\n", str);
    free(str);
    return 0;
}