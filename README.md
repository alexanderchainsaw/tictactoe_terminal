# <p align="center">Simple TicTacToe in the terminal</p>
![](https://github.com/alexanderchainsaw/demo_repo/blob/main/demo.gif)  
Simple tictactoe with score tracking and enumerated cells.  
Checking for game completion is done by slicing the board 
and converting each slice into a set()

     wins = [slice1, slice2, slice3, ...]
     if any(True for x in wins if len(set(x)) == 1):
         return True              
If after conversion the length of a
slice == 1, the game is over

---
 
     requirements: colorama==0.4.6
