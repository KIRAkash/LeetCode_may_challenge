"""Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 """
 class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)
        binary=binary.split("b")
        binary=list(binary[1])
        if(num>0):
            revnum="0b"
        else:
            revnum="1b"
        for i in binary:
            if(i=='0'):
                revnum+="1"
            elif(i=='1'):
                revnum+="0"
            else:
                revnum+="wtf"
        rev=int(revnum,2)
        return rev
    
