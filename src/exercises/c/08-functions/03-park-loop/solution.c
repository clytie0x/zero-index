#include <stdio.h>
#include <math.h>

int xs[1000];
int ys[1000];

double distance(int x1, int y1, int x2, int y2)
{
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d %d", &xs[i], &ys[i]);
    }
    double total = 0;
    double longest = 0;
    for (int i = 0; i < n; i++) {
        int next = (i + 1) % n;
        double leg = distance(xs[i], ys[i], xs[next], ys[next]);
        total += leg;
        if (leg > longest) {
            longest = leg;
        }
    }
    printf("%.2f\n", total);
    printf("%.2f\n", longest);
    return 0;
}
