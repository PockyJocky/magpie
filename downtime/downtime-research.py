embed
<drac2>
#input
spell = str("&1&")
spellLevel = int("&2&") if "&2&".isdecimal() else err("You need to provide a spell level")
modifier = int("&3&") if "&3&".isdecimal() else 1 #some wizards will be able to copy spells for cheaper, if not included assume spell is full price

#Character stuff
ch = character()
name = ch.name
downtimeActions = 0
dc = 10 + spellLevel
pb = ch.stats.prof_bonus
intMod = ch.stats.get_mod("int")

cost = (50 * modifier) * spellLevel

#validation
if ch.levels.get("Wizard") == 0:
    err(f"You are not a wizard, Harry. You may still be able to research spells but it will not be automated. Sorry.")

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

Body = f"{Body}You are looking to copy {spell} into your spell book. For a level {spellLevel} spell, the difficulty is {dc}.\n\n"

#Roll the dice

dieResult = roll("1d20") + pb + intMod

Body = f"{Body} **Rolling 1d20 + {pb} + {intMod}\nResult: {dieResult}**"

#Build the result

if dieResult >= dc:
    result = f"You were able to add the spell to your spellbook. Make sure you pay the {cost}gp it requires."
else:
    result = f"Bad luck this time, you are always welcome to try again."

#The Output

Title= f"{name} is trying to research {spell}."
Desc= f"{Body}"
Output = f"{result}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-f "{{Output}}"
-footer "!downtime made by @Pocky Jocky#8068"
