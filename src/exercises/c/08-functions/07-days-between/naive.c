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

int main()
{
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        int d1, m1, y1, d2, m2, y2;
        scanf("%d %d %d %d %d %d", &d1, &m1, &y1, &d2, &m2, &y2);
        int count = 0;
        while (d1 != d2 || m1 != m2 || y1 != y2) {
            d1++;
            if (d1 > days_in_month(m1, y1)) {
                d1 = 1;
                m1++;
                if (m1 > 12) {
                    m1 = 1;
                    y1++;
                }
            }
            count++;
        }
        printf("%d\n", count);
    }
    return 0;
}
