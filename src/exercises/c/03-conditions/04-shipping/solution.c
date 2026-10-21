#include <stdio.h>

int main()
{
    int zone, weight;
    scanf("%d %d", &zone, &weight);
    int price;
    if (zone == 1) {
        if (weight <= 1000) {
            price = 30;
        } else if (weight <= 5000) {
            price = 50;
        } else {
            price = 80;
        }
    } else {
        if (weight <= 1000) {
            price = 45;
        } else if (weight <= 5000) {
            price = 70;
        } else {
            price = 110;
        }
    }
    printf("%d\n", price);
    return 0;
}
