#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char key[100000][9];

void sort_letters(char s[])
{
    int length = strlen(s);
    for (int i = 1; i < length; i++) {
        char letter = s[i];
        int j = i - 1;
        while (j >= 0 && s[j] > letter) {
            s[j + 1] = s[j];
            j--;
        }
        s[j + 1] = letter;
    }
}

int compare_key(const void *p, const void *q)
{
    return strcmp((const char *)p, (const char *)q);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", key[i]);
        sort_letters(key[i]);
    }
    qsort(key, n, sizeof(key[0]), compare_key);
    long long pairs = 0;
    int start = 0;
    for (int i = 1; i <= n; i++) {
        if (i == n || strcmp(key[i], key[i - 1]) != 0) {
            long long size = i - start;
            pairs += size * (size - 1) / 2;
            start = i;
        }
    }
    printf("%lld\n", pairs);
    return 0;
}
