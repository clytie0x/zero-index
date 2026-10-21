#include <stdio.h>

int plate[100000];

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort(int a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(&a[j], &a[j + 1]);
            }
        }
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &plate[i]);
    }
    bubble_sort(plate, n);
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
