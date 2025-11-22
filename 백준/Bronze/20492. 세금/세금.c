#include <stdio.h>

int main() {

        float N;
        scanf("%f", &N);

        int A = (int)(N*0.78);
        int B = (int)(N-(N*0.2*0.22));
    
        printf("%d %d\n", A, B);
    
        return 0;
}