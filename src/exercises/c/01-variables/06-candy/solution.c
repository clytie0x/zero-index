#include <stdio.h>

int main()
{
    long long boxes, per_box, given;
    scanf("%lld %lld %lld", &boxes, &per_box, &given);
    printf("%lld\n", boxes * per_box - given);
    return 0;
}
