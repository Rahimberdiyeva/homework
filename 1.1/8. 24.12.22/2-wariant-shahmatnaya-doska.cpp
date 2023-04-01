#include<bits/stdc++.h>
using namespace std;
int n, h, g, i, j, a[10][10];
int main(){
	cin>>n;
	for(i=1;i<=n;i++){
		cin>>h>>g;
		a[h][g]=1;
}	
/* for(i=1;i<=8;i++){
for(j=1;j<=8;j++)
cout<<a[i][j]<<" ";
cout<<endl; 
}*/
	h=4*n;
	for(i=1;i<=8;i++)
	for(j=1;j<=7;j++)
	if(a[i][j]==1 & a[i][j+1]==1) h=h-2;
	for(i=1;i<=7;i++)
	for(j=1;j<=8;j++)
	if(a[i][j]==1 & a[i+1][j]==1) h=h-2;
	cout<<h;
}