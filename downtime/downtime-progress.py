embed
<drac2>
Header = ""
#Character stuff
ch = character()
name = ch.name
progress = 0
cc = "Progress"

#if they have a Progress counter
if ch.cc_exists(cc):
    ch.get_cc(cc)
    progress = ch.get_cc(cc)
    Header = f"{name} checks the progress in their current downtime activity."
    if progress >= 100:
        Body = "You have already completed your training, I'm going to reset your counter and you can start again with new training"
        ch.set_cc("Progress", 0)
    elif progress > 0:
        Body = f"You have {progress}% progress in your current downtime activity."
    else:
        Body = "You haven't made any progress yet."
else:
    ch.create_cc_nx("Progress", 0, 100, "none", "default", 0, None, "Progress", "Counter that tracks the amount of progress you have made in your current Training.")
    Header = f"{name} is setting up their Progress tracker"
    Body = f"You did not have the Progress counter created, I've done that for you. You can check this counter with `!downtime progress`."

#The Output

Title= f"{Header}"
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
