#include <stdio.h>

int main()
{
    int age;
    scanf("%d", &age);
    if (age < 3) {
        printf("0\n");
    } else if (age <= 12) {
        printf("60\n");
    } else if (age <= 59) {
        printf("120\n");
    } else {
        printf("60\n");
    }
    return 0;
}
