#include <stdio.h>

int main()
{
    int room, seat;
    char row;
    scanf("%d", &room);
    scanf(" %c", &row);
    scanf("%d", &seat);
    printf("%d-%c%02d\n", room, row, seat);
    return 0;
}
