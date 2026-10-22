#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    deque<int> shelf;
    for (int k = 0; k < q; k++) {
        string command;
        cin >> command;
        if (command == "BAKE") {
            int x;
            cin >> x;
            shelf.push_back(x);
        } else if (command == "FOUND") {
            int x;
            cin >> x;
            shelf.push_front(x);
        } else if (command == "FRESH") {
            if (shelf.empty()) {
                cout << "EMPTY\n";
            } else {
                cout << shelf.back() << '\n';
                shelf.pop_back();
            }
        } else if (command == "SALE") {
            if (shelf.empty()) {
                cout << "EMPTY\n";
            } else {
                cout << shelf.front() << '\n';
                shelf.pop_front();
            }
        } else {
            int i;
            cin >> i;
            if (i > (int)shelf.size()) {
                cout << "NONE\n";
            } else {
                cout << shelf[i - 1] << '\n';
            }
        }
    }
    cout << shelf.size() << '\n';
    return 0;
}
