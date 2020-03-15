#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  map<string, int> m;
  rep(i, n) {
    string s;
    cin >> s;
    if(m.count(s))
      m[s]++;
    else
      m[s] = 1;
  }
  int ans_cnt = 1;
  string ans;
  for(auto x : m) {
    if(x.second >= ans_cnt) {
      ans = x.first;
      ans_cnt = x.second;
    }
  }
  cout << ans << " " << ans_cnt << endl;
}
