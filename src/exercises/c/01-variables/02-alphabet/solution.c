#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    printf("%c %c\n", 'A' + n - 1, 'a' + n - 1);
    return 0;
}
