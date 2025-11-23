#include <stdio.h>

int main() {

        int N, K;
        scanf("%d %d", &N, &K);

        int ranks[K];
        for(int i = 0; i < K; i++) {
                scanf("%d", &ranks[i]);
        }

        for(int i = 0; i < K; i++) {
                int P = ranks[i] * 100 / N;
                if(0 <= P && P <= 4) printf("%d ", 1);
                else if(4 < P && P <= 11) printf("%d ", 2);
                else if(11 < P && P <= 23) printf("%d ", 3);
                else if(23 < P && P <= 40) printf("%d ", 4);
                else if(40 < P && P <= 60) printf("%d ", 5);
                else if(60 < P && P <= 77) printf("%d ", 6);
                else if(77 < P && P <= 89) printf("%d ", 7);
                else if(89 < P && P <= 96) printf("%d ", 8);
                else printf("%d ", 9);
        }
        printf("\n");

        return 0;
}