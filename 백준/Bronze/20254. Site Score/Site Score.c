#include <stdio.h>

int main() {

        int U_R, T_R, U_O, T_O;
        scanf("%d %d %d %d", &U_R,&T_R, &U_O, &T_O);

        printf("%d\n", 56*U_R + 24*T_R + 14*U_O + 6*T_O);
        return 0;
}