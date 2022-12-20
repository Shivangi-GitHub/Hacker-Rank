You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed 
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef

Sample Output

3
2 1 1


while True:
    n=int(input("Enter the number : "))
    if n>100000:
        print("enter the valid number")
    if n>=1 and n<=100000:
        break
    

l=[]
for i in range(1,n+1):
    m=input("enter a word : ")
    if m.islower():
        l.append(m)
       
h=[]
for i in l:
  for k in range(0,len(l)):
    if l[k] not in h:
      h.append(l[k])

print(len(h)) 

for j in h:
   print(l.count(j),end=" ")
