#include <stdio.h>

int main()
{
    char line[1005];
    fgets(line, sizeof line, stdin);
    int upper = 0, lower = 0, digits = 0, spaces = 0;
    for (int i = 0; line[i] != '\0'; i++) {
        char c = line[i];
        if (c >= 'A' && c <= 'Z') {
            upper++;
        } else if (c >= 'a' && c <= 'z') {
            lower++;
        } else if (c >= '0' && c <= '9') {
            digits++;
        } else if (c == ' ') {
            spaces++;
        }
    }
    printf("%d %d %d %d\n", upper, lower, digits, spaces);
    return 0;
}
