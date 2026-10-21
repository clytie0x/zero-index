#include <stdio.h>

char line[1000][1001];

int main()
{
    int rows, cols, k;
    scanf("%d %d %d", &rows, &cols, &k);
    for (int r = 0; r < rows; r++) {
        scanf("%s", line[r]);
    }
    int best = -1, best_r = 0, best_c = 0;
    for (int top = 0; top + k <= rows; top++) {
        for (int left = 0; left + k <= cols; left++) {
            int sum = 0;
            for (int r = top; r < top + k; r++) {
                for (int c = left; c < left + k; c++) {
                    sum += line[r][c] - '0';
                }
            }
            if (sum > best) {
                best = sum;
                best_r = top;
                best_c = left;
            }
        }
    }
    printf("%d\n%d %d\n", best, best_r + 1, best_c + 1);
    return 0;
}
