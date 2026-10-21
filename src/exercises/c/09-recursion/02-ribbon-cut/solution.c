#include <stdio.h>

int lengths[100000];

int gcd(int a, int b)
{
    if (b == 0) {
        return a;
    }
    return gcd(b, a % b);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &lengths[i]);
    }
    int piece = lengths[0];
    for (int i = 1; i < n; i++) {
        piece = gcd(piece, lengths[i]);
    }
    long long pieces = 0;
    for (int i = 0; i < n; i++) {
        pieces += lengths[i] / piece;
    }
    printf("%d\n", piece);
    printf("%lld\n", pieces);
    return 0;
}
