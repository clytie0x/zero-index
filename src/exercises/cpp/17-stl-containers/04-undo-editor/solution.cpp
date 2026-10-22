#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    vector<string> text;
    stack<pair<char, string>> history;
    for (int i = 0; i < q; i++) {
        string command;
        cin >> command;
        if (command == "TYPE") {
            string word;
            cin >> word;
            text.push_back(word);
            history.push({'T', word});
        } else if (command == "DELETE") {
            if (!text.empty()) {
                history.push({'D', text.back()});
                text.pop_back();
            }
        } else if (command == "UNDO") {
            if (!history.empty()) {
                auto change = history.top();
                history.pop();
                if (change.first == 'T') {
                    text.pop_back();
                } else {
                    text.push_back(change.second);
                }
            }
        } else {
            if (text.empty()) {
                cout << "EMPTY\n";
            } else {
                cout << text.back() << '\n';
            }
        }
    }
    if (text.empty()) {
        cout << "EMPTY\n";
    }
    for (int i = 0; i < (int)text.size(); i++) {
        cout << text[i] << (i + 1 < (int)text.size() ? ' ' : '\n');
    }
    return 0;
}
