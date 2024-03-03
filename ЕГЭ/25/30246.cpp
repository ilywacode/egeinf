// id: 30246

#include <bits/stdc++.h>

using namespace std;

int count_div(int n) {
  int x = 0;
  for (int i = 1; i < int(sqrt(n)) + 1; ++i) {
    if (n % i == 0) {
      x += 1;
      if (x != n / x) {
        x += 1;
      }
    }
  }
  return x;
}

int main() {
  int maxim = 0;
  for (int i = 10000; i < 5000001; ++i) {
    if (count_div(i) == 10) {
      maxim = max(maxim, i);
      cout << i << '\n';
    }
  }
  cout << maxim;
  return 0;
}