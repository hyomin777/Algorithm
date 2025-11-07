#include <stdio.h>

int main() {

        int hours;
        int minutes;
        scanf("%d %d", &hours, &minutes);

        printf("%d\n", (hours-9)*60 + minutes);

        return 0;

}