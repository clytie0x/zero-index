#include <stdio.h>

int horse[100000];

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &horse[i]);
    }
    int shift = k % n;
    for (int j = 0; j < n; j++) {
        printf("%d", horse[(j - shift + n) % n]);
        if (j < n - 1) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
