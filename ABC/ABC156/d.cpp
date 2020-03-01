#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

ll cmb(int n, int k, int mod) {
  int numerator = 1;
  for(int i = 0; i < k; i++) {
    numerator = (numerator * (n - i)) % mod;
  }
  int denominator = 1;
  for(int i = 1; i < k + 1; i++) {
    denominator = (denominator * i) % mod;
  }
  return (numerator * pow(denominator, mod - 2)) % mod;
}

ll myPow(ll x, ll n, ll m) {
  if(n == 0) return 1;
  if(n % 2 == 0)
    return myPow(x * x % m, n / 2, m);
  else
    return x * myPow(x, n - 1, m) % m;
}



ll mod = 100000000 + 7;
int main() {
  int n, a, b;
  cin >> n >> a >> b;

  cout << myPow(2, n, mod) -  << endl;
}
