#include <stdio.h>
#include <string.h>

int main() {

	char me[1000];
	char doctor[1000];
	
	fgets(me, sizeof(me), stdin);
	fgets(doctor, sizeof(doctor), stdin);

	if(strlen(me) >= strlen(doctor)) {
		printf("go\n");
	} else {
		printf("no\n");
	}

	return 0;
}