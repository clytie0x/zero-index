#include <stdio.h>
#include <string.h>

char first[100005], second[100005];
int used[100005];

int main()
{
    scanf("%s %s", first, second);
    int length = strlen(first);
    if (length != (int)strlen(second)) {
        printf("NO\n");
        return 0;
    }
    int same = 1;
    for (int i = 0; i < length; i++) {
        int found = 0;
        for (int j = 0; j < length && !found; j++) {
            if (!used[j] && second[j] == first[i]) {
                used[j] = 1;
                found = 1;
            }
        }
        if (!found) {
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
