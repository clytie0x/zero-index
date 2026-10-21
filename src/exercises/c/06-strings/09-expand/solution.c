#include <stdio.h>

char code[10005];

int main()
{
    scanf("%s", code);
    int i = 0;
    while (code[i] != '\0') {
        char letter = code[i];
        i++;
        int count = 0;
        while (code[i] >= '0' && code[i] <= '9') {
            count = count * 10 + (code[i] - '0');
            i++;
        }
        for (int k = 0; k < count; k++) {
            printf("%c", letter);
        }
    }
    printf("\n");
    return 0;
}
