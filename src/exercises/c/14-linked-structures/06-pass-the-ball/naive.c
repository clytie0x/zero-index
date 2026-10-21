#include <stdio.h>

int circle[5000];
int capacity;
int head = 0, tail = 0, count = 0;

void enqueue(int x)
{
    circle[tail] = x;
    tail = (tail + 1) % capacity;
    count++;
}

int dequeue(void)
{
    int x = circle[head];
    head = (head + 1) % capacity;
    count--;
    return x;
}

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    capacity = n;
    for (int i = 1; i <= n; i++) {
        enqueue(i);
    }
    for (int round = 0; round < n; round++) {
        for (int p = 0; p < k - 1; p++) {
            enqueue(dequeue());
        }
        if (round > 0) {
            printf(" ");
        }
        printf("%d", dequeue());
    }
    printf("\n");
    return 0;
}
