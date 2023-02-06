#include    <bits/stdc++.h>
#pragma comment(linker, "/STACK:268435456")
#define __unique(V) (V).resize(unique((V).begin(),(V).end())-(V).begin())
#define cntbit(X)   __builtin_popcount((X))
#define bit(S,i) (((S)>>(i))&1)
#define    first_bit(S) (__builtin_ctz((S)))
#define PI    acos(-1)
#define fi  first
#define se  second
#define LL  long long
#define ii  pair<int,int>
#define iii pair<int,ii>
#define eb  emplace_back
#define lch ((k) << 1)
#define rch ((k) << 11)
#define _abs(x) ((x) > 0 ? (x) : -(x))
#define TASK "dp_solution"
using namespace std;
mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());
const int N = 205;
int dp[N][N][N];
int c[N], a[N], f[N], m[N];
int n, A, C;
///--------------------------
void    maximize(int &u,int v){
    u = max(u, v);
}
///--------------------------
int     main(){
    ///
        srand(time(NULL));
        ios::sync_with_stdio(0);
        cin.tie(0);cout.tie(0);
        #ifdef TLH2203
            freopen(TASK".inp", "r", stdin);
            freopen(TASK".out", "w", stdout);
        #endif // TLH2203
    ///

    cin >> n >> A >> C;
    for(int i = 1; i <= n; ++i){
        cin >> c[i];
    }

    for(int i = 1; i <= n; ++i){
        cin >> a[i];
    }

    for(int i = 1; i <= n; ++i){
        cin >> f[i];
    }

    for(int i = 1; i <= n; ++i){
        cin >> m[i];
    }

    memset(dp,-1,sizeof(dp));
    dp[0][0][0] = 0;

    for(int i = 0; i < n; ++i){
        for(int x = 0; x <= A; ++x){
            for(int y = 0; y <= C; ++y) if (dp[i][x][y] >= 0){
                maximize(dp[i + 1][x][y], dp[i][x][y]);
                for(int t = m[i + 1];
                        t * a[i + 1] + x <= A && t * c[i + 1] + y <= C; ++t){
                            maximize(dp[i + 1][t * a[i + 1] + x][t * c[i + 1] + y],
                                     dp[i][x][y] + t * f[i + 1]);
                        }
            }
        }
    }

    int _x = 0;
    int _y = 0;

    for(int x = 0; x <= A; ++x){
        for(int y = 0; y <= C; ++y) if (dp[n][x][y] > dp[n][_x][_y]){
            _x = x;
            _y = y;
        }
    }

    cout << dp[n][_x][_y] << '\n';

    vector <int> consume_volumn(n + 5, 0);

    int _n = n;

    while (_n > 0){
        if (dp[_n][_x][_y] == dp[_n - 1][_x][_y]){
            consume_volumn[_n] = 0;
            _n--;
            continue;
        }

        for(int t = m[_n]; _x - t * a[_n] >= 0 && _y - t * c[_n] >= 0; ++t){
            if (dp[_n][_x][_y] == dp[_n - 1][_x - t * a[_n]][_y - t * c[_n]] + t * f[_n]){
                _x -= t * a[_n];
                _y -= t * c[_n];
                consume_volumn[_n] = t;
                _n--;
                break;
            }
        }
    }

    for(int i = 1; i <= n; ++i){
        cout << consume_volumn[i] << '\n';
    }


}





