#include <stdio.h>

int count[101];

int main()
{
    int n, q;
    scanf("%d %d", &n, &q);
    for (int i = 0; i < n; i++) {
        int score;
        scanf("%d", &score);
        count[score]++;
    }
    for (int i = 0; i < q; i++) {
        int k;
        scanf("%d", &k);
        int passed = 0;
        int score = 100;
        while (passed + count[score] < k) {
            passed += count[score];
            score--;
        }
        printf("%d\n", score);
    }
    return 0;
}
