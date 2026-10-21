#include <stdio.h>

int main()
{
    char symbols[] = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char text[70];
    int from_base, to_base;
    scanf("%s %d %d", text, &from_base, &to_base);
    long long value = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        int digit;
        if (text[i] >= '0' && text[i] <= '9') {
            digit = text[i] - '0';
        } else {
            digit = text[i] - 'A' + 10;
        }
        value = value * from_base + digit;
    }
    char digits[70];
    int length = 0;
    do {
        digits[length] = symbols[value % to_base];
        length++;
        value /= to_base;
    } while (value > 0);
    for (int i = length - 1; i >= 0; i--) {
        printf("%c", digits[i]);
    }
    printf("\n");
    return 0;
}
