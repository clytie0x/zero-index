#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<long long> place(n), speed(n);
    for (int i = 0; i < n; i++) {
        cin >> place[i];
    }
    for (int i = 0; i < n; i++) {
        cin >> speed[i];
    }
    long long best_distance = 0, best_speed = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            long long distance = place[j] - place[i];
            long long together = speed[i] + speed[j];
            if (distance > 0 && distance * best_speed > best_distance * together) {
                best_distance = distance;
                best_speed = together;
            }
        }
    }
    cout << fixed << setprecision(4) << (double)best_distance / best_speed << '\n';
    return 0;
}
