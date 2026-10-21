#include <stdio.h>

int main()
{
    int first_time, second_time;
    scanf("%d %d", &first_time, &second_time);
    if (first_time < second_time) {
        printf("first\n");
    } else if (second_time < first_time) {
        printf("second\n");
    } else {
        printf("tie\n");
    }
    return 0;
}
