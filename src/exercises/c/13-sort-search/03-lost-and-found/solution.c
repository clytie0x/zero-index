#include <stdio.h>

int code[1000];
int found[1000];

int main()
{
    int n, target;
    scanf("%d %d", &n, &target);
    for (int i = 0; i < n; i++) {
        scanf("%d", &code[i]);
    }
    int count = 0;
    for (int i = 0; i < n; i++) {
        if (code[i] == target) {
            found[count] = i + 1;
            count++;
        }
    }
    printf("%d\n", count);
    if (count > 0) {
        for (int i = 0; i < count; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", found[i]);
        }
        printf("\n");
    }
    return 0;
}
