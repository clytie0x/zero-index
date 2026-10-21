#include <stdio.h>

void print_binary(long long n)
{
    if (n >= 2) {
        print_binary(n / 2);
    }
    printf("%lld", n % 2);
}

int main()
{
    long long n;
    scanf("%lld", &n);
    print_binary(n);
    printf("\n");
    return 0;
}
