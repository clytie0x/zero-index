#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    long long tickets;
    int q;
    cin >> tickets >> q;
    queue<pair<string, int>> line;
    for (int i = 0; i < q; i++) {
        string command;
        cin >> command;
        if (command == "JOIN") {
            string name;
            int want;
            cin >> name >> want;
            line.push({name, want});
        } else if (command == "SELL") {
            if (line.empty()) {
                cout << "EMPTY\n";
            } else {
                auto fan = line.front();
                line.pop();
                long long got = min((long long)fan.second, tickets);
                tickets -= got;
                cout << fan.first << ' ' << got << '\n';
            }
        } else if (command == "LAST") {
            if (line.empty()) {
                cout << "EMPTY\n";
            } else {
                cout << line.back().first << '\n';
            }
        } else {
            cout << line.size() << ' ' << tickets << '\n';
        }
    }
    return 0;
}
