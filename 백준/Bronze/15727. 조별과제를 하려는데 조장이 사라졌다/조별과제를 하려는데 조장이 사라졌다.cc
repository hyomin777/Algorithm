#include <stdio.h>

int main() {
        int distance;
        scanf("%d", &distance);

        int count = distance / 5;
        distance % 5 ? count++ : count;

        printf("%d\n", count);
        return 0;
}