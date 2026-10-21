#include <stdio.h>

int people[501][501];

int main()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    for (int r = 1; r <= rows; r++) {
        for (int c = 1; c <= cols; c++) {
            scanf("%d", &people[r][c]);
        }
    }
    int questions;
    scanf("%d", &questions);
    for (int i = 0; i < questions; i++) {
        int r1, c1, r2, c2;
        scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
        long long sum = 0;
        for (int r = r1; r <= r2; r++) {
            for (int c = c1; c <= c2; c++) {
                sum += people[r][c];
            }
        }
        printf("%lld\n", sum);
    }
    return 0;
}
