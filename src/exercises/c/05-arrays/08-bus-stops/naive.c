#include <stdio.h>

int gap[100001];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 1; i <= n - 1; i++) {
        scanf("%d", &gap[i]);
    }
    for (int k = 0; k < q; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        if (a > b) {
            int temp = a;
            a = b;
            b = temp;
        }
        long long total = 0;
        for (int i = a; i < b; i++) {
            total += gap[i];
        }
        printf("%lld\n", total);
    }
    return 0;
}
