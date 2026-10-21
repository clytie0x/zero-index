#include <stdio.h>

int main()
{
    char first[21], last[21];
    scanf("%s %s", first, last);
    printf("+----------------------+\n");
    printf("| %-20s |\n", first);
    printf("| %-20s |\n", last);
    printf("+----------------------+\n");
    return 0;
}
