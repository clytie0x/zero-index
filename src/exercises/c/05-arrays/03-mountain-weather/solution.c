#include <stdio.h>

int temp[1000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &temp[i]);
    }
    int warmest = 0;
    int coldest = 0;
    for (int i = 1; i < n; i++) {
        if (temp[i] > temp[warmest]) {
            warmest = i;
        }
        if (temp[i] <= temp[coldest]) {
            coldest = i;
        }
    }
    printf("%d %d\n", temp[warmest], warmest + 1);
    printf("%d %d\n", temp[coldest], coldest + 1);
    return 0;
}
