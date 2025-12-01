#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(int food[], size_t food_len) {
    char* answer = (char*)malloc(20);
    answer = '0';
    char buffer;
    int temp;
    
    for(int i = 1; i < food_len; i++) {
        temp = food[i] / 2;
        buffer = (char)food[i] + '0';
        for(int j = 0; j < temp; j++) {
                answer = buffer + answer;
                answer = answer + buffer;
        }
    }
    

    return answer;
}