#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) {
    cin >> a[i];
  }
  int ans = 0;
  bool end = false;
  while(1) {
    rep(i, n) {
      if(a[i] % 2 == 1) {
        end = true;
        break;
      }
      a[i] /= 2;
    }
    if(end) break;
    ans++;
  }
  cout << ans << endl;
}
