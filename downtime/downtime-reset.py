embed
<drac2>

#Character stuff
ch = character()
name = ch.name

#if they have a Downtime counter
if ch.cc_exists("Downtime"):
    ch.set_cc("Downtime", 2)
    downtimeActions = ch.get_cc("Downtime")
    Body = f"You have successfully reset your downtime.\n\n Downtime actions: {downtimeActions}"
else:
    ch.create_cc_nx("Downtime", 0, 2, "none", "bubble", 2, None, "Downtime", "Counter that tracks the number of times you have done downtime activities in the current downtime cycle, max twice.")
    err("You did not have the Downtime counter created, I've done that for you. You can check this counter with `!downtime`.")

#The Output

Title= f"{name} has set their downtime."
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
