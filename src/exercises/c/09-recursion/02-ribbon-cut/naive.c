#include <stdio.h>

int lengths[100000];

int main()
{
    int n;
    scanf("%d", &n);
    int shortest = 1000000000;
    for (int i = 0; i < n; i++) {
        scanf("%d", &lengths[i]);
        if (lengths[i] < shortest) {
            shortest = lengths[i];
        }
    }
    int piece = 1;
    for (int d = shortest; d >= 1; d--) {
        int ok = 1;
        for (int i = 0; i < n; i++) {
            if (lengths[i] % d != 0) {
                ok = 0;
                break;
            }
        }
        if (ok) {
            piece = d;
            break;
        }
    }
    long long pieces = 0;
    for (int i = 0; i < n; i++) {
        pieces += lengths[i] / piece;
    }
    printf("%d\n", piece);
    printf("%lld\n", pieces);
    return 0;
}
