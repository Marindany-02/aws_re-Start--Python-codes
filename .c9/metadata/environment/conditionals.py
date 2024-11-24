{"filter":false,"title":"conditionals.py","tooltip":"/conditionals.py","undoManager":{"mark":24,"position":24,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":70},"action":"insert","lines":["userReply = input(\"Do you need to ship a package? (Enter yes or no) \")"],"id":29}],[{"start":{"row":0,"column":70},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":30}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"],"id":31},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":[" "],"id":32}],[{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["u"],"id":33},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["s"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["e"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["r"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["R"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["e"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["p"]}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["l"],"id":34},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["y"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"insert","lines":["y"],"id":35},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"insert","lines":["e"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"insert","lines":["s"]},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"insert","lines":[","]}],[{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":[","],"id":36}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":16},"action":"remove","lines":["if userReply=yes"],"id":37},{"start":{"row":1,"column":0},"end":{"row":2,"column":47},"action":"insert","lines":["if userReply == \"yes\":","    print(\"We can help you ship that package!\")"]}],[{"start":{"row":2,"column":47},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":38},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":4},"end":{"row":4,"column":73},"action":"insert","lines":["else:","    print(\"Please come back when you need to ship a package. Thank you.\")"],"id":39}],[{"start":{"row":3,"column":9},"end":{"row":4,"column":0},"action":"remove","lines":["",""],"id":40}],[{"start":{"row":3,"column":9},"end":{"row":3,"column":13},"action":"remove","lines":["    "],"id":41},{"start":{"row":3,"column":9},"end":{"row":4,"column":0},"action":"insert","lines":["",""]},{"start":{"row":4,"column":0},"end":{"row":4,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":8},"action":"remove","lines":["    "],"id":42}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "],"id":43}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":5},"action":"remove","lines":["userReply = input(\"Do you need to ship a package? (Enter yes or no) \")","if userReply == \"yes\":","    print(\"We can help you ship that package!\")","else:"],"id":44}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":73},"action":"remove","lines":["    print(\"Please come back when you need to ship a package. Thank you.\")"],"id":45},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":0},"end":{"row":9,"column":42},"action":"insert","lines":["userReply = input(\"Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) \")","if userReply == \"stamps\":","    print(\"We have many stamp designs to choose from.\")","elif userReply == \"envelope\":","    print(\"We have many envelope sizes to choose from.\")","elif userReply == \"copy\":","    copies = input(\"How many copies would you like? (Enter a number) \")","    print(\"Here are {} copies.\".format(copies))","else:","    print(\"Thank you, please come again.\")"]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"insert","lines":[" "],"id":46}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":1},"action":"remove","lines":[" "],"id":47}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":48}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["userReply = input(\"Do you need to ship a package? (Enter yes or no) \")",""],"id":49}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":47},"action":"insert","lines":["if userReply == \"yes\":","    print(\"We can help you ship that package!\")"],"id":50}],[{"start":{"row":2,"column":47},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":51},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":4},"end":{"row":4,"column":73},"action":"insert","lines":["else:","    print(\"Please come back when you need to ship a package. Thank you.\")"],"id":52}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"remove","lines":["    "],"id":53}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":3,"column":0},"end":{"row":3,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1728847533802,"hash":"e1442012cd6133b83ddeb257a036dd22f1b13046"}