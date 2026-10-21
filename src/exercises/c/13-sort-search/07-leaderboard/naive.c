#include <stdio.h>
#include <string.h>

struct contestant {
    char name[11];
    int solved;
    int penalty;
};

struct contestant list[50000];

int comes_after(struct contestant a, struct contestant b)
{
    if (a.solved != b.solved) {
        return a.solved < b.solved;
    }
    if (a.penalty != b.penalty) {
        return a.penalty > b.penalty;
    }
    return strcmp(a.name, b.name) > 0;
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s %d %d", list[i].name, &list[i].solved, &list[i].penalty);
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (comes_after(list[j], list[j + 1])) {
                struct contestant temp = list[j];
                list[j] = list[j + 1];
                list[j + 1] = temp;
            }
        }
    }
    int rank = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || list[i].solved != list[i - 1].solved || list[i].penalty != list[i - 1].penalty) {
            rank = i + 1;
        }
        printf("%d %s\n", rank, list[i].name);
    }
    return 0;
}
