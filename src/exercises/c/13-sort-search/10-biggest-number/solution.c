#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char card[100000][11];

int compare_card(const void *p, const void *q)
{
    const char *a = p;
    const char *b = q;
    char ab[21], ba[21];
    strcpy(ab, a);
    strcat(ab, b);
    strcpy(ba, b);
    strcat(ba, a);
    return strcmp(ba, ab);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", card[i]);
    }
    qsort(card, n, sizeof(card[0]), compare_card);
    if (strcmp(card[0], "0") == 0) {
        printf("0\n");
        return 0;
    }
    for (int i = 0; i < n; i++) {
        printf("%s", card[i]);
    }
    printf("\n");
    return 0;
}
