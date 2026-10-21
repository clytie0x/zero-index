#include <stdio.h>

long long stack[100000];
int size = 0;

void push(long long x)
{
    stack[size] = x;
    size++;
}

long long pop(void)
{
    size--;
    return stack[size];
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        char token[12];
        scanf("%11s", token);
        if (token[0] >= '0' && token[0] <= '9') {
            long long number = 0;
            for (int j = 0; token[j] != '\0'; j++) {
                number = number * 10 + (token[j] - '0');
            }
            push(number);
        } else {
            long long right = pop();
            long long left = pop();
            if (token[0] == '+') {
                push(left + right);
            } else if (token[0] == '-') {
                push(left - right);
            } else if (token[0] == '*') {
                push(left * right);
            } else {
                push(left / right);
            }
        }
    }
    printf("%lld\n", pop());
    return 0;
}
