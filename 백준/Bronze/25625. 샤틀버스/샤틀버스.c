#include <stdio.h>

int main() {

        int x, y;
        int time;
        scanf("%d %d", &x, &y);

        if(x > y) {
                time = x + y;
        } else {
                time = y - x;
        }

        printf("%d\n", time);

        return 0;
}