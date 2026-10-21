#include <stdio.h>
#include <string.h>

char card[100000][11];

int should_swap(const char *a, const char *b)
{
    char ab[21], ba[21];
    strcpy(ab, a);
    strcat(ab, b);
    strcpy(ba, b);
    strcat(ba, a);
    return strcmp(ba, ab) > 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", card[i]);
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (should_swap(card[j], card[j + 1])) {
                char temp[11];
                strcpy(temp, card[j]);
                strcpy(card[j], card[j + 1]);
                strcpy(card[j + 1], temp);
            }
        }
    }
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
