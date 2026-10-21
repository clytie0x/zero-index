#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int first;
    scanf("%d", &first);
    int highest = first, high_day = 1;
    int lowest = first, low_day = 1;
    for (int day = 2; day <= n; day++) {
        int temp;
        scanf("%d", &temp);
        if (temp > highest) {
            highest = temp;
            high_day = day;
        }
        if (temp < lowest) {
            lowest = temp;
            low_day = day;
        }
    }
    printf("%d %d\n", highest, high_day);
    printf("%d %d\n", lowest, low_day);
    return 0;
}
