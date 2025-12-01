#include <stdio.h>

int main() {

        int A, B, C;
        scanf("%d %d %d", &A, &B, &C);

        if(B >= C) {
                printf("%d\n", -1);
                return 0;
        }

        int profit = C - B;
        int result = (A / profit) + 1;

        printf("%d\n", result);

        return 0;
}