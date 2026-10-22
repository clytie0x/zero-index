#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    stack<string> basket;
    for (int i = 0; i < q; i++) {
        string command;
        cin >> command;
        if (command == "RETURN") {
            string title;
            cin >> title;
            basket.push(title);
        } else if (command == "SHELVE") {
            int k;
            cin >> k;
            if (basket.empty()) {
                cout << "EMPTY\n";
            } else {
                for (int j = 0; j < k && !basket.empty(); j++) {
                    if (j > 0) {
                        cout << ' ';
                    }
                    cout << basket.top();
                    basket.pop();
                }
                cout << '\n';
            }
        } else {
            if (basket.empty()) {
                cout << "EMPTY\n";
            } else {
                cout << basket.top() << '\n';
            }
        }
    }
    cout << basket.size() << '\n';
    return 0;
}
