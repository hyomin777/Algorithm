#include <stdio.h>
#include <time.h>

int main() {

        time_t current_time = time(NULL);
        struct tm *local_time = localtime(&current_time);

        char year[5];
        char month[5];
        char day[5];
        strftime(year, sizeof(year), "%Y", local_time);
        strftime(month, sizeof(month), "%m", local_time);
        strftime(day, sizeof(day), "%d", local_time);

        printf("%s\n%s\n%s\n", year, month, day);

        return 0;
}