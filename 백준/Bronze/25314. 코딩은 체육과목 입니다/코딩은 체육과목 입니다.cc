#include <stdio.h>
#include <string.h>

int main() {

        int input;
        scanf("%d", &input);

        char output[2000] = "";
        for(int i = input / 4; i > 0; i--) {
                strcat(output,  "long ");
        }
        strcat(output, "int");

        printf("%s\n", output);
        return 0;
}