[Back to Home](https://teanlouise.github.io)

![blackjack_title](https://user-images.githubusercontent.com/19520346/71759847-58d34380-2eff-11ea-8ac5-f833cc0d988c.PNG)

A simple blackjack game. This was completed as the milestone 2 project for Jose Portilla's "Zero-to-Hero Python" course. Basic Python functionality inlcuding Object-Oriented programming practices were used to implement this project.

Pytest was used to write a number of tests and automatic testing has been setup with Travis CI.

![blackjack_travis](https://user-images.githubusercontent.com/19520346/74307933-922a8900-4db2-11ea-9c67-bccd58586bd7.PNG)
 
**Gameplay:**
1. Create a bank roll according to user to be used for all subsequent games
2. Start the first round
3. Ask the player for their bet for this round
4. Make sure that the Player's bet does not exceed their available chips
5. Create a deck of 52 cards and shuffle
6. Deal two cards to the Dealer and two cards to the Player
7. Show only one of the Dealer's cards, the other remains hidden
8. Show both of the Player's cards
9. Ask the Player if they wish to Hit, and take another card
10. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
11. If a Player Stands, play the Dealer's hand. 
12. The dealer will always Hit until the Dealer's value meets or exceeds 17
13. Determine the winner 
14. Adjust the Player's chips accordingly to bank roll
15. Ask the Player if they'd like to play again
16. If so, start again from step 3


_The game starts with an introduction and prompt for how many chips to start with_
_(1) Dealer wins since they have a higher value than the player, lose the bet._
![blackjack_1](https://user-images.githubusercontent.com/19520346/71760376-7062fa00-2f08-11ea-8478-704719f2adda.PNG)
_(2) Payer wins since they have a higher value than the dealer, win the bet._ 
![blackjack_2](https://user-images.githubusercontent.com/19520346/71760381-71942700-2f08-11ea-8c2d-713a6dd45c21.PNG)
_(3) Both the dealer and the player have the same value, there is a tie and no change to players chips._
![blackjack_3](https://user-images.githubusercontent.com/19520346/71760380-70fb9080-2f08-11ea-9e52-440fc2e30685.PNG)
_(4) Betting more than available chips is not allowed. Player hits then stands, dealer busts so player wins and takes bet.__
![blackjack_4](https://user-images.githubusercontent.com/19520346/71760379-70fb9080-2f08-11ea-80ca-e6ae1cceb4b0.PNG)
_(5) Player bets all their chips, player hits and there is a tie. No change to chips._
![blackjack_5](https://user-images.githubusercontent.com/19520346/71760378-70fb9080-2f08-11ea-98ce-ca25cadfc187.PNG)
_(6) Player bets all their chips, player hits and busts. Player has no balance left so the game ends._
![blackjack_6](https://user-images.githubusercontent.com/19520346/71760377-7062fa00-2f08-11ea-95d0-a02570223e87.PNG)
