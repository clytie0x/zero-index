#include <bits/stdc++.h>
using namespace std;

struct Student {
    string name;
    int room;
    int score;
};

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<Student> list(n);
    for (Student &s : list) {
        cin >> s.name >> s.room >> s.score;
    }
    stable_sort(list.begin(), list.end(), [](const Student &a, const Student &b) {
        if (a.room != b.room) {
            return a.room < b.room;
        }
        return a.score > b.score;
    });
    for (const Student &s : list) {
        cout << s.room << ' ' << s.name << ' ' << s.score << '\n';
    }
    return 0;
}
