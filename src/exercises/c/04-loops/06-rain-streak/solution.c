#include <stdio.h>

int main()
{
    int rain;
    int rainy_days = 0, streak = 0, longest = 0;
    while (scanf("%d", &rain) == 1) {
        if (rain > 0) {
            rainy_days++;
            streak++;
            if (streak > longest) {
                longest = streak;
            }
        } else {
            streak = 0;
        }
    }
    printf("%d\n", rainy_days);
    printf("%d\n", longest);
    return 0;
}
