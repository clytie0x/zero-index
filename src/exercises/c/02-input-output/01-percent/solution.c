#include <stdio.h>

int main()
{
    int score, total;
    scanf("%d %d", &score, &total);
    printf("%d/%d = %.2f%%\n", score, total, score * 100.0 / total);
    return 0;
}
