import random
import discord
import os
from keep_alive import keep_alive

client = discord.Client()

class discordBlackJack:
  def game():
    
    ##### Discord Methods #######################################
    @client.event
    async def on_ready():
      print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
      if message.author == client.user:
        return

      if '<@!884666305876226088>' in message.content or '<@884666305876226088>' in message.content and message.channel.name == 'bot-stuff':
        onGame = True
        myHand = []
        dealerHand = []
        deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 
                5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 
                8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 
                10, 10, 10, 10, 10, 10, 10, 10]
        
        def giveCardToPlayer(): #Gives Player a Card
          card = random.choice(deck) 
          myHand.append(card)
          deck.remove(card)
        
        def giveCardToDealer():#Gives Dealer a Card
          card = random.choice(deck)
          dealerHand.append(card)
          deck.remove(card)
        
        ### Starting Hand #######################################
        giveCardToPlayer()
        giveCardToPlayer()
        giveCardToDealer()
        giveCardToDealer()

        ### Checks Player message for 'Hit' or 'Stay' ###########
        def check(m):
            return m.content.startswith('Hit') or m.content.startswith('hit') or m.content.startswith('Stay') or m.content.startswith('stay') and m.channel == message.channel

        ### Start of While Loop #################################
        while onGame is True:
          myHandPrint = ", ".join(str(e) for e in myHand)
          dealerHandPrint = ", ".join(str(e) for e in dealerHand)

          await message.channel.send("Dealer's Hand: "+ str(dealerHand[0]) + ", ?" + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + "\n'Hit' or 'Stay'?")
        
          sum = myHand[0] + myHand[1]
          sumOfDealer = dealerHand[0] + dealerHand[1]

          if sum == 21:
            await message.channel.send("BlackJack!: You Won")
            onGame = False

          msg = await client.wait_for('message', check=check)

          decision = msg.content

          if decision.startswith('Stay') or decision.startswith('stay'): ### STAY ###################
            sum = 0
            for i in myHand:
              sum = sum + i

            if sumOfDealer <= 16:
              giveCardToDealer()

              sumOfDealer = 0
              for i in dealerHand:
                sumOfDealer = sumOfDealer + i
            
            dealerHandPrint = ", ".join(str(e) for e in dealerHand)

            ### A Lot Of Condition Code Comparing Dealer and Player Hands########
            ### Could be created as a method ####################################
            if sumOfDealer == 21:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nDealer Wins")
            elif sumOfDealer > 21:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nDealer Bust: You Won")
            elif sumOfDealer >=17 and sum > sumOfDealer:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nYou Won Against Dealer")
            elif sumOfDealer <= 16 and sum > sumOfDealer:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nYou Won Against Dealer")
            elif sumOfDealer == sum:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nDraw: You Lost Against Dealer")
            else:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nDealer Wins")  

            onGame = False
            break
          elif decision.startswith('Hit') or decision.startswith('hit'): ### HIT #####################
            giveCardToPlayer()

            sum = 0
            for i in myHand:
              sum = sum + i
            
            myHandPrint = ", ".join(str(e) for e in myHand)

            if sum > 21:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nBust: You Lost")
              onGame = False
            if sum == 21:
              await message.channel.send("Dealer's Hand: "+ dealerHandPrint + " = " + str(sumOfDealer) + "\n" + str(message.author).split("#",1)[0] + "'s Hand: " + myHandPrint + " = " + str(sum) + "\nBlackJack: You Won")
              onGame = False
        return

    keep_alive()
    client.run(os.environ['BotToken'])