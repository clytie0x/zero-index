#include <stdio.h>

int main()
{
    int n;
    scanf("%d", &n);
    int result = 0;
    for (int i = 0; i < n; i++) {
        int color;
        scanf("%d", &color);
        result = result ^ color;
    }
    printf("%d\n", result);
    return 0;
}
