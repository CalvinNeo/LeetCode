package main

import (
    "fmt"
)

func longestArithSeqLengthWA(A []int) int {
    n := len(A)
    ans := 0
    dp := map[P] int{}

    for i := 0; i < n; i ++{
        for j := 0; j < i; j ++{
            d := A[i] - A[j]
            // fmt.Printf("last %v d %v\n", A[i], d)
            p1 := P{last:A[i], delta:d}
            v1, ok := dp[p1]
            if !ok{
                // 如果没有数列[A[j], A[i]]，则新创建一个
                dp[p1] = 2
                ans = Max(ans, 2)
            }
            v1, _ = dp[p1]
            // 否则查看是否可以延长这个数列的长度
            // 是否存在数列[A[j] - d, A[j]]
            p2 := P{last:A[j], delta:d}
            // fmt.Printf("need last %v delta %v\n", A[j], d)
            v2, ok2 := dp[p2]
            if ok2{
                // 如果存在，那么就可以延长一下
                // fmt.Printf("long %v by %v\n", A[j], A[i])
                if !ok && d == 0{
                    dp[p1] = Max(v1, v2)
                }else{
                    dp[p1] = Max(v1, v2 + 1)
                }
            }
            ans = Max(ans, dp[p1])
        }
        // fmt.Printf("dp %v\n", dp)
    }
    return ans
}

type P struct {
    last int
    delta int
}

func Max(a, b int) int{
    if a > b{
        return a
    }
    return b
}

func longestArithSeqLengthWA2(A []int) int {
    n := len(A)
    ans := 0
    dp := map[P] int{}

    for i := 0; i < n; i ++{
        for j := 0; j < i; j ++{
            d := A[i] - A[j]
            ki := P{last:A[i], delta:d} 
            kj := P{last:A[j], delta:d} 
            vi, oki := dp[ki] // 是否有数列 A[j] A[i]?
            vj, okj := dp[kj] // 是否有数列 A[j]-d A[j]

            if oki && okj{
                dp[ki] = Max(vi, vj + 1)
            }else if (!oki) && (!okj){
                dp[ki] = 2
            }else if oki{
                dp[ki] = Max(vi, 2)
            }else if okj{
                dp[ki] = Max(vi, vj + 1)
            }
            ans = Max(ans, dp[ki])
        }
    }
    return ans
}

func longestArithSeqLengthAC(A []int) int {
    n := len(A)
    ans := 2
    dp := map[P] int{}
    if n < 2{
        return 0
    }
    dp[P{last:1, delta:A[1]-A[0]}] = 2
    for i := 2; i < n; i ++{
        for j := 0; j < i; j ++{
            d := A[i] - A[j]
            ki := P{last:i, delta:d} 
            kj := P{last:j, delta:d} 
            vi, oki := dp[ki] // 是否有数列 A[j] A[i]?
            vj, okj := dp[kj] // 是否有数列 A[j]-d A[j]
            if !oki{
                vi = 0
            }
            if !okj{
                vj = 1
            }
            dp[ki] = Max(vi, vj+1)
            ans = Max(ans, dp[ki])
        }
    }
    return ans
}

func longestArithSeqLength(A []int) int {
    n := len(A)
    ans := 0
    dp := map[P] int{}

    for i := 0; i < n; i ++{
        for j := 0; j < i; j ++{
            d := A[i] - A[j]
            ki := P{last:i, delta:d} 
            kj := P{last:j, delta:d} 
            vi, oki := dp[ki] // 是否有数列 A[j] A[i]?
            vj, okj := dp[kj] // 是否有数列 A[j]-d A[j]

            if oki && okj{
                dp[ki] = Max(vi, vj + 1)
            }else if (!oki) && (!okj){
                dp[ki] = 2
            }else if oki{
                dp[ki] = Max(vi, 2)
            }else if okj{
                dp[ki] = Max(vi, vj + 1)
            }
            ans = Max(ans, dp[ki])
        }
    }
    return ans
}

func main(){
    fmt.Printf("%v\n", longestArithSeqLength([]int{3,6,9,12})) // 4
    fmt.Printf("%v\n", longestArithSeqLength([]int{9,4,7,2,10})) // 3
    fmt.Printf("%v\n", longestArithSeqLength([]int{20,1,15,3,10,5,8})) // 4
    fmt.Printf("%v\n", longestArithSeqLength([]int{24,3,0,3})) // 2
    fmt.Printf("%v\n", longestArithSeqLength([]int{12,28,13,6,34,36,53,24,29,2,23,0,22,25,53,34,23,50,35,43,53,11,48,56,44,53,31,6,31,57,46,6,17,42,48,28,5,24,0,14,43,12,21,6,30,37,16,56,19,45,51,10,22,38,39,23,8,29,60,18})) // 4
}