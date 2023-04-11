embed
<drac2>
#Initializing variables

itemName = str("&1&")
rarity = str("&2&")
bonus = int("&3&") if "&3&".isdecimal() else 0 #if no there is no third input it will assume there was no bonus

ch = character()

checkInfo = "Placeholder Check Info"
checkResult = "Placeholder Check Result"

reputation = 0
itemDiff = 5
itemDiffStr = [ "trivial", "easy", "tough", "hard", "very hard", "almost impossible"]

prices = []

magpieSearchActive = False


#Validate inputs

if itemName == "":
	err("You did not provide an item for the search")

if rarity.lower() == "common":
	itemDiff = 5
	prices.append(int(roll("2d4") * 25))
	prices.append(int(roll("2d4") * 25))
elif rarity.lower() == "uncommon":
	itemDiff = 10
	prices.append(int(roll("2d6") * 50))
	prices.append(int(roll("2d6") * 50))
elif rarity.lower() == "rare":
	itemDiff = 15
	prices.append(int(roll("2d8") * 400))
	prices.append(int(roll("2d8") * 400))
elif rarity.lower() == "very rare" or "very":
	itemDiff = 20
	prices.append(int(roll("2d10") * 2500))
	prices.append(int(roll("2d10") * 2500))
elif rarity.lower() == "legendary":
	itemDiff = 25
elif rarity.lower() == "artifact":
	itemDiff = 30
else:
	err("I could not parse the rarity submitted or you did not provide one")


#Check for the cc

if ch.cc_exists("Reputation"):
	reputation = int(ch.get_cc("Reputation"))
else:
	#make the cc for the player and let them know
	ch.create_cc_nx("Reputation", 0, 20, "none", "default", 0, None, "Reputation", "Points dedicated to acquiring rare and magical items")
	err("You did not have the Reputation Points counter created, I've done that for you. You can check this counter with `!cc Reputation`. Keeping this number up to date is your responsibility.")

#check for the Downtime counter
#populate counters
if ch.cc_exists("Downtime"):
    downtimeActions = ch.get_cc("Downtime")
    if downtimeActions >= 1:
        downtimeActions -= 1
        Body = f"Downtime tracker: You will have {downtimeActions} downtime actions remaining for this cycle after this action.\n\n"
        ch.set_cc("Downtime", downtimeActions)
    else:
        #todo: check the current date and output when the next cycle starts.
        err("You do not have any downtime actions remaining for this cycle, please wait till the next cycle to perform this action.")
else:
    err("You did not have the Downtime counter created. Please run `!downtime` before continuing.")


#Build the body of the information
itemDiffIndex = int(itemDiff / 5 - 1)
bonusStr = "have" if bonus > 0 else "have not"

checkInfo = f"{Body} Greetings {ch.name}, as I understand it, you came to me looking for {itemName}.\n\nThis item is {rarity} so it is {itemDiffStr[itemDiffIndex]} (DC {itemDiff}) to find a lead about and {itemDiffStr[itemDiffIndex + 1]} (DC {itemDiff + 5}) to find this item so that you can just go purchase it.\n\nYou have {reputation} reputation with me so far and you {bonusStr} decided to use that reputation or paid me extra to help the search (the player has applied this bonus manually).\n\n\nReminder: that if you applied Reputation and this roll succeeds, your Reputation may reset. \n\n Find only DC: {itemDiff}\nFind and buy DC: {itemDiff + 5}"

dieResult = roll("1d20") + bonus

bonusStrOutput = f"+ {bonus}" if bonus > 0 else ""

checkInfo = f"{checkInfo}\n\n Rolling 1d20 {bonusStrOutput}\nResult: {dieResult}"


#Build the check result

if dieResult >= itemDiff + 5:
	checkResult = f"I was able to find the {itemName} you were looking for, for direct purchase.\n\nThe cost for this item is going to be {max(prices)}gp.\n\n If you want it for cheap, a lead to find it on your own is worth {min(prices)}gp"
elif dieResult >= itemDiff:
	checkResult = f"I have a lead on where to find the {itemName} you were looking for.\n\nMy fee for finding this lead is {min(prices)}gp"
else:
	sarcasm = " " if reputation == 0 else " I do still owe you a favor."
	checkResult = f"Despite my best effort I was not able to find anything yet, but I'll keep looking if you want.{sarcasm}"


#The Output

Title= f"Magpie is looking for {itemName}"
Desc= f"{checkInfo}"
Output= f"{checkResult}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-f "{{Output}}"
-thumb "https://media.discordapp.net/attachments/828615051161370645/1030086917234114621/image0.jpg?width=378&height=484"
-footer "!search made by @Pocky Jocky#8068"
