#include <stdio.h>

int main()
{
    long long a, b;
    char op;
    scanf("%lld %c %lld", &a, &op, &b);
    switch (op) {
        case '+':
            printf("%lld\n", a + b);
            break;
        case '-':
            printf("%lld\n", a - b);
            break;
        case '*':
            printf("%lld\n", a * b);
            break;
        case '/':
            if (b == 0) {
                printf("error\n");
            } else {
                printf("%lld\n", a / b);
            }
            break;
        case '%':
            if (b == 0) {
                printf("error\n");
            } else {
                printf("%lld\n", a % b);
            }
            break;
    }
    return 0;
}
