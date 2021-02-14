#include <iostream>

void D(int m, int* x[10][])
{
	std::cout<<"sd";
}	

int main()
{
	int m = 10;
	int x[10][];
	int* px[10][] = &x;
	D(m,px);
	return 0;
}
