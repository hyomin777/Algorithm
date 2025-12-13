#include <stdio.h>

int get_digit_sum(int num) {
        int sum = 0;
        while(num > 0) {
                sum += num % 10;
                num /= 10;
        }
        return sum;
}

int main() {
        int num;
        int count = 0;
        scanf("%d", &num);

        for(int i = 1; i <= num; i++) {
                if(i % get_digit_sum(i) == 0) {
                        count++;
                }
        }

        printf("%d\n", count);

        return 0;
}