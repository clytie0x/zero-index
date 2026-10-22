#include <stdio.h>
#include <stdlib.h>

int main()
{
    int shelves;
    scanf("%d", &shelves);
    long long **prefix = malloc((shelves + 1) * sizeof(long long *));
    for (int s = 1; s <= shelves; s++) {
        int n;
        scanf("%d", &n);
        prefix[s] = malloc((n + 1) * sizeof(long long));
        prefix[s][0] = 0;
        for (int i = 1; i <= n; i++) {
            int words;
            scanf("%d", &words);
            prefix[s][i] = prefix[s][i - 1] + words;
        }
    }
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        int s, a, b;
        scanf("%d %d %d", &s, &a, &b);
        printf("%lld\n", prefix[s][b] - prefix[s][a - 1]);
    }
    for (int s = 1; s <= shelves; s++) {
        free(prefix[s]);
    }
    free(prefix);
    return 0;
}
