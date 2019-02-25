#-----Day 21: Generics-------#


/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

// Write your code here
template<typename T>
void printArray(vector<T> v){
    for(auto val : v){
        cout<< val <<endl;
    }
}




