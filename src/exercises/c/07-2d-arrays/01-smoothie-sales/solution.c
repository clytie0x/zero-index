#include <stdio.h>

int sales[100][100];

int main()
{
    int days, menus;
    scanf("%d %d", &days, &menus);
    for (int r = 0; r < days; r++) {
        for (int c = 0; c < menus; c++) {
            scanf("%d", &sales[r][c]);
        }
    }
    int best_day = 0, best_day_total = -1;
    for (int r = 0; r < days; r++) {
        int total = 0;
        for (int c = 0; c < menus; c++) {
            total += sales[r][c];
        }
        if (total > best_day_total) {
            best_day = r;
            best_day_total = total;
        }
    }
    int best_menu = 0, best_menu_total = -1;
    for (int c = 0; c < menus; c++) {
        int total = 0;
        for (int r = 0; r < days; r++) {
            total += sales[r][c];
        }
        if (total > best_menu_total) {
            best_menu = c;
            best_menu_total = total;
        }
    }
    printf("%d %d\n", best_day + 1, best_day_total);
    printf("%d %d\n", best_menu + 1, best_menu_total);
    return 0;
}
