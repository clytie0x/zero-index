#include <stdio.h>

char line[100005];

int main()
{
    fgets(line, sizeof line, stdin);
    int words = 0, current = 0, longest = 0;
    for (int i = 0; line[i] != '\0'; i++) {
        if (line[i] >= 'a' && line[i] <= 'z') {
            if (current == 0) {
                words++;
            }
            current++;
            if (current > longest) {
                longest = current;
            }
        } else {
            current = 0;
        }
    }
    printf("%d %d\n", words, longest);
    return 0;
}
