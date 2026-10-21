#include <stdio.h>

int main()
{
    int collected, exam;
    scanf("%d %d", &collected, &exam);
    if (collected + exam >= 50) {
        printf("pass\n");
    } else {
        printf("fail\n");
    }
    return 0;
}
