#include <bits/stdc++.h>
using namespace std;

int n;
long long budget;
vector<long long> price;
long long ways = 0;

void search(int i, long long sum)
{
    if (i == n) {
        if (sum <= budget) {
            ways++;
        }
        return;
    }
    search(i + 1, sum + price[i]);
    search(i + 1, sum);
}

int main()
{
    cin >> n >> budget;
    price.resize(n);
    for (int i = 0; i < n; i++) {
        cin >> price[i];
    }
    search(0, 0);
    cout << ways << '\n';
    return 0;
}
