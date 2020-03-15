#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<tuple<string, int, int>> t(n);
  rep(i, n) {
    string s;
    int a;
    cin >> s >> a;
    t[i] = make_tuple(s, -a, i);
  }

  sort(all(t));
  rep(i, n) {
    int a;
    tie(ignore, ignore, a) = t[i];
    cout << a+1 << endl;
  }
}
