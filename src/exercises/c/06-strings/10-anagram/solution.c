#include <stdio.h>

char first[100005], second[100005];

int main()
{
    scanf("%s %s", first, second);
    int count[26] = {0};
    for (int i = 0; first[i] != '\0'; i++) {
        count[first[i] - 'a']++;
    }
    for (int i = 0; second[i] != '\0'; i++) {
        count[second[i] - 'a']--;
    }
    int same = 1;
    for (int i = 0; i < 26; i++) {
        if (count[i] != 0) {
            same = 0;
        }
    }
    if (same) {
        printf("YES\n");
    } else {
        printf("NO\n");
    }
    return 0;
}
