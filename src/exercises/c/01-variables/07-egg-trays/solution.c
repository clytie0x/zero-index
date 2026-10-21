#include <stdio.h>

int main()
{
    int eggs, per_tray;
    scanf("%d %d", &eggs, &per_tray);
    printf("%d\n", (eggs - 1) / per_tray + 1);
    return 0;
}
