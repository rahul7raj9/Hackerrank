/* Enter your macros here */



#define INF 9999

#define toStr(x) #x

#define io(v) cin >> v  

#define FUNCTION(name,operator) inline void name(int &current, int candidate) {!(current operator candidate) ? current = candidate : false;}

#define foreach(v, i) for (int i = 0; i < v.size(); ++i)
