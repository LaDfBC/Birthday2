

class Message():
    year_dict = {  # JANUARY
        "1":
            {"1": ["Happy New Year, babe!  Hope you had a good night last night!  Thinking of you through the New Year!  "
                   " Since we're both off work today, let's go have some fun!", None],
                "2": ["Well, today we have to go back to work and the holidays are mostly over, but I wanted to let"
                      " you know how much you mean to me - there's Sea Salt caramel ice cream in the freezer for supper tonight.",
                      ' Enjoy Sea Salt Caramel Ice Cream'],
                "3": ['So what are your New Years Resolutions?  I have no idea as I\'m writing this but we should both'
                      ' make one and keep the other honest about it.  Might make our relationship even better?  I\'m'
                      ' looking forward to another year with you! Have a great day sugar pie!', None],
                "4": ['I love getting ice cream with you and right now that\'s kind of a problem since it\'s the middle'
                      ' of winter and there isn\'t really any place that\'s open right now.  I kind of wish we could just'
                      ' go to a Fritz\'s and get a big bunch of chocolate cookie dough stuff.  Those are fantastic cute'
                      ' little dates we go on and they make me love you as a person just a little bit more.  I know we'
                      ' can\'t go to a real place, but I\'m going to get some stuff from Schnucks tonight and let\'s have'
                      ' some cold sugar', 'Ice Cream \"Date\"'],
                "5": ['Well now that the New Year thing is wearing off, I\'m not sure what to talk about anymore.  So I\'ve'
                      ' decided to start listing all of the little things you do that I found so adorable.  Starting with'
                      ' cuddling up next to my arm and falling asleep there.  It\'s really comforting and I sometimes'
                      ' intentionally stick my arm out so you do it.  You\'re my favorite, most adorable person, honey!', None],
                "6": ['Gonna be totally honest with you, this thing has taken more of my time than any other thing in my'
                      ' life thus far, save for extremely major life achievements.  Not that I want you to feel guilty'
                      ' or anything but more that it\'s teaching me that there are a lot more things about you that are'
                      ' just so easy to love and I tend to focus on the worst side of everything and everybody and that\'s'
                      ' really not fair for you and I\'m sorry. So today is about your legendary, amazing patience.  You'
                      ' are the most patience, understanding, focused person ever and I cannot express enough how important'
                      ' that is to me.  You are the most amazing person ever and I will always love you darlilng!', None],
                "7": ['How about a shorter one for today?  I want you to have a very relaxing Sunday so I\'m going to'
                      ' get food for and make your lunches and all of the dinners this week, clean the kitchen, living'
                      ' room, and bathroom and you\'re going to lay on the couch and relax and text me if you ever want'
                      ' anything at all. Love you!', 'Relaxing Day - I do everything'],
                "8": ['Back to work Monday, and it\'s like the first real one after the Holiday season. I just wanted to'
                      ' tell you about how much your interest in silly things is adorable and fantastic.  In this instance'
                      ' I\'m talking about Christmas and how you basically have a tree setup before you have a Thanksgiving'
                      ' turkey.  And stockings everywhere.  And pine rope everywhere.  And more holiday dinnerware'
                      ' than we have normal dinnerware.  Hoping to get you a little bit happier to start off the week'
                      ' because you\'re thinking about Santa. I love you and hope you\'re happy.  I also think I\'m dating'
                      ' a horse girl but she\'s actually a reindeer girl.', None],
                "9": ['Hey darling.  You\'re sexy. I want to tie you up tonight.  And then I want to slap your ass and bite'
                      ' you and get you off.  I\'m going to massage you a little bit and then I\'m going to rip your pants'
                      ' off, shove you down and make you get the bed wet.  Also, I may have modified the program to'
                      ' send this one a bit later so you got it at work. Whoops. My bad.', 'Let me put some handcuffs on you'],
                "10": ['So you have this opinion that men are terrible gift givers and I\'m randomly thinking about it right'
                       ' now.  While it\'s mildly true that dudes are just not as good at figuring out the cute things'
                       ' that other people will enjoy, I don\'t necessarily think that it\'s true all the time.  I bring'
                       ' this up today because Kay sent out another deal and I might have bought you something. Uh oh.', None],
                "11": ['You know, you always try to put yourself out there as a mean girl who isn\'t nice or anything but'
                       ' I kind of think the opposite is true. You\'re generally extremely thoughtful and fun, caring an'
                       ' awful lot what people think about you and the people you care about.  Just thought I\'d bring it'
                       ' up today because I was thinking about it and I love how much you care, even if it does make'
                       ' us get a little angry at each other every so often. You\'re clearly very into wanting people'
                       ' to be happy, and it\'s just one more super cute way that you\'re basically the best girlfriend'
                       ' ever.  I love you deeply, shortcake, and hope you have a fantastic day today.', None],
                "12": ['Remember when we were flying to Mexico and you laid on my arm for a couple minutes? Yeah, do that'
                       ' more often.  You\'re a very cuddly person and uncharacteristicly warm when you hang on to me.'
                       ' Ok, so these notes are supposed to be about you so the point here is that you\'re an expert'
                       ' cuddler and maybe you can use that to your advantage.  I\'m not sure how, but hey, thought maybe'
                       ' if you tried to cuddle more often then maybe it\'d eventually make it\'s way to me.  Oh, also,'
                       ' the electric blanket is fantastic.  Love you babe!', ''],
                "13": ['Hey, I like your legs.  Funny enough, this is the first note I\'ve written about them since they\'re'
                       ' definitely one of the best sets I\'ve ever encountered. So anything I can do to help you keep those'
                       ' beautiful parts of your body around, I\d be happy to try. So yeah, weird creepy note, huh?'
                       ' I don\'t know about you, but I figured that all of your best qualities should be included in these'
                       ' things and legs are absolutely one of them.  Ok, end weird one.  Love you!', None],
                "14": ['Ok, how about a better note that\'s not totally weird?  You\'re absolutely brilliant and come'
                       ' up with solutions to any issues that arise so much quicker than me.  Not only that but it\'s'
                       ' equal parts super fun and totally frustrating to debate with you.  Anyway, despite what you may'
                       ' think sometimes, I absolutely enjoy dating a smart girl and this is definitely the best relationship'
                       ' I\'ve ever been in.  So keep on being intelligent all the time and frustrating me when I try'
                       ' to outsmart you...I might secretly love it.', None],
                "15": [
                    "So while I write this, we're watching Once, and you're writing in your Bullet Journal and I wanted"
                    " to let you know how hard it is to avoid tackling you and kissing you like 500 times.  You're "
                    " absolutely amazing and I love you in every possible way.", None],
                "16": [
                    "It's cold outside today, so let's put on a coat and jacket and get nice and cold so I can make you "
                    " hot chocolate and cuddle under a warm blanket!  You choose the movie to cuddle to!",
                    ' Hot Chocolate and Cuddles'],
                "17": ['', ''],
                "18": ['', ''],
                "19": ['', ''],
                "20": ['', ''],
                "21": ['', ''],
                "22": ['Hey!  Happy Anniversary!  So I know we promised not to give each other gifts this year, but can'
                       ' I at least take you out to a fancy dinner?  ', ''],
                "23": [' 2 years and a day.  Ever think we\'d make it this far?  I for one still think you\'re getting'
                       ' screwed out of an awesome relationship with some hot dude like Thor...or Blake Lively.  You could'
                       ' absolutely get either one of them and live in a mansion with people to cook and clean for you.  '
                       'But I\'m glad you\'re with me and not some super attractive Hollywood star.  Thanks for being'
                       ' so sweet and kind and level-headed and generally so cool about everything!', None],
                "24": ['', ''],
                "25": ['', ''],
                "26": ['', ''],
                "27": ['', ''],
                "28": ['I\'m writing this one the night after I did the first work on the dresser/bar that\'s going in'
                       ' the basement and it\'s cold.  Anyway, I love how you always give great advice, even though I'
                       ' don\'t listen anyway near often enough (And I\'m really sorry for that!).  Just wanted to let'
                       ' you know how much I love you being persistent and trying to help everyone around you to be better'
                       ' people!', None],
                "29": ['', ''],
                "30": ['', ''],
                "31": ""},
        "2": #FEBRUARY
            {"1": ['', ''],
              "2": ['', ''],
              "3": [
                  "Tonight, I want you to relax as I pop some kettle corn so you can enjoy a snack before bed.  Love you bunches,"
                  " Honey Bear!", None],
              "4": [
                  "You\'re smart, sexy, funny, cute, thoughtful, sweet, cuddly, brilliant, good at planning, good at cooking,"
                  " great at sex, fun to be around, and just generally an amazing person!  \"You are the best thing that\'s ever"
                  " been mine!\" -- Taylor Swift", None],
              "5": [
                  'I thought about making one of these near your birthday this year that just said "Marry Me?" and then'
                  ' have a ring waiting for you that I would show you when you read the message, but decided that was probably'
                  ' too soon.  Soooooo, maybe we go to a jewelry store and you just pick out a ring or bracelet that you think is cute?',
                  "Get a ring?"],
              "6": ['This is the second time I thought about sitting and eating ice cream with you and thought it\'d'
                    ' be a good time to talk about it and how much I miss you when you\'re not around.  I love those'
                    ' little moments where we\'re just eating something sweet and hanging out because of how you'
                    ' make it such a cute adorable little thing even when it\'s nothing at all.  So just another'
                    ' note about how much fun you are and how you  make everyone around you better and happier.', None],
              "7": ['', ''],
              "8": ['', ''],
              "9": ['I love you more than all of the flakes of snow in Antartica, all of the water in the ocean, and'
                    ' leaves in all of the rainforests anywhere.  I hope you know that I would do anything to make you happy'
                    ' and that this is just a reminder that I\'ll always be there for you!', None],
              "10": ['', ''],
              "11": ['', ''],
              "12": ['', ''],
              "13": ['Hey darling!  Today is Mardi Gras! Let\'s go to the bar and get a drink and some Irish food! Or if you'
                     ' want to stay home, I\'d be happy to serve you something and make Reubens or French Dips!',
                     ' Mardi Gras Drinks and Sandwiches - 2/13'],
              "14": ['', ''],
              "15": ['', ''],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['', ''],
              "19": ['', ''],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ""},
        "3": #MARCH
            {"1": ['', ''],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['Never understood why you don\'t love Eggnog.  Anyway, had a neat idea.  For a while, I was considering'
                    ' rewriting this thing in Spark (the iPhone language) after you switched from Android and even learned'
                    ' a little bit about it. Well, you mention every so often that you have these cool ideas for something'
                    ' to do on a phone and I bet you could market the hell out of it.  So either choose an idea you have now'
                    ' or your next one you really like and I will make the app for it!  Love you babe, and hope this gets'
                    ' your creative juices flowing!',
                        'Choose an app/idea for me to write for you.  It can\'t be a sexbot.'],
              "6": ['You\'re currently at Universal Orlando and I totally miss you right now.  It doesn\'t help that'
                    ' I\'m still writing these notes for you and thinking about you all the time.  So anyway, you'
                    ' sent over a picture of drinking cocoa and walking through a castle and looking at really cool'
                    ' dragon statues.  But I was focusing on was your smile and how much fun you were having. Look, we'
                    ' had a fight before you went on vacation and I\'m totally regretting it right now because I was'
                    ' being stupid and angry and stressed.  So this another way in the future apology for almost'
                    ' totally ruining your vacation.  I love you a ton and want to keep you forever.  Hope you have both'
                    ' a good past week in Universal and a good present week!', None],
              "7": ['Hey, we both like ice cream.  Can you believe it\'s already been a month since the last time'
                    ' you read a note about it? Anyway, I like your smile and your drive and how much you care about'
                    ' everything so just wanted to take this morning to let you know that I don\'t want to ever leave'
                    ' you at all.  Oh, also, you\'re easily one of the smartest people I\'ve ever known and I really'
                    ' like how you know that and can use it.  So keep being the best at everything and knowing how '
                    ' to do everything and'
                    ' let\'s go get a cold sugary snack tonight, ok?  Love you, have a good day!', 'Ice Cream Wherever!'],
              "8": ['', ''],
              "9": ['', ''],
              "10": ['', ''],
              "11": ['I want to go on another trip with you and hope you feel the same way.  I know Mexico wasn\'t the'
                     'greatest first experiment, but I keep thinking about how much fun we would have in Florida or California'
                     'or Colorado or anywhere. Maybe we can plan another trip and have a relaxing time?  Love you!', None],
              "12": ['', ''],
              "13": ['You\'re sitting on the couch applying nail polish as I\'m typing this and you look soo amazingly attractive.'
                     'You\'re so good at casually looking beautiful and I\'m very jealous of your ability to do that.'
                     'I love you and I\'m really glad you\'re mine - no matter how you look!', None],
              "14": ['', ''],
              "15": ['Hey, we both like ice cream.  Can you believe it\'s already been a month since the last time'
                    ' you read a note about it? Anyway, I like your smile and your drive and how much you care about'
                    ' everything so just wanted to take this morning to let you know that I don\'t want to ever'
                    ' leave you at all.  Oh, also, you\'re easily one of the smartest people I\'ve ever known'
                    ' and I really like how you know that and can use it.  So keep being the best at everything'
                    ' and knowing how to do everything and making everyone love you!  You\'re my favorite!', None],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['', ''],
              "19": ['So I wanted to write you a website for you, either for your professional career or just for some'
                      ' random reason but it seems like you wouldn\'t appreciate it.  However, I did figure out how to'
                      ' register a domain name and spun up a couple of examples so if you ever wanted something like that,'
                      ' please just let me know.', None],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ['', ''],
              "31": ""},
        "4": #APRIL
            {"1": ['APRIL FOOLS! Let\'s get some silly string and shoot each other in the spirit of the day!',
                   'SILLY STRING FIGHT'],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['', ''],
              "6": ['', ''],
              "7": ['Hey, to break in the warm weather, I thought we could go to a park nearby and either bike somewhere'
                    ' or take a hike and have lunch together on the trail.  I miss doing that with you all the time and'
                    ' just going wherever with you and hanging out.  I\'ll take care of the lunch and choosing where to'
                    ' go so all you have to do is let me know if I need to put the bikes on the back of the car!  Love you'
                    ' and I\'m excited to hit the trail with you!', 'Hike and lunch - my treat!'],
              "8": ['', ''],
              "9": ['', ''],
              "10": ['', ''],
              "11": ['', ''],
              "12": ['', ''],
              "13": ['', ''],
              "14": ['', ''],
              "15": ['', ''],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['Well, it\'s getting warm again!  Is it ice cream time yet!?  How about we go ahead and say it\'s'
                     ' warm enough!  Sound good?  Today I want to remind you about how much you mean to me and to'
                     ' everyone who knows you.  Today isn\'t about how you feel about yourself or what assholes care'
                     ' about you, it\'s about how your siblings, parents, and other relatives (and I) see in you!'
                     '  You\'re great at gift-giving, advice, cheering people up, and being there for someone'
                     ' literally any time they need you.  Plus, don\'t forget about how your sense of humor always'
                     ' makes people chuckle. Alright, well that\'s all for today, except I\'m also still thinking'
                     ' about it, so it\'s on me tonight.  Love you Cosmic Brownie!', 'Ice Cream Tonight!'],
              "19": ['', ''],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ""},
        "5": #MAY
            {"1": ['', ''],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['', ''],
              "6": ['', ''],
              "7": ['', ''],
              "8": ['', ''],
              "9": ['', ''],
              "10": ['We just got the new couch yesterday and I it. That would never have happened without you so thank'
                     ' you so much for driving us to choose one and getting it moved into the living room.  I appreciate'
                     ' you being so strong-willed and knowledgeable about what you want.  You have great tastes and make'
                     ' wonderful things happen all the time.  Love you!', None],
              "11": ['', ''],
              "12": ['', ''],
              "13": ['', ''],
              "14": ['', ''],
              "15": ["Remember that time we rode our bikes and found like 15 turtles?  Yeah, that was fun.  Let\'s do"
                     " that again! I\'ll load up the car and we can ride our bikes around Laumeier Sculpture Park and"
                     " make a Snapchat Story about all of the cool things we found. Can you tell that I wrote this"
                     " one on the day I found out about Stories?  And that I kind of want to make one now but there"
                     " aren\'t any adventures coming up soon?  Anyway, I really like riding bikes with you so let\'s"
                     " make it a date and then go get a snack or pack a picnic when we go out and ride around.  I love"
                     " you and want to make your life more enjoyable!", 'Bike ride + Picnic.'],
              "16": ['', ''],
              "17": ['So this is the last note I\'m writing before bed tonight and a random Office episode is on.  I will'
                     ' never forgive you for introducing that show to me.  Alright, but for real I\'m excited to go sleep'
                     ' with you and maybe sleep with you too.  Anyway, I may not forgive you for telling me about a show'
                     ' that I will continue to watch and rewatch but it\'s always worth it to go to bed at night next to'
                     ' you.  This is kind of a short one, sure, but one of the most important things you do and something'
                     ' I want to remind you about constantly is how great it feels to crawl in next to you and that if you'
                     ' ever don\'t feel the same way, I want to fix it immediately.  So let me know if you\'re ever not 100%'
                     ' comfortable or happy getting into bed! I love you and everything about you!', None],
              "18": ['', ''],
              "19": ['', ''],
              "20": ['Now it\'s definitely warm enough to maybe make date out of ice cream.  So, there\'s something'
                     ' we haven\'t done in a while that we both seemed to enjoy: Just getting a blanket and laying'
                     ' on the grass reading or playing on phones or whatever just to be calm and have a good time.'
                     '  You\'re a really good cuddle buddy and I want you to know how amazing you are and how it\'s'
                     ' great to wake up and go to sleep next to you every day!  I\'ll get the wine and maybe make it'
                     ' more expensive and we can have a picnic in the park where we have a nice relaxing day and'
                     ' afterwards go get Serendipity to "officially" break in summer!  Or not, whatever is more'
                     ' relaxing for you! ', 'Relaxdate, if you want!'],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ['', ''],
              "31": ""},
        "6": #JUNE
            {"1": ['', ''],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['', ''],
              "6": ['', ''],
              "7": ['', ''],
              "8": ['This is the first note I wrote in June, which doesn\'t feel like an interesting way to start'
                    ' one of these, but June is weird because there aren\'t really a lot of things planned months in'
                    ' advance.  Anyway, I love you and if there\'s nothing going on today, then we should go get waffles'
                    ' and ice cream!  Perfect thing to do in the summer!  Let\'s go have fun together!',
                    'Waffles and Ice Cream - 6/8'],
              "9": ['Waffles and Ice Cream yesterday, Eggs and Cake Today right!?  Isn\'t that how it works?  Just kidding,'
                    ' I love you so much and this kind of thing just makes me think about all the things I want to do'
                    ' with you!  You are an amazing, sexy, funny, and generally amazing person!', None],
              "10": ['', ''],
              "11": ['', ''],
              "12": ['', ''],
              "13": ['', ''],
              "14": ['', ''],
              "15": ['', ''],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['Hey. Hey, you.  We should go get FroYo tonight because it\'s been a month since ice cream and I'
                     ' miss going on silly little dates with you.  So I really want to go on a silly little date! Also,'
                     ' this seems like a good time to go ahead and mention how your giggle is the most addicting thing'
                     ' ever and how you make me crave hearing more of it.  There\'s a reason I keep making dumb jokes'
                     ' or make you do that thing while you womansplain how you don\'t have to laugh at the jokes of men'
                     ' if they aren\'t being funny. Because even though you say that, you laugh first like every single'
                     ' time so you\'re incentivizing me to keep doing it to hear you laugh again!  I love you so much more'
                     ' honeycomb!', 'FroYo - my treat!'],
              "19": ['', ''],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['I know by now we\'ve probably talked about movies on Art Hill but figured we could make this one'
                     ' special by going to Serendipity or some good place on the Hill first to have some excellent food'
                     ' before hanging out and snacking on wine and sweets while we watch the movie!  I\'m looking forward'
                     ' to a cute date night with you, as always.', 'Date on Art Hill'],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ""},
        "7": #JULY
             {"1": ['', ''],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['', ''],
              "6": ['', ''],
              "7": ['', ''],
              "8": ['', ''],
              "9": ['', ''],
              "10": ['', ''],
              "11": ['', ''],
              "12": ['', ''],
              "13": ['', ''],
              "14": ['', ''],
              "15": ['', ''],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['', ''],
              "19": ['', ''],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['This is randomly the first thing I wrote in July.  So there\'s a cool thing we should do tonight or'
                     ' sometime this week.  Back when we first started dating, we talked about having a picnic supper in'
                     ' a park some night where we would just hang out on a hill and eat pizza and dessert and chat.  We'
                     ' haven\'t done that and we need to!  My treat - looking forward to it!', 'Pizza and dessert in the park'],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ['', ''],
              "31": ""},
        "8": #AUGUST
            {"1": ['', ''],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['', ''],
              "6": ['', ''],
              "7": ['Hey Babe, I wanted to take this message to focus on how brilliant you are and how great you are at'
                    ' figuring out problems, puzzles and even just random trivia.  I love that you\'re so smart and '
                    'can challenge everyone on their ideas and come up with the best answer to a problem!', None],
              "8": ['', ''],
              "9": ['', ''],
              "10": ['', ''],
              "11": ['', ''],
              "12": ['I like your sugar skull.  Or, to be less generic, your decorating prowess.  I\'m very glad'
                     ' you stuck with me even after I was a dick about decorating.  I love how our house looks right now'
                     ' and everything that\'s in it.  I love you and all of the effort you put in!', None],
              "13": ['', ''],
              "14": ['', ''],
              "15": ['', ''],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['', ''],
              "19": ['', ''],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ['', ''],
              "31": ""},
        "9": #SEPTEMBER
            {"1": ['', ''],
              "2": ['', ''],
              "3": ['', ''],
              "4": ['', ''],
              "5": ['', ''],
              "6": ['', ''],
              "7": ['', ''],
              "8": ['', ''],
              "9": ['', ''],
              "10": ['', ''],
              "11": ['', ''],
              "12": ['', ''],
              "13": ['', ''],
              "14": ['', ''],
              "15": ['We haven\'t gone apple picking yet this year and I really enjoyed going with you last year,'
                     ' so today seems like a really good time to head out to Eckert\'s and get another bunch.  Then'
                     ' I\'ll try to make an apple with some of them and we can enjoy the rest!  Let\'s have a good day'
                     ' grabbing apples and hanging out!', 'Apple Picking!'],
              "16": ['', ''],
              "17": ['', ''],
              "18": ['', ''],
              "19": ['', ''],
              "20": ['', ''],
              "21": ['', ''],
              "22": ['', ''],
              "23": ['', ''],
              "24": ['', ''],
              "25": ['', ''],
              "26": ['', ''],
              "27": ['', ''],
              "28": ['', ''],
              "29": ['', ''],
              "30": ['The more I think about it, the more September is a difficult month to write notes for.  It\'s the'
                   ' last month I wrote a note for and the hardest one for me to be creative writing for.  So looking at'
                   ' it now, I think itw went alright and I hope you enjoyed it too!  I love you bunches and I\'m super '
                   ' excited to spend October and Halloween with you! Love you babe!', None]},
        "10": #OCTOBER
            {"1": ['You know you\'re like the best cuddle buddy ever, right? Somehow you can drain the heat from everyone'
                   ' else and still be the warmest, most snuggly person ever.  I really love just hanging out with you'
                   ' and mostly just enjoy the idle moments we have with one another.', None],
               "2": ['Somehow October feels like the real start of the cold part of the year instead of Novemeber or'
                     ' December.  That means we get to put the Duvet back on the bed and falling asleep together!  I'
                     ' love you and cuddling with you and how you act when you\'re half asleep. It\'s so cute!', None],
               "3": ['', ''],
               "4": ['', ''],
               "5": ['', ''],
               "6": ['', ''],
               "7": ['', ''],
               "8": ['', ''],
               "9": ['', ''],
               "10": ['', ''],
               "11": ['', ''],
               "12": ['', ''],
               "13": ['', ''],
               "14": ['', ''],
               "15": ['', ''],
               "16": ['', ''],
               "17": ['', ''],
               "18": ['Want to watch Hocus Pocus tonight?  I know how much you like it, so I\'ll make a big bag of popcorn'
                      ' and bring out the blankets so we can cuddle.  And then we can watch one of your favorite movies!  I'
                      ' love you and want you to always feel comfortable and happy at home.  Have a good day babe!', None],
               "19": ['', ''],
               "20": ['', ''],
               "21": ['', ''],
               "22": ['', ''],
               "23": ['', ''],
               "24": ['', ''],
               "25": ['', ''],
               "26": ['', ''],
               "27": ['', ''],
               "28": ['', ''],
               "29": ['', ''],
               "30": ['', ''],
               "31": ['Halloween!  Candy and Trick or Treating!  How about we go get leftover candy tomorrow?  It\'s always like'
                      ' 25% off and I\'ll get whatever kind you like best.  That\'s Whoppers, right?  So we\'ll go get a big'
                      ' bag of Whoppers!  I love you and want you to have all the things you love in life!', 'Whoppers! - 10/31']},
        "11": #NOVEMBER
            {"1": ['', ''],
               "2": ['', ''],
               "3": ['', ''],
               "4": ['', ''],
               "5": ['', ''],
               "6": ['', ''],
               "7": ['', ''],
               "8": ['', ''],
               "9": ['', ''],
               "10": ['', ''],
               "11": ['', ''],
               "12": ['', ''],
               "13": ['', ''],
               "14": ['', ''],
               "15": ['', ''],
               "16": ['', ''],
               "17": ['', ''],
               "18": ['', ''],
               "19": ['', ''],
               "20": ['', ''],
               "21": ['', ''],
               "22": ['', ''],
               "23": ['', ''],
               "24": ['', ''],
               "25": [
                   "Oh hey, this is the only self-indulgent immodest note of the 365 that I wrote for you.  It's my birthday and I do believe that one day "
                   " a year should be about you and you alone - just a day to relax.  Back to making you happy tomorrow.  But hey, let's make sure we have"
                   " sex today so we're both happy!", "Have really good sex"],
               "26": ['', ''],
               "27": ['', ''],
               "28": ['', ''],
               "29": ['', ''],
               "30": ['', '']},
        "12": #DECEMBER
            {"1": ['Hey it\'s December and almost Christmas.  You ready to drive around looking at lights all the time and'
                   ' actually being in the right month to listen to Christmas music?  I\'m really looking forward to your'
                   ' birthday and the holidays this year!  I also want to make a snowman with you since we haven\'t had the'
                   ' chance to really do that yet.  You\'re the best and I love just doing things with you.', None],
               "2": ['', ''],
               "3": ['', ''],
               "4": ["Remember that time we had no idea what to do and instead wound up at the Daniel Boone Home?  "
                     "That's still one of my favorite memories and I hope you enjoy it too!  It's time for the Christmas"
                     " Event there, so let's go have a good time!  We talked about making a date of it, so you get to pick:"
                     " Either you pick where to eat or you make me pick!  I pay either way.",
                     "Christmas Date at the Daniel Boone Home"],
               "5": ['', ''],
               "6": ['', ''],
               "7": ['', ''],
               "8": ['<<ANNOUNCE BIRTHDAY THING FOR NEXT YEAR>>', None],
               "9": ['Happy Birthday Apple!  I still wrote that thing that\'ll message you every day, but now it\'s going'
                     ' to go through your email.  I\'ve set it up so I can change any parameter within like 5 minutes, so '
                     ' if 8am is too early for you, I can change the email to send whenever you want!  Also, some of the'
                     ' messages are attached with cute little things I want to do for you, and those can be found in a '
                     ' To-Do list on the website Remember the Milk.  I\'ll get you the info for that shortly so you can'
                     ' check out today\'s thing!  I love you so much and hope you have a great birthday!',
                     'Open Presents!  There\'s one under the bed!  And another in your trunk.  And in your purse.'],
               "10": ["Hey Darling!  Good Morning!  Unfortunately it\'s not your birthday anymore, but I can still"
                      " try to make you happy every day.  I actually have one more present for you - on Sunday nights,"
                      " the Lemp Mansion has fried chicken meals!  We have a reservation tonight, so get a dress our and "
                      " show off!", 'Get fried chicken at the Lemp Mansion'],
               "11": ['Alright, I\'m unfortunately out of presents now, until Christmas at least.  I still want to use these'
                      ' to tell you how much I love you every day of the week!  So because I love you, the other cool '
                      ' thing about these messages is that I can change them at will and surprise you when things come'
                      ' up!  So feel free to mention things you want and I\'ll do my best to make them happen!', None],
               "12": ['We\'re halfway through December which means only 13 more days until Christmas!  We need to watch'
                      ' another awful low-budget holiday movie and have some popcorn soon.  We\'re still talking about the'
                      ' ones we watched form last year and we love cuddling, so let\'s go ahead and find some new ones!',
                      None],
               "13": ['I\'m sitting here watching Cinderella Story with you and I kind of enjoy it.  Does that make me '
                      ' crazy?  I think maybe I just like dumb movies as long as we can talk together and make fun of them.'
                      ' I hope you\'re doing well today and love you forever!', None],
               "14": ['Let\'s go see the lights at Candy Cane Lane (or somewhere else, if you want!) tonight! I love you'
                      ' and want to go see the lights with you every single year!', 'Date night seeing Christmas lights.'],
               "15": ['So I\'m realizing as I write this that while I love writing this list, I\'m finding 365 things I '
                      ' love about you.  Today I want to point out that I love your adorable giggle when we\'re just '
                      ' chatting and you find something funny.  It\'s so adorable and I wish you kept doing it forever.', None],
               "16": ['Totally unrelated, I\'m kind of craving Burritoville.  Anyway, while I was writing this one, you'
                      ' set your foot on my butt and it felt great.  So keep doing that since it\'s a super adorable thing'
                      ' and it makes me love you even more.', None],
               "17": ['Hey, week one of daily messages is done.  I hope you\'ve been enjoying them so far!  I love you'
                      ' and I know that you think I\'m probably really dumb for writing all these.  But hey, I want to win'
                      ' birthdays this year and doing something as extensive as this is the only way I know how.  Plus,'
                      ' I do love trying to make you smile - it\'s worth it every single time it works.', None],
               "18": ['Hey, you\'re super amazing.  Enjoy your day at work and know I\'m thinking about you all the time'
                      ' and want you to be happy forever.  I love you and wish we didn\'t have to work today so you could'
                      ' just relax and have fun.  There was a story on the internet a while ago about a girl who ran'
                      ' through the hallways at her boyfriend\'s college screaming TROLL! IN THE DUNGEON! ...just thought'
                      ' you ought to know.  and then collapsed on the ground.  He said "Guys, I finally found the one!"'
                      ' I thought that was a super cute story and wanted to do that to you at CushWake for a while, before'
                      ' realizing that would probably endanger your job more than it would help your day.  So, sorry that'
                      ' I haven\'t done that but having a job is kind of important and I would totally do it if your job'
                      ' didn\'t depend on it!  Love you tons, strawberry shortcake!', None],
               "19": ['So I\'ve been thinking about how many times you casually made my life better before I even realized'
                      ' you were doing it.  Made me think about it because someone started talking to me about how much fun'
                      ' I am in the game nights I go to.  And well, I wish I could do the same for you. First, I\'m really'
                      ' sorry that I\'m not a better boyfriend and second, you\'re just the best person ever and you are '
                      ' so damn good at recognizing and correcting the things that are going wrong in someone\'s life and'
                      ' then helping them fix it or, more commonly, fixing them yourself!  You are absolutely the most '
                      ' brilliant human I\'ve ever had the pleasure to meet and I love the hell out of you.  Have a great'
                      ' day babe!', None],
               "20": ['Something I\'ve been wanting to do while writing these and haven\'t really done so far is coming'
                      ' up with a fun little pet name for you some days.  There are a couple that are coming up through'
                      ' the summer months that I thought were pretty cute.  Anyway, pumpkin pie, doing this is pretty'
                      ' fun because you have a ton of good qualities and now you get to hear about them and (hopefully)'
                      ' smile every morning.  And it\'s good for both of us since I get to bug you with really dumb'
                      ' little pet names.  Well, this is a shorter one because it\'s just so much fun to try to bug'
                      ' you, applesauce!  Love you bunches, honey and oats!', ''],
               "21": ['We\'re watching Elf right now and we just got the snowball scene and now I just want to have a'
                      ' snowball fight with you, but it\'s not supposed to snow for like another 3 weeks.  So I started'
                      ' trying to make a plan where we made a ball pit or used flour socks or something else, but none of'
                      ' those make sense so this is more of a warning that the first day it snows you should be on your'
                      ' guard when you come home from work. :p  Love you bunches!', ''],
               "22": ['Hey, I miss you a ton right now. I know you\'re probably just starting work for the day or not'
                      ' even there yet but I\'m writing this one over lunch and really just want you to be here right now'
                      ' with me so we can cuddle or lay on each other or just spend time together. I really love you and'
                      ' enjoy even foot-cuddling with you and getting warm at night next to you.  Just go ahead and'
                      ' leave work for the day and come home and we can have a nice relaxing afternoon.  Love you honey bun!',
                      None],
               "23": ['It\'s the weekend of the best time of year!  So excited!  I got hot cocoa and some cookies'
                      ' for you so we can celebrate Christmas.  I love you so much and I\'m so excited to spend the'
                      ' holiday with you.  https://www.youtube.com/watch?v=mK0z1S8SwZc', None],
               "24": ['Santa\'s coming tomorrow and I\'m so excited.  We\'re going to leave milk and cookies for him and'
                      ' wait for the presents to magically appear under the tree and watch fun holiday movies.  We\'re also'
                      ' going to lay in bed and guess what we\'re getting from the other person...and then eat Santa\'s'
                      ' cookies and drink Santa\'s milk.  Hope you have a great day tomorrow!', None],
               "25": ['Merry Christmas!  Hope you enjoy getting presents!', None],
               "26": ['Merry day-after-Christmas! I know we both have to go back to work today but let\'s just imagine'
                      ' that it\'s another normal Tuesday, but for a 4 day week that ends in New Years!  I love you and'
                      ' will be thinking about you all day long!  Let me know if there\'s anything at all I can do to '
                      ' make you happier today!', ''],
               "27": ['Hey, December is almost over, but that just means we\'re almost to 3 years!  Did you ever think we\'d'
                      ' make it this far?  Anyway, while it\'s still cold out, how about we go ice skating again?  It\'s been'
                      ' a while and it\'s been a while since we did anything out in the cold like that.', 'Ice skating'],
               "28": ['I was listening to a random easy listening playlist today and a song came on where the singer was talking about'
                      ' how great her boyfriend was because he always showered like right before he showed up to the date.'
                      ' That seems kind of strange to me.  Like, why would you shower every single time when you could just'
                      ' apply deodorant?  Or like, if the point was to show her she was special, then get flowers and chocolate'
                      ' before every single date.  Anyway, the point of this was to let you know that I\'ll go and and shower'
                      ' before every time we go out for a date if that\'ll make you happy.  Love you darling!', None],
               "29": ['So this is kind of a funny note.  December is the first month for which I finished writing these notes,'
                      ' mostly because at one point I was worried about getting them all done and started doing the ones closest'
                      ' to your birthday first in order to buy myself some extra time to push out the rest.  I really wanted'
                      ' each one of these to be special and fun and for them to make your day brighter and less stressful!  I'
                      ' love you and want to do this as a recurring thing each year, maybe to a lesser degree - love ya!', None],
               "30": ['Hey, another three day weekend!  Well, this time we get to stay up until midnight and get tipsy'
                      ' and have a really good night.  So here\'s the plan: Let\'s go out to a bar to start the night'
                      ' where it\'s loud and we can get a little rowdy and then come home for the last bit and do that thing'
                      ' we do where we hang out and it\'s quiet.', None],
               "31": ['Happy New Years\' Eve!  Whatever we\'re doing tonight, I\'m excited to ring in the new year with you'
                      ' and kiss you at midnight!  It\'s been a great year and I can\'t wait to do another year with you!', '']
               }}


print(Message.year_dict["2"]["4"])
