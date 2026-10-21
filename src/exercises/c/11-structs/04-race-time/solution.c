#include <stdio.h>

typedef struct {
    int hours;
    int minutes;
    int seconds;
} Time;

typedef struct {
    char name[21];
    Time start;
    Time finish;
} Runner;

Runner runners[1000];

int to_seconds(Time t)
{
    return t.hours * 3600 + t.minutes * 60 + t.seconds;
}

Time from_seconds(int total)
{
    Time t;
    t.hours = total / 3600;
    t.minutes = total % 3600 / 60;
    t.seconds = total % 60;
    return t;
}

int used(const Runner *r)
{
    return to_seconds(r->finish) - to_seconds(r->start);
}

int faster(const Runner *a, const Runner *b)
{
    if (used(a) != used(b)) {
        return used(a) < used(b);
    }
    return to_seconds(a->finish) < to_seconds(b->finish);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        Runner *r = &runners[i];
        scanf("%s %d %d %d %d %d %d", r->name,
              &r->start.hours, &r->start.minutes, &r->start.seconds,
              &r->finish.hours, &r->finish.minutes, &r->finish.seconds);
    }
    int best = 0;
    for (int i = 1; i < n; i++) {
        if (faster(&runners[i], &runners[best])) {
            best = i;
        }
    }
    Time t = from_seconds(used(&runners[best]));
    printf("%s %d %d %d\n", runners[best].name, t.hours, t.minutes, t.seconds);
    return 0;
}
