# 5.1
song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""

print(song.replace(' m', ' M'))

# 5.2
questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

print(f'Q: {questions[0]}\n\
A: {answers[0]}\n\
Q: {questions[1]}\n\
A: {answers[1]}\n\
Q: {questions[2]}\n\
A: {answers[2]}')

# 5.3
print("""My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s And now thinks he's a %s."""\
     % ('roast beef', 'ham', 'head', 'clam'))

# 5.4
letter = """\tDear {salutation} {name},

\tThank you for your letter. We are sorry that our {product} {verbed} in your
{room}. Please not that it should never be used in a {room}, especially near any
{animals}.

\tSend us your receipt an {amount} for shipping and handling. We will send you
another {product} that, in out tests, is {percent}% less likely to have {verbed}.

\tThank you for your support.
\tSincerely,
\t{spokeman}
\t{job_title}"""

# 5.5
print(letter.format(salutation = 'sal', name = 'nam', product = 'pro', verbed = 'ver',\
     room = 'roo', animals = 'ani', amount = 'amo', percent = 'per', spokeman = 'spo',\
         job_title = 'jop'))

# 5.6
print('%sy Mc%sface' % ('duck'.title(), 'duck'.title()))
print('%sy Mc%sface' % ('gourd'.title(), 'gourd'.title()))
print('%sy Mc%sface' % ('spitz'.title(), 'spitz'.title()))

# 5.7
print('{0}y Mc{0}face'.format('duck'.title()))
print('{0}y Mc{0}face'.format('gourd'.title()))
print('{0}y Mc{0}face'.format('spitz'.title()))

# 5.8
print(f"{'duck'.title()}y Mc{'duck'.title()}face")
print(f"{'gourd'.title()}y Mc{'gourd'.title()}face")
print(f"{'spitz'.title()}y Mc{'spitz'.title()}face")