#include <stdio.h>

int main()
{
    int q;
    scanf("%d", &q);
    for (int k = 0; k < q; k++) {
        int a, b;
        scanf("%d %d", &a, &b);
        int count = 0;
        for (int x = a; x <= b; x++) {
            if (x < 2) {
                continue;
            }
            int is_prime = 1;
            for (int i = 2; i * i <= x; i++) {
                if (x % i == 0) {
                    is_prime = 0;
                    break;
                }
            }
            if (is_prime) {
                count++;
            }
        }
        printf("%d\n", count);
    }
    return 0;
}
