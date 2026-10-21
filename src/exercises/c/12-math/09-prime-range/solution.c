#include <stdio.h>

#define LIMIT 10000000

char is_composite[LIMIT + 1];
int prime_count[LIMIT + 1];

int main()
{
    for (int i = 2; i * i <= LIMIT; i++) {
        if (!is_composite[i]) {
            for (int j = i * i; j <= LIMIT; j += i) {
                is_composite[j] = 1;
            }
        }
    }
    prime_count[0] = 0;
    prime_count[1] = 0;
    for (int x = 2; x <= LIMIT; x++) {
        prime_count[x] = prime_count[x - 1];
        if (!is_composite[x]) {
            prime_count[x]++;
        }
    }
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("%d\n", prime_count[b] - prime_count[a - 1]);
    }
    return 0;
}
