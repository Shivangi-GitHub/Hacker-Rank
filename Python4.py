Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Function Description

Complete the minion_game in the editor below.

minion_game has the following parameters:

string string: the string to analyze
Prints

string: the winner's name and score, separated by a space on one line, or Draw if there is no winner
Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Sample Input

BANANA
Sample Output

Stuart 12

------------------------------------------------------------------------------------------------------------------------------------------------------------------


def minion_game(string):
    if len(string)>0 and len(string)<=10**6:
        s=[]
        k=[]
        for i in range(0,len(string)):
            if string[i] not in ["A","E","I","O","U"]:
                l=i
                while l<=len(string):
                    g=''
                    for j in range(i,l):
                        g=g+string[j]
                    
                    s.append(g)
                    l=l+1
            
            else:
                p=i
                while p<=len(string):
                    f=''
                    for j in range(i,p):
                        f=f+string[j]
                    
                    k.append(f)
                    p=p+1
    
     
        for h in k:
            if h=="":
                k.remove(h)

        for t in s:
            if t=="":
                s.remove(t)
    
    
        if len(s)>len(k):
            print("Stuart", len(s))
        elif len(k)>len(s):
            print("Kevin", len(k))
        else:
            print("Draw")
    
    
    # your code goes here
    
if __name__ == '__main__':
