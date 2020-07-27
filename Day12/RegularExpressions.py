import re
import this
pattern=r"sonu"

print(re.match(pattern,"Hi this is sonu bisht from dehradun. \nsonu"))
print(re.search(pattern,"Hi this is surendra bisht from dehradun. \nsonu"))
print(re.findall(pattern,"Hi this is sonu bisht from dehradun. \nsonuBisht"))

# sub function replaces the searched text.
str = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Surendra", str)
print(newstr)

# metacharacters : . (any character); ^ (start of string); $ (end of string) 

#characterClasses : 
#[abc][def]  will match ad,ae,af,bd,be,bf,cd,ce,cf.
#[a-z] ; [A-Z] ;[l-z] ; [0-9] ; [A-Za-z]
pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "LS8"):
   print("Match 1")


# metacharacter ? means "zero or one repetitions"
#pattern = r"colo(u)?r" will match color or colour

#9{1,3}  will represent repitition of 9 no of times should be in range of 1 to 3 
#pattern = r"9{1,3}$"

#() brackets denotes group/ we can apply metacharacter * + ? on these
pattern = r"a(bc)(de)(f(g)h)i"
#in this bc ,de,fgh and g is a group.
#groups() will print all groups catured. groups(0) will show whole string matching. groups(1) shows first group.


# gr(a|e)y this represents pattern gray or grey. can also be written as gr[ae]y

#specail sequences - \d represents digit, \s represents space, and \w represents word, can be aplhanumeric.
# upper case of these is opposite of what they are. i.e. for ex. \D will represent anything other than digit.



