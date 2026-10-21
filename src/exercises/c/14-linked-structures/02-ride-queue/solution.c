#include <stdio.h>
#include <string.h>

int queue[100000];
int head = 0, tail = 0;

int main()
{
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        char command[6];
        scanf("%5s", command);
        if (strcmp(command, "JOIN") == 0) {
            int ticket;
            scanf("%d", &ticket);
            queue[tail] = ticket;
            tail++;
        } else if (strcmp(command, "RIDE") == 0) {
            int seats;
            scanf("%d", &seats);
            if (head == tail) {
                printf("EMPTY\n");
                continue;
            }
            int boarded = 0;
            while (boarded < seats && head < tail) {
                if (boarded > 0) {
                    printf(" ");
                }
                printf("%d", queue[head]);
                head++;
                boarded++;
            }
            printf("\n");
        } else {
            printf("%d\n", tail - head);
        }
    }
    return 0;
}
