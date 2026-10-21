#include <stdio.h>

int main()
{
    char names[7][10] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
    long long today, shift;
    scanf("%lld %lld", &today, &shift);
    long long day = ((today + shift) % 7 + 7) % 7;
    printf("%s\n", names[day]);
    return 0;
}
