#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int food[], size_t food_len) {
    size_t buffer_size = 2;
    int i;
    for(i = 1; i < food_len; i++) {
        buffer_size += (food[i] / 2) * 2;
    }
    char* answer = (char*)malloc(buffer_size);
    answer[buffer_size-1] = '\0';
    
    char* left_ptr = answer;
    char* right_ptr = answer+buffer_size-2;
    
    i = 0;
    while(left_ptr != right_ptr) {
        int j = food[i] / 2;
        for(; j >= 1; j--) {
            if(left_ptr == right_ptr) break;
            *left_ptr = i + '0';
            left_ptr++;
            *right_ptr = i + '0';
            right_ptr--;
        }
        i++;
    }
    
    *left_ptr = '0';
    
    return answer;
}