#include <stdio.h>

int seconds[1000];

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void selection_sort(int a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        int min_index = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_index]) {
                min_index = j;
            }
        }
        swap(&a[i], &a[min_index]);
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &seconds[i]);
    }
    selection_sort(seconds, n);
    printf("%d\n", seconds[n / 2]);
    return 0;
}
