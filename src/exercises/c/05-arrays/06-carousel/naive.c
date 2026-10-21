#include <stdio.h>

int horse[100000];

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &horse[i]);
    }
    for (int step = 0; step < k; step++) {
        int last = horse[n - 1];
        for (int i = n - 1; i > 0; i--) {
            horse[i] = horse[i - 1];
        }
        horse[0] = last;
    }
    for (int j = 0; j < n; j++) {
        printf("%d", horse[j]);
        if (j < n - 1) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
