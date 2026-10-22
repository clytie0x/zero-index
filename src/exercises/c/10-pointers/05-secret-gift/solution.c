#include <stdio.h>
#include <stdlib.h>

int main()
{
    int rooms;
    scanf("%d", &rooms);
    for (int r = 0; r < rooms; r++) {
        int n;
        scanf("%d", &n);
        int *giver = malloc((n + 1) * sizeof(int));
        if (giver == NULL) {
            return 1;
        }
        for (int i = 1; i <= n; i++) {
            int drawn;
            scanf("%d", &drawn);
            giver[drawn] = i;
        }
        for (int j = 1; j <= n; j++) {
            printf("%d", giver[j]);
            if (j < n) {
                printf(" ");
            }
        }
        printf("\n");
        free(giver);
    }
    return 0;
}
