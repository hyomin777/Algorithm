#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int M, int N) {
    int answer = 0;
    int smaller, bigger;
    
    if(M >= N) {
        bigger = M;
        smaller = N;
    } else {
        bigger = N;
        smaller = M;
    }
    
    answer = smaller - 1;
    answer += smaller * (bigger - 1);
    return answer;
}