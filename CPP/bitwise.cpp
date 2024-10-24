#include <iostream>
using namespace std;

int main() {
    int a = 5;  // 0101 in binary
    int b = 3;  // 0011 in binary

    int result = a & b;  // Bitwise AND
    cout << "Result of a & b: " << result << std::endl;
    system("pause");
    return 0;
}
