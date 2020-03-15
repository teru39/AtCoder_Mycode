#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  string s;
  cin >> s;
  int ans = 0;
  bitset<100000> ss(s);
  for(int i = 0; i < s.size() - 1; i++) {
    if(ss[i + 1] == ss[i]) {
      ss[i + 1].flip();
      ans++;
    }
  }
  reverse(all(s));
  int ans2 = 0;
  bitset<100000> sss(s);
  for(int i = 0; i < s.size() - 1; i++) {
    if(sss[i + 1] == sss[i]) {
      sss[i + 1].flip();
      ans2++;
    }
  }
  cout << min(ans, ans2) << endl;
}


