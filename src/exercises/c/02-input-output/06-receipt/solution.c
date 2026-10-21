#include <stdio.h>

int main()
{
    char name1[11], name2[11], name3[11];
    int qty1, qty2, qty3;
    double price1, price2, price3;
    scanf("%s %d %lf", name1, &qty1, &price1);
    scanf("%s %d %lf", name2, &qty2, &price2);
    scanf("%s %d %lf", name3, &qty3, &price3);
    double amount1 = qty1 * price1;
    double amount2 = qty2 * price2;
    double amount3 = qty3 * price3;
    printf("%-10s%5s%12s\n", "Item", "Qty", "Amount");
    printf("%-10s%5d%12.2f\n", name1, qty1, amount1);
    printf("%-10s%5d%12.2f\n", name2, qty2, amount2);
    printf("%-10s%5d%12.2f\n", name3, qty3, amount3);
    printf("%-15s%12.2f\n", "Total", amount1 + amount2 + amount3);
    return 0;
}
