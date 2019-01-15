#include <unordered_set>
#include <iostream>
#include <utility>
#include <vector>
#include <string>
#include <stdlib.h>

using namespace std;

struct pair_hash {
    inline std::size_t operator()(const std::pair<int,int> & v) const {
        return v.first*1000+v.second;
    }
};

struct node {
    bool hasParent;
    node* parent;
    bool key;
};


void printgrid(vector<vector<node*>> grid){
    for (vector<node*> row : grid){
        for (node* el : row){
            cout << "(" << el->key << ", " << &el<< " -> " << el->parent << ") ";
        }
        cout << endl;
    }
}


void uniteAreas(vector<vector<node*>>& grid, pair<int,int> griddim){
    for (int y  = 0; y < griddim.second; y++) {
        for (int x = 0; x < griddim.first; x++) {
            bool found = false;
            for(int j = 0; j < 2; j++){
                int nx = x - (j == 1);
                int ny = y - (j == 0);
                if ((nx > -1) && (ny > -1) && grid[y][x]->key == grid[ny][nx]->key){
                    if(!found){
                        found = true;
                        node* iternode = grid[ny][nx];
                        while (iternode->hasParent){
                            iternode = iternode->parent;
                            //cout << "Top while loop " << iternode << "|" << x << "," << y << endl;
                        }
                        grid[y][x]->parent = iternode;
                        grid[y][x]->hasParent = true;
                    }
                    // Join the two sides
                    else{
                        // Self parent
                        node* iternode = grid[y][x];
                        while (iternode->hasParent){
                            iternode = iternode->parent;
                            //cout << "Heading in to " << iternode << endl;
                        }
                        // Other parent
                        node* othernode = grid[ny][nx];
                        while(othernode->hasParent){
                            othernode = othernode->parent;
                        }
                        if(othernode != iternode){
                            othernode->parent = iternode;
                            othernode->hasParent = true;
                        }
                    }
                }
            }
            if(!found){

            }
        }
        //printgrid(grid);
    }
}

node* topAncestor(node* from){
    node* iternode = from;
    //cout << "Iternode: " << iternode << endl;
    while (iternode->hasParent){
        iternode = iternode->parent;
    }
    return iternode;
}


int main() {
    int R, C;
    cin >> R >> C;
    vector<vector<node*>> grid;
    for (int i = 0; i < R; i++) {
        vector<node*> row;
        string inp;
        cin >> inp;
        for (int c = 0; c < C; c++) {
            node* newnode = (node*) malloc(sizeof(node));
            newnode->key = (inp[c] == '1');
            newnode->hasParent = false;
            newnode->parent = nullptr;
            row.push_back(newnode);
        }
        grid.push_back(row);
    }
    //cout << "Got input" << endl;
    uniteAreas(grid, make_pair(C,R));
    for (vector<node*> row : grid){
        for (node* element : row){
            //cout << element->key << "(" << element << "->" << element->parent << ", " << element->hasParent << ") ";
        }
        //cout << endl;
    }

    int n;
    cin >> n;
    //cout << n << endl;
    for(int i = 0; i < n; i++){
        int ax, ay, bx, by;
        cin >> ay >> ax >> by >> bx;
        //cout << ax << ay << bx << by << endl;
        string outstring;
        //cout << topAncestor(grid[ay - 1][ax - 1]) << " " << topAncestor(grid[by - 1][bx - 1]) << endl;
        if(topAncestor(grid[ay - 1][ax - 1]) == topAncestor(grid[by - 1][bx - 1])){
            if(grid[ay - 1][ax - 1]->key){
                outstring = "decimal";
            }
            else{
                outstring = "binary";
            }
        }else{
            outstring = "neither";
        }
        cout << outstring << endl;
    }
    return 0;
}
