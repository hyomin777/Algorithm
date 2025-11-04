#include <stdio.h>
#include <string.h>

int main() {
        int t;

        scanf("%d", &t);

        for(int i = 0; i < t; i++) {
                char input[1000];
                scanf("%s", input);

                printf("%c%c\n", input[0], input[strlen(input)-1]);
        }

        return 0;
}