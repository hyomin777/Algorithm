#include <stdio.h>

int main() {

        int t;
        scanf("%d", &t);

        for(int i = 0; i < t; i++) {
                int a, b;
                scanf("%d %d", &a, &b);

                int computer = 1;

                a = a % 10;
                b = b % 4;
                if(b == 0) b = 4;

                for(int j = 0; j < b; j++) {
                        computer = (computer * a) % 10;
                }

                if(computer == 0) {
                        computer = 10;
                }

                printf("%d\n", computer);
        }

        return 0;
}