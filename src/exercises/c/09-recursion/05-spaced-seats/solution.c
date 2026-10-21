#include <stdio.h>

int n;
int total = 0;
char seats[22];

void place(int pos)
{
    if (pos == n) {
        seats[n] = '\0';
        printf("%s\n", seats);
        total++;
        return;
    }
    seats[pos] = '0';
    place(pos + 1);
    if (pos == 0 || seats[pos - 1] == '0') {
        seats[pos] = '1';
        place(pos + 1);
    }
}

int main()
{
    scanf("%d", &n);
    place(0);
    printf("%d\n", total);
    return 0;
}
