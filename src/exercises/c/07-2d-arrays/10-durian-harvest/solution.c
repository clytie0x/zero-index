#include <stdio.h>

char line[1001][1002];
int prefix[1001][1001];

int main()
{
    int rows, cols, k;
    scanf("%d %d %d", &rows, &cols, &k);
    for (int r = 1; r <= rows; r++) {
        scanf("%s", line[r]);
        for (int c = 1; c <= cols; c++) {
            int ripe = line[r][c - 1] - '0';
            prefix[r][c] = ripe + prefix[r - 1][c] + prefix[r][c - 1] - prefix[r - 1][c - 1];
        }
    }
    int best = -1, best_r = 0, best_c = 0;
    for (int r = 1; r + k - 1 <= rows; r++) {
        for (int c = 1; c + k - 1 <= cols; c++) {
            int r2 = r + k - 1, c2 = c + k - 1;
            int sum = prefix[r2][c2] - prefix[r - 1][c2] - prefix[r2][c - 1] + prefix[r - 1][c - 1];
            if (sum > best) {
                best = sum;
                best_r = r;
                best_c = c;
            }
        }
    }
    printf("%d\n%d %d\n", best, best_r, best_c);
    return 0;
}
