#include <stdio.h>

int main() {
    FILE *file = fopen("input.txt", "r");
    char line[100];
    while (fgets(line, sizeof(line), file)!= NULL){
        for (int i; line[i] != '\0'; i++){
            
        }
    }
    char name[16];
    scanf("%5s", name);
    printf("%s\n", name);
}