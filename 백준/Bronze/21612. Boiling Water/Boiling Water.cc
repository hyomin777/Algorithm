#include <stdio.h>

int main() {

        int temp;
        scanf("%d", &temp);

        int kPa;
        int seaLevel;

        kPa = 5*temp-400;

        if(temp == 100) seaLevel = 0;
        else if(temp < 100) seaLevel = 1;
        else seaLevel = -1;

        printf("%d\n", kPa);
        printf("%d\n", seaLevel);

        return 0;
}