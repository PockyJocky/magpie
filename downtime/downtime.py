embed
<drac2>
Header = ""

#Character stuff
ch = character()
name = ch.name
downtimeActions = 0

#Custom counter stuff
cc = "Downtime"
ccVal = 0

#if they have a Downtime counter
if ch.cc_exists("Downtime"):
    Header = f"{name} checks their remaining downtime."
    ch.get_cc(cc)
    ccVal = ch.get_cc(cc)
    if ccVal >= 1:
        Body = f"You have {ccVal} downtime actions remaining for this cycle"
    else:
        #todo: check the current date and output when the next cycle starts.
        Body = "You do not have any downtime actions remaining for this cycle, please wait till the next cycle to perform another action."
else:
    ch.create_cc_nx("Downtime", 0, 2, "none", "bubble", 2, None, "Downtime", "Counter that tracks the number of times you have done downtime activities in the current downtime cycle, max twice.")
    Header = f"{name} is setting up their downtime counter"
    Body = "You did not have the Downtime counter created, I've done that for you. You can check this counter with `!downtime`."

#The Output

Title= f"{Header}"
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
