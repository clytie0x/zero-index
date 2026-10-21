#include <stdio.h>

int points[100000];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%d", &points[i]);
    }
    for (int k = 0; k < q; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        int total = 0;
        for (int i = 0; i < n; i++) {
            if (points[i] >= a && points[i] <= b) {
                total++;
            }
        }
        printf("%d\n", total);
    }
    return 0;
}
