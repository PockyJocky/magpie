# magpie
Magpie Alias Suite:

Magpie's Magic Item Search:

!search "<item>" "<rarity>" optional: <bonus>

Your Reputation Precedes You

Twice a month (resets on the 1st and 15th), you can contact Magpie the Fence to find a specific item. This is a straight d20 roll with a set DC based on the item's rarity: 5 for Common, 10 for Uncommon, 15 for Rare, 20 for Very Rare, 25 for Legendary, and 30 for Artifact. If the roll beats the DC by 5 or more, then congratulations! Magpie can find it and you can purchase it outright. If the roll equals the DC or beats it by less than 5, then Magpie has heard rumors of the item, where it might be located, and what you might have to do to get your hands on it. This is a plot hook! Gather four other Pathfinders to go and seek out the loot, and one of our DMs will run an encounter for you. This may be a single combat encounter, an RP event, or something else that matches the item's lore and value, but generally will be less involved than a full quest. (Or, if it works out, the encounter can be worked into an existing/occurring quest.) If successful, the item is yours (in addition to the usual XP and GP rewards).

This alias helps automate these checks.





Magpie's Downtime Dosser:

There is a collection of things you can do while not working with the group. Go ahead and take a gander.

Downtime commands:

!downtime
When you first run this command, it will set up your downtime counter, afterwards it will output the amount of remaining downtime actions you have.

!downtime setup
This is a universal set-up command. It's the same as running !downtime and !downtime progress without having the counters set up.

!downtime set
This will manually set the number of downtime actions you have, modifying the custom counter. This is the same as doing: !cc Downtime set x.

!downtime reset
This sets the amount of downtime you have to 0, modifying the custom counter. This is the same as doing: !cc Downtime set 0.

!downtime progress
When you first run this command, it will set up your progress counter, afterwards it will output the amount of progress you have made in your downtime training.

!downtime progress set
This will manually set the amount of progress you have, modifying the custom counter. This is the same as doing: !cc Progress set x.

!downtime progress reset
This sets the amount of progress you have to 0, modifying the custom counter. This is the same as doing: !cc Progress set 0.

!downtime train <skill/language/tool> <training name> <bonus>
The first input is the type of training you are attempting, the only valid inputs are skill, language, and tool. The second input is the name of the training you are attempting, please be accurate in your spelling. The third argument is any optional bonuses you have, such as paying extra per +1 you want to receieve.

!downtime research <spell name> <spell level> <bonus>
The first input is the name of the spell you are trying to learn. The second input is the level of that spell, please be accurate as the harder the spell, the harder it is to learn. The third input is any optional bonuses you have, such as paying extra per +1 you want to receieve.

!downtime scribe <spell name> <spell level> <proficient>
The first input is the name of the spell you are trying to scribe. The second input is the level of that spell, please be accurate as the higher the level, the more expensive the spell. The third input is whether you are proficient in the spell, the spell is cheaper if you are. Note: if you do not provide a yes/no to proficiency, the alias will assume you are not proficient.

!downtime help
Displays this message.
