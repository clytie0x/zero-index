#include <stdio.h>

int main()
{
    long long first, last;
    scanf("%lld %lld", &first, &last);
    long long count = last - first + 1;
    printf("%lld\n", (first + last) * count / 2);
    return 0;
}
