#include <stdio.h>

int colors[1000000];

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &colors[i]);
    }
    for (int i = 0; i < n; i++) {
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (colors[j] == colors[i]) {
                count++;
            }
        }
        if (count % 2 == 1) {
            printf("%d\n", colors[i]);
            break;
        }
    }
    return 0;
}
