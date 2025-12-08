#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int num, int total) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(num * sizeof(int));
    int i, j, k;
    int div = total / num;
    int temp = 0;

    for(i = div - num; i <= total; i++) {
        for(j = 0; j < num; j++) {
            temp += i + j;
        }

        if(temp == total) break;
        else temp = 0;
    }
    
    i += num-1;
    for(k = 1; k <= num; k++) {
        answer[num - k] = i;
        i--;
    }
    
    return answer;
}