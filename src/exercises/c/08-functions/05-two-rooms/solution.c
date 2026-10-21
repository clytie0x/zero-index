#include <stdio.h>

int room_a[1000];
int room_b[1000];

void read_array(int values[], int n)
{
    for (int i = 0; i < n; i++) {
        scanf("%d", &values[i]);
    }
}

int max_of_array(int values[], int n)
{
    int best = values[0];
    for (int i = 1; i < n; i++) {
        if (values[i] > best) {
            best = values[i];
        }
    }
    return best;
}

int min_of_array(int values[], int n)
{
    int worst = values[0];
    for (int i = 1; i < n; i++) {
        if (values[i] < worst) {
            worst = values[i];
        }
    }
    return worst;
}

int sum_of_array(int values[], int n)
{
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += values[i];
    }
    return sum;
}

int main()
{
    int n, m;
    scanf("%d", &n);
    read_array(room_a, n);
    scanf("%d", &m);
    read_array(room_b, m);
    printf("%d %d\n", max_of_array(room_a, n), min_of_array(room_a, n));
    printf("%d %d\n", max_of_array(room_b, m), min_of_array(room_b, m));
    int left = sum_of_array(room_a, n) * m;
    int right = sum_of_array(room_b, m) * n;
    if (left > right) {
        printf("A\n");
    } else if (left < right) {
        printf("B\n");
    } else {
        printf("SAME\n");
    }
    return 0;
}
