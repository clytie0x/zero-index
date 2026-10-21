#include <stdio.h>

typedef struct {
    long long x;
    long long y;
} Point;

typedef struct {
    Point pos;
    int dir;
} Robot;

const char DIRECTIONS[] = "NESW";
const int DX[4] = {0, 1, 0, -1};
const int DY[4] = {1, 0, -1, 0};

Robot robots[1000];

int direction_index(char d)
{
    for (int i = 0; i < 4; i++) {
        if (DIRECTIONS[i] == d) {
            return i;
        }
    }
    return -1;
}

void turn_left(Robot *r)
{
    r->dir = (r->dir + 3) % 4;
}

void turn_right(Robot *r)
{
    r->dir = (r->dir + 1) % 4;
}

void forward(Robot *r, long long steps)
{
    r->pos.x += DX[r->dir] * steps;
    r->pos.y += DY[r->dir] * steps;
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        char d;
        scanf("%lld %lld %c", &robots[i].pos.x, &robots[i].pos.y, &d);
        robots[i].dir = direction_index(d);
    }
    for (int k = 0; k < q; k++) {
        int id;
        char command;
        scanf("%d %c", &id, &command);
        Robot *r = &robots[id - 1];
        if (command == 'F') {
            long long steps;
            scanf("%lld", &steps);
            forward(r, steps);
        } else if (command == 'L') {
            turn_left(r);
        } else {
            turn_right(r);
        }
    }
    int pairs = 0;
    for (int i = 0; i < n; i++) {
        printf("%lld %lld %c\n", robots[i].pos.x, robots[i].pos.y, DIRECTIONS[robots[i].dir]);
        for (int j = i + 1; j < n; j++) {
            if (robots[i].pos.x == robots[j].pos.x && robots[i].pos.y == robots[j].pos.y) {
                pairs++;
            }
        }
    }
    printf("%d\n", pairs);
    return 0;
}
