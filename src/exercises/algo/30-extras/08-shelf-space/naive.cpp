#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> space(n + 1);
    for (int i = 1; i <= n; i++) {
        cin >> space[i];
    }
    for (int j = 0; j < q; j++) {
        int box;
        cin >> box;
        int shelf = 0;
        for (int i = 1; i <= n; i++) {
            if (space[i] >= box) {
                shelf = i;
                break;
            }
        }
        if (shelf > 0) {
            space[shelf] -= box;
        }
        cout << shelf << '\n';
    }
    return 0;
}
