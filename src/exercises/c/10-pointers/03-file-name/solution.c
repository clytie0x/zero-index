#include <stdio.h>

char *find_last(char *s, char c)
{
    char *found = NULL;
    for (char *p = s; *p != '\0'; p++) {
        if (*p == c) {
            found = p;
        }
    }
    return found;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        char path[105];
        scanf("%s", path);
        char *name = path;
        char *slash = find_last(path, '/');
        if (slash != NULL) {
            name = slash + 1;
        }
        char *dot = find_last(name, '.');
        if (dot == NULL) {
            printf("%s -\n", name);
        } else {
            *dot = '\0';
            printf("%s %s\n", name, dot + 1);
        }
    }
    return 0;
}
