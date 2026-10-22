#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<pair<int, int>> students(n);
    for (int i = 0; i < n; i++) {
        int first_day, last_day;
        cin >> first_day >> last_day;
        students[i] = {last_day, first_day};
    }
    sort(students.begin(), students.end());
    int sessions = 0, last_session = 0;
    for (int i = 0; i < n; i++) {
        if (students[i].second > last_session) {
            sessions++;
            last_session = students[i].first;
        }
    }
    cout << sessions << '\n';
    return 0;
}
