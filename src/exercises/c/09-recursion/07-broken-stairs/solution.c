#include <stdio.h>

int broken[71];
long long memo[71];

long long ways(int step)
{
    if (step < 0) {
        return 0;
    }
    if (broken[step] == 1) {
        return 0;
    }
    if (step == 0) {
        return 1;
    }
    if (memo[step] != -1) {
        return memo[step];
    }
    memo[step] = ways(step - 1) + ways(step - 2) + ways(step - 3);
    return memo[step];
}

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < k; i++) {
        int step;
        scanf("%d", &step);
        broken[step] = 1;
    }
    for (int i = 0; i <= n; i++) {
        memo[i] = -1;
    }
    printf("%lld\n", ways(n));
    return 0;
}
