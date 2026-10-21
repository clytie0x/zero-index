#include <bits/stdc++.h>
using namespace std;

string banned[100];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    cin >> k;
    for (int i = 0; i < k; i++) {
        cin >> banned[i];
    }
    cin.ignore(1000000, '\n');
    string text;
    getline(cin, text);
    int n = text.size();
    int i = 0;
    while (i < n) {
        if (text[i] == ' ') {
            i++;
            continue;
        }
        int j = i;
        while (j < n && text[j] != ' ') {
            j++;
        }
        string word = text.substr(i, j - i);
        bool hide = false;
        for (int b = 0; b < k; b++) {
            if (word == banned[b]) {
                hide = true;
            }
        }
        if (hide) {
            for (int p = i; p < j; p++) {
                text[p] = '*';
            }
        }
        i = j;
    }
    cout << text << '\n';
    return 0;
}
