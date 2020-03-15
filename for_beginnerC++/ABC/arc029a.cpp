#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<int> niku(n);
  rep(i, n) {
    cin >> niku[i];
  }
  int ans = 1001001001;
  for(int tmp = 0; tmp < (1 << n); tmp++) {
    bitset<4> ss(tmp);
    int ans1 = 0;
    int ans2 = 0;
    for(int i = 0; i < n; i++) {
      if(ss.test(i))
        ans1 += niku[i];
      else
        ans2 += niku[i];
    }
    ans = min(ans, max(ans1, ans2));
  }
  cout << ans << endl;
}
