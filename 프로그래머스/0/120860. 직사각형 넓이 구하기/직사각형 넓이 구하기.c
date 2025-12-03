#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// dots_rows는 2차원 배열 dots의 행 길이, dots_cols는 2차원 배열 dots의 열 길이입니다.
int solution(int** dots, size_t dots_rows, size_t dots_cols) {
    int answer = 0;
    int x_1 = -256;
    int y_1 = -256;
    int x_2, y_2, temp;
    
    for(int i = 0; i < dots_rows; i++) {
        temp = dots[i][0];
        if(temp > x_1) {
            x_2 = x_1;
            x_1 = temp;
        } else if(temp < x_1) {
            x_2 = temp;
        }
        
        temp = dots[i][1];
        if(temp > y_1) {
            y_2 = y_1;
            y_1 = temp;
        } else if(temp < y_1) {
            y_2 = temp;
        }
    }
    
    answer = (x_1 - x_2) * (y_1 - y_2);
    return answer;
}