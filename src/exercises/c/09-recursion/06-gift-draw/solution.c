#include <stdio.h>

int n;
int total = 0;
int gift[10];
int taken[10];

void draw(int pos)
{
    if (pos == n) {
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", gift[i]);
        }
        printf("\n");
        total++;
        return;
    }
    for (int v = 1; v <= n; v++) {
        if (taken[v] == 0 && v != pos + 1) {
            taken[v] = 1;
            gift[pos] = v;
            draw(pos + 1);
            taken[v] = 0;
        }
    }
}

int main()
{
    scanf("%d", &n);
    draw(0);
    if (total == 0) {
        printf("none\n");
    }
    return 0;
}
