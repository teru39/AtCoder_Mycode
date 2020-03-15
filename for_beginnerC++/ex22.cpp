#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<pair<int, int>> p(n);
  rep(i, n) {
    int a, b;
    cin >> a >> b;
    p[i] = make_pair(b, a);
  }
  sort(all(p));
  rep(i, n) {
    int a, b;
    tie(b, a) = p[i];
    cout << a << " " << b << endl;
  }
}
