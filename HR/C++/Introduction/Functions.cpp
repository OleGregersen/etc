#include <iostream>
#include <cstdio>
using namespace std;

/*
Add `int max_of_four(int a, int b, int c, int d)` here.
*/
int max_of_four(int a,int b,int c,int d)
{
    int i;
    if(a>b && a>c && a>d)
    {
        i = a;
    }
    else if(b>a && b>c && b>d)
    {
        i = b;
    }
    else if(c>a && c>b && c>d)
    {
        i = c;
    }
    else if(d>a && d>b && d>c)
    {
        i = d;
    }
return i;
}

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
