#include <stdio.h>
#include <string.h>

int deck[100000];
int capacity = 100000;
int head = 0, tail = 0, count = 0;

int main()
{
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        char command[11];
        scanf("%10s", command);
        if (strcmp(command, "TOP") == 0) {
            int card;
            scanf("%d", &card);
            head = (head - 1 + capacity) % capacity;
            deck[head] = card;
            count++;
        } else if (strcmp(command, "BOTTOM") == 0) {
            int card;
            scanf("%d", &card);
            deck[tail] = card;
            tail = (tail + 1) % capacity;
            count++;
        } else if (count == 0) {
            printf("EMPTY\n");
        } else if (strcmp(command, "DRAWTOP") == 0) {
            printf("%d\n", deck[head]);
            head = (head + 1) % capacity;
            count--;
        } else {
            tail = (tail - 1 + capacity) % capacity;
            printf("%d\n", deck[tail]);
            count--;
        }
    }
    if (count == 0) {
        printf("EMPTY\n");
    } else {
        for (int i = 0; i < count; i++) {
            if (i > 0) {
                printf(" ");
            }
            printf("%d", deck[(head + i) % capacity]);
        }
        printf("\n");
    }
    return 0;
}
