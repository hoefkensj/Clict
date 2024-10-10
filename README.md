# (n)Vim Is a terrible Editor.
*for all you vim fanboys out there : hold your horses,... ive got reasons!*

## The best editor:
in order to not risk any vim enthousiasts bursting into flames again ill appease them first: Maybe .... , Vim is the best commandline* text editor out there.An with all the commandline text editors ive tried in mind i think that Indeed it probably is the best commandline texteditor availeble. Keep this in mind while reading the rest of the article, as you probably will think at some point : "yeah but do you know an editor that does it better or if you think you can do it better why dont you make your own..."

I'll answer those two questions right here to: 
- first one: If i knew a text editor that did everything better, i wouldnt bother with vim and just use that other text editor. 
- second one: If making a text editor was just that, i might considder givving it a go but as soon as you realize that in order for it to be usable your also building the tooling around it , either as part of a bloated editor or as modules loadable as plugins, besides in what editor would i program it would be my first question,... 


## the best editor can still suck hairy monkeyballs.
so if you think with any of the points i will raize that that is actually a good thing , or even the best possible way of doing that thing id say "its cold up in stockholm in the winter isnt it?" however if you can prove to me that i am objectively wrong, in any way , first ill be happy to learn that (i dont claim to know everything about vim , or know all its features and availeble plugins), and secondly ill be happy to cross out the section , replace it with the objectively good way vim can do it, and attribute the change to you if you want.

## whats wrong with vim? well:
### lets start at the simple things first : Naming stuff

naming stuff differently just to be different is idiotic. iYank should be something apple uses but nobody else. We more or less as a people agreed on the language we use in order to communicate more efficiently ... use it please

- **Yank**: wrong word. if i yank your harddisk out of your pc ,  i'm not making a copy of the disk. If i yank that money out of your wallet , i wont get arrested for counterfitting but for theft ,so pick a name that actually reflects what you do to the best of its abbilities,
- **Delete** Line != copy and overwrite pastebuffer imho i think it means remove these bunch of letters never to be seen again. if in a file manager i cut my keys in order to paste them but have to delete some javascript projecs on my usbe first , i dont want to find out that after pressing shift delete , my keys are gone but i can now paste the javascript keys anywhere i like... (to the vim fanboys, im talking about the naming of stuff here not the capability of doing it another way)
- **Visual (mode)**, i can see my text in normal mode and in insert mode just fine whats extra visual about visual mode? just call it line and block selection mode will ya...? because thats what it actually does. 
- **Motions** you mean hotkeys? or shortcut(-s|-keys), a swipe is a motion `<C-d>` is not , `<Ctrl-d>` is merely pressing the `d` key or whatever key or or even any action on your input device that will result in the shell receiving the ascii char : `d`. But you say given that hotkey is equally bad of a name since you say it doesnt have to be a key on a keyboard that produces that ascii character. and true , but that is actually exactly why hotkey is the best description for it. since yes it does not have to come from a keyboard but if you look at where the name key (-in keyboard) comes from it comes from a mechanism that unlocks something. in this case the 'hot' key unlocks certain behavior in the program ,.. a perfect -and has come full circle- use for the word.

Are these really the hill you guys wish to die on, "this is our lingo our secret handshake , our way of recognising one another"? just change the names if not only to make it easier for beginners to know what to search the help for.

as a form of this is things that arent named wrong but where the rest of the world has chosen a different name for that thing, even if you predate any default word being used for it , at some point you should reallign yourself with the rest of the world and not stubbornly try to be different -because you think you are better- 

## Keybindings:
*yeah but you can change....* , hold your horses, hear me out first

### Defaults! Especially sane ones.
default keybindings that make sense and are intuitive are REALLY important for first time users, and beginners in general, and since "beginner" also means "has no clue about how to configure things" this makes it extra important to pick defaults not because of legacy but because it makes sense or is near what one would expect it to be going by what else is on the market. So why vim has this insane keybindings, still is beyond me, since the people who have been using vim for a year wont mind , as they know how to change them in a heartbeat, if they dont already get changed on the fly by their config files

### ~~hjkl is futuristic 4D Chess...~~ 
' or debt from the stoneage '
At first i figured, the vim devs must have had a good reason to choose these letters , i mmust be missing the idea behind it, so i figured why not jkl; also all unused in vim, (or nothing more often used then moving a cursor anyway), perhaps l so -> is most often used and they wanted to spare your right pinky finger (for 99% of keyboards out there),unlike the blatent attack they pull on your left pinky finger (mor on that later) or maybe up down are that much more used then left,  (i must be doing stuff wrong if i check what keys i use most often when checking the heatmap on my inv.T arrows. down,left,up,right), so i looked it up and im average as studies have shown left,down,right up so vim devs chose to upt the two most often used keys on the same finger.... odd... turns out the guy who wrote vi , pre-default keyboard layouts, had the arrowkeys located on hjkl and they stuck with it :facepalm: (vim guys , stay calm and remember : beginners dont know how to map keys,you do)

ESC , is also the most wrong choice for an editor that amaims for one not to have to leave homerow,.. as you ahve to press that key every 5 seconds and i dont know about you guys but i cant reach esc with my pinky while keeping the rest of my fingers on homerow.
what whould i suggest? anything , caps lock (more on this one later), lalt ralt, rctrl, lctrl, lmeta, rmeta,menu,

no single set of keys to either toggle between the two most used modes or set of keys that rotates between all modes , in normal mode , i goes to insert , R to replace v to visual and jadajada , insertkey goes to insert and then to replace and back to insert. 

in normal mode everything is accessible with a single keystroke, except , saving, quitting , my take on quitting is exit, there is no quit without save... thats just quit. and you can put a safety net , you modified ,.... wish to save y/n or since you use swp files any way just quit and dont delete the swp. why cant wq just save quit, without having to do the : thing first - but sir its a command and...- then wtf is the whole normal mode thing for? and i mean common especially for things you need every fucking time you edit a file open save quit save as different name nmew file ,dup file,, and seriously q+a, and then another ! just because i 

next topic: wtf is going on with end of line not being end of line, but almost end of line... same for pasting by default, any one ever pasted a piece of text and needed to insert text at the next to last character you pasted? anyone ? ever ? , no by default if you paste you  paste the text, have to switch to normalmode (esc yay) move cursor one place over, and go back to insert mode ,... 



### make sense of this:

- **copy (.)** the dot means current line in the weird world of vim but fine -0 and +0 also work just 0 copies to line 1 , wait sec some more weird stuff has to be explained first. so copy copies a line by number to another ~~line by number ~~ to another line below the line by number . So :5copy+3 copies line number 5 to the line 4 places below the line your cursor is on. so with your cursor on line 1 entering `:5copy+2` copies the contents of line 5 to line 4 ,... (not 3) 







# some other mistakes:

dont know if this is the fault of lua, or the fault of (n)vim but if its the fault/the way lua works , (n)vim was wrong in picking lua. period:
you can split your config into as many files as you like , spread over as many folders and subfolders and locations as you want, wich is nice i guess, but make a mistake either syntax wise or against any of the rules set by nvim and none of your 5000 config files wil load when you start , not your keybinds, colorshemes , plugins .... wich is insane and dumb , and about every vim enthousiast has jumped u p behind his keyboard now and has started yelling , that im wrong and that this is not the case ... and i must inform them no im not. --- they want to say but if you use lazy or any other plugin manager and that this wont happen if you do... but last time i checked vim did not come with a plugin manager so vim has no plugin manager to do that for me... someone who obviously also tought nvim was idiotic for picking this behavior put in allot of effort to write a 3rd party plugin that fixes this indeed, but if you buy a car with no engine management , and have to do the procedure each time by hand but someone has automated it, the car manufacturor is still a blatent idiot that should be held accountable for the major failure there

the fun thing about this is that if you made a mistake in the config somewhere and you want to use vim to correct it your not using the vim your used to but the default vim you dont or barely know the usage of (why else would you have changed the default config in the first place)



- keep indents on empty lines ... here is how to do it vim style , remap the enter key to :
  - -> <enter> <enter> [some character] <backspace> , as it wont remove the indents if there has been text on the line , meaning every time you hit enter you are adding and removing stuff thats 5 actions instead of 2 (newline , add indent -> normal with enter ) , not only that  , as you can assume this is great for a nice clean undo history , but it doesnt even work all the time. because this is only the case when you use the enter key to add the lines, anyting else will still not do it (paste)