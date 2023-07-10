#include <bits/stdc++.h>
#include "windows.h"
#define MAX_SIZE 1010
using namespace std;

struct CNode
{
    int x;//x坐标
    int y;//y坐标
    int flag;//是否可以行走的点
    int dir;//标记行船方向
    CNode *p;//父节点指针
};
CNode G[MAX_SIZE][MAX_SIZE][2];//状态空间 坐标，访问
int V[MAX_SIZE][MAX_SIZE][2]; //访问标记
deque <CNode> q;//搜索队列
int num;//商仆对数
int cap;//船容量
bool solve;//解标记
int steps;//步数

void Init();//初始化
void BFS();//BFS搜索
void Output(CNode *p);//输出

int main(){
    Init();//进行初始化
    while(!q.empty()&&!solve){//BFS搜索
        BFS();
    }
    if(!solve)
        cout<<"\n问题无解\n";
    else{
        cout<<"\n过河方案:\n";
        Output(&G[0][0][1]);//回朔法输出
        cout<<"最少需要"<<steps<<"步\n";
    }
    return 0;
}

void Init(){
    cout<<"共有商仆对数:";
    cin>>num;
    cout<<"船容量:";
    cin>>cap;
    int i,j;
    for(int i = 0 ; i <= num ; i++){
        for(int j = 0 ; j <= num ; j++){//初始化状态空间
            G[i][j][0].x = G[i][j][1].x = i;//坐标x
            G[i][j][0].y = G[i][j][1].y = j;//坐标y
            G[i][j][0].flag = G[i][j][1].flag = 0;//均初始化为不可行点为0
            G[i][j][0].p = G[i][j][1].p = NULL;//结点
            G[i][j][0].dir = -1;//行船方向左或者下
            G[i][j][1].dir = 1;//行船方向右或者上
            V[i][j][0] = V[i][j][1] = 0;//未访问
        }
    }
    for( i = 0 ; i <= num ; i++){//将可行点标记为1
        G[0][i][0].flag = G[num][i][0].flag = G[i][i][0].flag = 1;
        G[0][i][1].flag = G[num][i][1].flag = G[i][i][1].flag = 1;
    }
    G[num][num][0].flag = G[num][num][1].flag = 0 ;//右上角为初始状态设置为0
    solve = false;//标记问题有解与否
    q.push_back(G[num][num][0]);//初始点进人队列
    steps = 0;//记录下最少的渡河次数
}

void BFS(){
    int x,y;//队首所在坐标
    int dx,dy;//变化坐标
    int nx,ny;//行船后坐标
    int dir;//行船方向
    if(q.empty()||solve)//搜索队列为空或者有解，退出搜索
        return;
    x=q.front().x;//取出队首坐标
    y=q.front().y;
    dir=q.front().dir;
    q.pop_front();//队首出队

    for(dx = 0 ; dx <= cap ; dx++){
        for(dy = 0 ; dy <= cap - dx; dy++){//枚举所有可能的状态
            nx = x + dx * dir;
            ny = y + dy * dir;

            if(nx < 0 || nx > num || ny < 0 || ny > num )//坐标越界
                continue;
            if(G[nx][ny][0].flag == 0)//达到不可行点
                continue;
            if(dx == 0 && dy == 0)//坐标没变化
                continue;
            if(dir > 0 && V[nx][ny][1] == 1)//该点被访问过
                continue;
            if(dir < 0 && V[nx][ny][0] == 1)//该点被访问过
                continue;
            if(dir>0){//放入队列
                G[nx][ny][0].p = &G[x][y][1];
                q.push_back(G[nx][ny][0]);
            }
            else{//放入队列
                G[nx][ny][1].p = &G[x][y][0];
                q.push_back(G[nx][ny][1]);
            }
            if(dir>0)//标记被访问
                V[nx][ny][1] = 1;
            else
                V[nx][ny][0] = 1;
            if(nx == 0 && ny == 0){//达到终点
                solve = true;
                return;
            }
        }
    }
}

void Output(CNode *p){//回溯法输出遍历结果
    if(p -> p == NULL){
        cout<<"("<<p->x<<","<<p->y<<")\n";
        return;
    }
    Output(p->p);
    cout<<"("<<p->x<<","<<p->y<<")\n";
    steps++;
}

/*
- - - - - - - - - - - - - - - - - -
3对
*  *
** *
*  *
4对
*    *
*  * *
**   *
*    *
5对
*     *
*    **
*  *  *
**    *
*     *
6对
*      *
*     **
*    * *
*  *   *
**     *
*      *
n对 图形为 N
*/