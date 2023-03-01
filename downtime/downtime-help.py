embed
<drac2>
#The Output
Body= f"Downtime commands:\n\n"
Body= f"{Body}!downtime\nWhen you first run this command, it will set up your downtime counter, afterwards it will output the amount of remaining downtime actions you have.\n\n"
Body= f"{Body}!downtime setup\nThis is a universal set-up command. It's the same as running `!downtime` and `!downtime progress` without having the counters set up.\n\n"
Body= f"{Body}!downtime set\nThis will manually set the number of downtime actions you have, modifying the custom counter. This is the same as doing: `!cc Downtime set x`.\n\n"
Body= f"{Body}!downtime reset\nThis sets the amount of downtime you have to 0, modifying the custom counter. This is the same as doing: `!cc Downtime set 0`.\n\n"
Body= f"{Body}!downtime progress\nWhen you first run this command, it will set up your progress counter, afterwards it will output the amount of progress you have made in your downtime training.\n\n"
Body= f"{Body}!downtime progress set\nThis will manually set the amount of progress you have, modifying the custom counter. This is the same as doing: `!cc Progress set x`.\n\n"
Body= f"{Body}!downtime progress reset\nThis sets the amount of progress you have to 0, modifying the custom counter. This is the same as doing: `!cc Progress set 0`.\n\n"
Body= f"{Body}!downtime train <skill/language/tool> <training name> <bonus>\nThe first input is the type of training you are attempting, the only valid inputs are skill, language, and tool. The second input is the name of the training you are attempting, please be accurate in your spelling. The third argument is any optional bonuses you have, such as paying extra per +1 you want to receieve.\n\n"
Body= f"{Body}!downtime research <spell name> <spell level> <bonus>\nThe first input is the name of the spell you are trying to learn. The second input is the level of that spell, please be accurate as the harder the spell, the harder it is to learn. The third input is any optional bonuses you have, such as paying extra per +1 you want to receieve.\n\n"
Body= f"{Body}!downtime scribe <spell name> <spell level> <proficient>\nThe first input is the name of the spell you are trying to scribe. The second input is the level of that spell, please be accurate as the higher the level, the more expensive the spell. The third input is whether you are proficient in the spell, the spell is cheaper if you are. Note: if you do not provide a yes/no to proficiency, the alias will assume you are not proficient.\n\n"
Body= f"{Body}!downtime help\nDisplays this message."
Title= f"Downtime help"
Desc= f"{Body}"
</drac2>
-title "{{Title}}"
-desc "{{Desc}}"
-footer "!downtime made by @Pocky Jocky#8068"
