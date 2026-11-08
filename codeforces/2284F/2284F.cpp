#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const ll MOD = 1e9 + 7;

ll pw(ll b, ll e) {                       // fast power: b^e mod MOD
    ll r = 1; b %= MOD;
    while (e) { if (e & 1) r = r * b % MOD; b = b * b % MOD; e >>= 1; }
    return r;
}

int main() {
    int T; scanf("%d", &T);
    const int N = 500005;
    vector<ll> ip(N);                     // ip[i] = (1/2)^i mod MOD
    ll inv2 = (MOD + 1) / 2;
    ip[0] = 1;
    for (int i = 1; i < N; i++) ip[i] = ip[i-1] * inv2 % MOD;

    while (T--) {
        int n; static char buf[N];
        scanf("%d %s", &n, buf);
        string s(buf);
        if (n == 1) { puts("0"); continue; }   // no steps, score is 0

        int cnt = 0;                      // how many 1s are in S
        for (char c : s) cnt += (c == '1');

        // g = fraction of supersets that "hit" a group of numbers.
        // If the group already contains a number from S, it's always hit (1).
        // Otherwise all its numbers are optional, and the chance at least one is picked
        // is 1 - (1/2)^size.
        auto g = [&](bool hit, int sz) -> ll {
            return hit ? 1 : (1 - ip[sz] + MOD) % MOD;
        };

        // For each step j, the starting numbers that end up as value 0 (Z) or the top value (W).
        // hz/sz = "does it contain a number from S" / "how many numbers"
        // hu/su = same for the union U = Z + W
        vector<char> hz(n), hw(n), hu(n);
        vector<int>  sz(n), sw(n), su(n);

        hz[0] = s[0] == '1';     sz[0] = 1;
        hw[0] = s[n-1] == '1';   sw[0] = 1;
        hu[0] = hz[0] | hw[0];   su[0] = 2;

        for (int j = 1; j <= n - 1; j++) {
            int h = 2*j - n;
            if (h >= 0) { hz[j] = hu[h]; sz[j] = su[h]; }           // built from an earlier U
            else        { hz[j] = s[n-2*j] == '1'; sz[j] = 1; }     // a single original number
            if (j <= n - 2) {
                int h1 = 2*j + 1 - n;
                if (h1 >= 0) { hw[j] = hu[h1]; sw[j] = su[h1]; }
                else         { hw[j] = s[n-1-2*j] == '1'; sw[j] = 1; }
                hu[j] = hz[j] | hw[j];
                su[j] = sz[j] + sw[j];
            }
        }

        // Prefix products of a_t = g(U_t), their inverses, and prefix sums of inverses.
        // (arrays are shifted by 1 so index -1 becomes 0)
        vector<ll> A(n+1), IA(n+1), SIA(n+2), B(n+1), SB(n+1);
        A[0] = 1; IA[0] = 1;
        for (int t = 0; t <= n - 2; t++) {
            ll a = g(hu[t], su[t]);
            A[t+1]  = A[t]  * a % MOD;
            IA[t+1] = IA[t] * pw(a, MOD - 2) % MOD;
        }
        SIA[0] = 0;
        for (int i = 0; i <= n - 1; i++) SIA[i+1] = (SIA[i] + IA[i]) % MOD;

        // b_x = g({x}) for a single number x: 1 if x is in S, otherwise 1/2
        B[0] = 1; SB[0] = 0;
        for (int x = 1; x <= n - 1; x++) {
            ll b = (s[x] == '1') ? 1 : inv2;
            B[x]  = B[x-1] * b % MOD;
            SB[x] = (SB[x-1] + B[x]) % MOD;
        }

        // For each step j, add up the expected mex over all values of k using the prefix tricks
        ll tot = 0;
        for (int j = 1; j <= n - 1; j++) {
            int lim = n - j - 1;                  // largest value that can still exist
            int M = min(lim, j);
            ll Aj = A[j];
            ll sum = (SIA[j+1] - SIA[j-M] + MOD) % MOD * Aj % MOD;   // part from a_t
            if (lim > j) sum = (sum + Aj * SB[lim - j]) % MOD;       // part from single numbers
            tot = (tot + g(hz[j], sz[j]) * sum) % MOD;
        }

        // 2^(number of optional numbers) = total supersets, we worked with fractions
        printf("%lld\n", tot * pw(2, n - cnt) % MOD);
    }
}
