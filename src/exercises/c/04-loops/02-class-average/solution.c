#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int total = 0;
    int passed = 0;
    for (int i = 1; i <= n; i++) {
        int score;
        scanf("%d", &score);
        total += score;
        if (score >= 50) {
            passed++;
        }
    }
    printf("%.2f\n", (double)total / n);
    printf("%d\n", passed);
    return 0;
}
