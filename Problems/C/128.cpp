#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> P;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int N, M;
  cin >> N >> M;
  vector<int> a(N);
  rep(i, M) {
    int k;
    cin >> k;
    rep(j, k) {
      int s;
      cin >> s;
      s--;
      a[s] |= 1 << i;
    }
  }
  int p = 0;
  rep(i, M) {
    int x;
    cin >> x;
    p |= x << i;
  }

  int ans = 0;
  for(int s = 0; s < (1 << N); s++) {
    int t = 0;
    for(int i = 0; i < N; i++) {
      if(s >> i & 1) {
        t ^= a[i];
      }
    }
    if(t == p) {
      ans++;
    }
  }
  cout << ans << endl;
  return 0;
}
