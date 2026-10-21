#include <stdio.h>

char board[100][101];
int dr[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dc[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

int main()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    for (int r = 0; r < rows; r++) {
        scanf("%s", board[r]);
    }
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            if (board[r][c] == '*') {
                printf("*");
            } else {
                int mines = 0;
                for (int d = 0; d < 8; d++) {
                    int nr = r + dr[d];
                    int nc = c + dc[d];
                    if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && board[nr][nc] == '*') {
                        mines++;
                    }
                }
                printf("%d", mines);
            }
        }
        printf("\n");
    }
    return 0;
}
