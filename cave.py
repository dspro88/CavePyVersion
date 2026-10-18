import random
import time
import array as arr
import csv
# listened to:
# Busta Rhymes -- Extinction Level Event: The Final World Front'
class Character:
    def __init__(self, name, health, attack, defense, timesPlayed, timesWon, timesLost, treasureEarned, totalRolls):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.timesPlayed = timesPlayed
        self.timesWon = timesWon
        self.timesLost = timesLost
        self.treasureEarned = treasureEarned
        self.totalRolls = totalRolls
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")
def save_stats(player):
    with open('stats.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player.name, player.timesPlayed, player.timesWon, player.timesLost, player.treasureEarned, player.totalRolls])
def introduction():
    print("""You find yourself inside of a dark cave. The air is damp and the walls are covered in moss. You must navigate through the cave safely as there are dangers lurking everywhere.""")
    print()
def statReadout(name, timesPlayed, timesWon, timesLost, treasureEarned, totalRolls):
    print(f'{name}!!! You have played {timesPlayed} times, won {timesWon} times, and lost {timesLost} times. You have earned {treasureEarned} treasure. You have rolled {totalRolls} times in total.')
    print()
def main():
    playAgain = 'yes'
    player = Character("Bucky Bullshit", 100, 10, 0, 0, 0, 0, 0, 0)
    while playAgain == 'yes' or playAgain == 'y':
        player.timesPlayed += 1
        statReadout(player.name, player.timesPlayed, player.timesWon, player.timesLost, player.treasureEarned, player.totalRolls)
        time.sleep(2)
        print('Generating cave...')
        caveLength = random.randint(25, 500)
        caveData = arr.array('i', [0] * caveLength)
        x = 0
        while x < caveLength:
            caveData[x] = random.randint(0, 3)
            x += 1 
        stillAlive = True
        player.health = 100
        position = 0
        time.sleep(2)
        introduction()
        while stillAlive:
            print(f'Rolling....................................')
            time.sleep(2)
            print()
            diceRoll = random.randint(1, 12)
            print(f'You rolled a {diceRoll}')
            player.totalRolls += 1
            position = position + diceRoll
            time.sleep(2)
            print()
            if position >= caveLength:
                print(f'You have reached the end of the cave. You win!')
                player.timesWon += 1
                print(f'Saving data... Please do not close the program or power off your computer.')
                time.sleep(2)
                save_stats(player)
                print(f'Data saved successfully!')
                time.sleep(2)
                break
            '''
            0 = safe
            1 = monster
            2 = fairy
            3 = toxic gas
            '''
            if caveData[position] == 3:
                print(f'It smells weird in here... Toxic gas fills the air and you take damage!')
                damage = random.randint(10, 100)
                print(f'You take {damage} damage from the toxic gas!')
                if damage > 69:
                    print(f'Phil Swift: "NOW THATS A LOTTA DAMAGE!"')
                player.take_damage(damage)
                if player.health <= 0:
                    stillAlive = False
                    player.timesLost += 1
                    print(f'Saving data... Please do not close the program or power off your computer.')
                    time.sleep(2)
                    save_stats(player)
                    print(f'Data saved successfully!')
            if caveData[position] == 2:
                print(f'A fairy appears and heals you for a certain amount of health!')
                heal = random.randint(10, 100)
                player.health += heal
                if heal > 69:
                    print(f'Phil Swift: "NOW THATS A LOTTA HEALING!"')
                print(f'You have been healed for {heal} health. You now have {player.health} health.')
                time.sleep(2)
            if caveData[position] == 1:
                print(f'A monster appears and attacks you!')
                damage = random.randint(5, 100)
                print(f'The monster deals {damage} damage to you!')
                if damage > 69:
                    print(f'Phil Swift: "NOW THATS A LOTTA DAMAGE!"')
                player.take_damage(damage)
                if player.health <= 0:
                    print(f'GAME OVER!!!!')
                    stillAlive = False
                    player.timesLost += 1
                    print(f'Saving data... Please do not close the program or power off your computer.')
                    time.sleep(2)
                    save_stats(player)
                    print(f'Data saved successfully!')
                time.sleep(2)
            elif caveData[position] == 0:
                print(f'You have safely navigated through the cave and found treasure!')
                treasure = random.randint(100, 1000)
                print(f'You have found {treasure} treasure!')
                print(f'You now have {player.treasureEarned + treasure} treasure in total.')
                player.treasureEarned += treasure
                time.sleep(2)
            pass
        # COMMENT THE LAST TWO LINES BELOW TO PREVENT THE GAME FROM ASKING TO PLAY AGAIN
        # print('Would you like to try again? (yes or no)')
        # playAgain = input()
if __name__ == "__main__":
    main()