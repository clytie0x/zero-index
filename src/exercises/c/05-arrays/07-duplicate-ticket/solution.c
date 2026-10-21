#include <stdio.h>

int seen[1000001];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        int number;
        scanf("%d", &number);
        if (seen[number] == 1) {
            printf("%d %d\n", i, number);
            return 0;
        }
        seen[number] = 1;
    }
    printf("-1\n");
    return 0;
}
