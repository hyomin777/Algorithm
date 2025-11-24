#include <stdio.h>
#include <string.h>

int main() {

        int t;
        scanf("%d", &t);
        getchar();

        for(int i = 0; i < t; i++) {
                char sentence[1000];
                fgets(sentence, sizeof(sentence), stdin);

                size_t len = strlen(sentence);

                if(len > 0 && sentence[len-1] == '\n') {
                        sentence[len-1] = '\0';
                        len--;
                }

                if(len > 0 && sentence[len-1] != '.') {
                        sentence[len] = '.';
                        sentence[len+1] = '\0';
                }

                printf("%s\n", sentence);
        }

        return 0;
}