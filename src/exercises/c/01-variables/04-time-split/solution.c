#include <stdio.h>

int main()
{
    int total;
    scanf("%d", &total);
    int hours = total / 3600;
    int minutes = total % 3600 / 60;
    int seconds = total % 60;
    printf("%d %d %d\n", hours, minutes, seconds);
    return 0;
}
