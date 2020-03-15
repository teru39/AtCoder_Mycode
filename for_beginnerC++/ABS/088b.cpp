#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main() {
  int n;
  cin >> n;
  vector<int> a(n);
  rep(i, n) {
    cin >> a[i];
  }
  sort(all(a));
  reverse(all(a));
  int al = 0, bo = 0;
  rep(i, n) {
    if(i % 2 == 0)
      al += a[i];
    else
      bo += a[i];
  }
  cout << al - bo << endl;
}
