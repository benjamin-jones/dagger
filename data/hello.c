#include <stdio.h>

void func3() {
 int a = 3;
 int b = 6;
 printf("%d\n",a+b);
}

void func2() {
 func3();
}

void func1() {
 func2();
}

int main(int argv, char **argc) {
	printf("Hello world\n");
	func1();
	return 0;
}
