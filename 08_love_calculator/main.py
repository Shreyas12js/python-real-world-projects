print("-"*5, "Welcome to the Love calculator", "-"*5)

name1 = input("Enter your name: ").lower()
name2 = input("Enter your lover name: ").lower()

combined_name = name1 + name2

# TRUE
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true_score = str( t + r + u + e)

# LOVE
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
# reuse e

love_score = str(l + o + v + e)

combined = int(true_score + love_score)

if combined < 25 or combined > 70:
    print("Not a True Love, your score is", combined)
elif 25 <= combined <= 70:
    print("True Love, your score is", combined)
else:
    print("Average Love, your score is", combined)
