#include <stdio.h>

int count[1000001];
int prefix[1000002];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        int points;
        scanf("%d", &points);
        count[points]++;
    }
    prefix[0] = 0;
    for (int v = 0; v <= 1000000; v++) {
        prefix[v + 1] = prefix[v] + count[v];
    }
    for (int k = 0; k < q; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", prefix[b + 1] - prefix[a]);
    }
    return 0;
}
