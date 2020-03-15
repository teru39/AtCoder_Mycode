#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  string s;
  cin >> s;
  int s0 = 0, s1 = 0;
  for(auto x : s) {
    if(x == '0')
      s0++;
    else
      s1++;
  }
  cout << min(s0, s1) * 2 << endl;
}
