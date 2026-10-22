#include <stdio.h>

char line[1005];

void tidy(char *s)
{
    char *write = s;
    for (char *read = s; *read != '\0'; read++) {
        if (*read != ' ') {
            *write = *read;
            write++;
        } else if (write > s && *(write - 1) != ' ') {
            *write = ' ';
            write++;
        }
    }
    if (write > s && *(write - 1) == ' ') {
        write--;
    }
    *write = '\0';
}

int main()
{
    fgets(line, sizeof line, stdin);
    for (char *p = line; *p != '\0'; p++) {
        if (*p == '\n' || *p == '\r') {
            *p = '\0';
        }
    }
    tidy(line);
    printf("%s\n", line);
    return 0;
}
