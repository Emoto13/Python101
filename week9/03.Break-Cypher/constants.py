INSERT_QUERY = '''INSERT INTO predishnoto_reshenie_vajeshe (message, encrypted_message)
                  VALUES (?, ?);
                    '''
GET_MESSAGE_QUERY = '''SELECT message
                        FROM predishnoto_reshenie_vajeshe
                        WHERE encrypted_message = ?'''

SYMBOLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '!', '<', '.',
           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
           ]

SECRET_MESSAGE = '''f0aa25cd443edb4cacf75bb24c5ad303
e641386ea86d75a37a79d7a8ca142103
e902668782c8ff35c741a60abb2ee751
b88cb6ce3803814cbe6b4f621210693c
ef9fcdb53e4e10b12bfcd5e9e78135dc
cae8d14edd025e72c59dbab6f378c95a
60b36cd3c72aa7c0ddbc69436d7eca96
8fc42c6ddf9966db3b09e84365034357
74459ca3cf85a81df90da95ff6e7a207
2cb9df9898e55fd0ad829dc202ddbd1c
c13367945d5d4c91047b3b50234aa7ab
be5d5d37542d75f93a87094459f76678
caf98268abd13bb8ed384da0313e2dd6
8534a9e46af4ac17812152f8b21e3ffd
0cc175b9c0f1b6a831c399e269772661
23678db5efde9ab46bce8c23a6d91b50
1822266030c65a00f35ba3836cd61158
aab9e1de16f38176f86d7a92ba337a8d
ebdacc3da0a7c89897c9433855c6cd1d
4d643b1bd384922ca968749b93b81db5
a2a551a6458a8de22446cc76d639a9e9
1ced92c2ce3df0ae7a634022e7455469
cc5c0452c1308f585de22b4afc7723f7
6e57d6c47d23024e41f4a1aac73a3ea9
a170c4cb1ae103745ec02e015cb86727
dd7536794b63bf90eccfd37f9b147d7f
92159805cf28ee78e13c41ebbbb1aeb4
639bae9ac6b3e1a84cebb7b403297b79
0cc175b9c0f1b6a831c399e269772661
efa35b82d8622819a31a8bc9208a076f
9942d8472ee432bb4179199f5beae701
9e925e9341b490bfd3b4c4ca3b0c1ef2
cebd65946444e5cd3e861a2dbf69e221
030c76e4f0ed31202379e6df29def1d6
326577fbe6d73973bd67437829bf9301
bb90e57a80b6817ef63ea3b42f948a0a
f9da66cdef69f6ffdc642a29a29eae93
18218139eec55d83cf82679934e5cd75
7f021a1415b86f2d013b2618fb31ae53
46c48bec0d282018b9d167eef7711b2c
b2700999997b51194434005c3d95e619
9f31730024c592d8aa6c3e567e9895dd
c67fd61e3b7d35f07e3ca92c8a84a5ab
be5d5d37542d75f93a87094459f76678
99be1ee67a0137092d3d112c0620c552
9dfc8dce7280fd49fc6e7bf0436ed325
e7cbf67460e47dea4b13e81304850d5f'''
