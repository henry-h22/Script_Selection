Hi everyone I'm doing a course on speech synthesis and for part of my project I'm implementing a greedy algorithm that tries to create an optimal ordering of a set of utterances such that for every new utterance in the list we get the maximum number of new diphones. thanks bye.

Next steps:

determine hypotheses, finalize methodology, run it, WRITE DOWN numbers and SAVE AND LABEL figures!!

specifically:
- reread the cmu arctic paper to see when they stop selecting (and other methodology decisions that we can use and then cite :)
- read over my own notes about script selection, check my notebook!!
- rewatch the script selection videos
- MAYBE read some of the other papers from that module, see what they're on about. lol.

NOTES:
- we have changed the end behavior to be 'either we have this many utterances or we got all of the diphones'
- another metric by which to compare methods could be counting how many utterances they need to get every diphone. or something

- WE CAN COMPARE PHONES HISTOGRAMS RATHER THAN DIPHONE HISTOGRAMS. THAT ROCKS. YAY!!!!
    - hey MULT script selection really shows off the differences in cost functions visually

next:
- maybe make a scoring function that doesn't normalize for length
    - probably a variant of the aware sPUa, and then we can compare the distributions of those two, ideally easy to see
        - best bit: we can secretly do that quick study last cuz we're like 99% sure of the outcome

- run these actual studies
    - i think we should hold onto as much of this data as possible, so we could graph it in R or do other data stuff to it
    - even just storing it all in a big text file

- SELECT. AN. ACTUAL. SCRIPT. HENRY. PLEASE.
    - I think the takeaway from the first study is that Aware is the best method, because it doesn't leave any diphones on the table
    - Then, it looks like proportional is best, which makes a lot of sense. Yay!
    - We can probably just go ahead and select with that straight away. Boo yah.
    - The CMU paper does two hand-pruning steps, one with visual inspection and one with literally trying to say the phrases and cutting the hard to say ones
        - We should do some version of this. I suppose. Cool. Science!!!

- DO NOT FORGET we also need test phrases in the script that we record on Thursday.
    - Lets make sure that some have jargon that we selected for, and that some don't
    - Side note-- the fact that we want to be able to select entire words when jargon occurs ABSOLUTELY motivates some tweaks to join/target cost
        - namely, we wanna make the join cost more important than the target cost, so that we select whole in-database words and phrases more frequently. YAY!!!!

- it's all coming together fr




NOTES BEING TAKEN DURING THE LITERAL SCRIPT SELECTION:
- Using 'aware' script selection algorithm and 'proportional' scoring
    - selecting 700 utterances, because that's about how many ARCTIC A has pre-prune.

- we now perform the manual pruning step, inspired by the ARCTIC paper
    - we do so by genuinely giving it a go reading out the utterances, and just straight up deleting the ones that I can't naturally read:
        - a: in one breath (too long)
        - b: in one take (too complex)

- HEY: AFTER THAT PRUNING, ID LIKE ONE FINAL PHONE AND/OR DIPHONE HISTOGRAM
    - and also, if we removed the only copy of any of the things, I wanna know about it
        