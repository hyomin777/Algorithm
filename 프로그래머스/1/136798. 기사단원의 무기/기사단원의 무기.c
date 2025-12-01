#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int get_num_divisor(int number) {
    if(number == 1) return 1;
    
    int num_divisor = 2;
    int half = number / 2;
    
    for(int i = 2; i <= half; i++) {
        if(!(number % i)) {
            num_divisor++;
        }    
    }
    
    return num_divisor;
}

int solution(int number, int limit, int power) {
    int answer = 0;
    
    for(int i = 1; i <= number; i++) {
        int num_divisor = get_num_divisor(i);
        
        if(num_divisor > limit) {
            num_divisor = power;
        }
        
        answer += num_divisor;
    }
    
    return answer;
}