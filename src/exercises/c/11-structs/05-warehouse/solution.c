#include <stdio.h>
#include <string.h>

typedef struct {
    char code[11];
    int quantity;
    int price;
} Item;

Item items[100];

int find_item(const char code[], int m)
{
    for (int i = 0; i < m; i++) {
        if (strcmp(items[i].code, code) == 0) {
            return i;
        }
    }
    return -1;
}

int main()
{
    int m, q;
    scanf("%d %d", &m, &q);
    for (int i = 0; i < m; i++) {
        scanf("%s %d %d", items[i].code, &items[i].quantity, &items[i].price);
    }
    int rejected = 0;
    for (int k = 0; k < q; k++) {
        char type[4], code[11];
        int amount;
        scanf("%s %s %d", type, code, &amount);
        Item *item = &items[find_item(code, m)];
        if (strcmp(type, "IN") == 0) {
            item->quantity += amount;
        } else if (item->quantity >= amount) {
            item->quantity -= amount;
        } else {
            rejected++;
        }
    }
    long long total = 0;
    for (int i = 0; i < m; i++) {
        printf("%s %d\n", items[i].code, items[i].quantity);
        total += (long long)items[i].quantity * items[i].price;
    }
    printf("%lld\n", total);
    printf("%d\n", rejected);
    return 0;
}
