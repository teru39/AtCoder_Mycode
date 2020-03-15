#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, a, b;
  cin >> n >> a >> b;
  int ans = 0;

  for(int i = 1; i <= n; i++) {
    string si = to_string(i);
    int sum = 0;
    rep(j, si.size()) {
      sum += (int)(si[j] - '0');
    }
    if(a <= sum && sum <= b) ans += i;
  }
  cout << ans << endl;
}
