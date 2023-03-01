embed
<drac2>
downtimeInput = int("&1&") if "&1&".isdecimal() else err("You need to provide a number in order to set the downtime")

#Character stuff
ch = character()
name = ch.name
downtimeActions = 0

#if they have a Downtime counter
if ch.cc_exists("Downtime"):
    downtimeActions = ch.get_cc("Downtime")
    ch.set_cc("Downtime", downtimeInput)
    Body = f"You have {downtimeActions} downtime actions remaining for this cycle\n\n Setting your number of downtime actions to {downtimeInput}"
else:
    ch.create_cc_nx("Downtime", 0, 2, "none", "bubble", 2, None, "Downtime", "Counter that tracks the number of times you have done downtime activities in the current downtime cycle, max twice.")
    err("You did not have the Downtime counter created, I've done that for you. You can check this counter with `!downtime`.")

#The Output

Title= f"{name} has set their remaining downtime."
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
