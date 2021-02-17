import nltk
from nameparser.parser import HumanName
from nltk.corpus import wordnet


person_list = []
person_names=person_list
def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)

    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []
#     print (person_list)

text = """
TRIAL  AND   ACQUITTAL.

The Trial of  Mr James Stuart  who was  tried at
the High Court of  Justicary, for beings art and part
in a duel in which Sir   Alexander Boswell   lost his
life, and after a  trial of 18   hours   he  was   acquited
from the Bar

THE Trial of Mr James Smart came on this day. (Monday,
10th June,) before the High Court  of Jucticiary.   The
Indictment having been reard, the Lord Justice Clerk then ask-
Mr Stuart whether he was guilty---answered " My   Lord   I  am
not guilty, "  Mr Cockburn, then made an eloquent and impres-
sive speech, in which he fully denied all the charges   in the in-
dictment ; And  on Mr Cockburn adverting to the death of Sir
A. Boswell, Mr Stuart seemed very murch affected Mr Cock-
burn said, there was not a  friend the   deceased had  felt such
poignant anguish at his heart.    He concluded  by saving, that
Mr Stuart acted under a moral necessity; and that a verdict of
not guilty would be most grateful  to humnilty and  most con-
sistent with the laws.

Solicitor-General.—As no objections had been stated  to the
relevancy of the indictment, he had not to slate in reply.
Earl Rosslyn was the first witness called.

Soliciter General.— Are you acquainted with the gentleman
at the bar? he answered I   am, and  then  went on to state at 
great length and with much  perspiicuity;  all the circumstances
connected with it,

Honouroble John Douglass.—1 was acquainted with Sir A.
Boswell. In the month of March I attended him to an niter-
view with Lord Rosslyn. The interview was in the Waterloo
Hotel. I went with Sir A. into a room where the Earl of Ross-
lyn was was, and he held in his hand, I think, two papers. Lord
Rosslyn mentio ed, that he had called this meeting upon a very
unpleasant business—those papers were copies— that a frind of
his obtained possesson of the originals, which contained obnoxi-
ous passages as to Mr Stuart's character.

Dr Wood.— On the 26th March last. Sir Alexander Boswell
called upon the deponent;—he requested my professional at-
tendence ;— he left my house, and returned soon after ;-—I Then
accompanied him and Mr Douglas in a carriage to Queensferry
afterwards to the village of Auchertool. We then proceeded
to the ground. Mr Stuart and Lord Rosslyn were upon, the
ground also. Lord Rosslyn desired me to remain at sorne space
of ground, But I went forward—I heard the discharge of the
pistols. Mr Listen and I turned our backs for the purpose of
not seeing, when we turned round, upon hearing the fire, we
saw Sir Alexander had fallen—we ran and found that the ball
had entered the middle of the right clavicle. Two bones were
exstracted on the spot, the first by myself, and the second by
Mr Liston. It was my opinion from the first that the wound
was mortal, Sir Alexander said in the course of the journey,
that he was determined to fire in the air.

Mr Liston.—Mr Stuart called upon the deponent to go to
the country along with him. And  when on Fife side, he in-
formed him, he was to fight a duel with Sir Alexander Boswell.
Mr S. said he had no malice against Sir Alexander: he said, if
he had the misfortune to hit him, he wished it might be on the
great toe, as a gentleman in  England did lately on a similar oc- 
casion.  The deponent gave the same evidence as Dr Wood.

Mr Thomas Allan, banker.— Deponent heard of duel shortly
after it happened. He saw Mr Stuar at Calias. Mr Stuart ask-
ed deponent what news. I said the news were bad for him—
then says he, Sir A. is dead, When I told him that was the
case, he burst into tears and was much agitated.

Mr Walker (a tutor in Sir A.'s family)--I am tutor to Sir James
Boswell. I have been tutor in the family for several years and
knew Sir A Boswell. I think the hand-writing of the Whig
Song is not Sir A. nor that of any of the family. The address
seems to be the same with the rest.

The Lord Justice Clerk said the Jury would weigh all thes 
tircumstances seriously in their minds, they would give a verdict
consonant to he he dictates of their own conscience, aud, if in
this case they were nnabled to come to a decided and clear
opinion, the advantage and privilege of that doubt belonged to
the gentleman at the Bar. The Jury chocse Sir John Hope,
Bart as their Chancellor ; and after consulting for a few minutes
in the Jury box the chancellor delivered an unanimous verdict
Not Guilty.  The verdict was received with loud cheers.
"""

names = get_human_names(text)
for person in person_list:
    person_split = person.split(" ")
    for name in person_split:
        if wordnet.synsets(name):
            if(name in person):
                person_names.remove(person)
                break

print(person_names)