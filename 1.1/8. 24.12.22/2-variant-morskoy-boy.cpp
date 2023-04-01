#include <bits/stdc++.h>
using namespace std;
int n,m,x,i,j ; char a[1000][1000];
int main()
{
	cin>>n>>m;
	for(i=1;i<=n;i++)
	for(j=1;j<=m;j++)
	cin>>a[i][j];
	for(i=1; i<=n;i++)
	a[i][0] = '.';
	for (i=0;i<=m+1;i++){
	a[0][i] = '.';
	a[n+1][i] = '.';
}
	for (i=0;i<=n;i++) {
	a[i][m+1] = '.';
}
	for (i=1; i<=n;i++)
	for (j=1; j<=m;j++) 
	if (a[i][j] == '.' & a[i+1][j] == '.' & a[i-1][j] == '.' & a[i][j+1] == '.' & a[i][j-1] == '.') 
	x++;
cout<<x;
}
 