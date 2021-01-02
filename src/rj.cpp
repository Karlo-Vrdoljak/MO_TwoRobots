/*
{
######################
#       Author       #
#        Gary        #
#        2020        #
######################
*/
//#pragma GCC target ("avx2")
//#pragma GCC optimization ("O3")
//#pragma GCC optimization ("unroll-loops")
#pragma GCC optimize(2)
#include<bits/stdc++.h>
#define rb(a,b,c) for(int a=b;a<=c;++a)
#define rl(a,b,c) for(int a=b;a>=c;--a)
#define LL long long
#define IT iterator
#define PB push_back
#define II(a,b) make_pair(a,b)
#define FIR first
#define SEC second
#define FREO freopen("check.out","w",stdout)
#define rep(a,b) for(int a=0;a<b;++a)
#define SRAND mt19937 rng(chrono::steady_clock::now().time_since_epoch().count())
#define random(a) rng()%a
#define ALL(a) a.begin(),a.end()
#define POB pop_back
#define ff fflush(stdout)
#define fastio ios::sync_with_stdio(false)
#define check_min(a,b) a=min(a,b)
#define check_max(a,b) a=max(a,b)
using namespace std;
const int INF=0x3f3f3f3f;
typedef pair<int,int> mp;
/*}
*/
typedef pair<mp,mp> data;
int walk[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
    int n,m;
    vector <string> Maze;
    bool check(int x,int y){
      if(x<0||y<0||x>=n||y>=m) return false;
      if(Maze[x][y]=='#') return false;
      return true;
    }
  int dp[40][40][40][40];
class TwoRobots{
  public:
  int move(vector <string> c){
    memset(dp,63,sizeof(dp));
    Maze=c;
    mp sa,sb,ta,tb;
    n=c.size();
    m=c[0].size();
    rep(i,n)
    rep(j,m){
      if(c[i][j]=='a'){
        ta=II(i,j);
      }
      if(c[i][j]=='b'){
        tb=II(i,j);
      }
      if(c[i][j]=='A'){
        sa=II(i,j);
      }
      if(c[i][j]=='B'){
        sb=II(i,j);
      }
    } 
    queue<pair<int,data> > q;
    q.push(II(0,II(sa,sb)));
    dp[sa.FIR][sa.SEC][sb.FIR][sb.SEC]=0;
    while(!q.empty()){
      pair<int,data> now=q.front();
      q.pop();
      if(now.SEC.FIR==ta&&now.SEC.SEC==tb) return now.FIR;
      int xa,ya,xb,yb;
      xa=now.SEC.FIR.FIR;
      ya=now.SEC.FIR.SEC;
      xb=now.SEC.SEC.FIR;
      yb=now.SEC.SEC.SEC;
      rep(i,4){
        int nxa,nya;
        nxa=xa+walk[i][0];
        nya=ya+walk[i][1];
        if(!check(nxa,nya)) continue;
        rep(j,4){
          int nxb,nyb;
          nxb=xb+walk[j][0];
          nyb=yb+walk[j][1];
          if(!check(nxb,nyb)) continue;
          if(nxb==xa&&nyb==ya&&nxa==xb&&nya==yb) continue;
          if(nxb==nxa&&nyb==nya) continue;
          if(dp[nxa][nya][nxb][nyb]==INF){
            dp[nxa][nya][nxb][nyb]=now.FIR+1;
            q.push(II(now.FIR+1,II(II(nxa,nya),II(nxb,nyb))));
          }
        }
      }
    }
    return -1;
  }
}s;
//int main(){
//  cout<<s.move({"...A...",
// ".#####.",
// ".#####b",
// "B#####.",
// ".#####.",
// ".#####.",
// "..a...."});
//  return 0;
//}
/** [\u31243][\u24207][\u26694][\u26550][\u65306]
  *
  *
  *
  *
  **/
