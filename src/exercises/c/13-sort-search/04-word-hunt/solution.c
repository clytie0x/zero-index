#include <stdio.h>
#include <string.h>
#include <ctype.h>

char text[1005], word[105];

void strip_newline(char s[])
{
    for (int i = 0; s[i] != '\0'; i++) {
        if (s[i] == '\n' || s[i] == '\r') {
            s[i] = '\0';
        }
    }
}

int main()
{
    fgets(text, sizeof text, stdin);
    fgets(word, sizeof word, stdin);
    strip_newline(text);
    strip_newline(word);
    int n = strlen(text);
    int m = strlen(word);
    int count = 0;
    int first = -1;
    for (int i = 0; i + m <= n; i++) {
        int j = 0;
        while (j < m && tolower(text[i + j]) == tolower(word[j])) {
            j++;
        }
        if (j == m) {
            if (count == 0) {
                first = i + 1;
            }
            count++;
        }
    }
    printf("%d %d\n", count, first);
    return 0;
}
