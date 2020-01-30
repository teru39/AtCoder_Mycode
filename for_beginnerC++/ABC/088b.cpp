#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define all(v) (v).begin(), (v).end()

int main()
{
  int n;
  cin >> n;
  vector<int> v(n);
  rep(i, n)
  {
    cin >> v[i];
  }
  sort(all(v));
  reverse(all(v));
  int a = 0, b = 0;
  rep(i, n)
  {
    if (i % 2 == 0)
    {
      a += v[i];
    }
    else
    {
      b += v[i];
    }
  }
  cout << a - b << endl;
}
