#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    int answer = 0;
    double dnum1 = num1;
    double dnum2 = num2;
    answer = ((dnum1/dnum2)*1000);
    return answer;
}