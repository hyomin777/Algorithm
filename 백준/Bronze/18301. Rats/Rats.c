#include <stdio.h>

int main() {
        int n_1, n_2, n_12;
        scanf("%d %d %d", &n_1, &n_2, &n_12);

        printf("%d\n", (n_1+1)*(n_2+1)/(n_12+1)-1);
        return 0;
}