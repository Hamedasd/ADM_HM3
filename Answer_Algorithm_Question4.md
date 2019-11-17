
# 4. Algorithmic question


You are given a string, s. Let's define a subsequence as the subset of characters that respects the order we find them in s. For instance, a subsequence of "DATAMINING" is "TMNN". Your goal is to define and implement an algorithm that finds the length of the longest possible subsequence that can be read in the same way forward and backwards. For example, given the string "DATAMININGSAPIENZA" the answer should be 7 (dAtamININgsapIenzA).

### Answer:

 We are suposed to find longest palindrome subsequence.
To do this I think the best and easist way is to use a recursive function, it's not the most efficient approch however our string would not be so big to make any problem for this function.
In this approch each time our function finds subsequence drop the rest of string and only consider this subsequence, to make sure it's the longest possible subsequence it would be compared to the longest palindrome subsequence. 

To make this alorgithum works, we need three iterators turning around main and new subsequence which is subsequence of the larger one



```python
def longest_palindrome(string):
    lenght = 0
    if len(string)<=1:
        return len(string)
    if string[0]== string[-1]:
        lenght +=2 + longest_palindrome(string[1:-1])
    else:
        lenght += max( longest_palindrome(string[:-1]) ,longest_palindrome(string[1:]))
  
    return lenght
```


```python
longest_palindrome('DATAMININGSAPIENZA')
```




    7


