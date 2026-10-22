#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin >> q;
    stack<string> back_pages, forward_pages;
    string current = "home";
    for (int i = 0; i < q; i++) {
        string command;
        cin >> command;
        if (command == "VISIT") {
            string page;
            cin >> page;
            back_pages.push(current);
            current = page;
            while (!forward_pages.empty()) {
                forward_pages.pop();
            }
        } else if (command == "BACK") {
            if (!back_pages.empty()) {
                forward_pages.push(current);
                current = back_pages.top();
                back_pages.pop();
            }
        } else {
            if (!forward_pages.empty()) {
                back_pages.push(current);
                current = forward_pages.top();
                forward_pages.pop();
            }
        }
        cout << current << '\n';
    }
    return 0;
}
