#include <stdio.h>

char formula[100001];
int stack[100000];
int size = 0;

char opening_of(char c)
{
    if (c == ')') {
        return '(';
    } else if (c == ']') {
        return '[';
    }
    return '{';
}

int first_error(void)
{
    size = 0;
    for (int i = 0; formula[i] != '\0'; i++) {
        char c = formula[i];
        if (c == '(' || c == '[' || c == '{') {
            stack[size] = i;
            size++;
        } else if (c == ')' || c == ']' || c == '}') {
            if (size == 0 || formula[stack[size - 1]] != opening_of(c)) {
                return i + 1;
            }
            size--;
        }
    }
    if (size > 0) {
        return stack[0] + 1;
    }
    return 0;
}

int main()
{
    int t;
    scanf("%d", &t);
    for (int k = 0; k < t; k++) {
        scanf("%100000s", formula);
        int position = first_error();
        if (position == 0) {
            printf("OK\n");
        } else {
            printf("ERROR %d\n", position);
        }
    }
    return 0;
}
