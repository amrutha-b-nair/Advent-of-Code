#include <stdio.h>

int main() {
    FILE *file;
    file = fopen("input.txt", "r");
    // char buffer[100]; 
    int character;
    int storey = 0;
    int count = 0;
    while ((character = fgetc(file)) != EOF) {
        count ++;
        if (character == '(') {
          storey ++;
        }
        else if (character == ')') {
          storey -= 1;
        }

        if (storey == -1) {
          printf("%i\n", count);
          return 0;
        }
    }
    printf("%i\n", storey);
    fclose(file);
}
