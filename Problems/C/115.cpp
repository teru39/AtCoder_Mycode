#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n, k;
  cin >> n >> k;
  vector<int> v(n);
  rep(i, n) {
    cin >> v[i];
  }

  sort(all(v));
  int left = 0;
  int right = k - 1;
  int ans = 1101101101;
  for(int i = 0; i <= n - k; i++) {
    ans = min(ans, v[right] - v[left]);
    right++;
    left++;
  }
  cout << ans << endl;
}
