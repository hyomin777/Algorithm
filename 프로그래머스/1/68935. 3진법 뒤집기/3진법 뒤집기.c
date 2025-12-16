#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <math.h>

long long convert_to_reversed_ternary(int n) { 
    long long result = 0;
    int mod;
    
    while(n > 0) {
        mod = n % 3;
        n /= 3;
        
        result *= 10;
        result += mod; 
    }
    
    return result;
}

int convert_to_decimal(long long ternary) { 
    int result = 0;
    int count = 0;
    int mod;
    int power_of_three = 1;
    
    while(ternary > 0) {
        mod = ternary % 10;
        ternary /= 10;
        
        result += mod * power_of_three;
        power_of_three *= 3;
    }
    
    return result;
}

int solution(int n) {
    long long answer_long = convert_to_reversed_ternary(n);
    return convert_to_decimal(answer_long);
}