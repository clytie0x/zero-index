#include <stdio.h>

int seat[100001];

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &seat[i]);
    }
    for (int i = 0; i < q; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        swap(&seat[a], &seat[b]);
    }
    for (int i = 1; i <= n; i++) {
        printf("%d", seat[i]);
        if (i < n) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
