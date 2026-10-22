#include <stdio.h>

int words[100000];
int start[100001];
int count[100001];

int main()
{
    int shelves;
    scanf("%d", &shelves);
    int used = 0;
    for (int s = 1; s <= shelves; s++) {
        scanf("%d", &count[s]);
        start[s] = used;
        for (int i = 0; i < count[s]; i++) {
            scanf("%d", &words[used]);
            used++;
        }
    }
    int q;
    scanf("%d", &q);
    for (int i = 0; i < q; i++) {
        int s, a, b;
        scanf("%d %d %d", &s, &a, &b);
        long long sum = 0;
        for (int j = a; j <= b; j++) {
            sum += words[start[s] + j - 1];
        }
        printf("%lld\n", sum);
    }
    return 0;
}
