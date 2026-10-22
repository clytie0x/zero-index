#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    priority_queue<int> parcels;
    for (int i = 0; i < q; i++) {
        char op;
        cin >> op;
        if (op == '+') {
            int weight;
            cin >> weight;
            parcels.push(weight);
        } else if (parcels.empty()) {
            cout << "EMPTY\n";
        } else {
            cout << parcels.top() << '\n';
            parcels.pop();
        }
    }
    return 0;
}
