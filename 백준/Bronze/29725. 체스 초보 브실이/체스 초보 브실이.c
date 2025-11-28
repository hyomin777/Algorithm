#include <stdio.h>
#include <ctype.h>

int main() {

        char board[8][8];
        char line[10];

        int score = 0;
        int temp;
        char piece;

        int i, j;

        for(i = 0; i < 8; i++) {
                fgets(line, sizeof(line), stdin);

                for(j = 0; j < 8; j++) {
                        board[i][j] = line[j];
                }
        }

        for(i = 0; i < 8; i++) {
                for(j = 0; j < 8; j++) {
                        piece = toupper(board[i][j]);

                        if(piece == 'P') temp = 1;
                        else if(piece == 'N') temp = 3;
                        else if(piece == 'B') temp = 3;
                        else if(piece == 'R') temp = 5;
                        else if(piece == 'Q') temp = 9;
                        else temp = 0;

                        if(temp && isupper(board[i][j])) {
                                score += temp;
                        } else if(temp && islower(board[i][j])) {
                                score -= temp;
                        }
                }
        }

        printf("%d\n", score);

        return 0;
}