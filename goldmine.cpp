#include<bits/stdc++.h>
#define mod 1000000007
#define max 500000005
#define size 2005
using namespace std;
typedef  long long int ll;
template<typename T> inline T maxi(T a,T b)
{
    return a>b?a:b;
}
template<typename T> inline T mini(T a,T b)
{
    return a<b?a:b;
}
template<typename T> inline T absl(T a)
{
    return a>0?a:-a;
}
template<typename T> inline T gcd(T a,T b)
{
    T t;
    if(a<b)
    {
        while(a)
        {
            t=a;
            a=b%a;
            b=t;
        }
        return b;
    }
    else
    {
        while(b)
        {
            t=b;
            b=a%b;
            a=t;
        }
        return a;
    }
}
#define mp(a,b) make_pair(a,b)
void multiply(ll A[3][3],ll B[3][3])
{
    ll mul[3][3];
    for(ll i=0;i<3;++i)
    {
        for(ll j=0;j<3;++j)
        {
            mul[i][j]=0;
            for(ll k=0;k<3;++k)
            {
                mul[i][j]=(mul[i][j]%mod+(A[i][k]*B[k][j])%mod)%mod;
            }
        }
    }
    for(ll i=0;i<3;++i)
    {
        for(ll j=0;j<3;++j)
        {
            A[i][j]=mul[i][j];
        }
    }
 }
 ll power(ll A[3][3],ll n)
 {
    ll res[3][3]={{0,1,1},{1,0,0},{0,1,0}};
    while(n>0)
    {
        if(n&1)
        {
            multiply(res,A);
        }
        multiply(A,A);
        n=n>>1;
    }
    return (res[0][0]+res[0][1])%mod;
 }
 ll solve(ll n)
 {
     ll A[3][3]={{0,1,1},{1,0,0},{0,1,0}};
   return power(A,n-2);
}
void input()
{
   ll t;
   cin>>t;
   while(t--)
   {
    ll n;
    scanf("%lld",&n);
    if(n==1)
    printf("0\n");
    else if(n<=3)
    printf("1\n");
    else
    printf("%lld\n",solve(n-2));
   }
}
int main()
{
  input();
  return 0;
}
