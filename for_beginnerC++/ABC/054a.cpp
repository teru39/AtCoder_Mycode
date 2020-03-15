  #define _GLIBCXX_DEBUG
  #include <bits/stdc++.h>
  using namespace std;
  typedef long long ll;
  #define rep(i, n) for(int i = 0; i < (int)(n); i++)
  #define all(v) (v).begin(), (v).end()

  int main() {
    int a, b;
    cin >> a >> b;
    if(a == 1) a += 13;
    if(b == 1) b += 13;
    if(a > b)
      cout << "Alice";
    else if(a < b)
      cout << "Bob";
    else
      cout << "Draw";
    cout << endl;
  }
