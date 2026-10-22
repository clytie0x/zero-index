#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> line;
    for (int i = 0; i < n; i++) {
        int type;
        cin >> type;
        if (type == 1) {
            int x;
            cin >> x;
            line.push_back(x);
        } else if (line.empty()) {
            cout << "empty\n";
        } else {
            cout << line.front() << '\n';
            line.erase(line.begin());
        }
    }
    return 0;
}
