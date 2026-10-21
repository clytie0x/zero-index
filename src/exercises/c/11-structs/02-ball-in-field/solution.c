#include <stdio.h>

typedef struct {
    int x;
    int y;
} Point;

typedef struct {
    Point low;
    Point high;
} Rect;

int where(Rect field, Point ball)
{
    if (ball.x < field.low.x || ball.x > field.high.x || ball.y < field.low.y || ball.y > field.high.y) {
        return 2;
    }
    if (ball.x == field.low.x || ball.x == field.high.x || ball.y == field.low.y || ball.y == field.high.y) {
        return 1;
    }
    return 0;
}

int main()
{
    Rect field;
    scanf("%d %d %d %d", &field.low.x, &field.low.y, &field.high.x, &field.high.y);
    int n;
    scanf("%d", &n);
    int count[3] = {0, 0, 0};
    for (int i = 0; i < n; i++) {
        Point ball;
        scanf("%d %d", &ball.x, &ball.y);
        count[where(field, ball)]++;
    }
    printf("%d %d %d\n", count[0], count[1], count[2]);
    return 0;
}
