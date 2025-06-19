'''

🧠 What is Shell Sort?

Shell Sort is an in-place comparison-based sorting algorithm.
It’s a generalization of Insertion Sort that allows exchange of items that are far apart.


"Shell Sort reduces the number of swaps compared to Insertion Sort by comparing distant 
elements using a shrinking gap. Its performance depends on the chosen gap sequence."






The idea is:

    In Insertion Sort, elements are moved one at a time.

    In Shell Sort, elements are moved across gaps to move them closer to their correct positions.

    This drastically reduces the total number of swaps required.

⚙️ How Does Shell Sort Work?

    Start with a gap value (initially half the array size).

    Perform gapped insertion sort for this gap size.

    Reduce the gap (commonly gap = gap // 2).

    Repeat until gap becomes 0.

⏱️ Time and Space Complexity
Case	Time Complexity
Best Case	Ω(n log n) (depends on gap)
Average Case	Θ(n log² n) or better
Worst Case	O(n²)

    Space Complexity: O(1) (in-place)

    Not stable.

🧪 Gap Sequences

The performance of Shell Sort heavily depends on the gap sequence used.
Common gap sequences:

    Shell’s original: n//2, n//4, ..., 1

    Hibbard: 2^k - 1

    Knuth: (3^k - 1) / 2

    Sedgewick: Mixed formula, better theoretical performance.

    🔍 Research shows using optimized gap sequences like Sedgewick or Ciura gives much better performance.

✅ Advantages

    Simple to implement.

    Performs better than Bubble, Selection, and sometimes Insertion Sort.

    Requires no extra memory (in-place).

    Works well for medium-sized datasets.

❌ Disadvantages

    Not as efficient as advanced algorithms (Merge, Quick, Heap) on large datasets.

    Performance highly dependent on gap sequence.

    Not stable.

📊 Real Use Case?

Shell Sort is mostly used:

    In embedded systems where memory is limited.

    In educational or academic settings for learning purposes.

    Rarely used in practice for large-scale applications.

🧠 Interview Tip

    Shell Sort is an optimization of Insertion Sort and is useful when:















'''












def Shellsort(alist):
    gap = len(alist)//2
    while gap >0:
        for index in range(gap,len(alist)):
            current_element = alist[index]
            pos = index
            while pos>=gap and current_element < alist[pos-gap]:
                alist[pos] = alist[pos-gap]
                pos = pos-gap
            alist[pos]=current_element
        gap = gap//2

list1 = [4,5,1,8,3,6]
Shellsort(list1)
print(list1)

