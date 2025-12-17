#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// babbling_len은 배열 babbling의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* babbling[], size_t babbling_len) {
    int answer = 0;
    char *babbues[4] = {"aya", "ye", "woo", "ma"};
    int flag = -1;
    
    for(int i = 0; i < babbling_len; i++) {
        const char *curr_ptr = babbling[i];
        int possible = 0;
        
        while(*curr_ptr != '\0') {
            int found = 0;
            
            for(int k = 0; k < 4; k++) {
                int len = strlen(babbues[k]);
                
                if((flag != k) && (strncmp(curr_ptr, babbues[k], len) == 0)) {
                    flag = k;
                    curr_ptr += len;
                    found = 1;
                    possible = 1;
                }
            }            
            
            if(!found) {
                possible = 0;
                break;
            }
        }
        
        flag = -1;
        if(possible) answer++;
    }
    return answer;
}