#include <stdio.h>
#include <stdlib.h>

int main()
{
    int rows, cols, q;
    scanf("%d %d %d", &rows, &cols, &q);
    int *table = malloc((rows + 1) * cols * sizeof(int));
    for (int r = 1; r <= rows; r++) {
        for (int c = 0; c < cols; c++) {
            scanf("%d", &table[r * cols + c]);
        }
    }
    for (int i = 0; i < q; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        for (int c = 0; c < cols; c++) {
            int temp = table[a * cols + c];
            table[a * cols + c] = table[b * cols + c];
            table[b * cols + c] = temp;
        }
    }
    for (int r = 1; r <= rows; r++) {
        for (int c = 0; c < cols; c++) {
            printf("%d", table[r * cols + c]);
            if (c < cols - 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
    free(table);
    return 0;
}
