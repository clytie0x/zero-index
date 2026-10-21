#include <stdio.h>

int prev[300001];
int next[300001];

void remove_car(int x)
{
    next[prev[x]] = next[x];
    prev[next[x]] = prev[x];
}

void insert_after(int p, int x)
{
    prev[x] = p;
    next[x] = next[p];
    prev[next[p]] = x;
    next[p] = x;
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int car = 1; car <= n; car++) {
        insert_after(prev[0], car);
    }
    for (int i = 0; i < q; i++) {
        char command;
        scanf(" %c", &command);
        if (command == 'I') {
            int x, y;
            scanf("%d %d", &x, &y);
            insert_after(x, y);
        } else {
            int x;
            scanf("%d", &x);
            remove_car(x);
        }
    }
    if (next[0] == 0) {
        printf("EMPTY\n");
        return 0;
    }
    for (int car = next[0]; car != 0; car = next[car]) {
        printf("%d", car);
        if (next[car] != 0) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
