#include <stdio.h>
#include <stdlib.h>

void swap_rows(int **x, int **y)
{
    int *temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int rows, cols, q;
    scanf("%d %d %d", &rows, &cols, &q);
    int **table = malloc((rows + 1) * sizeof(int *));
    for (int r = 1; r <= rows; r++) {
        table[r] = malloc(cols * sizeof(int));
        for (int c = 0; c < cols; c++) {
            scanf("%d", &table[r][c]);
        }
    }
    for (int i = 0; i < q; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        swap_rows(&table[a], &table[b]);
    }
    for (int r = 1; r <= rows; r++) {
        for (int c = 0; c < cols; c++) {
            printf("%d", table[r][c]);
            if (c < cols - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
    for (int r = 1; r <= rows; r++) {
        free(table[r]);
    }
    free(table);
    return 0;
}
