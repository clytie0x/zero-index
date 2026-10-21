#include <stdio.h>

int score[200000];

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void bubble_sort_desc(int a[], int n)
{
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (a[j] < a[j + 1]) {
                swap(&a[j], &a[j + 1]);
            }
        }
    }
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%d", &score[i]);
    }
    bubble_sort_desc(score, n);
    for (int i = 0; i < q; i++) {
        int k;
        scanf("%d", &k);
        printf("%d\n", score[k - 1]);
    }
    return 0;
}
