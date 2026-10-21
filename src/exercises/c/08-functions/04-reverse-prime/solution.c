#include <stdio.h>

int is_prime(int n)
{
    if (n < 2) {
        return 0;
    }
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return 1;
}

int reverse_number(int n)
{
    int result = 0;
    while (n > 0) {
        result = result * 10 + n % 10;
        n /= 10;
    }
    return result;
}

int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    int count = 0;
    for (int n = a; n <= b; n++) {
        if (is_prime(n) && is_prime(reverse_number(n))) {
            count++;
        }
    }
    printf("%d\n", count);
    return 0;
}
