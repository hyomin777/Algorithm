#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// section_len은 배열 section의 길이입니다.
int solution(int n, int m, int section[], size_t section_len) {
    int answer = 0;
    int current = 0;
    
    for(int i = 0; i < section_len; i++) {
        if(current < section[i]) {
            current = section[i] + m - 1;
            answer++;
        }
    }
    
    return answer;
}