#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long volume;
    cin >> volume;
    long long sizes = 0;
    long long best = LLONG_MAX;
    for (long long a = 1; a <= volume; a++) {
        for (long long b = a; a * b <= volume; b++) {
            if (volume % (a * b) == 0) {
                long long c = volume / (a * b);
                if (c >= b) {
                    sizes++;
                    best = min(best, 2 * (a * b + b * c + c * a));
                }
            }
        }
    }
    cout << sizes << ' ' << best << '\n';
    return 0;
}
