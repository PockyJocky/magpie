embed
<drac2>
#input
trainingType = str("&1&")
training = str("&2&")
bonus = int("&3&") if "&3&".isdecimal() else 0 #if no there is no third input it will assume there was no bonus

trainingType = trainingType.lower()
training = training.lower()

#input validation
if trainingType not in ["skill", "tool", "language"]:
    err("You provided an unhandled training type, `!downtime train skill`, `!downtime train tool`, or `!downtime train language` are the only valid training types")

if bonus > 5:
    err("The max bonus for training is +5 please do not exceed this.")

training = training.replace("'", "")

if "smith" in training:
    training = "smith's tools"
elif "thieves" in training or "thiefs" in training:
    training = "thieve's tools"

#Character stuff
ch = character()
name = ch.name
downtimeActions = 0
progress = 0
modifier = 0

cost = 25 + (25 * bonus)

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

if ch.cc_exists("Progress"):
    progress = ch.get_cc("Progress")
else:
    err("You did not have the Progress counter created. Please run `!downtime progress` before continuing.")

if progress < 100:
    Body = f"{Body}You currently have {progress}% toward finishing your {training.capitalize()} training.\n\n"
else:
    ch.set_cc("Progress", 0)
    err("You are finished with your training, I have reset your progress counter so you can start new training.")

#which kind of skill/tool/language is it?
skillDifficulty = 2

uncommon = ["stealth", "perception", "investigation", "arcana", "survival", "insight", "abyssal", "celestial", "draconic", "deep speech", "infernal", "primordial", "sylvan", "undercommon", "thieve's tools", "smith's tools"]

if training in uncommon:
    Body = f"{Body} {training.capitalize()} is an uncommon {trainingType} training.\n\n"
    skillDifficulty = 1
else:
    Body = f"{Body} {training.capitalize()} is a common {trainingType} training.\n\n**Note: your progress in common training will appear doubled due to the thresold being half the threshold of uncommon training.**\n\n"

if trainingType == "skill":
    modifier = ch.skills[training].value
else:
    chStats = ch.stats
    modifier = chStats.get_mod("int")

dieResult = roll("1d20") + modifier + bonus

if bonus == 0:
    Body = f"{Body} **Rolling 1d20 + {modifier}\nResult: {dieResult}**"
else:
    Body = f"{Body} **Rolling 1d20 + {modifier} + {bonus}\nResult: {dieResult}**"

#Build the result
adjustedProgress = dieResult * skillDifficulty

ch.mod_cc("Progress", adjustedProgress)

newProgress = ch.get_cc("Progress")

result = f"You have made {adjustedProgress}% on your training. Your progress now reads: {newProgress}/100.\n\nMake sure you pay the {cost}gp for the training session."

#The Output

Title= f"{name} is trying to train their {training.capitalize()}."
Desc= f"{Body}"
Output = f"{result}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-f "{{Output}}"
-footer "!downtime made by @Pocky Jocky#8068"
