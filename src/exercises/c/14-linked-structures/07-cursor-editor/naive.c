#include <stdio.h>

char keys[2000001];
char text[2000001];

int main()
{
    scanf("%2000000s", keys);
    int length = 0, cursor = 0;
    for (int i = 0; keys[i] != '\0'; i++) {
        char c = keys[i];
        if (c == '<') {
            if (cursor > 0) {
                cursor--;
            }
        } else if (c == '>') {
            if (cursor < length) {
                cursor++;
            }
        } else if (c == '#') {
            if (cursor > 0) {
                for (int j = cursor - 1; j < length - 1; j++) {
                    text[j] = text[j + 1];
                }
                length--;
                cursor--;
            }
        } else {
            for (int j = length; j > cursor; j--) {
                text[j] = text[j - 1];
            }
            text[cursor] = c;
            length++;
            cursor++;
        }
    }
    if (length == 0) {
        printf("EMPTY\n");
        return 0;
    }
    text[length] = '\0';
    printf("%s\n", text);
    return 0;
}
