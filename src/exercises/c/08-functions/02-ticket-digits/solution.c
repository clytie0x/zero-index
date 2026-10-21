#include <stdio.h>

int digit_sum(int n)
{
    int sum = 0;
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main()
{
    int n;
    scanf("%d", &n);
    int best_ticket = -1;
    int best_sum = -1;
    for (int i = 0; i < n; i++) {
        int ticket;
        scanf("%d", &ticket);
        int sum = digit_sum(ticket);
        if (sum > best_sum || (sum == best_sum && ticket < best_ticket)) {
            best_ticket = ticket;
            best_sum = sum;
        }
    }
    printf("%d %d\n", best_ticket, best_sum);
    return 0;
}
