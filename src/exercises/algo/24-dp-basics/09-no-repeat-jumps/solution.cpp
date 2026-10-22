#include <bits/stdc++.h>
using namespace std;

const int MOD = 1000000007;

int main()
{
    int n;
    cin >> n;
    // ways[j][i] คือจำนวนวิธีไปหยุดที่ขั้น i โดยก้าวสุดท้ายยาว j ขั้น
    vector<vector<long long>> ways(4, vector<long long>(n + 1, 0));
    for (int i = 1; i <= n; i++) {
        for (int jump = 1; jump <= 3 && jump <= i; jump++) {
            int from = i - jump;
            long long total = 0;
            if (from == 0) {
                total = 1;
            } else {
                for (int last = 1; last <= 3; last++) {
                    if (last != jump) {
                        total += ways[last][from];
                    }
                }
            }
            ways[jump][i] = total % MOD;
        }
    }
    cout << (ways[1][n] + ways[2][n] + ways[3][n]) % MOD << '\n';
    return 0;
}
