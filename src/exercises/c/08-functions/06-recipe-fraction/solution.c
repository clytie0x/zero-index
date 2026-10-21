#include <stdio.h>

long long gcd(long long a, long long b)
{
    while (b != 0) {
        long long remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

int main()
{
    int n;
    scanf("%d", &n);
    long long top = 0;
    long long bottom = 1;
    for (int i = 0; i < n; i++) {
        int a, b;
        scanf("%d/%d", &a, &b);
        top = top * b + a * bottom;
        bottom = bottom * b;
        long long g = gcd(top, bottom);
        top /= g;
        bottom /= g;
    }
    if (bottom == 1) {
        printf("%lld\n", top);
    } else {
        printf("%lld/%lld\n", top, bottom);
    }
    return 0;
}
