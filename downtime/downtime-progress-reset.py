embed
<drac2>
#input stuff

#Character stuff
ch = character()
name = ch.name
progress = 0

#if they have a Progress counter
if ch.cc_exists("Progress"):
    progress = ch.get_cc("Progress")
    Body = f"You have {progress}% progress in your current downtime activity.\n\n Resetting your progress to 0.\n\n"
    ch.set_cc("Progress", 0)
    Body = f"{Body} Setting your progress to {progressInput}%."
else:
    ch.create_cc_nx("Progress", 0, 100, "none", "default", 0, None, "Progress", "Counter that tracks the amount of progress you have made in your current Training.")
    err("You did not have the Progress counter created, I've done that for you. You can check this counter with `!downtime progress`.")

#The Output
Title= f"{name} has set their progress."
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
