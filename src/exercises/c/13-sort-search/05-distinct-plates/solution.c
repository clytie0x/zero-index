#include <stdio.h>
#include <stdlib.h>

int plate[100000];

int compare_int(const void *p, const void *q)
{
    int x = *(const int *)p;
    int y = *(const int *)q;
    if (x < y) {
        return -1;
    }
    if (x > y) {
        return 1;
    }
    return 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &plate[i]);
    }
    qsort(plate, n, sizeof(int), compare_int);
    int distinct = 0;
    int most = 0;
    int start = 0;
    for (int i = 1; i <= n; i++) {
        if (i == n || plate[i] != plate[i - 1]) {
            distinct++;
            if (i - start > most) {
                most = i - start;
            }
            start = i;
        }
    }
    printf("%d %d\n", distinct, most);
    return 0;
}
