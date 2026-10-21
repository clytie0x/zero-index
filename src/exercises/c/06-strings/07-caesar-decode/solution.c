#include <stdio.h>

char text[1005];

int main()
{
    int key;
    scanf("%d", &key);
    while (getchar() != '\n') {
    }
    fgets(text, sizeof text, stdin);
    int shift = (26 - key % 26) % 26;
    for (int i = 0; text[i] != '\0'; i++) {
        char c = text[i];
        if (c >= 'a' && c <= 'z') {
            text[i] = (c - 'a' + shift) % 26 + 'a';
        } else if (c >= 'A' && c <= 'Z') {
            text[i] = (c - 'A' + shift) % 26 + 'A';
        } else if (c == '\n' || c == '\r') {
            text[i] = '\0';
        }
    }
    printf("%s\n", text);
    return 0;
}
