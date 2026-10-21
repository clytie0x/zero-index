#include <stdio.h>

long long arrive[100000];
long long cook_time[100000];
long long served_at[100000];
int waiting[100000];
int capacity;
int head = 0, tail = 0, count = 0;

void enqueue(int x)
{
    waiting[tail] = x;
    tail = (tail + 1) % capacity;
    count++;
}

int dequeue(void)
{
    int x = waiting[head];
    head = (head + 1) % capacity;
    count--;
    return x;
}

int main()
{
    int n, k;
    scanf("%d %d", &n, &k);
    capacity = k;
    for (int i = 0; i < n; i++) {
        scanf("%lld %lld", &arrive[i], &cook_time[i]);
    }
    long long finish = 0;
    for (int i = 0; i < n; i++) {
        long long t = arrive[i];
        while (count > 0 && finish <= t) {
            int next = dequeue();
            finish += cook_time[next];
            served_at[next] = finish;
        }
        if (count == 0 && finish <= t) {
            finish = t + cook_time[i];
            served_at[i] = finish;
        } else if (count < k) {
            enqueue(i);
        } else {
            served_at[i] = -1;
        }
    }
    while (count > 0) {
        int next = dequeue();
        finish += cook_time[next];
        served_at[next] = finish;
    }
    for (int i = 0; i < n; i++) {
        printf("%lld\n", served_at[i]);
    }
    return 0;
}
