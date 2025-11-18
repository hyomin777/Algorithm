#include <stdio.h>
#include <string.h>

int main() {

        char myMBTI[5];
        int num;
        scanf("%s", myMBTI);
        scanf("%d", &num);

        int count = 0;
        for(int i = 0; i < num; i++) {

                char friendMBTI[5];
                scanf("%s", friendMBTI);

                if(strcmp(myMBTI, friendMBTI) == 0) {
                        count += 1;
                }
        }

        printf("%d\n", count);

        return 0;
}