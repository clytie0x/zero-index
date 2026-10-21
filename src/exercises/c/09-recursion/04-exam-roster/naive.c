#include <stdio.h>

int ids[100000];

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
        int position = 0;
        for (int i = 0; i < n; i++) {
            if (ids[i] == target) {
                position = i + 1;
                break;
            }
        }
        printf("%d\n", position);
    }
    return 0;
}
