# Strange-Planet
This is my solution to the problem "Strange Planet" you can find on the web 
http://infolab.stanford.edu/~ullman/ialc/spr10/slides/fa1.pdf
especifically at slide 9

It's about an strange planet with a given number of population and 3 kind of species that cannot reproduce with one of their own kind
so they have to breed with another... like specimen 'a' only can breed with 'b' or 'c' but not 'a' and vice versa... 
when 'a' and 'b' breed they die and two baby 'c' are born, the same happens when 'b' and 'c' breed, they die and two 'a' are born
The point of the problem is to know if the planet's destiny is to fail, that happens when there is only one species left, for example all
'b' and 'c' died and only 'a' survived but as I said before, an 'a' cannot reproduce with one of it's kind... so that's it, the planet
failed :'c ... now you have to ask the mean question... given and specific number of population, I don't know, maybe 5, is the planet
destined to fail? 
So... if you whant to know more about the problem please check the link :)

Well, now the solution:

I notice that planets with a population of 2,4,5,7,8,10,11 y 13 y 14 are always destined to fail... actually you can see 4 and 8 like
an expansion of planet 2...
Then we have 3... 3 is sometimes destined to fail and sometimes not, depends of the distribution (please please please check the 
powerpoint "planetas", there you can see what i'm talking about with beautiful images)
So planets which pupolation is multiple of 3, are and expansion of it and like 3, they have 3 possibilities, never fail, never fail 
again, or fail. This last one have the three ways of failing a-0-0, 0-b-0 or 0-0-c

When the population is the result of multiply only numbers wich population always fail, the result fails too.

PS: see the powerpoint "planetas"
