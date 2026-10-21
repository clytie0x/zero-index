#include <stdio.h>

int count[101];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int score;
        scanf("%d", &score);
        count[score]++;
    }
    for (int s = 100; s >= 0; s--) {
        if (count[s] > 0) {
            printf("%d %d\n", s, count[s]);
        }
    }
    return 0;
}
