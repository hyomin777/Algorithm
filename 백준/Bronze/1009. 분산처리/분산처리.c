#include <stdio.h>

int main() {

        int t;
        scanf("%d", &t);

        int a, b;
        int total_data;

        for(int i = 0; i < t; i++) {
                scanf("%d %d", &a, &b);
                int computer = 1;

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