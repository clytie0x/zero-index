#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    vector<int> house(n);
    for (int &x : house) {
        cin >> x;
    }
    for (int i = 0; i < q; i++) {
        int left, right;
        cin >> left >> right;
        int count = 0;
        for (int x : house) {
            if (left <= x && x <= right) {
                count++;
            }
        }
        cout << count << '\n';
    }
    return 0;
}
