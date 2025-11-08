#include <stdio.h>
#include <string.h>


int isIncludeSeven(const char* str){
        int len = strlen(str);

        for(int i = 0; i < len; i++) {
                if(str[i] == '7') {
                        return 1;
                }
        }
        return 0;
}


int main() {

        int num;
        char str[11];
        int divisible;

        scanf("%d", &num);
        snprintf(str, sizeof(str), "%d", num);

        int include = isIncludeSeven(str);

        if(num % 7 == 0) {
                divisible = 1;
        } else {
                divisible = 0;
        }

        if(!divisible && !include) {
                printf("0\n");
        } else if(divisible && !include) {
                printf("1\n");
        } else if(!divisible && include) {
                printf("2\n");
        } else {
                printf("3\n");
        }

        return 0;

}