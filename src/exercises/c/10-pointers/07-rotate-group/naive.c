#include <stdio.h>

int line[100001];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &line[i]);
    }
    for (int i = 0; i < q; i++) {
        int l, r, k;
        scanf("%d %d %d", &l, &r, &k);
        k %= r - l + 1;
        for (int step = 0; step < k; step++) {
            int head = line[l];
            for (int j = l; j < r; j++) {
                line[j] = line[j + 1];
            }
            line[r] = head;
        }
    }
    for (int i = 1; i <= n; i++) {
        printf("%d", line[i]);
        if (i < n) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
