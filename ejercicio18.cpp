#include <iostream>
#include <cstdlib>


using std::cout;
using std::endl;

int main (){
	float y=1.0;
	float x=0.0;
	float h=0.1; 
	int N=3/h;
   for (int i=0;i<N;i++){
	y=y-h*y;
	x=x+h;

   cout << x <<" " <<y << endl;
  }
return 0;
}
