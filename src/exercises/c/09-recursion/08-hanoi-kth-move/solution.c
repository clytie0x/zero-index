#include <stdio.h>

long long power_of_two[61];

void find_move(int n, long long k, char from, char to, char via)
{
    long long middle = power_of_two[n - 1];
    if (k < middle) {
        find_move(n - 1, k, from, via, to);
    } else if (k == middle) {
        printf("%d %c %c\n", n, from, to);
    } else {
        find_move(n - 1, k - middle, via, to, from);
    }
}

int main()
{
    power_of_two[0] = 1;
    for (int i = 1; i <= 60; i++) {
        power_of_two[i] = power_of_two[i - 1] * 2;
    }
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < q; i++) {
        long long k;
        scanf("%lld", &k);
        find_move(n, k, 'A', 'C', 'B');
    }
    return 0;
}
