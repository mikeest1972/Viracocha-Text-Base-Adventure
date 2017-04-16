# Viracocha text base adventure

from math import *
import time


class Monsters:

    def __init__(self, name, hp, atack, PM, level, loot): # I creat the character with this
        self.name = name
        self.hp = hp
        self.atack = atack
        self.PM = PM
        self.level = level
        self.loot = [loot]
        self.dead = False


class characters(object):


    def __init__(self, name, clase):
        self.name = name
        self.level = 1
        self.kamas = 0 #Kamas is the currency in this world
        self.clase = clase
        self.clasename = clase['Clase']
        self.inte = clase['inte'] #inte is inteligence
        self.luck = clase['luck']
        self.vita = clase['vita']
        self.vitatohp = 2 * self.vita
        self.hp = clase['hp'] + self.vitatohp
        self.stre = clase['str']
        self.PA = clase['PA']
        self.PM = clase['PM']
        self.agi = clase['agi']
        self.atackincreseinstre = 2 * self.stre
        self.x = 0
        self.y = 0
        self.exp = 0
        self.hechizos = []
        self.dead = False
        self.castigo = False
        self.inventory = []




    def IncreseXLocation(self):
        character1Map.x += 1
        character1.x = self.x

    def IncreseYLocation(self):
        character1Map.y +=1
        character1.y = self.y

    def DecreseXLocation(self):
        character1Map.x -=1
        character1.x = self.x

    def DecreseYLocation(self):
        character1Map.y -=1
        character1.y = self.y

    def ChangetoIntX(self):
        return str(self.x)

    def ChangetoIntY(self):
        return str(self.y)

    def SetXequal(self):
        self.x = character1.x

    def SetYequal(self):
        self.y = character1.y

    def Calculatelifewithlevel(self):

        pass

    def AddSpell(self):

        if self.level > 0:

            if self.clase == Sacro:
                PieDeSacrogito = {
                    'Name': 'Pie de Sacrogito',
                    'Elemento': 'stre',
                    'Base Attack': 10,
                    'PA': 3,
                    'Range': 'Short',
                    'Level': 1
                }
                Atraction = {
                    'Name': 'Atraction',
                    'Elemento': 'otro',
                    'Base Attack': 0,
                    'PA': 3,
                    'Range': 'Long',
                    'Level': 1
                }

                Castigo = {
                    'Name': 'Castigo',
                    'Elemento': 'otro',
                    'Base Attack': 0,
                    'PA': 3, 'Range': 'Short',
                    'Level': 1,
                    'Atackincrese per life lost': 1
                }
                self.hechizos.append(PieDeSacrogito)
                self.hechizos.append(Atraction)
                self.hechizos.append(Castigo)

                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass
            pass
        if self.level == 3:

            if self.clase == Sacro:
                Elusion = {
                    'Name': 'Elusion',
                    'Elemento': 'otro',
                    'Base Attack': 0,
                    'PA': 3,
                    'Range': 'Short',
                    'Level': 1,
                    'Atack of enemy for 1 turn': 0
                }
                self.hechizos.append(Elusion)

                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 9:

            if self.clase == 'Sacro':
                print("Spellas were added")
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 12:

            if self.clase == 'Sacro':
                print("spells were added")
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 15:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 20:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 25:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 30:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 35:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 40:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 45:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 55:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 60:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 70:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 80:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 90:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 100:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass
        if self.level == 200:

            if self.clase == 'Sacro':
                pass
            if self.clase == 'Yopuka':
                pass
            if self.clase == 'Ocra':
                pass

            pass








Sacro = {
    'Clase': 'Sacro',
    'hp': 60,
    'PA': 6,
    'PM': 3,
    'vita': 0,
    'str': 0,
    'agi': 0,
    'inte': 0,
    'luck': 0

}
Yopuka = {
    'Clase': 'Sacro',
    'hp': 55,
    'PA': 6,
    'PM': 3,
    'vita': 0,
    'str': 0,
    'agi': 0,
    'inte': 0,
    'luck': 0

}
Ocra = {
    'Clase': 'Sacro',
    'hp': 55,
    'PA': 6,
    'PM': 3,
    'vita': 0,
    'str': 0,
    'agi': 0,
    'inte': 0,
    'luck': 0

}

# Here I will create my players




global character1
global character2
global character3




character1 = characters("Bludyx-acro", Sacro)
character2 = characters("Ira", Yopuka)
character3 = characters("Flechitus", Ocra)
# test to see if it worked
print("test de personaje")
print(character1.name)
print(character1.clase)




class Cascos:

    def __init__(self,name , hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy
        self.name = name




class Capa:

    def __init__(self, hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy

class  Botas:

    def __init__(self, hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy


class  Cinto:

    def __init__(self, hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy


class  Anillo:

    def __init__(self, hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy


class  Amuleto:

    def __init__(self, hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy

class  Arma:

    def __init__(self, hp, stre, agi, inte, luck, PA, PM, kamasforsale, kamastobuy):
        self.hp = hp
        self.stre = stre
        self.agi = agi
        self.inte = inte
        self.luck = luck
        self.PA = PA
        self.PM = PM
        self.kamasforsale = kamasforsale
        self.kamastobuy = kamastobuy



class Recursos:

    def __init__(self, name):
        self.name = name




class Map(characters):

    def __init__(self,name, clase, action):
        super(Map, self).__init__(name, clase)
        self.action = action

    def MoveInMap(self):
        if self.action == "move left":
            characters.DecreseXLocation(character1Map)
            print("Your new cordinates are: ")
            print("x = " + character1Map.ChangetoIntX())
            print("y = " + character1Map.ChangetoIntY())




print(character1.x)
action = "move left"

character1Map = Map("Bludyx-acro", Sacro, action)
print(character1Map.x)
print(character1Map.y)
Map.MoveInMap(character1Map)
print(character1.x)




class Experience():


    def __init__(self, exp, level):
        self.level = level
        self.exptolevelup = 100 * pow(3, ((self.level/10) - 3))
        self.exp = exp
        self.Percetexpadquired = self.exp/self.exptolevelup

    def ExperienceIncrese(self, expincrese):

        self.exp = self.exp + expincrese




    def LevelIncrese(self):

        if self.level < 200:
            if self.exp >= self.exptolevelup:
                self.exp = self.exp - self.exptolevelup
                self.level += 1
                character1.level = self.level
                print("Level UP")
                print(character1.level)
                if character1.level == 3:
                    character1.AddSpell()
                if character1.level == 6:
                    character1.AddSpell()
                if character1.level == 9:
                    character1.AddSpell()
                if character1.level == 12:
                    character1.AddSpell()
                if character1.level == 15:
                    character1.AddSpell()
                if character1.level == 20:
                    character1.AddSpell()
                if character1.level == 25:
                    character1.AddSpell()
                if character1.level == 30:
                    character1.AddSpell()
                if character1.level == 35:
                    character1.AddSpell()
                if character1.level == 40:
                    character1.AddSpell()
                if character1.level == 45:
                    character1.AddSpell()
                if character1.level == 55:
                    character1.AddSpell()
                if character1.level == 60:
                    character1.AddSpell()
                if character1.level == 70:
                    character1.AddSpell()
                if character1.level == 80:
                    character1.AddSpell()
                if character1.level == 90:
                    character1.AddSpell()
                if character1.level == 100:
                    character1.AddSpell()
                if character1.level == 200:
                    character1.AddSpell()
                time.sleep(1)
                self.LevelIncrese()
                self.ShowExpGraphiclly()








    def ShowExpGraphiclly(self):

        self.Percentagegained = ((self.exp)/(self.exptolevelup)) * 100
        print(self.Percetexpadquired)

        if self.Percentagegained <= 5:
            print("Exp bar: ")
            print("EXP  ||=                    ||  ")


        if self.Percentagegained <= 10 and self.Percentagegained > 5:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||==                   ||  ")

        if self.Percentagegained <= 15 and self.Percentagegained > 10:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||===                  ||  ")

        if self.Percentagegained <= 20 and self.Percentagegained > 15:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||====                 ||  ")

        if self.Percentagegained <= 25 and self.Percentagegained > 20:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||=====                ||  ")

        if self.Percentagegained <= 30 and self.Percentagegained > 25:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||======               ||  ")

        if self.Percentagegained <= 35 and self.Percentagegained > 30:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||=======              ||  ")

        if self.Percentagegained <= 40 and self.Percentagegained > 35:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||========             ||  ")

        if self.Percentagegained <= 45 and self.Percentagegained > 40:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||=========           ||  ")

        if self.Percentagegained <= 50 and self.Percentagegained > 45:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||==========          ||  ")

        if self.Percentagegained <= 55 and self.Percentagegained > 50:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||===========         ||  ")

        if self.Percentagegained <= 60 and self.Percentagegained > 55:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||============        ||  ")

        if self.Percentagegained <= 65 and self.Percentagegained > 60:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||=============       ||  ")

        if self.Percentagegained <= 70 and self.Percentagegained > 65:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||==============      ||  ")

        if self.Percentagegained <= 75 and self.Percentagegained > 70:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||===============     ||  ")

        if self.Percentagegained <= 80 and self.Percentagegained > 75:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||================    ||  ")

        if self.Percentagegained <= 85 and self.Percentagegained > 80:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||=================   ||  ")

        if self.Percentagegained <= 90 and self.Percentagegained > 85:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||==================  ||  ")

        if self.Percentagegained <= 95 and self.Percentagegained > 90:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||=================== ||  ")

        if self.Percentagegained <= 100 and self.Percentagegained > 95:
            print("Exp bar: ")
            print(self.Percentagegained)
            print("EXP  ||====================|| LESS THAN 5% ")

        if self.Percentagegained > 100:
            self.LevelIncrese()


class Battle:

    def __init__(self, monster, characterperson):
        self.monster = monster
        self.nameofmonster = monster.name
        self.Monsteratack = monster.atack
        self.monsterlevel = monster.level
        self.monserhp = monster.hp
        self.charactername = characterperson.name
        self.characterClasename = characterperson.clasename
        self.charactorhp = characterperson.hp
        self.dead1 = characterperson.dead
        self.monserdead1 = monster.dead
        self.stre = characterperson.stre
        self.charactorspells = characterperson.hechizos
        self.charactorcastigo = characterperson.castigo
        self.charactorPA = characterperson.PA
        self.charactorlevel = characterperson.level
        self.castigoboost = 0
        self.botin1 = monster.botin[0].name



    def StrngthboostPie(self):
        if self.charactorcastigo == True:
            atack = (2 * self.stre) + self.charactorspells[0]['Base Attack']
            castigobonus = self.castigoboost
            self.monserhp = self.monserhp - (castigobonus + atack)
            print(self.monserhp)
        else:
            atack = (2 * self.stre) + self.charactorspells[0]['Base Attack']
            self.monserhp = self.monserhp - atack
            print(self.monserhp)
    def NostrgthboostPie(self):

        if self.charactorcastigo == True:
            castigobonus = self.castigoboost
            self.monserhp = self.monserhp - (self.charactorspells[0]['Base Attack'] + castigobonus)
            print(self.monserhp)
        else:
            self.monserhp = self.monserhp - self.charactorspells[0]['Base Attack']
            print(self.monserhp)



    def ExcecuteSpellPie(self):
        time.sleep(1)
        print('-3 PA')
        self.charactorPA= self.charactorPA - 3
        print(self.charactorspells[0]['Name'] + "!!!")
        print(self.monserhp)
        if self.stre > 0:
            self.StrngthboostPie()
            if self.monserhp <= 0:
                self.monserdead1 = True
        else:
            self.NostrgthboostPie()

            if self.monserhp <= 0:
                self.monserdead1 = True


    def Castigoforzado(self):
        print(self.charactorspells[2]['Name'] + '!!!!')
        self.charactorPA = self.charactorPA - 3
        print(self.charactorPA)
        self.charactorcastigo = True

    def monstersturn(self):
        print("Monster atacks")
        print(self.Monsteratack)
        self.charactorhp = self.charactorhp - self.Monsteratack
        self.castigoboost = self.castigoboost + self.Monsteratack
        self.Newturn()

    def Newturn(self):
        self.charactorPA = character1.PA
        self.charactorPM = character1.PM
        self.battlemechanism()





    def battlemechanism(self):

        if self.dead1 == False and self.monserdead1 == False:
            print("YOU ARE IN A BATTLE!!!")
            print("""========================================\n========================================""")
            print(self.nameofmonster)
            print("level: " + str(self.monsterlevel))
            print("HP : " + str(self.monserhp))
            print("""========================================\n========================================""")
            print(self.charactername + ', ' + self.characterClasename)
            print("Your spells are: ")
            print(self.charactorspells)
            print('level: '+ str(self.charactorlevel))
            print("HP : " + str(self.charactorhp))
            print('PA : ' + str(self.charactorPA))
            if self.charactorPA > 0:
                battleaction = input("what would you do?")
                if battleaction == "pie":
                    self.ExcecuteSpellPie()
                    self.battlemechanism()
                if battleaction == "castigo":
                    self.Castigoforzado()
                    self.battlemechanism()
                if battleaction == 'pass':
                    self.monstersturn()
            else:
                self.monstersturn()






        else:
            if self.dead1 == True:
                print('You dide AJAJJAJAAJ')
            if self.monserdead1 == True:
                print('You won!!!!')
                print(self.botin1)

class Stores:

    def __init__(self, name, charachter):
        self.name = name
        self.itemsForsale = [SombreroDeJalato]
        self.kk = charachter.kamas
        self.charachterinventory = charachter.inventory

    def diplayItems(self):
        print('\n\nThis is for sale: ')
        for i, v in enumerate(self.itemsForsale):
            print(i, v.name, str(v.kamastobuy))

    def AskForDetails(self):

        itemD = input("On what item would you like to know more about? ")
        print('HP:', self.itemsForsale[int(itemD)].hp, 'Agilidad:', self.itemsForsale[int(itemD)].agi,
              'Fuerza:', self.itemsForsale[int(itemD)].stre, 'Inteligencia:', self.itemsForsale[int(itemD)].inte,
              'Suerte:', self.itemsForsale[int(itemD)].luck, 'PA:', self.itemsForsale[int(itemD)].PA,
              'PM', self.itemsForsale[int(itemD)].PM, 'KK:', self.itemsForsale[int(itemD)].kamasforsale)
        self.diplayItems()

    def buyFromcharachter(self, item):
        kamastoplayer = self.charachterinventory[int(item)].kamastobuy
        print(kamastoplayer)




class AddtoInventory:

    def __init__(self, charachter, object):
        self.person = charachter
        self.inventory1 = self.person.inventory
        self.Object = object

    def AdditemtoInventory(self):

        self.inventory1.append(self.Object)
        print(str(self.FindIndexnumber(self.Object)) + ".- " + self.inventory1[self.FindIndexnumber(self.Object)].name)



    def sellItemFromInventory(self):
        pass

    def ThrowawayItemFromInventory(self):
        throwaway = input('what do you want to throw away (put the number from the inventory: )')
        reasurance = input('Are you shoure you want to throw away ' + str(throwaway))
        if reasurance == 'yes':

            del self.inventory1[int(throwaway)]
            print(self.inventory1[throwaway].name + 'wast thrown away')
        else:
            print('ok')

    def FindIndexnumber(self, object1):
        inde = self.inventory1.index(object1)
        return inde
    def LookAtInventory(self):
        print('\n\nThis is in your inventory: ')
        for i, v in enumerate(self.inventory1):
            print(i,v.name)












# FROM HERE ON IS WHERE I CREATED THE THINGS SO I COULD TEST IT











character1.AddSpell()
print("Sacrogitos spells at level 1")
print(character1.hechizos)


print("The exp necesary for the next level")
# character1exp = Experience(1, 9)
# print(character1exp.exptolevelup)
# print(character1exp.exp)
# character1exp.ExperienceIncrese(10)
# character1exp.ShowExpGraphiclly()

# Here I will define las razas



# here I will create my players









#while True:
    #action = input("Where to move?")
    #Map.MoveInMap(character1Map)



SombreroAventurero = Cascos('Sombrero Aventurero',2, 2, 2, 2, 2, 0, 0, 10000, 10000)
SombreroDeJalato = Cascos('Sombrero de Jalato',2, 2, 2, 2, 2, 0, 0, 10000, 10000)

# Create the monsters
jalatin = Monsters("Jalatin", 20, 4, 4, 1, SombreroAventurero)

# Test monster jalatin
print("Test monster jalatin")
print("Jalatin botin:")
print(jalatin.botin)
print("Jalatin level: ")
print(jalatin.level)
print("Jalatin atack: ")
print(jalatin.atack)
battle1 = Battle(jalatin, character1)
print("Monster in batle atack")
print(battle1.monster.atack)
print("MOnster in abattle name: ")
print(battle1.monster.name)
print("Monster in battle level: ")
print(battle1.monster.level)
print("Character in battle name: ")
print(battle1.charactername)
print(battle1.characterClasename)
# battle1.battlemechanism()


addobject = AddtoInventory(character1, SombreroAventurero)
addobject.AdditemtoInventory()
addobject = AddtoInventory(character1, SombreroDeJalato)
addobject.AdditemtoInventory()
addobject.LookAtInventory()
#addobject.ThrowawayItemFromInventory()

Mercadillo = Stores("Mercadillo", character1)
Mercadillo.diplayItems()
Mercadillo.buyFromcharachter(0)



# print(character1inventory.inventory1[0].name)



# Cascos

#print("Test de sombreo aventurero")
#print(SombreroAventurero.hp)
#print(SombreroAventurero.kamasforsale)

# Anillos
#print("Anillo aventurero")
#AnilloAventurero = Anillo(2, 2, 2, 2, 2, 0, 0, 1000, 1000)
#print(AnilloAventurero.kamastobuy)

# Capas

# Botas

# cinturon

# amuletos

# armas

# recuros

