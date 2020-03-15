#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, k;
  cin >> n >> k;
  double ans = 0.0;

  for(int i = 1; i <= n; i++) {
    int now = i;
    double tmp = 1.0;
    while(now < k) {
      tmp /= 2;
      now *= 2;
    }
    ans += tmp;
  }
  printf("%.12lf\n",ans/n);
}
