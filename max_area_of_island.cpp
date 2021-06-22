#include <iostream>
#include <vector>

using namespace std;
/*
class Solution {
    int[][] grid;
    boolean[][] seen;

    public int area(int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length ||
                seen[r][c] || grid[r][c] == 0)
            return 0;
        seen[r][c] = true;
        return (1 + area(r+1, c) + area(r-1, c)
                  + area(r, c-1) + area(r, c+1));
    }

    public int maxAreaOfIsland(int[][] grid) {
        this.grid = grid;
        seen = new boolean[grid.length][grid[0].length];
        int ans = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                ans = Math.max(ans, area(r, c));
            }
        }
        return ans;
    }
}*/

class Solution {
	
	vector<vector<int>> mygrid;
  vector<vector<bool>> seen;

	public:
  	void display(){
			cout << "\nitems are :\n" << endl; 
    
			//display method 1
			/*for(vector<int> vec: grid){
				for(int item:vec){
					cout << item << " ";
				}
				cout << endl;
			} */

			//display method 2
			for(int i=0; i < mygrid.size(); i++){
				for(int j=0; j< mygrid[i].size(); j++){
					cout << mygrid[i][j] << " ";
				} 
				cout << endl;
			}		
  	}
	
  	int area(int row, int col){
      int res = 0;

    	if(row >= 0 && row < mygrid.size() && 
         col >= 0 && col < mygrid[row].size() && 
         mygrid[row][col] == 1 && seen[row][col] == 0){ 
				seen[row][col] = 1;
				res = 1 + area(row-1, col) + area(row+1, col) + area(row, col-1) + area(row, col+1);
			}

			return res;
		}

		int maxAreaOfIsland(vector<vector<int> >& grid){
		
			mygrid = grid;
      vector<vector<bool>> flag(grid.size(),vector<bool>(grid[0].size()));
			seen = flag;  
      int maxArea = 0;
     
			for(int i=0;i<grid.size();i++){
				for(int j=0;j<grid[0].size();j++){
					maxArea = max(maxArea, area(i,j));
				}
			}

			return maxArea;
		}
};

int main(){

	Solution sol;
	vector<vector<int> > grid = {
					{0,0,1,0,0,0,0,1,0,0,0,0,0},
					{0,0,0,0,0,0,0,1,1,1,0,0,0},
					{0,1,1,0,1,0,0,0,0,0,0,0,0},
					{0,1,0,0,1,1,0,0,1,0,1,0,0},
					{0,1,0,0,1,1,0,0,1,1,1,0,0},
					{0,0,0,0,0,0,0,0,0,0,1,0,0},
					{0,0,0,0,0,0,0,1,1,1,0,0,0},
					{0,0,0,0,0,0,0,1,1,0,0,0,0}};

	cout << "max area of island is " << sol.maxAreaOfIsland(grid);

  return 0;
}

