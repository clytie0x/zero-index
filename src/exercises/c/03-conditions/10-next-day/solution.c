#include <stdio.h>

int main()
{
    int day, month, year;
    scanf("%d %d %d", &day, &month, &year);
    int days_in_month;
    switch (month) {
        case 2:
            if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
                days_in_month = 29;
            } else {
                days_in_month = 28;
            }
            break;
        case 4:
        case 6:
        case 9:
        case 11:
            days_in_month = 30;
            break;
        default:
            days_in_month = 31;
    }
    if (day < days_in_month) {
        day++;
    } else {
        day = 1;
        if (month < 12) {
            month++;
        } else {
            month = 1;
            year++;
        }
    }
    printf("%d %d %d\n", day, month, year);
    return 0;
}
