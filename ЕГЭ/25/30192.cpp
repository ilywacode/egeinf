// id: 30192

#include <bits/stdc++.h>

using namespace std;

bool is_prime(int n) {
  for (int i = 2; i < int(sqrt(n)) + 1; ++i) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

int main() {
  cout << (is_prime(41203) ? "Prime" : "Not prime");
}