#include <stdio.h>
#include <ctype.h>


int main() {

	int N;
	scanf("%d", &N);
	getchar();

	for(int i = 0; i < N; i ++) {
		char sentence[40];
		fgets(sentence, sizeof(sentence), stdin);
		sentence[0] = toupper(sentence[0]);
		
		printf("%s", sentence);
	}	

	return 0;
}