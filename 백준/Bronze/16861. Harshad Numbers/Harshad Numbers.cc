#include <stdio.h>
#include <string.h>

int main() {

        int n;
        char buffer[12];
        scanf("%d", &n);

        while(1) {
                int sum = 0;
                snprintf(buffer, sizeof(buffer), "%d", n);

                for(int i = 0; i < strlen(buffer); i++) {
                        sum += buffer[i] - '0';
                }

                if((n % sum) == 0) {
                        printf("%d\n", n);
                        return 0;
                } else {
                        n++;
                }
        }

        return 0;
}