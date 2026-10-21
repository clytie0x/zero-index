#include <stdio.h>
#include <string.h>

int stack[100000];
int size = 0;

int main()
{
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        char command[5];
        scanf("%4s", command);
        if (strcmp(command, "PUSH") == 0) {
            int dish;
            scanf("%d", &dish);
            stack[size] = dish;
            size++;
        } else if (strcmp(command, "POP") == 0) {
            if (size == 0) {
                printf("EMPTY\n");
            } else {
                size--;
                printf("%d\n", stack[size]);
            }
        } else if (strcmp(command, "TOP") == 0) {
            if (size == 0) {
                printf("EMPTY\n");
            } else {
                printf("%d\n", stack[size - 1]);
            }
        } else {
            printf("%d\n", size);
        }
    }
    return 0;
}
