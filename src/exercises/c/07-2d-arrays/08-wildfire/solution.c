#include <stdio.h>

char forest[100][101], next_forest[100][101];
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main()
{
    int rows, cols, minutes;
    scanf("%d %d %d", &rows, &cols, &minutes);
    for (int r = 0; r < rows; r++) {
        scanf("%s", forest[r]);
    }
    for (int t = 0; t < minutes; t++) {
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                next_forest[r][c] = forest[r][c];
                if (forest[r][c] == '*') {
                    next_forest[r][c] = '.';
                } else if (forest[r][c] == '#') {
                    for (int d = 0; d < 4; d++) {
                        int nr = r + dr[d];
                        int nc = c + dc[d];
                        if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && forest[nr][nc] == '*') {
                            next_forest[r][c] = '*';
                        }
                    }
                }
            }
        }
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                forest[r][c] = next_forest[r][c];
            }
        }
    }
    for (int r = 0; r < rows; r++) {
        printf("%s\n", forest[r]);
    }
    return 0;
}
