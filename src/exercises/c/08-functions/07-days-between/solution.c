#include <stdio.h>

int is_leap(int year)
{
    return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
}

int days_in_month(int month, int year)
{
    if (month == 2) {
        return is_leap(year) ? 29 : 28;
    }
    if (month == 4 || month == 6 || month == 9 || month == 11) {
        return 30;
    }
    return 31;
}

int day_number(int day, int month, int year)
{
    int total = 0;
    for (int y = 1900; y < year; y++) {
        total += is_leap(y) ? 366 : 365;
    }
    for (int m = 1; m < month; m++) {
        total += days_in_month(m, year);
    }
    return total + day;
}

int main()
{
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        int d1, m1, y1, d2, m2, y2;
        scanf("%d %d %d %d %d %d", &d1, &m1, &y1, &d2, &m2, &y2);
        printf("%d\n", day_number(d2, m2, y2) - day_number(d1, m1, y1));
    }
    return 0;
}
