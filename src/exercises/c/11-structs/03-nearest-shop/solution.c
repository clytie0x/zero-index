#include <stdio.h>

typedef struct {
    long long x;
    long long y;
} Point;

typedef struct {
    char name[21];
    Point place;
} Shop;

Shop shops[1000];

long long distance_squared(Point a, Point b)
{
    long long dx = a.x - b.x;
    long long dy = a.y - b.y;
    return dx * dx + dy * dy;
}

int main()
{
    Point home;
    scanf("%lld %lld", &home.x, &home.y);
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s %lld %lld", shops[i].name, &shops[i].place.x, &shops[i].place.y);
    }
    int best = 0;
    long long best_distance = distance_squared(home, shops[0].place);
    for (int i = 1; i < n; i++) {
        long long d = distance_squared(home, shops[i].place);
        if (d < best_distance) {
            best = i;
            best_distance = d;
        }
    }
    printf("%s %lld\n", shops[best].name, best_distance);
    return 0;
}
