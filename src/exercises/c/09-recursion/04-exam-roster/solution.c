#include <stdio.h>

int ids[100000];

int search(int a[], int low, int high, int target)
{
    if (low > high) {
        return -1;
    }
    int mid = (low + high) / 2;
    if (a[mid] == target) {
        return mid;
    }
    if (a[mid] < target) {
        return search(a, mid + 1, high, target);
    }
    return search(a, low, mid - 1, target);
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        scanf("%d", &ids[i]);
    }
    for (int k = 0; k < q; k++) {
        int target;
        scanf("%d", &target);
        printf("%d\n", search(ids, 0, n - 1, target) + 1);
    }
    return 0;
}
