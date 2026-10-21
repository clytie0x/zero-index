#include <stdio.h>

int main()
{
    int start_hour, start_minute, end_hour, end_minute;
    double distance;
    scanf("%d:%d", &start_hour, &start_minute);
    scanf("%d:%d", &end_hour, &end_minute);
    scanf("%lf", &distance);
    int minutes = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute);
    printf("%d:%02d\n", minutes / 60, minutes % 60);
    printf("%.2f\n", distance * 60 / minutes);
    return 0;
}
