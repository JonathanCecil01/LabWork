#include <iostream>
#include <vector>
#define edge pair<int, int>

using namespace std;

class Graph
{ 
    private:
        vector<pair<int, edge> > G;  // graph
        vector<pair<int, edge> > T;  // mst
        int *parent;
        int V;  // number of vertices/nodes in graph
    public:
        Graph(int V);
        void AddWeightedEdge(int u, int v, int w);
        int find_set(int i);
        void union_set(int u, int v);
        void kruskal();
        void print();
};

Graph::Graph(int V)
{
    this->V = V;
}
void Graph::AddWeightedEdge(int u, int v, int w)
{
    
}


int main()
{
    cout<<"CodeSpaceRocks"<<endl;
    return 0;
}