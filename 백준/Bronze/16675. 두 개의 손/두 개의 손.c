#include <stdio.h>

int main() {

	char M_l, M_r, T_l, T_r;
	scanf("%c %c %c %c", &M_l, &M_r, &T_l, &T_r);

	char flag = 1;

	if((M_l!=M_r) && (T_l!=T_r)) {
		printf("?\n");
		flag = flag >> 1;
	}

	if(flag && (M_l==M_r)) {
		if((M_l=='R') && ((T_l=='P') || (T_r=='P'))) {
			printf("TK\n");
			flag = flag >> 1;
		} else if((M_l=='S') && ((T_l=='R') || (T_r=='R'))) {
			printf("TK\n");
			flag = flag >> 1;
		} else if((M_l=='P') && ((T_l=='S') || (T_r=='S'))) {
			printf("TK\n");
			flag = flag >> 1;
		}	
	}
	
	if(flag && (T_l==T_r)) {
		if((T_l=='R') && ((M_l=='P') || (M_r=='P'))) {
			printf("MS\n");
			flag = flag >> 1;		
		} else if((T_l=='S') && ((M_l=='R') || (M_r=='R'))) {
			printf("MS\n");
			flag = flag >> 1;
		} else if((T_l=='P') && ((M_l=='S') || (M_r=='S'))) {
			printf("MS\n");
			flag = flag >> 1;
		}
	}

	if(flag) {
		printf("?\n");
	}

	return 0;
}
