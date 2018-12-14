import pprint
# We use triple ' to capture all text.
message = '''1In the beginning was the Word, and the Word was with God, and the Word was God.
2The same was in the beginning with God.
3All things were made by him; and without him was not any thing made that was made.
4In him was life; and the life was the light of men.
5And the light shineth in darkness; and the darkness comprehended it not.
6There was a man sent from God, whose name was John.
7The same came for a witness, to bear witness of the Light, that all men through him might believe.
8He was not that Light, but was sent to bear witness of that Light.
9That was the true Light, which lighteth every man that cometh into the world.
10He was in the world, and the world was made by him, and the world knew him not.
11He came unto his own, and his own received him not.
12But as many as received him, to them gave he power to become the sons of God, even to them that believe on his name:
13Which were born, not of blood, nor of the will of the flesh, nor of the will of man, but of God.
14And the Word was made flesh, and dwelt among us, (and we beheld his glory, the glory as of the only begotten of the Father,) full of grace and truth.
15John bare witness of him, and cried, saying, This was he of whom I spake, He that cometh after me is preferred before me: for he was before me.
16And of his fulness have all we received, and grace for grace.
17For the law was given by Moses, but grace and truth came by Jesus Christ.
18No man hath seen God at any time; the only begotten Son, which is in the bosom of the Father, he hath declared him.
19And this is the record of John, when the Jews sent priests and Levites from Jerusalem to ask him, Who art thou?
20And he confessed, and denied not; but confessed, I am not the Christ.
21And they asked him, What then? Art thou Elias? And he saith, I am not. Art thou that prophet? And he answered, No.
22Then said they unto him, Who art thou? that we may give an answer to them that sent us. What sayest thou of thyself?
23He said, I am the voice of one crying in the wilderness, Make straight the way of the Lord, as said the prophet Esaias.
24And they which were sent were of the Pharisees.
25And they asked him, and said unto him, Why baptizest thou then, if thou be not that Christ, nor Elias, neither that prophet?
26John answered them, saying, I baptize with water: but there standeth one among you, whom ye know not;
27He it is, who coming after me is preferred before me, whose shoe's latchet I am not worthy to unloose.
28These things were done in Bethabara beyond Jordan, where John was baptizing.
29The next day John seeth Jesus coming unto him, and saith, Behold the Lamb of God, which taketh away the sin of the world.
30This is he of whom I said, After me cometh a man which is preferred before me: for he was before me.
31And I knew him not: but that he should be made manifest to Israel, therefore am I come baptizing with water.
32And John bare record, saying, I saw the Spirit descending from heaven like a dove, and it abode upon him.
33And I knew him not: but he that sent me to baptize with water, the same said unto me, Upon whom thou shalt see the Spirit descending, and remaining on him, the same is he which baptizeth with the Holy Ghost.
34And I saw, and bare record that this is the Son of God.
35Again the next day after John stood, and two of his disciples;
36And looking upon Jesus as he walked, he saith, Behold the Lamb of God!
37And the two disciples heard him speak, and they followed Jesus.
38Then Jesus turned, and saw them following, and saith unto them, What seek ye? They said unto him, Rabbi, (which is to say, being interpreted, Master,) where dwellest thou?
39He saith unto them, Come and see. They came and saw where he dwelt, and abode with him thatm day: for it was about the tenth hour.
40One of the two which heard John speak, and followed him, was Andrew, Simon Peter's brother.
41He first findeth his own brother Simon, and saith unto him, We have found the Messias, which is, being interpreted, the Christ.
42And he brought him to Jesus. And when Jesus beheld him, he said, Thou art Simon the son of Jona: thou shalt be called Cephas, which is by interpretation, A stone.
43The day following Jesus would go forth into Galilee, and findeth Philip, and saith unto him, Follow me.
44Now Philip was of Bethsaida, the city of Andrew and Peter.
45Philip findeth Nathanael, and saith unto him, We have found him, of whom Moses in the law, and the prophets, did write, Jesus of Nazareth, the son of Joseph.
46And Nathanael said unto him, Can there any good thing come out of Nazareth? Philip saith unto him, Come and see.
47Jesus saw Nathanael coming to him, and saith of him, Behold an Israelite indeed, in whom is no guile!
48Nathanael saith unto him, Whence knowest thou me? Jesus answered and said unto him, Before that Philip called thee, when thou wast under the fig tree, I saw thee.
49Nathanael answered and saith unto him, Rabbi, thou art the Son of God; thou art the King of Israel.
50Jesus answered and said unto him, Because I said unto thee, I saw thee under the fig tree, believest thou? thou shalt see greater things than these.
51And he saith unto him, Verily, verily, I say unto you, Hereafter ye shall see heaven open, and the angels of God ascending and descending upon the Son of man.'''

message = ''.join([i for i in message if not i.isdigit()]) # Remove's any digit from the text.
char = 0
word = 1
for y in message.upper():
    char = char + 1
    if (y == ' '):
        word = word + 1
    #count.setdefault(character, 0)
    #count[character] = count[character] + 1
print('Number of characters in string:')
pprint.pprint(char)
print('Number words in string:')
pprint.pprint(word)