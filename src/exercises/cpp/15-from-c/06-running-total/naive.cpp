#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    long long total = 0;
    long long lowest = 0;
    for (int i = 0; i < n; i++) {
        int amount;
        cin >> amount;
        total += amount;
        if (i == 0 || total < lowest) {
            lowest = total;
        }
        cout << total << ' ' << lowest << endl;
    }
    return 0;
}
