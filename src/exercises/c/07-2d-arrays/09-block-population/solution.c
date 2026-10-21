#include <stdio.h>

long long prefix[501][501];

int main()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    for (int r = 1; r <= rows; r++) {
        for (int c = 1; c <= cols; c++) {
            int people;
            scanf("%d", &people);
            prefix[r][c] = people + prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
        }
    }
    int questions;
    scanf("%d", &questions);
    for (int i = 0; i < questions; i++) {
        int r1, c1, r2, c2;
        scanf("%d %d %d %d", &r1, &c1, &r2, &c2);
        printf("%lld\n", prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]);
    }
    return 0;
}
