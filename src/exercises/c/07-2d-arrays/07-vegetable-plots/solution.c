#include <stdio.h>

char garden[100][101];

int main()
{
    int rows, cols;
    scanf("%d %d", &rows, &cols);
    for (int r = 0; r < rows; r++) {
        scanf("%s", garden[r]);
    }
    int plots = 0, largest = 0;
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            int top_free = (r == 0 || garden[r - 1][c] != '#');
            int left_free = (c == 0 || garden[r][c - 1] != '#');
            if (garden[r][c] == '#' && top_free && left_free) {
                plots++;
                int width = 0;
                while (c + width < cols && garden[r][c + width] == '#') {
                    width++;
                }
                int height = 0;
                while (r + height < rows && garden[r + height][c] == '#') {
                    height++;
                }
                if (width * height > largest) {
                    largest = width * height;
                }
            }
        }
    }
    printf("%d %d\n", plots, largest);
    return 0;
}
