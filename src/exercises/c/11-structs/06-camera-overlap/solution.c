#include <stdio.h>

typedef struct {
    long long x;
    long long y;
} Point;

typedef struct {
    Point low;
    Point high;
} Rect;

long long min_ll(long long a, long long b)
{
    return a < b ? a : b;
}

long long max_ll(long long a, long long b)
{
    return a > b ? a : b;
}

Rect make_rect(Point a, Point b)
{
    Rect r;
    r.low.x = min_ll(a.x, b.x);
    r.low.y = min_ll(a.y, b.y);
    r.high.x = max_ll(a.x, b.x);
    r.high.y = max_ll(a.y, b.y);
    return r;
}

Rect read_rect()
{
    Point a, b;
    scanf("%lld %lld %lld %lld", &a.x, &a.y, &b.x, &b.y);
    return make_rect(a, b);
}

int main()
{
    int n;
    scanf("%d", &n);
    Rect common = read_rect();
    for (int i = 1; i < n; i++) {
        Rect r = read_rect();
        common.low.x = max_ll(common.low.x, r.low.x);
        common.low.y = max_ll(common.low.y, r.low.y);
        common.high.x = min_ll(common.high.x, r.high.x);
        common.high.y = min_ll(common.high.y, r.high.y);
    }
    long long width = common.high.x - common.low.x;
    long long height = common.high.y - common.low.y;
    if (width > 0 && height > 0) {
        printf("%lld\n", width * height);
    } else {
        printf("0\n");
    }
    return 0;
}
