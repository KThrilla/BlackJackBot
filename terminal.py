import random

class terminalGame:

  def game():
    onGame = True
    myHand = []
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 
            4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
            7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,
            10, 10, 10, 10, 11, 11, 11, 11]
    
    def giveCard(): #Gives Player a Card
      card = random.choice(deck) 
      myHand.append(card)
      deck.remove(card)
    
    ### Starting Hand #######################################
    giveCard()
    giveCard()
    print(myHand)

    sum = myHand[0] + myHand[1]

    if sum == 21:
      print("BlackJack!: You Won")
      onGame = False

    ### Start of While Loop #################################
    while onGame is True:
      decision = input("Hit or Stay: ")

      if decision == "Stay" or decision == "stay":
        onGame = False
        break
      elif decision == "Hit" or decision == "hit":
        giveCard()

        sum = 0
        for i in myHand:
          sum = sum + i
        
        print(myHand)

        if sum > 21:
          print("Bust!: You Lost")
          onGame = False
        if sum == 21:
          print("BlackJack!: You Won")
          onGame = False