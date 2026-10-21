#include <stdio.h>

char map[100][101];
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int main()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    for (int r = 0; r < rows; r++) {
        scanf("%s", map[r]);
    }
    int coast = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (map[r][c] == '#') {
                for (int d = 0; d < 4; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || map[nr][nc] == '.') {
                        coast++;
                    }
                }
            }
        }
    }
    printf("%d\n", coast);
    return 0;
}
