#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    multiset<int> books;
    for (int i = 0; i < n; i++) {
        int price;
        cin >> price;
        books.insert(price);
    }
    for (int j = 0; j < m; j++) {
        int budget;
        cin >> budget;
        auto it = books.upper_bound(budget);
        if (it == books.begin()) {
            cout << -1 << '\n';
        } else {
            it = prev(it);
            cout << *it << '\n';
            books.erase(it);
        }
    }
    return 0;
}
