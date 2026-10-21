#include <stdio.h>

int main()
{
    long long x1, y1, x2, y2, x3, y3;
    scanf("%lld %lld %lld %lld %lld %lld", &x1, &y1, &x2, &y2, &x3, &y3);
    long long twice = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
    if (twice < 0) {
        twice = -twice;
    }
    if (twice % 2 == 0) {
        printf("%lld.0\n", twice / 2);
    } else {
        printf("%lld.5\n", twice / 2);
    }
    return 0;
}
