#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  string s;
  cin >> s;
  reverse(all(s));
  ll ans = 0;
  for(int tmp = 0; tmp < (1 << s.size() - 1); tmp++) {
    bitset<10> ss(tmp);
    ans += s[0] - '0';
    ll now = 1;
    for(int i = 0; i < s.size() - 1; i++) {
      if(ss.test(i)) {
        now = 1;
      } else {
        now *= 10;
      }
      ans += (s[i + 1] - '0') * now;
    }
  }
  cout << ans << endl;
}
