#include <stdio.h>

int line[100001];

void reverse(int *first, int *last)
{
    while (first < last) {
        int temp = *first;
        *first = *last;
        *last = temp;
        first++;
        last--;
    }
}

void rotate_left(int *first, int *last, int k)
{
    int len = last - first + 1;
    k %= len;
    if (k == 0) {
        return;
    }
    reverse(first, first + k - 1);
    reverse(first + k, last);
    reverse(first, last);
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &line[i]);
    }
    for (int i = 0; i < q; i++) {
        int l, r, k;
        scanf("%d %d %d", &l, &r, &k);
        rotate_left(&line[l], &line[r], k);
    }
    for (int i = 1; i <= n; i++) {
        printf("%d", line[i]);
        if (i < n) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
