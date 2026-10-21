#include <stdio.h>

char photo[100][101];

int main()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    for (int r = 0; r < rows; r++) {
        scanf("%s", photo[r]);
    }
    for (int c = 0; c < cols; c++) {
        for (int r = rows - 1; r >= 0; r--) {
            printf("%c", photo[r][c]);
        }
        printf("\n");
    }
    return 0;
}
