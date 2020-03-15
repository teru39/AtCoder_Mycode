#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()
int gcd(int a, int b) {
  if(b == 0) return a;
  return gcd(b, a % b);
}
int main() {
  int n, x;
  cin >> n >> x;
  int ans;
  cin >> ans;
  ans = abs(ans - x);
  rep(i, n - 1) {
    int a;
    cin >> a;
    a = abs(a - x);
    ans = gcd(ans, a);
  }
  cout << ans << endl;
}
