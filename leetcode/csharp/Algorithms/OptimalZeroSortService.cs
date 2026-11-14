using System;

namespace Algorithms.xunit;

    public interface ISortService
    {
        SortResult  minMoves(List<int> lst);
    }

    public record SortResult
    {
        public required List<int> SortedLst;
        public int ZeroSwaps;
        public required string TargetZeroDirection;
    }

    public class OptimalZeroSortService : ISortService
    {
        /// <summary>
        /// Implementation: Dual-Direction Optimal Zero's Swap Counter
        /// 
        /// Performance:
        /// O(n) Linear Time complexity. Equiped to handle datasets of 10^5 elements.
        /// 
        /// Logic:
        /// 1. Calculate whether it is more optimal to group zeros on the left or the right.
        /// 2. Run a standard optimized sort on the non-zero numbers while positioning the zeros on their calculated optimal side.
        /// 
        /// </summary>
        /// <param name="arr">arr to sort, merge and calculate the global minimum number of adjacent swaps.</param>
        /// <param name="ascending">True/False toggle for descending or ascending order.</param>
        /// <returns>The global minimum number of adjacent swaps.</returns>
        public SortResult minMoves(List<int> arr)
        {
            if (arr == null || arr.Count <= 1)
            {
                return new SortResult { SortedLst = arr, ZeroSwaps = 0, TargetZeroDirection = "Left" };
            }

            int swapsLeft = 0;
            int nonzeros = 0;
            int zeros = 0;

            // Tally zeros and nonzeros, Left Swaps
            foreach(int nums in arr){
                if (nums != 0){
                    nonzeros++;
                } else {
                    zeros++;
                    swapsLeft += nonzeros; // Total non-zeros to the left of this zero
                }
            }

            // Mathematical shortcut to calculate the Right Swaps instantly ( e.g. given [1, 0, 1, 0] when: 2 * 2 = 4 (nonzeros * zeros) - 2 (swapsLeft) then swapsRight = 2)
            // without needing a second iteration pass
            int swapsRight = (nonzeros * zeros) - swapsLeft;

            // Determine optimal direction based entirely on zero-involved movements
            bool pushZerosLeft = swapsLeft <= swapsRight;
            int optimalSwaps = pushZerosLeft ? swapsLeft : swapsRight;

            // PASS 2: Allocation-Free In-Place Layout Rewrite
            int arrCnt = arr.Count - 1;
            int nonZeroWriteIdx = 0;

            if (pushZerosLeft)
            {
                    // fill Non-Zeros RIGHT to LEFT to prevent overwriting unread elements.
                    nonZeroWriteIdx = arrCnt;

                    for (int i = arrCnt; i >= 0; i--)
                    {
                        if (arr[i] != 0) {
                            arr[nonZeroWriteIdx--] = arr[i];
                        }
                    }
                        
                    // fill left with zeros
                    for (int i = 0; i < zeros; i++) {
                        arr[i] = 0;
                    }
                } else {
                    // Fill Non-Zeros LEFT to RIGHT to prevent overwriting unread elements.

                    for (int i = 0; i <= arrCnt; i++)
                    {
                        if (arr[i] != 0) {
                            arr[nonZeroWriteIdx++] = arr[i];
                        }
                    }
                    
                    // Fill right leftover space with Zeros
                    for (int i = nonzeros; i <= arrCnt; i++){
                        arr[i] = 0;
                    }
            }

            // PASS 3: Sort non-zeros natively in-place
            int nonzerostart = pushZerosLeft ? zeros : 0;
            Array.Sort(arr.ToArray(), nonzerostart, nonzeros);

            return new SortResult 
            { 
                SortedLst = arr, 
                ZeroSwaps = optimalSwaps, 
                TargetZeroDirection = pushZerosLeft ? "Left" : "Right" 
            };
        }
    }
