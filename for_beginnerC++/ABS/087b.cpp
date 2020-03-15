#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int a, b, c, x;
  cin >> a >> b >> c >> x;
  int ans = 0;
  rep(i, a + 1) {
    rep(j, b + 1) {
      rep(k, c + 1) {
        if(i * 500 + j * 100 + k * 50 == x) ans++;
      }
    }
  }
  cout << ans << endl;
}
