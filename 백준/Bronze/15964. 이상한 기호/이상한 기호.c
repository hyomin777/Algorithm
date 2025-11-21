#include <stdio.h>

int main() {

        long A, B;
        long result;
        scanf("%ld %ld", &A, &B);

        result = (A+B)*(A-B);
        printf("%ld\n", result);

        return 0;
}