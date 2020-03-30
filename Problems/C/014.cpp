#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  int num = 1000005;
  vector<int> imos(num);
  rep(i, n) {
    int a, b;
    cin >> a >> b;
    imos[a]++;
    imos[b + 1]--;
  }
  int ans = 0;
  rep(i, num) {
    if(i > 0) imos[i] += imos[i - 1];
    ans = max(ans, imos[i]);
  }
  cout << ans << endl;
  return 0;
}
