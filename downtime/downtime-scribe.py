embed
<drac2>
#input
spell = str("&1&")
spellLevel = int("&2&") if "&2&".isdecimal() else err("You need to provide a spell level as a number")
prof = str("&3&")

#Character stuff
ch = character()
name = ch.name
downtimeActions = 0
cost = 0
prof = prof.lower()
downtimeRequired = 0

if prof == "yes":
    proficient = "are"
elif prof == "no":
    proficient = "are not"
else:
    prof = "no"
    proficient = "did not provide whether you were proficient in so I'm going to assume you are not"

if spellLevel == 0:
    if prof == "yes":
        cost = 15
    elif prof == "no":
        cost = 18
    downtimeRequired = 1
elif spellLevel == 1:
    if prof == "yes":
        cost = 25
    elif prof == "no":
        cost = 30
    downtimeRequired = 1
elif spellLevel == 2:
    if prof == "yes":
        cost = 100
    elif prof == "no":
        cost = 120
    downtimeRequired = 1
elif spellLevel == 3:
    if prof == "yes":
        cost = 250
    elif prof == "no":
        cost = 300
    downtimeRequired = 1
elif spellLevel == 4:
    if prof == "yes":
        cost = 500
    elif prof == "no":
        cost = 600
    downtimeRequired = 1
elif spellLevel == 5:
    if prof == "yes":
        cost = 1000
    elif prof == "no":
        cost = 1200
    downtimeRequired = 2
elif spellLevel == 6:
    if prof == "yes":
        cost = 2500
    elif prof == "no":
        cost = 3000
    downtimeRequired = 2
elif spellLevel == 7:
    if prof == "yes":
        cost = 5000
    elif prof == "no":
        cost = 6000
    downtimeRequired = 3
elif spellLevel == 8:
    if prof == "yes":
        cost = 7500
    elif prof == "no":
        cost = 9000
    downtimeRequired = 4
elif spellLevel == 9:
    err("Learning 9th level spells is currently not supported.")
else:
    err("You provided a spell level that is not supported, please try again with a non-decimal number that is 0-8")

#populate counters
if ch.cc_exists("Downtime"):
    downtimeActions = ch.get_cc("Downtime")
    if downtimeActions > 0:
        if downtimeActions - downtimeRequired >= 0:
            downtimeActions -= downtimeRequired
            Body = f"Downtime tracker: You will have {downtimeActions} downtime actions remaining for this cycle after this action.\n\n"
        else:
            downtimeRequired -= downtimeActions
            downtimeActions = 0
            Body = f"Downtime tracker: You will have {downtimeActions} downtime actions remaining for this cycle after this action.\n You will need to pay {downtimeRequired} more downtime actions to finish this task.\n\n"
        ch.set_cc("Downtime", downtimeActions)
    else:
        #todo: check the current date and output when the next cycle starts.
        err("You do not have any downtime actions remaining for this cycle, please wait till the next cycle to perform this action.")
else:
    err("You did not have the Downtime counter created. Please run `!downtime` before continuing.")

Body = f"{Body}You are looking to scibe {spell} into a scroll. For a level {spellLevel} spell that you {proficient} proficient in, the cost to scribe this spell is {cost}gp.\n\n"

#The Output

Title= f"{name} is trying to scribe {spell}."
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
