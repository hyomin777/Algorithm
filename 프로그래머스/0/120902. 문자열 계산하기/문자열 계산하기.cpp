#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string my_string) {
    int answer = 0;
    int num = 0;
    char op = 0;
    // 1. stringstream 객체에 문자열을 넣습니다.
    stringstream ss(my_string);
    
    // 2. 첫 번째 숫자를 읽어서 answer에 저장합니다.
    ss >> answer;
    
    // 3. (연산자)와 (숫자)가 순서대로 계속 읽어지는 동안 반복합니다.
    // 예: "+ 5", "- 10" ...
    while (ss >> op >> num) {
        if (op == '+') {
            answer += num;
        } else if (op == '-') {
            answer -= num;
        }
    }

    return answer;
}