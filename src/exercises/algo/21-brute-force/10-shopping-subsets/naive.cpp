#include <bits/stdc++.h>
using namespace std;

int n;
long long budget;
vector<long long> price;
long long ways = 0;

void go(int i, long long sum)
{
    if (i == n) {
        if (sum <= budget) {
            ways++;
        }
        return;
    }
    go(i + 1, sum + price[i]);
    go(i + 1, sum);
}

int main()
{
    cin >> n >> budget;
    price.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    go(0, 0);
    cout << ways << '\n';
    return 0;
}
