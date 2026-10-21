#include <stdio.h>
#include <string.h>

int main()
{
    int n;
    char name[25], first[25], last[25];
    scanf("%d", &n);
    scanf("%s", name);
    strcpy(first, name);
    strcpy(last, name);
    for (int i = 1; i < n; i++) {
        scanf("%s", name);
        if (strcmp(name, first) < 0) {
            strcpy(first, name);
        }
        if (strcmp(name, last) > 0) {
            strcpy(last, name);
        }
    }
    printf("%s\n%s\n", first, last);
    return 0;
}
