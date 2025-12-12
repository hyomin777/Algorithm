#include <stdio.h>

int main() {

        int arr[5];
        for(int i = 0; i < 5; i++) {
                scanf("%d", &arr[i]);
        }

        int count = 0;
        int flag;
        flag = (arr[0] < 0) ? 1 : 0;

        while(arr[0] < arr[1]) {
                if(arr[0] < 0) {
                        count += arr[2];
                        arr[0]++;
                } else if(arr[0] == 0 && flag) {
                        count += arr[3];
                        flag = 0;
                } else {
                        count += arr[4];
                        arr[0]++;
                }
        }

        printf("%d\n", count);

        return 0;
}