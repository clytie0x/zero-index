#include <stdio.h>

long long counter;
long long target;
int found;

void hanoi(int n, char from, char to, char via)
{
    if (n == 0 || found == 1) {
        return;
    }
    hanoi(n - 1, from, via, to);
    if (found == 1) {
        return;
    }
    counter++;
    if (counter == target) {
        printf("%d %c %c\n", n, from, to);
        found = 1;
        return;
    }
    hanoi(n - 1, via, to, from);
}

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < q; i++) {
        scanf("%lld", &target);
        counter = 0;
        found = 0;
        hanoi(n, 'A', 'C', 'B');
    }
    return 0;
}
