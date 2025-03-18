Hi everyone I'm doing a course on speech synthesis and for part of my project I'm implementing a greedy algorithm that tries to create an optimal ordering of a set of utterances such that for every new utterance in the list we get the maximum number of new diphones. thanks bye.

Next steps:

determine hypotheses, finalize methodology, run it, WRITE DOWN numbers and SAVE AND LABEL figures!!

specifically:
- reread the cmu arctic paper to see when they stop selecting (and other methodology decisions that we can use and then cite :)
- read over my own notes about script selection, check my notebook!!
- rewatch the script selection videos

NOTES:
- we have NOT changed the end behavior to be 'either we have this many utterances or we got all of the diphones'
- another metric by which to compare methods could be counting how many utterances they need to get every diphone. or something
- we can totally put pseudocode in this paper yeah?

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
    - if an utterance is too long, but it includes a word that we consider to be domain-specific (i.e. HMM, Gaussian, Cepstrum, etc), we delete some of the utterance. In some cases
        - e.g. ( henrySimon_00303 "But if you go back to look at the material on token passing, you'll realize that we can ask the tokens to remember anything at all while they're passing through the HMM states, not just the ends of words" ) becomes "we can ask the tokens to remember anything at all while they're passing through the HMM states"
    - Hilariously (I think), one of the longest utterances that we had to remove from the data was "The sort of things that you might include in your script design might be: choosing sentences that are easy to read out loud, so that your speaker can say them fluently without too many mistakes; you might want to cover low-frequency linguistic forms such as questions; you might want to boost the coverage of phrase-final and phrase-initial units, because in long sentences they're very rare; and you might want to include some domain-specific material, if you think your final system is going to be more frequently used in a particular domain (for example, reading out the news, or reading out emails, or something really simple like telling the time)"
    - I also think that we can prune in real time, when we get into the studio. yk?

- HEY: AFTER THAT PRUNING, ID LIKE ONE FINAL PHONE AND/OR DIPHONE HISTOGRAM
    - and also, if we removed the only copy of any of the things, I wanna know about it
    - I actually would also love one of these for every single voice we build (if that's possible :)
    # WE WILL MAKE ONE OF THOSE. YES/

# Notes on test sentences:

I'm gonna have a few from papers, and some of these are going to have MATH in them. As we know, Festival's front end isn't super capable of dealing with that, which is totally a reason to bring up sequence to sequence models, cuz they could just look at the text and say oh! C(x1) means this, so long as it's seen that in the data, whereas with unit selection and a text to phone front-end that's MUCH harder.

The following are the 8 phrases I've chosen to act as domain-specific test phrases, their sources, and where I got them from.
Speaking of Domain, the field evolves so fast, fundamental stuff important, same thing w this voice, yada yada.

## First 3: utterances from videos from modules 6 and beyond

For example, we're getting some spurious pitch marks where there's no voicing just because this unvoiced speech happens to have some energy around F0 by chance, and that happened to lead to some zero crossings.
    - Has terminology, is long, great
    - From Module 6: Epoch detection video

Obviously, to do that, we need to add duration information, so we're going to have to have a duration model that helps us get from the linguistic timescale out to the fixed frame rate.
    - Terminology, and goes over an important issue
    - Module 8: Doing Text-to-Speech

And we'll use that error as a signal to send back through the network to backpropagate, and it will tell the weights where they need to increase or decrease.
    - More terminology
    - Module 8: Training a Neural Network


## Next 9: taken from readings!

This could be as simple as a phoneme sequence, but for better results it will need to include supra-segmental information such as the prosody pattern of the speech to be produced
    - Says stuff like supra-segmental
    - From Simon King's beginner's guide to parametric speech synthesis

The target cost, Ct (ui, ti) , is an estimate of the difference between a database unit, ui, and the target, ti, which it is supposed to represent
    - This sentence has mathematical notation, which is gonna be HARD for unit selection to handle. (usecase for character input rather than linguistic specification)
    - This is from the Hunt and Black paper on CHATR form module 3

Next the Festvox dataset_select script was run to search for the subset of the 52K nice utterances having the best diphone coverage
    - From the CMU Arctic paper
    - Terminology, and also the NAME of a thing, which of course is gonna cause issues
    - Also number

The chief disadvantage is the relatively large time window over which the auto-correlation must be computed in order to cover adequately F0 ranges encountered in human speech
    - From the RAPT paper on autocorrelation and F0 stuff
    - Terms, but honestly this one seems fairly do-able

Given Sp, p = 0,1,2,..., a sampled speech signal with sampling interval T = 1/Fs, analysis frame interval t, and analysis window size w at each frame we advance z = t/T samples with n = w/T samples in the autocorrelation window
    - Also from RAPT
    - WOOF though that's a doozy

F0 values are averaged over every input symbol using the extracted durations d (Figure 3)
    - From the fastpitch paper, figure reference whatever

The model demonstrates how conditioning on prosodic information can significantly improve the convergence and quality of synthesized speech in a feed-forward model, enabling more coherent pronunciation across its independent outputs, and lead to state-of-the-art results
    - From the fastpitch conclusion, classic verbose sentence tbh

We train a neural language model to generate an acoustic code matrix C conditioned on a phoneme sequence x
    - Half a sentence from the VALL-E paper
    - That's like the thing. In-database and out of database concepts yk

We prepend the transcription phoneme of the enrolled speech to the phoneme sequence of the given sentence as the phoneme prompt, and use the first layer acoustic token of the enrolled speech as an acoustic prefix
    - A sentence from VALL-E paper, edited to remove a token that I myself didn't even know how to pronounce
    - Totally a cool sentence u know the vibes