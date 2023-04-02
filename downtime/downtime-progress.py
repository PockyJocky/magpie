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
        ch.delete_cc("Progress")
    elif progress > 0:
        Body = progress.desc + f"\nYou have made {progress}% toward your training."
    else:
        Body = "You haven't made any progress yet."
else:
    err("You did not have the Progress counter created, start a new training by doing `!downtime training` running that command for the first time will record what kind of training you are attempting. After that, run `!downtime progress` to track your progress."

#The Output

Title= f"{Header}"
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
