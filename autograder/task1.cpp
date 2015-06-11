#include <iostream>
#include <unistd.h>

using namespace std;

//test program to add 2 numbers for python autograder
int main() {
  freopen("task1.in", "r", stdin);
  freopen("task1.out", "w", stdout);
  int a, b;
  cin >> a >> b;

  //mess up the output in special cases
  //on purpose: testing Time out and wrong output functions
  if (a%2==1)
    usleep(2400 * 1000);
  if (a < 1000 && a > 500)
    b++;

  cout << a + b << endl;
  return 0;
}
