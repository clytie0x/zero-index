#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<int> parcels;
    for (int i = 0; i < q; i++) {
        char op;
        cin >> op;
        if (op == '+') {
            int weight;
            cin >> weight;
            parcels.push_back(weight);
        } else if (parcels.empty()) {
            cout << "EMPTY\n";
        } else {
            int best = 0;
            for (int j = 1; j < (int)parcels.size(); j++) {
                if (parcels[j] > parcels[best]) {
                    best = j;
                }
            }
            cout << parcels[best] << '\n';
            parcels.erase(parcels.begin() + best);
        }
    }
    return 0;
}
