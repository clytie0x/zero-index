#include <stdio.h>

int main()
{
    int minutes1, seconds1, millis1;
    int minutes2, seconds2, millis2;
    int minutes3, seconds3, millis3;
    scanf("%d:%d.%d", &minutes1, &seconds1, &millis1);
    scanf("%d:%d.%d", &minutes2, &seconds2, &millis2);
    scanf("%d:%d.%d", &minutes3, &seconds3, &millis3);
    int total = (minutes1 + minutes2 + minutes3) * 60000
              + (seconds1 + seconds2 + seconds3) * 1000
              + millis1 + millis2 + millis3;
    printf("%d:%02d.%03d\n", total / 60000, total / 1000 % 60, total % 1000);
    return 0;
}
