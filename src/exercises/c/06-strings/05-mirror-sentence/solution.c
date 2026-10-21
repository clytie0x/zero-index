#include <stdio.h>
#include <ctype.h>

char line[100005];
char letters[100005];

int main()
{
    fgets(line, sizeof line, stdin);
    int length = 0;
    for (int i = 0; line[i] != '\0'; i++) {
        if (isalpha(line[i])) {
            letters[length] = tolower(line[i]);
            length++;
        }
    }
    int is_palindrome = 1;
    for (int i = 0; i < length / 2; i++) {
        if (letters[i] != letters[length - 1 - i]) {
            is_palindrome = 0;
        }
    }
    if (is_palindrome) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}
