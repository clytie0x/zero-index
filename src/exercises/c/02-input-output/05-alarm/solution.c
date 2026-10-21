#include <stdio.h>

int main()
{
    int hour, minute, wait;
    scanf("%d:%d", &hour, &minute);
    scanf("%d", &wait);
    int alarm = (hour * 60 + minute + wait) % 1440;
    printf("%02d:%02d\n", alarm / 60, alarm % 60);
    return 0;
}
