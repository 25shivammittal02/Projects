//SUdoku Solver
#include <bits/stdc++.h>
using namespace std;


int b =0;
bool canPlace(int a[][9], int i, int j, int num, int n)
{
    b++;
    for(int k=0;k<n;k++)
    {
        if(a[i][k]==num or a[k][j]==num)
        {
            return false;
        }
    }

    int sx = 3*(i/3);
    int sy = 3*(j/3);

    for(int x=sx;x<sx+3;x++)
    {
        for(int y=sy;y<sy+3;y++)
        {
            if(a[x][y]==num)
            {
                return false;
            }
        }
    }
    return true;
}

bool SolveSudoku(int a[][9], int i, int j, int n)
{
    if(i==n) //if all rows end, then print the answer
    {
        return true;
    }
    if(j==n) //if column ends, then move to enxt line
    {
        return SolveSudoku(a, i+1,0,n);
    }
    if(a[i][j]!=0) //if already a number is present, skip it
    {
        return SolveSudoku(a,i,j+1,n);
    }

    for(int num=1;num<=n;num++) //place ine number check if possible to solve further
    {
        if(canPlace(a,i,j,num,n))
        {
            a[i][j]=num;
            bool Aagesolvehoga = SolveSudoku(a,i,j+1,n);
            if(Aagesolvehoga)
            {
                return true;
            }
        }
    }
    a[i][j]=0;
    return false;
}


int main()
{
    system("cls");
    system("color 2f");
    int n =9;
    int a[9][9];
    cout<<"\t\t\tWELCOME TO SUDOKU SOLVER SOFTWARE ####"<<endl<<endl;
    cout<<"Folow the following instructions"<<endl;
    cout<<"1) Enter the numbers with a gap"<<endl;
    cout<<"2) Enter 0 in place of blank spaces\n"<<endl;
    cout<<"\nPress 1 to continue or 0 to exit"<<endl;
    int t;
    cin>>t;
    if(t==0)
    {
        return 0;
    }
    system("cls");
    system("color 2f");
    cout<<"Get ready to solve any of your SUDOKUs\n"<<endl;
    cout<<"Enter your SUDOKU to be solved"<<endl;

    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>a[i][j];
        }
    }
    system("cls");
    system("color 3");
    cout<<"Your Solved SudoKu is here->"<<endl;
    cout<<endl;
    SolveSudoku(a,0,0,n);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<"\nPress 1 to Play again or 0 to exit"<<endl;
    int z;
    cin>>z;
    if(z==1)
    {
        main();
    }
    else
    {
        return 0;
    }
}

/*
Sample
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

//harest sudoku ever
0 8 0 0 0 0 0 0 0
0 0 3 6 0 0 0 0 0
0 7 0 0 9 0 2 0 0
0 5 0 0 0 7 0 0 0
0 0 0 0 4 5 7 0 0
0 0 0 1 0 0 0 3 0
0 0 1 0 0 0 0 6 8
0 0 8 5 0 0 0 1 0
0 9 0 0 0 0 4 0 0

*/