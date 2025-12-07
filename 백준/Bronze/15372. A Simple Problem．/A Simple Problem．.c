#include <stdio.h>

int main() {

        int T;
        scanf("%d", &T);

        for(int i = 0; i < T; i++) {

                long N;
                scanf("%ld", &N);

                long square_n = N*N;

                printf("%ld\n", square_n);
        }

        return 0;
}