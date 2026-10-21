#include <stdio.h>

int height[500001];
int answer[500001];
int stack[500000];
int size = 0;

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
        scanf("%d", &height[i]);
    }
    for (int i = 1; i <= n; i++) {
        while (size > 0 && height[stack[size - 1]] < height[i]) {
            size--;
            answer[stack[size]] = i;
        }
        stack[size] = i;
        size++;
    }
    for (int i = 1; i <= n; i++) {
        printf("%d", answer[i]);
        if (i < n) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
