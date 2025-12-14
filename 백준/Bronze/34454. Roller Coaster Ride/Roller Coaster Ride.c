#include <stdio.h>

int main() {

        int N, C, P;
        scanf("%d %d %d", &N, &C, &P);

        if(C*P >= N) printf("yes\n");
        else printf("no\n");

        return 0;
}