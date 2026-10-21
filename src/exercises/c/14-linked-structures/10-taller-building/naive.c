#include <stdio.h>

int height[500001];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &height[i]);
    }
    for (int i = 1; i <= n; i++) {
        int found = 0;
        for (int j = i + 1; j <= n; j++) {
            if (height[j] > height[i]) {
                found = j;
                break;
            }
        }
        printf("%d", found);
        if (i < n) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
