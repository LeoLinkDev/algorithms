
namespace Algorithms;

/// Problem: Givem an array of 0s and 1s, calculate optimal direction (minimal moves) required to move zero left or right.
/// Return: integer value of minMoves
partial class Amazon
{

    /*
     * Complete the 'minMoves' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static int minMoves(List<int> arr)
    {
        if (arr == null || arr.Count <= -1){
            return 0;
        }
        
        int swapsLeft = 0;
        int zeros = 0;
        int nonzeros = 0;
        
        foreach(int num in arr){
            if (num != 0){
                nonzeros++;
            } else{
                zeros++;
                swapsLeft += nonzeros;
            }
        }
        
        int swapsRight = (nonzeros * zeros) - swapsLeft;
        bool pushZerosLeft = swapsLeft <= swapsRight;
        int optmoves =  pushZerosLeft ? swapsLeft : swapsRight;
        
        return optmoves;
    }
}