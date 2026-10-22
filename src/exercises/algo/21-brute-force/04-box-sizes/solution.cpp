#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long volume;
    cin >> volume;
    long long sizes = 0;
    long long best = LLONG_MAX;
    for (long long a = 1; a * a * a <= volume; a++) {
        for (long long b = a; a * b * b <= volume; b++) {
            if (volume % (a * b) == 0) {
                long long c = volume / (a * b);
                sizes++;
                best = min(best, 2 * (a * b + b * c + c * a));
            }
        }
    }
    cout << sizes << ' ' << best << '\n';
    return 0;
}
