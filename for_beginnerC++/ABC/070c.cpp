#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()
ll gcd(ll a, ll b) {
  if(b == 0) return a;
  return gcd(b, a % b);
}
ll lcm(ll a, ll b) {
  ll g = gcd(a, b);
  return a / g * b;
}
int main() {
  int n;
  cin >> n;
  ll ans = 1LL;
  rep(i, n) {
    ll a;
    cin >> a;
    ans = lcm(ans, a);
  }

  cout << ans << endl;
}
