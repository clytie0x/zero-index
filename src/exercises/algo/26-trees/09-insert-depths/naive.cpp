#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> key(n), left(n, -1), right(n, -1);
    for (int i = 0; i < n; i++) {
        cin >> key[i];
        int d = 0;
        if (i > 0) {
            int cur = 0;
            while (true) {
                d++;
                int &next = (key[i] < key[cur]) ? left[cur] : right[cur];
                if (next == -1) {
                    next = i;
                    break;
                }
                cur = next;
            }
        }
        if (i > 0) {
            cout << ' ';
        }
        cout << d;
    }
    cout << '\n';
    return 0;
}
