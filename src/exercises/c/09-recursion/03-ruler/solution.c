#include <stdio.h>

void ruler(int k)
{
    if (k == 0) {
        return;
    }
    ruler(k - 1);
    for (int i = 0; i < k; i++) {
        printf("-");
    }
    printf("\n");
    ruler(k - 1);
}

int main()
{
    int k;
    scanf("%d", &k);
    ruler(k);
    return 0;
}
