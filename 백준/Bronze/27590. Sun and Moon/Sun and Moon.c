#include <stdio.h>

int main() {

	int d_s, y_s;
	int d_m, y_m;
	scanf("%d %d", &d_s, &y_s);
	scanf("%d %d", &d_m, &y_m);

	int current_s = -d_s;
	int current_m = -d_m;

	while(1) {
		if(current_s == current_m) {
			printf("%d\n", current_s);
			return 0;	
		} else if(current_s > 5000) {
			return -1;
		}
		while(current_s < current_m) {
			current_s += y_s;
		}
		
		while(current_m < current_s) {
			current_m += y_m;
		}
	}

	return 0;
}
