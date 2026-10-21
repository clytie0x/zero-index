#include <stdio.h>

int score[1000];

int main()
{
    int n;
    scanf("%d", &n);
    int total = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &score[i]);
        total += score[i];
    }
    int stars = 0;
    for (int i = 0; i < n; i++) {
        if (score[i] * n >= total) {
            stars++;
        }
    }
    printf("%d\n", stars);
    return 0;
}
