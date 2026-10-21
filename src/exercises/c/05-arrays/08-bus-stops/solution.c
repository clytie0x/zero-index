#include <stdio.h>

long long dist[100001];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    dist[1] = 0;
    for (int i = 2; i <= n; i++) {
        int gap;
        scanf("%d", &gap);
        dist[i] = dist[i - 1] + gap;
    }
    for (int k = 0; k < q; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        printf("%lld\n", dist[b] - dist[a]);
    }
    return 0;
}
