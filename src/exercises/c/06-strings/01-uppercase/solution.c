#include <stdio.h>

int main()
{
    char word[105];
    scanf("%s", word);
    for (int i = 0; word[i] != '\0'; i++) {
        if (word[i] >= 'a' && word[i] <= 'z') {
            word[i] = word[i] - 'a' + 'A';
        }
    }
    printf("%s\n", word);
    return 0;
}
