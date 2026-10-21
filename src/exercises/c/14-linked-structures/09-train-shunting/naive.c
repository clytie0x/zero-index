#include <stdio.h>

int train[300001];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    int length = n;
    for (int i = 0; i < n; i++) {
        train[i] = i + 1;
    }
    for (int k = 0; k < q; k++) {
        char command;
        scanf(" %c", &command);
        if (command == 'I') {
            int x, y;
            scanf("%d %d", &x, &y);
            int at = 0;
            if (x != 0) {
                while (train[at] != x) {
                    at++;
                }
                at++;
            }
            for (int i = length; i > at; i--) {
                train[i] = train[i - 1];
            }
            train[at] = y;
            length++;
        } else {
            int x;
            scanf("%d", &x);
            int at = 0;
            while (train[at] != x) {
                at++;
            }
            for (int i = at; i < length - 1; i++) {
                train[i] = train[i + 1];
            }
            length--;
        }
    }
    if (length == 0) {
        printf("EMPTY\n");
        return 0;
    }
    for (int i = 0; i < length; i++) {
        printf("%d", train[i]);
        if (i < length - 1) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
