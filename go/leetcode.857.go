package main

import (
    "container/heap"
    "fmt"
    "math"
    "sort"
)

func MaxIndex(a []float64) int{
    n := len(a)
    if n < 2{
        return 0
    }
    ans := 0
    for i := 1; i < n; i++{
        if a[i] > a[ans]{
            ans = i
        }
    }
    return ans
}

func MinIndex(a []float64) int{
    n := len(a)
    if n < 2{
        return 0
    }
    ans := 0
    for i := 1; i < n; i++{
        if a[i] < a[ans]{
            ans = i
        }
    }
    return ans
}

func MakeRange(min, max int) []int {
    a := make([]int, max - min)
    for i := range a {
        a[i] = min + i
    }
    return a
}

func mincostToHireWorkersWA(quality []int, wage []int, K int) float64 {
    GetBad := func (selected []int) (ind int, v float64, tot float64){
        Q := 0.0
        A := make([]float64, 0)
        for i, s := range selected{
            if s == 1{
                Q += float64(quality[i])
            }
        }
        for i, s := range selected{
            if s == 1{
                maxWage := float64(wage[i]) / (float64(quality[i]) / Q)
                A = append(A, maxWage)
            }
        }
        ind = MaxIndex(A) // 最坏的位置
        v = A[ind] * (float64(quality[ind]) / Q) // 当前人的工资
        // fmt.Printf("GetBad %d %v %v\n", ind, selected, A)
        tot = A[ind]  // 最坏的总工资
        return 
    }

    n := len(quality)
    if n == 0 || K == 0{
        return 0.0
    }
    choice := make([]int, n)
    for i := 0; i < n; i++{
        if i < K{
            choice[i] = 1
        }else{
            choice[i] = 0
        }
    }
    // fmt.Printf("C %v\n", choice)
    // _, _, KKK := GetBad([]int{1, 0, 1})
    // fmt.Printf("AAAAA %v\n", KKK)
    _, _, ans := GetBad(choice)
    for i := K; i < n; i++{
        // fmt.Printf("Begin Iter[%v] %v\n", i, choice)
        _, _, ori_tot := GetBad(choice)
        best_j := -1
        best_jv := 0.0
        for j := 0; j < i; j++{
            if choice[j] == 0{
                // 如果j已经没有被选中了
                continue
            }
            // 尝试用i换j
            choice[i] = 1
            choice[j] = 0
            _, _, new_tot := GetBad(choice)
            // fmt.Printf("+++ %v %v new %v ori %v\n", i, j, new_tot, ori_tot)
            if new_tot < ori_tot{
                // 如果能换
                if best_j == -1 || best_jv > new_tot{
                    best_j = j
                    best_jv = new_tot
                }
            }
            choice[i] = 0
            choice[j] = 1
            // fmt.Printf("--- %v\n", choice)
        }
        if best_j != -1{
            // 选择最优的进行交换
            choice[i] = 1
            choice[best_j] = 0
            // fmt.Printf("Replace %v with %v, now %v\n", best_j, i, choice)
        }
        // fmt.Printf("After Iter[%v] %v\n", i, choice)
    }
    _, _, ans = GetBad(choice)
    // ind, v, ans := GetBad(choice)
    // fmt.Printf("%v %v %v %v\n", ind, v, ans, choice)
    return ans
}

type IntHeap []int
 
func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *IntHeap) Push(x interface{}) {
    // Push and Pop use pointer receivers because they modify the slice's length,
    // not just its contents.
    *h = append(*h, x.(int))
}
func (h *IntHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0: n-1]
    return x
}

type IntSort []InPair  
 
func (c IntSort) Len() int {  
    return len(c)  
}  
func (c IntSort) Swap(i, j int) {  
    c[i], c[j] = c[j], c[i]  
}  
func (c IntSort) Less(i, j int) bool {
    return c[i].per < c[j].per
}  

type InPair struct {
    i int
    per float64
    q int
    w int
}

func mincostToHireWorkers(quality []int, wage []int, K int) float64 {
    n := len(quality)
    A := make([]InPair, n)
    for i := 0; i < n; i++{
        A[i] = InPair{i:i, per:float64(wage[i])/float64(quality[i]), q:quality[i], w:wage[i]}
    }
    sort.Sort(IntSort(A))

    h := &IntHeap{}
    heap.Init(h)

    curq := 0
    ans := 99999999999.0
    for _, a := range A{
        q := a.q
        // w := a.w
        per := a.per
        // i := a.i

        heap.Push(h, -q)
        curq += q
        if h.Len() > K{
            rq := - (heap.Pop(h)).(int)
            // fmt.Printf("Out %v\n", rq)
            curq -= rq
        }
        // fmt.Printf("curq %v per %v\n", curq, per)
        if h.Len() == K{
            ans = math.Min(float64(curq)*per, ans)
        }
    }
    return ans
}

func main(){
    fmt.Printf("%v\n", mincostToHireWorkers([]int{10,20,5}, []int{70,50,30}, 2)) // 105.00000
    fmt.Printf("%v\n", mincostToHireWorkers([]int{3,1,10,10,1}, []int{4,8,2,2,7}, 3)) // 30.66667
}