#include <stdio.h>

int main() {

        int n, m;
        unsigned long long num_n;
        unsigned long long num_m;

        scanf("%d %d", &n, &m);
        scanf("%llu", &num_n);
        scanf("%llu", &num_m);

        printf("%llu\n", num_n*num_m);

        return 0;
}