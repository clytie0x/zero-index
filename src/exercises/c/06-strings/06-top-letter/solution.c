#include <stdio.h>
#include <ctype.h>

char line[100005];

int main()
{
    int count[26] = {0};
    fgets(line, sizeof line, stdin);
    for (int i = 0; line[i] != '\0'; i++) {
        if (isalpha(line[i])) {
            count[tolower(line[i]) - 'a']++;
        }
    }
    int best = 0;
    for (int i = 1; i < 26; i++) {
        if (count[i] > count[best]) {
            best = i;
        }
    }
    printf("%c %d\n", 'a' + best, count[best]);
    return 0;
}
