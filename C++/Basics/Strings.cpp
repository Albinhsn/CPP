#include <iostream>
#include <string>
using namespace std;

int main()
{
    // Complete the program
    string a, b;
    cin >> a >> b;
    int c = a.size(), d = b.size();
    cout << c << " " << d << "\n";
    cout << a + b << "\n";
    char e = a[0], f = b[0];
    a[0] = f;
    b[0] = e;
    cout << a << " " << b << "\n";
    return 0;
}