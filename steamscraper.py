from bs4 import BeautifulSoup
import requests                          #Modules

#CUSTOM FUNCTION
def _freeGames():             
    if "Free" in txtName:  #if string is in name
        print(txtName.strip())  #had to strip the \n
    

url = ("https://web.archive.org/web/20211118000213/https://store.steampowered.com/") 

#GETS HTML PAGE
results = requests.get(url)                   #requests page
doc = BeautifulSoup(results.text, "html.parser")        #grabs page

#FINDS BLOCK CONTAINING ALL GAMES+PRICES
results = doc.find("div", class_="home_ctn tab_container")  

#FINDS ALL GAMES+PRICES
games = results.find_all("a") #<a> tags


f = open("steamergames.txt", "w")   #opens file in write

#GETTING EACH GAME SEPARATED
for eachGame in games:    #in each <a> tag of the class <"home_ctn tab_container">
    game = eachGame.find("div", class_="tab_item_name")    #finds the name div tag
    price = eachGame.find("div", class_="discount_final_price")     #finds the price div tag
    
    #WRITES TO FILE
    try: 
        gameSpecific = game.string  #turns to strings
        priceSpecific = price.string   #^^
        gamePrice = gameSpecific," ", priceSpecific   #puts strings together with space
        gamePrice = "".join(gamePrice)   #joins the strings together
        f.write(gamePrice + "\n")   #writes the two variables joined as one then goes to next line
        
    
    #PASSING ERRORS
    except:
        pass

f.close() #closes file



#USER INPUTS
userInput1 = float(input("How much are you willing to spend on a game? $"))          #inputs
userInput2 = input("Would you like to see the free games also?(Y/N) ")                #^^

#READS FILE
with open("steamergames.txt", "r") as f:    #open file
    for txtGames in f:   #each game with price in file
        gamesNprice = f.readline()  #reads each line separately
        txtPrice = gamesNprice.partition("$")[2]   #takes prices by finding $
        txtName = gamesNprice.partition("$")[0]   #takes names like this ^  
        try:        #fix error
            txtPrice = float(txtPrice.strip())  #turns price to float and strips whitespace
            if txtPrice < userInput1:    #decision maker
                print(txtName, " $",txtPrice, sep="")    #shows your options
       
        #PASSING MORE ERRORS      
        except:    
            pass

        
        if userInput2 == "y":
            _freeGames()       #calling funtion depending on input
        elif userInput2 == "Y":
            _freeGames()




        
        



