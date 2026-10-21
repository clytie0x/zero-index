#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct contestant {
    char name[11];
    int solved;
    int penalty;
};

struct contestant list[50000];

int compare_rank(const void *p, const void *q)
{
    const struct contestant *a = p;
    const struct contestant *b = q;
    if (a->solved != b->solved) {
        return a->solved > b->solved ? -1 : 1;
    }
    if (a->penalty != b->penalty) {
        return a->penalty < b->penalty ? -1 : 1;
    }
    return strcmp(a->name, b->name);
}

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s %d %d", list[i].name, &list[i].solved, &list[i].penalty);
    }
    qsort(list, n, sizeof(list[0]), compare_rank);
    int rank = 0;
    for (int i = 0; i < n; i++) {
        if (i == 0 || list[i].solved != list[i - 1].solved || list[i].penalty != list[i - 1].penalty) {
            rank = i + 1;
        }
        printf("%d %s\n", rank, list[i].name);
    }
    return 0;
}
