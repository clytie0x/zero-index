#include <stdio.h>
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

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", key[i]);
        sort_letters(key[i]);
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (strcmp(key[j], key[j + 1]) > 0) {
                char temp[9];
                strcpy(temp, key[j]);
                strcpy(key[j], key[j + 1]);
                strcpy(key[j + 1], temp);
            }
        }
    }
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
