# R012 ChatGPT layer packets

This file describes all 116 measured prompt/state/side networks. It contains no semantic topic labels.

Positive and negative mean cosine alignment and anti-alignment with the evolving whole-prompt final-position state. Negative does not by itself establish suppression, contradiction or exclusion.

## State 00 — input_embedding

Paired positive_head: membership Jaccard 1.000000; edge Jaccard 1.000000; shared tokens 4186.
Paired negative_tail: membership Jaccard 1.000000; edge Jaccard 1.000000; shared tokens 1237.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 4186
- Directed 10-NN edges: 41860
- Undirected edges: 30377
- Communities: 16
- Modularity: 0.737890

All communities:

- C0 (n=741): representatives [␠transformations, ␠communications, ␠computational, ␠psychological, ␠quantitative, ␠simulation, ␠investigations, ␠tuning, ␠substances, ␠decomposition]; target-extreme [中国, ␠visualization, 国家, ␠research, ␠tiles, ␠ships]; classes {'alphabetic': 701, 'mixed': 40}
- C1 (n=534): representatives [));\n\n, ");\r\n, )));\n, ');\r\n\r\n, ])));\n, ");\r\n\r\n, >";\r\n, ));\r\n, "));\r\n, ']));\n]; target-extreme [);\n, ();\n, );\r\n, );\n\n, ";\n, ;\r\n\r\n]; classes {'alphabetic': 1, 'mixed': 2, 'punctuation': 531}
- C2 (n=470): representatives [[, }), ]), )), .", .”, )\, ␠+, )}, =]; target-extreme [), “, )., \, .\, ]]; classes {'alphabetic': 17, 'mixed': 11, 'punctuation': 442}
- C3 (n=409): representatives [␠calculating, ␠comparing, ␠providing, ␠provides, ␠gives, ␠indicates, ␠allows, ␠represents, ␠makes, ␠determined]; target-extreme [␠examines, ␠combines, ␠identifies, ␠relies, ␠interpreting, ␠incorporates]; classes {'alphabetic': 407, 'mixed': 2}
- C4 (n=349): representatives [)\n, .\n\n, .\n, \n\n, ……\n\n, \r\n, ;\n, )\n\n, '\r\n, _\n\n]; target-extreme [\n\n, \r\n, .\n, 。\n, )\n, ;\n]; classes {'alphabetic': 4, 'mixed': 1, 'punctuation': 338, 'whitespace': 6}
- C5 (n=324): representatives [s, ing, 的, i, ␠of, ␠�, S, 은, (, t]; target-extreme [␠=, (, 的, ␠that, ␠and, The]; classes {'alphabetic': 258, 'mixed': 25, 'punctuation': 41}
- C6 (n=243): representatives [)))\n, "))\r\n, )))))\n, ))))\n, )))\r\n, ")\r\n, ")))\n, ')\r\n\r\n, )))\n\n, ]))\r\n]; target-extreme [)\r\n, ]\n, ()\n, ')\n, ")\n, }\n]; classes {'punctuation': 243}
- C7 (n=176): representatives [␠\r\n, \t\t\n, \r\n␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠\r\n, \n␠␠␠␠\n, ␠␠␠␠␠␠␠␠\r\n, \n\t\n, ␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠\r\n]; target-extreme [␠\r\n, \n␠\n,  \n, \n\t\n, \n␠␠␠␠\n, \t\n]; classes {'alphabetic': 2, 'punctuation': 6, 'whitespace': 168}
- C8 (n=165): representatives [【, """\n, /*\r\n, """\r\n, ///\r\n, ﻿, /*\n, """\n\n, -----------\n, ---------\n]; target-extreme [**\n, *\n, package, /*\n, *\r\n, **\r\n]; classes {'alphabetic': 11, 'mixed': 3, 'punctuation': 151}
- C9 (n=162): representatives [).\n\n\n, )\n\n\n, ).\n\n\n\n, .\n\n\n\n, );\n\n\n, ])\n\n\n, \n\n\n, .\n\n\n, ')\n\n\n, ")\n\n\n]; target-extreme [\n\n\n, .\n\n\n, ␠\n\n, \n\n\n\n, )\n\n\n, \r\n\r\n\r\n]; classes {'alphabetic': 2, 'mixed': 2, 'punctuation': 136, 'special': 1, 'whitespace': 21}
- C10 (n=160): representatives [){\n, ␠+\n, ){\r\n, '){\n, ␠+\r\n, ␠=\n, ␠{\n, ␠{\r\n, {\r\n, (){\r\n]; target-extreme [␠{\n, |\n, ␠|\n, {, ){\n, =\n]; classes {'mixed': 1, 'punctuation': 154, 'whitespace': 5}
- C11 (n=152): representatives ["),\n, ",\n, ]),\n, )),\r\n, '),\n, )),\n, '),\r\n, .",\n, ")),\n, ",\r\n]; target-extreme [，\n, ),\n, ,\r\n, ',\n, ,\n\n, ",\n]; classes {'alphabetic': 1, 'punctuation': 151}
- C12 (n=134): representatives ["}}>\n, ">\n, */\r\n, }>\n, }*/\n, '}>\n, "}>\n, */\n, ␠*/\n, ␠*/\r\n]; target-extreme [>\n, >\r\n, >\n\n, >, ␠*/\n, )>\n]; classes {'mixed': 1, 'punctuation': 133}
- C13 (n=70): representatives [\t, ␠␠,  , ␠␠␠, ␠␠␠␠␠␠␠, ␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠, ␠␠␠␠␠␠␠, \t, ␠␠␠␠␠␠␠␠␠␠␠, ␠, ␠␠]; classes {'alphabetic': 1, 'numeric': 3, 'punctuation': 2, 'whitespace': 64}
- C14 (n=51): representatives [␠manually, ␠electronically, ␠simultaneously, ␠automatically, ␠separately, ␠immediately, ␠effectively, ␠internationally, ␠independently, ␠collectively]; target-extreme [␠recursively, ␠physically, ␠independently, ␠systematically, ␠individually, ␠internally]; classes {'alphabetic': 50, 'mixed': 1}
- C15 (n=46): representatives [):\n, ):\r\n, ]):\n, "):\n, "):\r\n, )):\n, ':\r\n, ):\r\n\r\n, ]):\r\n, ()):\n]; target-extreme [):\n, :\r\n, ):\r\n, ):\n\n, '):\n, "):\n]; classes {'punctuation': 46}

Strongest intercommunity connections:

- C0 to C3: 786 token edges; mean cosine 0.156408
- C1 to C6: 412 token edges; mean cosine 0.333348
- C2 to C4: 343 token edges; mean cosine 0.302038
- C1 to C4: 258 token edges; mean cosine 0.323251
- C0 to C5: 210 token edges; mean cosine 0.133712
- C2 to C5: 206 token edges; mean cosine 0.198774
- C4 to C6: 187 token edges; mean cosine 0.354642
- C1 to C11: 125 token edges; mean cosine 0.295086
- C3 to C5: 122 token edges; mean cosine 0.148030
- C4 to C8: 112 token edges; mean cosine 0.269352
- C1 to C9: 107 token edges; mean cosine 0.324533
- C2 to C8: 100 token edges; mean cosine 0.225324
- C0 to C14: 98 token edges; mean cosine 0.151425
- C4 to C9: 94 token edges; mean cosine 0.355035
- C6 to C12: 84 token edges; mean cosine 0.285973

#### negative_tail

- Nodes: 1237
- Directed 10-NN edges: 12370
- Undirected edges: 8917
- Communities: 10
- Modularity: 0.372438

All communities:

- C0 (n=224): representatives [␠współprac, ␠spriteBatch, ␠الكمبي, BrowserRouter, idUser, ␠לבח, uibModal, ␠SwiftUI, xfff, ScrollPane]; target-extreme [tearDown, .JWT, 时许, xfff, \Response, .Servlet]; classes {'alphabetic': 161, 'mixed': 57, 'punctuation': 6}
- C1 (n=219): representatives [edula, airro, ␠yanında, Direccion, ktör, ␠soirée, semicolon, ugador, 賺, традицион]; target-extreme [.usuario, ␠бренд, prend, érience, ␠benefici, ␠Câmara]; classes {'alphabetic': 211, 'mixed': 7, 'punctuation': 1}
- C2 (n=177): representatives [Ḝ, ␠שאנ, ␠מדה, .ReadUInt, książ, 䣘, ␠dwó, عظيم, 헐, แถ]; target-extreme [␠ayr, 褟, euillez, ␠atol, ␠breat, urrenc]; classes {'alphabetic': 171, 'mixed': 6}
- C3 (n=176): representatives [䴓, ﭩ, תושבי, 췐, ㌃, ᚖ, ﯪ, Ⓤ, 荄, ␠אברה]; target-extreme [㠓, ཡ, 𝖞, ꒦, ᩈ, ᅢ]; classes {'alphabetic': 143, 'mixed': 2, 'punctuation': 31}
- C4 (n=149): representatives [뵀, 🖒, ﰿ, нибуд, ␠discrepan, Ӭ, ﲬ, أخو, ␠überh, 🤱]; target-extreme [ﮍ, んですけど, ᴖ, 𖠚, 쿳, 덯]; classes {'alphabetic': 129, 'mixed': 7, 'punctuation': 13}
- C5 (n=110): representatives [מבוג, �, ␠pożyczk, �, 깄, 힜, �, �, 枍, 팼]; target-extreme [됫, 깄, 얽, 觃, מעצב, �]; classes {'alphabetic': 74, 'mixed': 1, 'punctuation': 35}
- C6 (n=82): representatives [␠לטובת, התפתח, ␠możliwość, ␠śwież, ␠entwick, יכ, צטר, が増え, ␠umożliw, ␠универс]; target-extreme [␠as, 6, ␠one, 5, ␠gotta, ␠do]; classes {'alphabetic': 80, 'numeric': 2}
- C7 (n=56): representatives [쥉, פרופ, ספורט, ␠Boehner, ␠sektör, ␠Monsanto, מנהיג, עיתונ, ␠Politico, 뮌]; target-extreme [עיתונ, 𫠊, פסיכ, פוליט, ␠פוסטים, למידה]; classes {'alphabetic': 55, 'punctuation': 1}
- C8 (n=27): representatives [ឥ, Ἥ, Ằ, ἔ, อำนา, ὐ, ὁ, ὖ, Ἑ, ἤ]; target-extreme [␠alcan, ἔ, แฮ, อำนา, Ἑ, Ἥ]; classes {'alphabetic': 27}
- C9 (n=17): representatives [␠libertine, ␠svens, ␠clit, ␠erotici, ␠norge, ␠creampie, ␠kinky, ␠bordel, ␠Fucked, ␠boob]; target-extreme [␠Blowjob, ␠gratuiti, ␠bordel, ␠clit, ␠norge, 잖아]; classes {'alphabetic': 17}

Strongest intercommunity connections:

- C3 to C4: 300 token edges; mean cosine 0.132307
- C0 to C2: 298 token edges; mean cosine 0.115332
- C0 to C1: 280 token edges; mean cosine 0.106084
- C1 to C2: 269 token edges; mean cosine 0.111640
- C3 to C5: 260 token edges; mean cosine 0.133424
- C0 to C3: 238 token edges; mean cosine 0.121487
- C2 to C3: 235 token edges; mean cosine 0.126216
- C2 to C5: 204 token edges; mean cosine 0.121828
- C4 to C5: 168 token edges; mean cosine 0.126333
- C1 to C3: 138 token edges; mean cosine 0.111967
- C1 to C4: 138 token edges; mean cosine 0.108764
- C2 to C4: 131 token edges; mean cosine 0.114171
- C0 to C5: 122 token edges; mean cosine 0.118294
- C2 to C6: 119 token edges; mean cosine 0.114718
- C1 to C6: 118 token edges; mean cosine 0.107144

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 4186
- Directed 10-NN edges: 41860
- Undirected edges: 30377
- Communities: 16
- Modularity: 0.737890

All communities:

- C0 (n=741): representatives [␠transformations, ␠communications, ␠computational, ␠psychological, ␠quantitative, ␠simulation, ␠investigations, ␠tuning, ␠substances, ␠decomposition]; target-extreme [中国, ␠visualization, 国家, ␠research, ␠tiles, ␠ships]; classes {'alphabetic': 701, 'mixed': 40}
- C1 (n=534): representatives [));\n\n, ");\r\n, )));\n, ');\r\n\r\n, ])));\n, ");\r\n\r\n, >";\r\n, ));\r\n, "));\r\n, ']));\n]; target-extreme [);\n, ();\n, );\r\n, );\n\n, ";\n, ;\r\n\r\n]; classes {'alphabetic': 1, 'mixed': 2, 'punctuation': 531}
- C2 (n=470): representatives [[, }), ]), )), .", .”, )\, ␠+, )}, =]; target-extreme [), “, )., \, .\, ]]; classes {'alphabetic': 17, 'mixed': 11, 'punctuation': 442}
- C3 (n=409): representatives [␠calculating, ␠comparing, ␠providing, ␠provides, ␠gives, ␠indicates, ␠allows, ␠represents, ␠makes, ␠determined]; target-extreme [␠examines, ␠combines, ␠identifies, ␠relies, ␠interpreting, ␠incorporates]; classes {'alphabetic': 407, 'mixed': 2}
- C4 (n=349): representatives [)\n, .\n\n, .\n, \n\n, ……\n\n, \r\n, ;\n, )\n\n, '\r\n, _\n\n]; target-extreme [\n\n, \r\n, .\n, 。\n, )\n, ;\n]; classes {'alphabetic': 4, 'mixed': 1, 'punctuation': 338, 'whitespace': 6}
- C5 (n=324): representatives [s, ing, 的, i, ␠of, ␠�, S, 은, (, t]; target-extreme [␠=, (, 的, ␠that, ␠and, The]; classes {'alphabetic': 258, 'mixed': 25, 'punctuation': 41}
- C6 (n=243): representatives [)))\n, "))\r\n, )))))\n, ))))\n, )))\r\n, ")\r\n, ")))\n, ')\r\n\r\n, )))\n\n, ]))\r\n]; target-extreme [)\r\n, ]\n, ()\n, ')\n, ")\n, }\n]; classes {'punctuation': 243}
- C7 (n=176): representatives [␠\r\n, \t\t\n, \r\n␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠\r\n, \n␠␠␠␠\n, ␠␠␠␠␠␠␠␠\r\n, \n\t\n, ␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠\r\n]; target-extreme [␠\r\n, \n␠\n,  \n, \n\t\n, \n␠␠␠␠\n, \t\n]; classes {'alphabetic': 2, 'punctuation': 6, 'whitespace': 168}
- C8 (n=165): representatives [【, """\n, /*\r\n, """\r\n, ///\r\n, ﻿, /*\n, """\n\n, -----------\n, ---------\n]; target-extreme [**\n, *\n, package, /*\n, *\r\n, **\r\n]; classes {'alphabetic': 11, 'mixed': 3, 'punctuation': 151}
- C9 (n=162): representatives [).\n\n\n, )\n\n\n, ).\n\n\n\n, .\n\n\n\n, );\n\n\n, ])\n\n\n, \n\n\n, .\n\n\n, ')\n\n\n, ")\n\n\n]; target-extreme [\n\n\n, .\n\n\n, ␠\n\n, \n\n\n\n, )\n\n\n, \r\n\r\n\r\n]; classes {'alphabetic': 2, 'mixed': 2, 'punctuation': 136, 'special': 1, 'whitespace': 21}
- C10 (n=160): representatives [){\n, ␠+\n, ){\r\n, '){\n, ␠+\r\n, ␠=\n, ␠{\n, ␠{\r\n, {\r\n, (){\r\n]; target-extreme [␠{\n, |\n, ␠|\n, {, ){\n, =\n]; classes {'mixed': 1, 'punctuation': 154, 'whitespace': 5}
- C11 (n=152): representatives ["),\n, ",\n, ]),\n, )),\r\n, '),\n, )),\n, '),\r\n, .",\n, ")),\n, ",\r\n]; target-extreme [，\n, ),\n, ,\r\n, ',\n, ,\n\n, ",\n]; classes {'alphabetic': 1, 'punctuation': 151}
- C12 (n=134): representatives ["}}>\n, ">\n, */\r\n, }>\n, }*/\n, '}>\n, "}>\n, */\n, ␠*/\n, ␠*/\r\n]; target-extreme [>\n, >\r\n, >\n\n, >, ␠*/\n, )>\n]; classes {'mixed': 1, 'punctuation': 133}
- C13 (n=70): representatives [\t, ␠␠,  , ␠␠␠, ␠␠␠␠␠␠␠, ␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠, ␠␠␠␠␠␠␠, \t, ␠␠␠␠␠␠␠␠␠␠␠, ␠, ␠␠]; classes {'alphabetic': 1, 'numeric': 3, 'punctuation': 2, 'whitespace': 64}
- C14 (n=51): representatives [␠manually, ␠electronically, ␠simultaneously, ␠automatically, ␠separately, ␠immediately, ␠effectively, ␠internationally, ␠independently, ␠collectively]; target-extreme [␠recursively, ␠physically, ␠independently, ␠systematically, ␠individually, ␠internally]; classes {'alphabetic': 50, 'mixed': 1}
- C15 (n=46): representatives [):\n, ):\r\n, ]):\n, "):\n, "):\r\n, )):\n, ':\r\n, ):\r\n\r\n, ]):\r\n, ()):\n]; target-extreme [):\n, :\r\n, ):\r\n, ):\n\n, '):\n, "):\n]; classes {'punctuation': 46}

Strongest intercommunity connections:

- C0 to C3: 786 token edges; mean cosine 0.156408
- C1 to C6: 412 token edges; mean cosine 0.333348
- C2 to C4: 343 token edges; mean cosine 0.302038
- C1 to C4: 258 token edges; mean cosine 0.323251
- C0 to C5: 210 token edges; mean cosine 0.133712
- C2 to C5: 206 token edges; mean cosine 0.198774
- C4 to C6: 187 token edges; mean cosine 0.354642
- C1 to C11: 125 token edges; mean cosine 0.295086
- C3 to C5: 122 token edges; mean cosine 0.148030
- C4 to C8: 112 token edges; mean cosine 0.269352
- C1 to C9: 107 token edges; mean cosine 0.324533
- C2 to C8: 100 token edges; mean cosine 0.225324
- C0 to C14: 98 token edges; mean cosine 0.151425
- C4 to C9: 94 token edges; mean cosine 0.355035
- C6 to C12: 84 token edges; mean cosine 0.285973

#### negative_tail

- Nodes: 1237
- Directed 10-NN edges: 12370
- Undirected edges: 8917
- Communities: 10
- Modularity: 0.372438

All communities:

- C0 (n=224): representatives [␠współprac, ␠spriteBatch, ␠الكمبي, BrowserRouter, idUser, ␠לבח, uibModal, ␠SwiftUI, xfff, ScrollPane]; target-extreme [tearDown, .JWT, 时许, xfff, \Response, .Servlet]; classes {'alphabetic': 161, 'mixed': 57, 'punctuation': 6}
- C1 (n=219): representatives [edula, airro, ␠yanında, Direccion, ktör, ␠soirée, semicolon, ugador, 賺, традицион]; target-extreme [.usuario, ␠бренд, prend, érience, ␠benefici, ␠Câmara]; classes {'alphabetic': 211, 'mixed': 7, 'punctuation': 1}
- C2 (n=177): representatives [Ḝ, ␠שאנ, ␠מדה, .ReadUInt, książ, 䣘, ␠dwó, عظيم, 헐, แถ]; target-extreme [␠ayr, 褟, euillez, ␠atol, ␠breat, urrenc]; classes {'alphabetic': 171, 'mixed': 6}
- C3 (n=176): representatives [䴓, ﭩ, תושבי, 췐, ㌃, ᚖ, ﯪ, Ⓤ, 荄, ␠אברה]; target-extreme [㠓, ཡ, 𝖞, ꒦, ᩈ, ᅢ]; classes {'alphabetic': 143, 'mixed': 2, 'punctuation': 31}
- C4 (n=149): representatives [뵀, 🖒, ﰿ, нибуд, ␠discrepan, Ӭ, ﲬ, أخو, ␠überh, 🤱]; target-extreme [ﮍ, んですけど, ᴖ, 𖠚, 쿳, 덯]; classes {'alphabetic': 129, 'mixed': 7, 'punctuation': 13}
- C5 (n=110): representatives [מבוג, �, ␠pożyczk, �, 깄, 힜, �, �, 枍, 팼]; target-extreme [됫, 깄, 얽, 觃, מעצב, �]; classes {'alphabetic': 74, 'mixed': 1, 'punctuation': 35}
- C6 (n=82): representatives [␠לטובת, התפתח, ␠możliwość, ␠śwież, ␠entwick, יכ, צטר, が増え, ␠umożliw, ␠универс]; target-extreme [␠as, 6, ␠one, 5, ␠gotta, ␠do]; classes {'alphabetic': 80, 'numeric': 2}
- C7 (n=56): representatives [쥉, פרופ, ספורט, ␠Boehner, ␠sektör, ␠Monsanto, מנהיג, עיתונ, ␠Politico, 뮌]; target-extreme [עיתונ, 𫠊, פסיכ, פוליט, ␠פוסטים, למידה]; classes {'alphabetic': 55, 'punctuation': 1}
- C8 (n=27): representatives [ឥ, Ἥ, Ằ, ἔ, อำนา, ὐ, ὁ, ὖ, Ἑ, ἤ]; target-extreme [␠alcan, ἔ, แฮ, อำนา, Ἑ, Ἥ]; classes {'alphabetic': 27}
- C9 (n=17): representatives [␠libertine, ␠svens, ␠clit, ␠erotici, ␠norge, ␠creampie, ␠kinky, ␠bordel, ␠Fucked, ␠boob]; target-extreme [␠Blowjob, ␠gratuiti, ␠bordel, ␠clit, ␠norge, 잖아]; classes {'alphabetic': 17}

Strongest intercommunity connections:

- C3 to C4: 300 token edges; mean cosine 0.132307
- C0 to C2: 298 token edges; mean cosine 0.115332
- C0 to C1: 280 token edges; mean cosine 0.106084
- C1 to C2: 269 token edges; mean cosine 0.111640
- C3 to C5: 260 token edges; mean cosine 0.133424
- C0 to C3: 238 token edges; mean cosine 0.121487
- C2 to C3: 235 token edges; mean cosine 0.126216
- C2 to C5: 204 token edges; mean cosine 0.121828
- C4 to C5: 168 token edges; mean cosine 0.126333
- C1 to C3: 138 token edges; mean cosine 0.111967
- C1 to C4: 138 token edges; mean cosine 0.108764
- C2 to C4: 131 token edges; mean cosine 0.114171
- C0 to C5: 122 token edges; mean cosine 0.118294
- C2 to C6: 119 token edges; mean cosine 0.114718
- C1 to C6: 118 token edges; mean cosine 0.107144

## State 01 — block_0_output

Paired positive_head: membership Jaccard 0.963309; edge Jaccard 0.903968; shared tokens 5356.
Paired negative_tail: membership Jaccard 0.946306; edge Jaccard 0.862968; shared tokens 4406.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5361
- Directed 10-NN edges: 53610
- Undirected edges: 38722
- Communities: 12
- Modularity: 0.585485

All communities:

- C0 (n=1017): representatives [ik, ol, ile, ities, ap, ick, ok, ter, um, ken]; target-extreme [lut, hap, oningen, inki, ek, nx]; classes {'alphabetic': 986, 'mixed': 29, 'numeric': 1, 'punctuation': 1}
- C1 (n=955): representatives [␠cut, ␠difference, ␠think, ␠laser, ␠report, ␠left, ␠holes, ␠product, ␠spectra, ␠Size]; target-extreme [␠Spare, ␠Chicken, ␠staircase, ␠difference, ␠fingerprints, ␠holes]; classes {'alphabetic': 929, 'mixed': 26}
- C2 (n=702): representatives [痦, ␠goalkeeper, نطق, .DropDownStyle, ␠לפעול, ␠commentary, ␠checker, ␠carbohydrate, ␠thermostat, INFRINGEMENT]; target-extreme [␠Checker, -feedback, 屼, ␠perl, \tcontroller, toString]; classes {'alphabetic': 537, 'mixed': 144, 'punctuation': 21}
- C3 (n=649): representatives [ようになりました, になりました, だと思います, になると, していました, それでも, ありがとうございます, ались, ␠الجميع, дается]; target-extreme [见面, ались, דמו, ので, 这样说, ␠Approved]; classes {'alphabetic': 629, 'mixed': 16, 'punctuation': 4}
- C4 (n=542): representatives [␠contractors, ␠discrepancy, ␠discrepancies, ␠Surgery, ␠transformations, ␠fragmentation, ␠concentrations, ␠Council, ␠Conservation, ␠completeness]; target-extreme [␠fairness, ␠intervention, ␠instruct, ␠inspector, ␠king, ␠confrontation]; classes {'alphabetic': 516, 'mixed': 26}
- C5 (n=495): representatives [).\n\n\n, ).\n\n\n\n, .\n, .", )\n, .\n\n, \n\n, ␠\r\n, )\r\n, \r\n]; target-extreme [.\n, ., .\n\n, \n\n\n\n, ␠, \n\n\n]; classes {'alphabetic': 11, 'mixed': 16, 'punctuation': 447, 'whitespace': 21}
- C6 (n=408): representatives [");\r\n, ")\r\n, ));\r\n, ]))\r\n, ))\n, )))\n, "))\r\n, ')\r\n\r\n, )))\r\n, ))\r\n]; target-extreme [）\r\n, \r\n\r\n, ␠')\n, ]\r\n, ␠'/')\n, ␠'');\n\n]; classes {'alphabetic': 1, 'mixed': 2, 'punctuation': 402, 'whitespace': 3}
- C7 (n=157): representatives [␠Richardson, ␠Turkey, ␠Malaysia, ␠Japan, ␠Russia, ␠Montgomery, ␠Korea, ␠Afghanistan, ␠Singapore, ␠America]; target-extreme [␠Iraq, ␠Malaysia, ␠Richardson, ␠Montgomery, ␠Turkey, ␠Darling]; classes {'alphabetic': 154, 'mixed': 3}
- C8 (n=150): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, -------------</, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠\t\t\t, ␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠\t\t, \n␠\n, *****\n\n, \t\t␠␠␠␠␠␠␠␠␠␠␠, -----------\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 2, 'punctuation': 62, 'whitespace': 86}
- C9 (n=99): representatives [>k, }}>, ␠}}>\n, ">\n, $k, ␠?>\n, ␠?>">\n, '}}>\n, )f, )r]; target-extreme [">\n, >\r\n, ?>\n, >>\n, ">\r\n, ␠-->\r\n]; classes {'alphabetic': 8, 'mixed': 29, 'punctuation': 61, 'whitespace': 1}
- C10 (n=97): representatives [),\n, "),\n, ")),\n, ",\n, ]),\n, ],\n, '),\r\n, )),\r\n, ),\r\n, '),\n]; target-extreme [],\n, "],\n, ,\r\n, '),\r\n, '],\n, ],\r\n]; classes {'punctuation': 97}
- C11 (n=90): representatives [␠don, ␠�, ␠�, ␠according, ␠�, ␠�, ␠�, ␠weren, ␠�, ifferences]; target-extreme [There, ␠�, ␠according, ␠�, Difference, ␠不]; classes {'alphabetic': 49, 'mixed': 6, 'punctuation': 35}

Strongest intercommunity connections:

- C1 to C4: 1371 token edges; mean cosine 0.133144
- C0 to C1: 1096 token edges; mean cosine 0.133062
- C1 to C2: 940 token edges; mean cosine 0.125676
- C2 to C3: 784 token edges; mean cosine 0.120945
- C1 to C3: 692 token edges; mean cosine 0.128382
- C0 to C3: 652 token edges; mean cosine 0.128767
- C0 to C2: 646 token edges; mean cosine 0.118520
- C2 to C4: 634 token edges; mean cosine 0.122760
- C5 to C6: 534 token edges; mean cosine 0.307083
- C0 to C4: 468 token edges; mean cosine 0.126807
- C3 to C4: 409 token edges; mean cosine 0.125356
- C0 to C7: 236 token edges; mean cosine 0.127070
- C4 to C7: 174 token edges; mean cosine 0.122690
- C2 to C7: 174 token edges; mean cosine 0.119265
- C1 to C7: 168 token edges; mean cosine 0.127586

#### negative_tail

- Nodes: 4654
- Directed 10-NN edges: 46540
- Undirected edges: 33850
- Communities: 10
- Modularity: 0.466190

All communities:

- C0 (n=796): representatives [␠AssemblyFileVersion, BootApplication, .destroyAllWindows, routeProvider, ᶫ, .setBackgroundResource, ␠OnCollision, ␠WPARAM, CloseOperation, ␠ParameterDirection]; target-extreme [_ESCAPE, MediaPlayer, Jvm, 凫, .createSequentialGroup, 揄]; classes {'alphabetic': 548, 'mixed': 218, 'punctuation': 30}
- C1 (n=762): representatives [\tdes, ␠profes, _done, ␠RECE, _Settings, _ISS, ROSS, ␠NUM, ␠Occup, ␠unh]; target-extreme [␠Phys, /div, DTD, _CAP, .asset, _WATCH]; classes {'alphabetic': 397, 'mixed': 365}
- C2 (n=680): representatives [母校, профессиона, ␠retail, ␠acidic, 奢侈品, ␠vibrant, 诠释, 游艇, мещ, 밈]; target-extreme [Introduced, rapid, 财税, 戏曲, 场馆, 重心]; classes {'alphabetic': 671, 'mixed': 9}
- C3 (n=509): representatives [а, ์, ing, ␠of, ␠ס, ␠הח, 𝑎, s, �, ﾞ]; target-extreme [␠of, import, ␠with, ␠for, _of, ␠נת]; classes {'alphabetic': 431, 'mixed': 20, 'numeric': 1, 'punctuation': 57}
- C4 (n=449): representatives [からの, 最常见的, ␠vielleicht, нный, 所所, مناسبة, ␠بلا, 気軽に, منظمات, 深入推进]; target-extreme [就能够, 現代, 创始, 笫, 供养, ␠במהלך]; classes {'alphabetic': 441, 'mixed': 7, 'punctuation': 1}
- C5 (n=358): representatives [🏦, 🉑, ✽, 💨, ₶, ﯭ, 🏛, �, 👩, 🚌]; target-extreme [הצלחת, �, łoż, ᴈ, 䢼, 䄀]; classes {'alphabetic': 231, 'mixed': 1, 'punctuation': 126}
- C6 (n=334): representatives [␠Showing, ␠retrieve, ␠preached, ␠Getting, ␠restarting, ␠Running, ␠upcoming, ␠sessions, ␠fetching, Repo]; target-extreme [Fetching, ␠braking, ␠Creating, ␠Naming, rowsing, Writes]; classes {'alphabetic': 257, 'mixed': 77}
- C7 (n=283): representatives [#{@, (sh, (clean, (itemId, (template, (run, ␠*&, ␠,$, $get, ={`/]; target-extreme [,www, <Class, /renderer, #{@, \tconstructor, (strings]; classes {'alphabetic': 17, 'mixed': 161, 'punctuation': 104, 'whitespace': 1}
- C8 (n=282): representatives [␠işle, ␠получа, ␠çalış, ␠cré, ␠sécur, ␠açık, ␠ciné, ␠salarié, zano, ␠consum]; target-extreme [␠cré, ␠ciné, attro, iveau, ␠Método, ␠Cré]; classes {'alphabetic': 277, 'mixed': 4, 'punctuation': 1}
- C9 (n=201): representatives [Hugh, ␠AHL, 金陵, ␠Churchill, ␠Shiv, ␠Jenna, 禾, 榆林, 湖人, 哈登]; target-extreme [␠veter, ␠AHL, ␠Jays, ␠Giul, ␠Madison, Hugh]; classes {'alphabetic': 200, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C5: 907 token edges; mean cosine 0.137256
- C2 to C4: 744 token edges; mean cosine 0.130342
- C0 to C2: 742 token edges; mean cosine 0.127713
- C0 to C1: 742 token edges; mean cosine 0.122805
- C1 to C6: 698 token edges; mean cosine 0.125918
- C1 to C2: 604 token edges; mean cosine 0.126899
- C2 to C6: 528 token edges; mean cosine 0.129961
- C1 to C3: 473 token edges; mean cosine 0.127344
- C2 to C8: 441 token edges; mean cosine 0.130394
- C3 to C4: 440 token edges; mean cosine 0.131025
- C0 to C7: 400 token edges; mean cosine 0.130184
- C1 to C8: 398 token edges; mean cosine 0.130748
- C1 to C7: 391 token edges; mean cosine 0.130066
- C2 to C3: 373 token edges; mean cosine 0.123087
- C0 to C8: 372 token edges; mean cosine 0.131462

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5555
- Directed 10-NN edges: 55550
- Undirected edges: 40108
- Communities: 12
- Modularity: 0.588061

All communities:

- C0 (n=1303): representatives [␠difference, ␠contractors, ␠discrepancy, ␠laser, ␠discrepancies, ␠Surgery, ␠fragmentation, ␠holes, ␠concentrations, ␠completeness]; target-extreme [␠fairness, 见面, ␠Chicken, ␠staircase, ␠instruct, ␠intervention]; classes {'alphabetic': 1232, 'mixed': 71}
- C1 (n=976): representatives [ik, ol, ile, ities, ak, ap, ick, ter, ok, um]; target-extreme [lut, hap, inki, ek, nx, jni]; classes {'alphabetic': 937, 'mixed': 34, 'numeric': 1, 'punctuation': 4}
- C2 (n=888): representatives [ようになりました, 痦, していました, ありがとうございます, になりました, だと思います, それでも, になると, ␠الجميع, نطق]; target-extreme [דמו, ้าย, ので, ␠الحقيقي, 屼, صيب]; classes {'alphabetic': 779, 'mixed': 87, 'punctuation': 22}
- C3 (n=574): representatives [).\n\n\n, ).\n\n\n\n, .\n, .", )\n, .\n\n, \n\n, ␠\r\n, \r\n, ␠don]; target-extreme [.\n, ., .\n\n, \n\n\n\n, ␠, \n\n\n]; classes {'alphabetic': 50, 'mixed': 19, 'punctuation': 442, 'whitespace': 63}
- C4 (n=563): representatives [␠cut, ␠think, ␠left, ␠report, ␠product, ␠monitor, ␠fit, ␠shrink, ␠book, ␠height]; target-extreme [␠Spare, ␠standby, ␠shrink, ␠plunge, 戳, 这样说]; classes {'alphabetic': 541, 'mixed': 22}
- C5 (n=472): representatives [");\r\n, ")\r\n, ));\r\n, ]))\r\n, ))\n, ')\r\n\r\n, ))\r\n, )))\n, "))\r\n, )))\r\n]; target-extreme [）\r\n, .'\n, \r\n\r\n, ␠')\n, ]\r\n, ␠'/')\n]; classes {'alphabetic': 2, 'mixed': 2, 'punctuation': 465, 'whitespace': 3}
- C6 (n=177): representatives [),\n, "),\n, ")),\n, ",\n, ]),\n, )),\r\n, }}>, ],\n, ),\r\n, ␠}}>\n]; target-extreme [">\n, ],\n, "],\n, ,\r\n, '),\r\n, '],\n]; classes {'punctuation': 176, 'whitespace': 1}
- C7 (n=176): representatives [ались, ил, дается, ления, ании, ␠pensar, теля, ились, ивают, или]; target-extreme [ались, oningen, ики, واب, иков, ücken]; classes {'alphabetic': 171, 'mixed': 5}
- C8 (n=160): representatives [␠goalkeeper, ␠Malaysia, ␠Russia, ␠Richardson, ␠Japan, ␠Afghanistan, ␠Turkey, ␠Singapore, ␠Montgomery, ␠America]; target-extreme [␠Iraq, ␠Richardson, 쟙, ␠Malaysia, ␠Montgomery, ␠goalkeeper]; classes {'alphabetic': 159, 'mixed': 1}
- C9 (n=130): representatives [\tboard, >k, \tcontrol, $k, )}), )r, order, ,k, \tposition, )y]; target-extreme [%d, \tcontroller, _barang, /T, _where, ,state]; classes {'alphabetic': 53, 'mixed': 73, 'punctuation': 4}
- C10 (n=84): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不]; target-extreme [␠�, ␠�, ␠不, ␠�, ␠�, ␠remain]; classes {'alphabetic': 46, 'mixed': 2, 'punctuation': 36}
- C11 (n=52): representatives [␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠\t\t, \t\t␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 2, 'punctuation': 3, 'whitespace': 47}

Strongest intercommunity connections:

- C0 to C4: 1516 token edges; mean cosine 0.136045
- C0 to C2: 1200 token edges; mean cosine 0.121391
- C0 to C1: 1082 token edges; mean cosine 0.124917
- C1 to C4: 691 token edges; mean cosine 0.135133
- C3 to C5: 582 token edges; mean cosine 0.300607
- C1 to C2: 574 token edges; mean cosine 0.119583
- C2 to C4: 509 token edges; mean cosine 0.123616
- C1 to C7: 444 token edges; mean cosine 0.138634
- C0 to C8: 393 token edges; mean cosine 0.127768
- C2 to C7: 368 token edges; mean cosine 0.130563
- C2 to C3: 257 token edges; mean cosine 0.131592
- C1 to C8: 235 token edges; mean cosine 0.129418
- C5 to C6: 218 token edges; mean cosine 0.275819
- C1 to C9: 214 token edges; mean cosine 0.141560
- C3 to C6: 207 token edges; mean cosine 0.240538

#### negative_tail

- Nodes: 4408
- Directed 10-NN edges: 44080
- Undirected edges: 32073
- Communities: 9
- Modularity: 0.467647

All communities:

- C0 (n=779): representatives [␠AssemblyFileVersion, BootApplication, .destroyAllWindows, routeProvider, ␠işle, ␠OnCollision, .setBackgroundResource, ␠WPARAM, .CompareTag, CloseOperation]; target-extreme [_ESCAPE, MediaPlayer, ,www, Jvm, 凫, .createSequentialGroup]; classes {'alphabetic': 539, 'mixed': 217, 'punctuation': 23}
- C1 (n=712): representatives [␠profes, からの, 母校, 最常见的, ␠AHL, 奢侈品, 金陵, 游艇, 诠释, 额外]; target-extreme [就能够, ␠veter, 财税, 戏曲, 场馆, 現代]; classes {'alphabetic': 711, 'mixed': 1}
- C2 (n=658): representatives [␠RECE, ROSS, _ISS, ␠NUM, ILI, (itemId, (sh, (template, (run, _IND]; target-extreme [/div, DTD, .asset, _WATCH, _CAP, _ASS]; classes {'alphabetic': 238, 'mixed': 420}
- C3 (n=644): representatives [\tdes, профессиона, _done, ␠retail, ␠Showing, ␠retrieve, _Settings, ␠acidic, ␠vibrant, ␠preached]; target-extreme [Fetching, Introduced, rapid, ␠braking, ␠Método, iplinary]; classes {'alphabetic': 518, 'mixed': 126}
- C4 (n=617): representatives [␠получа, Hugh, ␠çalış, ␠cré, ␠sécur, ␠بلا, ␠ciné, ␠Athen, ␠liber, ␠ס]; target-extreme [␠Phys, ␠cré, ␠נת, ␠ciné, attro, ␠حر]; classes {'alphabetic': 589, 'mixed': 9, 'punctuation': 19}
- C5 (n=389): representatives [ᶫ, 🏦, 🉑, ✽, 💨, ₶, ﯭ, 🏛, �, 👩]; target-extreme [הצלחת, �, łoż, ᴈ, 䢼, 䄀]; classes {'alphabetic': 260, 'mixed': 2, 'punctuation': 127}
- C6 (n=245): representatives [␠vielleicht, ␠данный, ␠Após, Pago, ␠새로, ereço, ␠הבוקר, ␠преж, ␠쉽게, usuario]; target-extreme [iveau, ␠sexuales, ␠usuário, ␠במהלך, attività, cherche]; classes {'alphabetic': 242, 'mixed': 3}
- C7 (n=220): representatives [а, ing, ์, 𝑎, ␠of, s, �, �, ␠doesnt, ﾞ]; target-extreme [␠of, ␠with, ␠for, _of, ␠OF, ␠to]; classes {'alphabetic': 167, 'mixed': 13, 'punctuation': 40}
- C8 (n=144): representatives [#{@, ␠*&, ={`/, =new, ␠@$, =<?=$, ‥, ;;;;;;;;, ␠=$, 項目]; target-extreme [import, #{@, #ifndef, itled, (@, #ifdef]; classes {'alphabetic': 13, 'mixed': 27, 'numeric': 1, 'punctuation': 102, 'whitespace': 1}

Strongest intercommunity connections:

- C2 to C3: 1104 token edges; mean cosine 0.126613
- C0 to C5: 996 token edges; mean cosine 0.136838
- C1 to C3: 969 token edges; mean cosine 0.128917
- C1 to C4: 805 token edges; mean cosine 0.126884
- C0 to C1: 787 token edges; mean cosine 0.127130
- C0 to C2: 787 token edges; mean cosine 0.122976
- C0 to C3: 647 token edges; mean cosine 0.124848
- C3 to C4: 630 token edges; mean cosine 0.127082
- C2 to C4: 581 token edges; mean cosine 0.127287
- C0 to C4: 573 token edges; mean cosine 0.127938
- C1 to C6: 421 token edges; mean cosine 0.130523
- C4 to C5: 387 token edges; mean cosine 0.130257
- C4 to C6: 385 token edges; mean cosine 0.127611
- C1 to C5: 384 token edges; mean cosine 0.128803
- C1 to C2: 342 token edges; mean cosine 0.123776

## State 02 — block_1_output

Paired positive_head: membership Jaccard 0.946124; edge Jaccard 0.867415; shared tokens 5760.
Paired negative_tail: membership Jaccard 0.944473; edge Jaccard 0.860622; shared tokens 5494.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6006
- Directed 10-NN edges: 60060
- Undirected edges: 42977
- Communities: 11
- Modularity: 0.572368

All communities:

- C0 (n=1110): representatives [␠contractors, ␠transformations, ␠electrodes, ␠kitchen, ␠tomatoes, ␠discrepancy, ␠contractor, ␠constituency, ␠laser, ␠negotiations]; target-extreme [␠intervention, ␠Spare, Scotland, ␠Contractor, ␠staircase, ␠holes]; classes {'alphabetic': 1081, 'mixed': 28, 'punctuation': 1}
- C1 (n=1109): representatives [ik, ities, ap, ol, ak, ick, ley, et, ine, ok]; target-extreme [иков, ight, ики, inki, lut, orted]; classes {'alphabetic': 1088, 'mixed': 16, 'numeric': 1, 'punctuation': 4}
- C2 (n=962): representatives [␠cut, ␠think, ␠difference, ␠stripped, ␠control, ␠monitor, ␠spray, ␠drop, ␠deviation, ␠strapped]; target-extreme [␠standby, ␠instruct, plaint, 戳, ␠knocking, ␠variance]; classes {'alphabetic': 945, 'mixed': 17}
- C3 (n=936): representatives [")\r\n, ).\n\n\n\n, )))\r\n, ");\r\n, .", ));\r\n, ');\r\n\r\n, "))\r\n, ))\r\n, .\n\n]; target-extreme [., ],\n, ）\r\n, .\n, '),\r\n, ␠')\n]; classes {'alphabetic': 12, 'mixed': 12, 'numeric': 3, 'punctuation': 865, 'whitespace': 44}
- C4 (n=855): representatives [␠şikay, نطق, ␠לגמרי, 턔, ␠fontSize, 嵝, 痦, ␠нагрузк, ␠flashlight, なかなか]; target-extreme [скоп, ␠GetString, ␠loadData, -feedback, ␠birthdays, .Txt]; classes {'alphabetic': 723, 'mixed': 122, 'punctuation': 10}
- C5 (n=528): representatives [だと思います, ようになりました, ␠그것을, ␠الجميع, ありがとうございます, していました, になりました, ませんでした, だったので, それでも]; target-extreme [ались, 不會, ので, 见面, несен, ␠изделия]; classes {'alphabetic': 507, 'mixed': 11, 'punctuation': 10}
- C6 (n=306): representatives [yk, rk, DM, ,k, lb, LK, [k, FB, "f, (k]; target-extreme [nx, rk, xF, jt, ␠abc, >n]; classes {'alphabetic': 212, 'mixed': 93, 'punctuation': 1}
- C7 (n=78): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, \t\t␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 4, 'punctuation': 20, 'whitespace': 54}
- C8 (n=60): representatives [␠�, ␠不, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; target-extreme [_barang, ␠不, ␠�, ␠�, ␠�, ␠�]; classes {'alphabetic': 30, 'mixed': 3, 'punctuation': 27}
- C9 (n=46): representatives [␠Size, \theight, ␠sizes, size, \tcolor, \twidth, left, \tleft, \tposition, Color]; target-extreme [\twidth, ␠Right, color, Right, ␠Size, ␠Line]; classes {'alphabetic': 38, 'mixed': 8}
- C10 (n=16): representatives [++){\n, ␠""){\n, ])){\n, ␠()=>, ()){, )){\r\n, ){\n, ␠(){, ){\r\n, ()){\n]; target-extreme []){\n, ){\n, )){\r\n, "){\r\n, ++){\n, "){\n]; classes {'punctuation': 16}

Strongest intercommunity connections:

- C0 to C2: 1861 token edges; mean cosine 0.137747
- C0 to C1: 1423 token edges; mean cosine 0.130315
- C0 to C4: 1163 token edges; mean cosine 0.125944
- C1 to C2: 1039 token edges; mean cosine 0.136271
- C4 to C5: 831 token edges; mean cosine 0.132651
- C2 to C4: 761 token edges; mean cosine 0.127022
- C1 to C4: 663 token edges; mean cosine 0.121210
- C1 to C5: 590 token edges; mean cosine 0.137082
- C2 to C5: 530 token edges; mean cosine 0.136509
- C1 to C6: 487 token edges; mean cosine 0.133701
- C0 to C5: 424 token edges; mean cosine 0.132300
- C4 to C6: 263 token edges; mean cosine 0.120107
- C0 to C6: 163 token edges; mean cosine 0.119525
- C3 to C4: 160 token edges; mean cosine 0.121801
- C3 to C6: 139 token edges; mean cosine 0.151964

#### negative_tail

- Nodes: 5595
- Directed 10-NN edges: 55950
- Undirected edges: 40092
- Communities: 10
- Modularity: 0.485660

All communities:

- C0 (n=1068): representatives [\tdes, _done, _Settings, (template, (run, (ed, ␠sessions, _beh, -field, ␠TEMP]; target-extreme [rapid, _af, /div, .div, .asset, ␠alf]; classes {'alphabetic': 318, 'mixed': 750}
- C1 (n=950): representatives [␠işle, ᶅ, 🏦, ᶫ, ✽, ﯭ, /ayushman, 뺍, ἃ, 🉑]; target-extreme [łoż, 建军, �, 䢼, ｩ, Ἄ]; classes {'alphabetic': 685, 'mixed': 18, 'punctuation': 246, 'whitespace': 1}
- C2 (n=898): representatives [俄乌, 母校, からの, 自然而, 诠释, 最常见的, ␠بلا, ␠преж, 额外, 放学]; target-extreme [就能够, הצלחת, 场馆, 天府, 过度, 财税]; classes {'alphabetic': 891, 'mixed': 6, 'punctuation': 1}
- C3 (n=869): representatives [␠profes, ␠получа, ␠liber, Hugh, ␠RECE, ␠AHL, ␠sécur, ␠univers, ␠preached, ␠Ult]; target-extreme [␠ciné, ␠פר, ␠объ, ␠veter, ␠حر, acyj]; classes {'alphabetic': 849, 'mixed': 20}
- C4 (n=575): representatives [␠AssemblyFileVersion, GeneratedValue, .destroyAllWindows, .setBackgroundResource, .CompareTag, ␠OnCollision, ␠WPARAM, CloseOperation, addPreferredGap, ␠GUIStyle]; target-extreme [_ESCAPE, Jvm, ,www, _stdio, /renderer, /banner]; classes {'alphabetic': 306, 'mixed': 260, 'punctuation': 9}
- C5 (n=447): representatives [์, а, ing, ␠cré, 𝑎, �, ␠of, ﾞ, �, ь]; target-extreme [␠of, ␠with, _of, �, ␠OF, ␠for]; classes {'alphabetic': 365, 'mixed': 16, 'punctuation': 66}
- C6 (n=328): representatives [هة, ␠Après, area, Pago, ␠ולאחר, ␠Copa, zano, ␠המשפחה, ␠dopo, ␠após]; target-extreme [iveau, ␠Método, ␠após, attro, conexao, ␠cursos]; classes {'alphabetic': 318, 'mixed': 9, 'punctuation': 1}
- C7 (n=197): representatives [␠החל, ジャン, ␠ס, תח, ␠الق, ␠bł, ␠الط, ␠בעל, ␠الاحت, ␠اللا]; target-extreme [␠الاخ, ␠נת, いう, ␠بن, ␠הג, ␠היש]; classes {'alphabetic': 197}
- C8 (n=155): representatives [␠{{$, =<?=$, ␠//$, ＊, ="<?=$, ␠@}, 〜, ␠*@, #{@, >{{$]; target-extreme [import, ～, #ifndef, ％, ＿, ;}]; classes {'alphabetic': 17, 'mixed': 7, 'punctuation': 130, 'whitespace': 1}
- C9 (n=108): representatives [␠retrieve, building, Fetching, ␠Adds, ␠Skipping, Gets, ␠fetching, ␠Loads, (fetch, Adds]; target-extreme [Fetching, Introduced, ␠Naming, ␠récup, Detach, ␠Creating]; classes {'alphabetic': 96, 'mixed': 12}

Strongest intercommunity connections:

- C0 to C3: 1456 token edges; mean cosine 0.129531
- C2 to C3: 1129 token edges; mean cosine 0.130382
- C0 to C4: 1109 token edges; mean cosine 0.122677
- C1 to C4: 1089 token edges; mean cosine 0.136191
- C1 to C2: 996 token edges; mean cosine 0.129268
- C1 to C3: 742 token edges; mean cosine 0.130447
- C0 to C2: 617 token edges; mean cosine 0.125769
- C1 to C5: 555 token edges; mean cosine 0.137251
- C3 to C6: 533 token edges; mean cosine 0.127410
- C2 to C6: 500 token edges; mean cosine 0.133805
- C3 to C4: 493 token edges; mean cosine 0.125864
- C2 to C4: 459 token edges; mean cosine 0.126962
- C3 to C5: 425 token edges; mean cosine 0.129649
- C0 to C6: 363 token edges; mean cosine 0.126395
- C2 to C5: 357 token edges; mean cosine 0.129198

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5842
- Directed 10-NN edges: 58420
- Undirected edges: 41841
- Communities: 10
- Modularity: 0.572277

All communities:

- C0 (n=1167): representatives [␠contractors, ␠transformations, ␠difference, ␠electrodes, ␠contractor, ␠discrepancy, ␠holes, ␠laser, ␠tomatoes, ␠constituency]; target-extreme [␠intervention, ␠Spare, ␠instruct, ␠staircase, ␠Contractor, ␠holes]; classes {'alphabetic': 1122, 'mixed': 44, 'punctuation': 1}
- C1 (n=1058): representatives [ik, ities, ap, ley, ol, ak, ark, ine, ok, et]; target-extreme [иков, ight, ики, inki, lap, orted]; classes {'alphabetic': 1037, 'mixed': 18, 'punctuation': 3}
- C2 (n=938): representatives [")\r\n, ");\r\n, )))\r\n, ).\n\n\n\n, .", "))\r\n, ));\r\n, ');\r\n\r\n, ))\r\n, .\n\n]; target-extreme [., ],\n, ）\r\n, ␠')\n, .\n, '),\r\n]; classes {'alphabetic': 11, 'mixed': 8, 'numeric': 4, 'punctuation': 870, 'whitespace': 45}
- C3 (n=833): representatives [نطق, ␠şikay, 痦, 턔, 嵝, ␠fontSize, ␠нагрузк, ␠flashlight, .DropDownStyle, ␠оборудования]; target-extreme [␠abc, ␠изделия, скоп, ␠GetString, ␠loadData, _barang]; classes {'alphabetic': 717, 'mixed': 111, 'punctuation': 5}
- C4 (n=747): representatives [␠cut, ␠think, ␠signal, ␠stripped, ␠drop, ␠product, ␠sit, ␠strapped, ␠strike, ␠pushed]; target-extreme [␠standby, plaint, 戳, overwrite, ␠knocking, ␠cry]; classes {'alphabetic': 732, 'mixed': 15}
- C5 (n=521): representatives [だと思います, ようになりました, ␠الجميع, ␠그것을, ませんでした, それでも, ありがとうございます, になりました, になると, していました]; target-extreme [ались, 不會, ので, несен, 变为, מסוגל]; classes {'alphabetic': 504, 'mixed': 9, 'punctuation': 8}
- C6 (n=222): representatives [␠�, DM, ,k, ␠�, ␠不, ␠�, [k, ␠�, }s, ␠�]; target-extreme [xF, ,state, >n, /T, >y, \tap]; classes {'alphabetic': 115, 'mixed': 78, 'punctuation': 29}
- C7 (n=220): representatives [ประเทศไทย, ␠Malaysia, ington, ␠Liverpool, ␠Montgomery, ␠Japan, ␠Scotland, ␠Richardson, ␠cupboard, ␠Boston]; target-extreme [Scotland, ␠Powell, ␠sterling, ␠Malaysia, 쟙, ␠Montgomery]; classes {'alphabetic': 217, 'mixed': 2, 'punctuation': 1}
- C8 (n=80): representatives [␠control, \tsignal, ␠height, \theight, \tcontrol, \tboard, \tMatrix, \tcolor, \twidth, left]; target-extreme [\twidth, \tcontroller, ␠foto, \tsignal, .control, ␠Right]; classes {'alphabetic': 69, 'mixed': 11}
- C9 (n=56): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠\t\t\t, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 2, 'punctuation': 3, 'whitespace': 51}

Strongest intercommunity connections:

- C0 to C4: 1753 token edges; mean cosine 0.136204
- C0 to C1: 1237 token edges; mean cosine 0.129961
- C0 to C3: 1219 token edges; mean cosine 0.125564
- C1 to C4: 785 token edges; mean cosine 0.136941
- C3 to C5: 733 token edges; mean cosine 0.130728
- C1 to C3: 663 token edges; mean cosine 0.121147
- C3 to C4: 603 token edges; mean cosine 0.124340
- C1 to C5: 533 token edges; mean cosine 0.137956
- C4 to C5: 481 token edges; mean cosine 0.138108
- C0 to C7: 412 token edges; mean cosine 0.127303
- C0 to C5: 406 token edges; mean cosine 0.129749
- C1 to C6: 359 token edges; mean cosine 0.137658
- C1 to C7: 305 token edges; mean cosine 0.132645
- C3 to C7: 249 token edges; mean cosine 0.125277
- C3 to C6: 164 token edges; mean cosine 0.124585

#### negative_tail

- Nodes: 5716
- Directed 10-NN edges: 57160
- Undirected edges: 40966
- Communities: 10
- Modularity: 0.479204

All communities:

- C0 (n=1234): representatives [_done, _Settings, ␠AHL, (template, (run, area, ␠RECE, (ed, -field, _beh]; target-extreme [_af, /div, .asset, .div, ␠alf, /renderer]; classes {'alphabetic': 457, 'mixed': 777}
- C1 (n=908): representatives [母校, هة, からの, 诠释, ␠بلا, 最常见的, ␠Après, ␠преж, ␠ולאחר, 额外]; target-extreme [就能够, 场馆, 天府, 过度, 抵挡, 敏捷]; classes {'alphabetic': 894, 'mixed': 12, 'punctuation': 1, 'whitespace': 1}
- C2 (n=862): representatives [␠AssemblyFileVersion, GeneratedValue, .destroyAllWindows, .setBackgroundResource, 俄乌, .CompareTag, ␠OnCollision, ␠işle, ᶅ, ␠получа]; target-extreme [_ESCAPE, הצלחת, Jvm, 建军, ,www, _stdio]; classes {'alphabetic': 619, 'mixed': 220, 'punctuation': 23}
- C3 (n=754): representatives [␠profes, Hugh, ␠liber, ␠univers, ␠cleans, ␠Ult, ␠unint, ␠triumph, ␠tavern, ␠Ski]; target-extreme [␠פר, ␠объ, ␠veter, ␠Giul, ␠arriv, ␠пар]; classes {'alphabetic': 741, 'mixed': 12, 'punctuation': 1}
- C4 (n=692): representatives [🏦, ✽, 뺍, ᶫ, ﯭ, 🉑, 💨, мещ, 밈, ₶]; target-extreme [łoż, �, 䢼, ｩ, Ἄ, �]; classes {'alphabetic': 443, 'mixed': 13, 'punctuation': 236}
- C5 (n=416): representatives [а, ์, ing, ␠cré, ﾞ, �, ␠of, 𝑎, ␠ciné, �]; target-extreme [␠of, ␠with, _of, �, ␠OF, ␠for]; classes {'alphabetic': 331, 'mixed': 18, 'punctuation': 67}
- C6 (n=357): representatives [␠retrieve, ␠unpredictable, ␠preached, ␠vibrant, ␠vaguely, ␠disparate, building, ␠promising, ␠cohesive, ␠contentious]; target-extreme [Fetching, Introduced, rapid, ␠Naming, 财税, 重心]; classes {'alphabetic': 341, 'mixed': 16}
- C7 (n=225): representatives [ジャン, תח, ␠החל, ␠الط, ␠حر, ␠ס, ␠bł, ␠اللا, ␠הח, ␠граф]; target-extreme [␠حر, ␠الاخ, ␠נת, ␠بن, ␠היש, ␠הג]; classes {'alphabetic': 225}
- C8 (n=187): representatives [$get, ␠{{$, =<?=$, ＊, ␠//$, $time, 〜, ="<?=$, ␠*@, ■]; target-extreme [import, #ifndef, ％, ～, ;}, ＿]; classes {'alphabetic': 13, 'mixed': 39, 'punctuation': 134, 'whitespace': 1}
- C9 (n=81): representatives [Pago, anco, Tabla, usuario, Nama, grupo, ␠gestión, קטגוריה, Grupo, ARIO]; target-extreme [iveau, ␠Método, conexao, ␠cursos, ␠семь, itled]; classes {'alphabetic': 78, 'mixed': 3}

Strongest intercommunity connections:

- C2 to C4: 1328 token edges; mean cosine 0.136287
- C0 to C3: 1325 token edges; mean cosine 0.128738
- C0 to C2: 1208 token edges; mean cosine 0.123401
- C1 to C2: 961 token edges; mean cosine 0.130690
- C1 to C3: 788 token edges; mean cosine 0.128397
- C0 to C6: 736 token edges; mean cosine 0.128663
- C1 to C6: 686 token edges; mean cosine 0.130954
- C0 to C1: 667 token edges; mean cosine 0.125609
- C1 to C4: 609 token edges; mean cosine 0.127840
- C2 to C3: 605 token edges; mean cosine 0.129547
- C3 to C6: 537 token edges; mean cosine 0.130532
- C1 to C5: 458 token edges; mean cosine 0.132345
- C4 to C5: 426 token edges; mean cosine 0.137618
- C3 to C4: 401 token edges; mean cosine 0.130794
- C2 to C6: 395 token edges; mean cosine 0.127898

## State 03 — block_2_output

Paired positive_head: membership Jaccard 0.933832; edge Jaccard 0.841235; shared tokens 5363.
Paired negative_tail: membership Jaccard 0.914455; edge Jaccard 0.794480; shared tokens 4928.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5474
- Directed 10-NN edges: 54740
- Undirected edges: 39066
- Communities: 10
- Modularity: 0.568440

All communities:

- C0 (n=1011): representatives [␠cut, ␠kitchen, ␠government, ␠product, ␠control, ␠holes, ␠cooker, ␠difference, ␠vinegar, ␠transform]; target-extreme [␠standby, ␠variance, ␠Spare, ␠choke, ainting, ␠valve]; classes {'alphabetic': 991, 'mixed': 20}
- C1 (n=1008): representatives [ik, ick, ap, ain, ak, et, ol, ark, ities, ine]; target-extreme [иков, inki, orted, ight, \tap, ücken]; classes {'alphabetic': 998, 'mixed': 8, 'punctuation': 2}
- C2 (n=862): representatives [␠şikay, 痦, 턔, 业内人士, ␠fontSize, 嵝, ␠нагрузк, ␠openFileDialog, มากม, ␠spriteBatch]; target-extreme [_vote, .Txt, скоп, 眼科, ␠underline, ␠abc]; classes {'alphabetic': 722, 'mixed': 115, 'punctuation': 25}
- C3 (n=812): representatives [␠contractors, ␠contractor, ␠transformations, ␠оборудования, ␠photographers, 加盟商, ␠director, ␠officer, ␠employees, ology]; target-extreme [␠intervention, plaint, ␠Contractor, istribution, 运营商, ␠instruct]; classes {'alphabetic': 788, 'mixed': 23, 'punctuation': 1}
- C4 (n=738): representatives [');\r\n\r\n, ");\r\n, "))\r\n, .", ")\r\n, ));\r\n, ))\r\n, ])\r\n, ");\r\n\r\n, "));\n]; target-extreme [., ␠');\n, ],\n, >"\r\n, )';\n, '),\r\n]; classes {'alphabetic': 32, 'mixed': 16, 'punctuation': 668, 'whitespace': 22}
- C5 (n=435): representatives [になると, ␠think, だったので, ようになりました, それでも, になりました, ␠الجميع, ␠사람들이, ␠לגמרי, ますが]; target-extreme [ので, 不會, ␠please, ğini, くなった, ماذا]; classes {'alphabetic': 427, 'mixed': 6, 'punctuation': 2}
- C6 (n=305): representatives [yk, rk, \tcontrol, ,k, \tboard, \twrite, \theight, DM, \twidth, ␠Data]; target-extreme [overwrite, \twidth, rk, nx, \tdf, xF]; classes {'alphabetic': 229, 'mixed': 73, 'punctuation': 3}
- C7 (n=198): representatives [osterone, ington, stein, ประเทศไทย, utherland, ␠Malaysia, ␠Wellington, ␠Hawaii, ␠Richardson, ␠George]; target-extreme [Scotland, _barang, uffman, ␠Powell, ␠North, orth]; classes {'alphabetic': 195, 'mixed': 3}
- C8 (n=83): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, تركيب, ␠␠␠␠␠␠␠␠, \t\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t\t\t, تصوير]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 11, 'mixed': 1, 'numeric': 5, 'punctuation': 4, 'whitespace': 62}
- C9 (n=22): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠不, ␠�, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠�, ␠不, ␠�, ␠对]; classes {'alphabetic': 6, 'punctuation': 16}

Strongest intercommunity connections:

- C0 to C3: 1830 token edges; mean cosine 0.132848
- C0 to C1: 1126 token edges; mean cosine 0.135271
- C2 to C3: 861 token edges; mean cosine 0.125045
- C0 to C2: 850 token edges; mean cosine 0.124338
- C1 to C3: 739 token edges; mean cosine 0.126560
- C1 to C2: 665 token edges; mean cosine 0.120337
- C2 to C5: 546 token edges; mean cosine 0.129019
- C1 to C6: 494 token edges; mean cosine 0.135599
- C3 to C5: 487 token edges; mean cosine 0.134445
- C1 to C5: 461 token edges; mean cosine 0.135722
- C0 to C5: 342 token edges; mean cosine 0.130269
- C1 to C7: 323 token edges; mean cosine 0.131233
- C2 to C6: 323 token edges; mean cosine 0.121769
- C0 to C6: 252 token edges; mean cosine 0.138424
- C0 to C7: 241 token edges; mean cosine 0.125879

#### negative_tail

- Nodes: 5347
- Directed 10-NN edges: 53470
- Undirected edges: 38167
- Communities: 10
- Modularity: 0.481384

All communities:

- C0 (n=1265): representatives [\tdes, _done, _ISS, _Settings, ␠AHL, ␠promising, ␠cleans, (ed, _through, ␠retrieve]; target-extreme [rapid, _CUR, _af, /div, .div, ␠Naming]; classes {'alphabetic': 502, 'mixed': 763}
- C1 (n=858): representatives [.destroyAllWindows, ✽, .CompareTag, .setBackgroundResource, ␠OnCollision, ␠WPARAM, ᶅ, SectionsIn, 🏦, 🉑]; target-extreme [쐬, הצלחת, Jvm, établ, 🤬, \brief]; classes {'alphabetic': 514, 'mixed': 201, 'punctuation': 143}
- C2 (n=840): representatives [俄乌, 母校, 诠释, 最常见的, からの, 旸, ジャン, ␠acidic, ␠trụ, مناسبة]; target-extreme [天府, 血腥, 建军, 过度, 创始, 解释]; classes {'alphabetic': 826, 'mixed': 13, 'punctuation': 1}
- C3 (n=587): representatives [삻, ␠işle, ␠profes, ␠получа, ␠liber, ␠thỏa, ␠sécur, économ, тверж, ␠RECE]; target-extreme [␠affili, ␠объ, עני, ␠ciné, ␠compreh, ␠Phys]; classes {'alphabetic': 568, 'mixed': 17, 'punctuation': 2}
- C4 (n=506): representatives [␠بلا, 𝑖, ␠وإ, ␠без, É, ␠ס, ␠החל, è, ␠Sé, ␠הא]; target-extreme [␠פר, ␠È, łoż, ␠пар, 𝒸, Е]; classes {'alphabetic': 491, 'mixed': 14, 'punctuation': 1}
- C5 (n=432): representatives [Hugh, ␠Carrie, ␠volcano, area, ␠Mari, ␠Copa, ␠FIFA, ␠Crawford, ␠Ski, zano]; target-extreme [␠alf, ␠Elder, ␠Giul, MSC, cherche, ␠بن]; classes {'alphabetic': 417, 'mixed': 15}
- C6 (n=323): representatives [هة, Pago, 就能够, 都是非常, grupo, ␠במהלך, ␠były, usuario, ␠før, ␠ולאחר]; target-extreme [就能够, iveau, acyj, ␠Método, ␠após, ␠семь]; classes {'alphabetic': 318, 'mixed': 5}
- C7 (n=232): representatives [а, ␠of, ์, ing, �, �, es, ِ, �, �]; target-extreme [␠of, _of, ␠with, ␠for, ␠OF, import]; classes {'alphabetic': 156, 'mixed': 19, 'punctuation': 55, 'whitespace': 2}
- C8 (n=209): representatives [=<?=$, ␠{{$, ␠@$, #{@, ´, ␠​, ="<?=$, ␠*&, ＊, ␠@{$]; target-extreme [,www, ％, ～, ␠{{{, ª, ＿]; classes {'alphabetic': 10, 'mixed': 22, 'punctuation': 177}
- C9 (n=95): representatives [�, �, �, �, �, �, �, �, �, 荼]; target-extreme [�, 笫, 荼, �, �, �]; classes {'alphabetic': 21, 'mixed': 1, 'punctuation': 73}

Strongest intercommunity connections:

- C0 to C3: 1211 token edges; mean cosine 0.132352
- C0 to C1: 1050 token edges; mean cosine 0.122868
- C0 to C2: 999 token edges; mean cosine 0.125227
- C1 to C2: 849 token edges; mean cosine 0.128704
- C2 to C3: 839 token edges; mean cosine 0.130770
- C0 to C5: 720 token edges; mean cosine 0.128232
- C3 to C5: 604 token edges; mean cosine 0.131013
- C1 to C3: 588 token edges; mean cosine 0.132043
- C1 to C4: 556 token edges; mean cosine 0.131826
- C3 to C4: 539 token edges; mean cosine 0.137404
- C2 to C6: 467 token edges; mean cosine 0.132017
- C2 to C4: 415 token edges; mean cosine 0.128173
- C2 to C5: 410 token edges; mean cosine 0.128520
- C4 to C5: 371 token edges; mean cosine 0.131805
- C0 to C6: 358 token edges; mean cosine 0.128565

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5632
- Directed 10-NN edges: 56320
- Undirected edges: 40201
- Communities: 10
- Modularity: 0.572464

All communities:

- C0 (n=1421): representatives [␠contractors, ␠kitchen, ailer, ␠government, 加盟商, ␠photographers, ␠product, ␠director, ␠officer, ␠contractor]; target-extreme [␠intervention, ␠standby, ␠variance, overwrite, ␠choke, ␠Spare]; classes {'alphabetic': 1364, 'mixed': 56, 'punctuation': 1}
- C1 (n=1049): representatives [ik, ick, ap, ain, et, ol, ak, ot, ine, ley]; target-extreme [иков, inki, orted, \tap, ight, ücken]; classes {'alphabetic': 1031, 'mixed': 18}
- C2 (n=804): representatives [␠şikay, 痦, 읩, 嵝, ␠fontSize, .getOrElse, 턔, ␠openFileDialog, ␠нагрузк, ␠spriteBatch]; target-extreme [.Txt, 眼科, ␠drawback, скоп, ␠outFile, ␠newIndex]; classes {'alphabetic': 684, 'mixed': 93, 'punctuation': 27}
- C3 (n=715): representatives [');\r\n\r\n, ");\r\n, "))\r\n, .", ));\r\n, ")\r\n, ");\r\n\r\n, ))\r\n, ])\r\n, "));\n]; target-extreme [., ␠');\n, ],\n, >"\r\n, )';\n, '),\r\n]; classes {'alphabetic': 26, 'mixed': 15, 'punctuation': 666, 'whitespace': 8}
- C4 (n=698): representatives [だと思います, になると, ␠think, 业内人士, だったので, ようになりました, ␠unfortunately, になりました, それでも, していました]; target-extreme [ので, ␠услуги, ␠изделия, 不會, _barang, ␠please]; classes {'alphabetic': 683, 'mixed': 13, 'punctuation': 2}
- C5 (n=388): representatives [␠cut, ␠stripped, ␠report, ␠complaints, 建議, ␠placed, ␠worried, ␠recommendations, ␠vaccinated, ␠warned]; target-extreme [plaint, ␠frightened, ␠instruct, ␠advise, ␠knocking, 信]; classes {'alphabetic': 383, 'mixed': 5}
- C6 (n=236): representatives [osterone, ington, ␠Malaysia, ประเทศไทย, ␠Wellington, ␠Liverpool, ␠Hawaii, utherland, ␠Montgomery, ␠Richardson]; target-extreme [Scotland, uffman, ␠Powell, ␠Newsletter, ␠North, airobi]; classes {'alphabetic': 232, 'mixed': 3, 'punctuation': 1}
- C7 (n=198): representatives [␠control, \tcontrol, ,k, data, \tsignal, \tboard, \twidth, \theight, ␠Data, \tdata]; target-extreme [\twidth, \tdf, \tsignal, \tMatrix, >y, ␠Right]; classes {'alphabetic': 114, 'mixed': 81, 'punctuation': 3}
- C8 (n=97): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t\t\t, \t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 8, 'mixed': 1, 'numeric': 5, 'punctuation': 5, 'whitespace': 78}
- C9 (n=26): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠不, ␠�, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠�, ␠不, ␠�, ␠对]; classes {'alphabetic': 6, 'punctuation': 20}

Strongest intercommunity connections:

- C0 to C1: 1423 token edges; mean cosine 0.130668
- C0 to C5: 1116 token edges; mean cosine 0.137177
- C0 to C2: 1079 token edges; mean cosine 0.123665
- C0 to C4: 888 token edges; mean cosine 0.131340
- C2 to C4: 799 token edges; mean cosine 0.127351
- C1 to C4: 654 token edges; mean cosine 0.133860
- C1 to C2: 586 token edges; mean cosine 0.119643
- C0 to C6: 516 token edges; mean cosine 0.127911
- C4 to C5: 410 token edges; mean cosine 0.135311
- C1 to C5: 370 token edges; mean cosine 0.134210
- C1 to C6: 338 token edges; mean cosine 0.131789
- C1 to C7: 337 token edges; mean cosine 0.134912
- C2 to C5: 265 token edges; mean cosine 0.123844
- C2 to C7: 252 token edges; mean cosine 0.125959
- C0 to C7: 244 token edges; mean cosine 0.135415

#### negative_tail

- Nodes: 4970
- Directed 10-NN edges: 49700
- Undirected edges: 35439
- Communities: 11
- Modularity: 0.473612

All communities:

- C0 (n=992): representatives [\tdes, _done, _ISS, _Settings, ␠AHL, _through, ␠NUM, (ed, _have, (template]; target-extreme [_CUR, _af, /div, ␠Naming, .div, .Success]; classes {'alphabetic': 278, 'mixed': 714}
- C1 (n=982): representatives [삻, .destroyAllWindows, ␠işle, 俄乌, ␠WPARAM, .CompareTag, ␠OnCollision, .setBackgroundResource, ✽, ᶅ]; target-extreme [łoż, 쐬, 血腥, 建军, 𝒸, הצלחת]; classes {'alphabetic': 674, 'mixed': 156, 'punctuation': 152}
- C2 (n=858): representatives [␠profes, ␠получа, ␠liber, ␠RECE, тверж, ␠univers, ␠promising, ␠sécur, ␠преж, ␠ciné]; target-extreme [rapid, ␠объ, ␠affili, ␠ciné, ␠Elder, ␠compreh]; classes {'alphabetic': 829, 'mixed': 28, 'punctuation': 1}
- C3 (n=383): representatives [诠释, 金陵, 深入推进, 艰辛, ␠embraces, 探讨, -free, 澄清, 变身, 财税]; target-extreme [天府, 过度, 解释, 创始, 无私, 构筑]; classes {'alphabetic': 373, 'mixed': 10}
- C4 (n=381): representatives [هة, ジャン, ␠of, а, ␠ס, ์, ing, ␠המשפחה, 𝑖, es]; target-extreme [␠of, _of, ␠with, ␠for, ␠OF, ␠פר]; classes {'alphabetic': 305, 'mixed': 21, 'punctuation': 54, 'whitespace': 1}
- C5 (n=360): representatives [Hugh, area, Pago, péri, ␠clases, grupo, zano, 領域, ␠Rivera, ışı]; target-extreme [iveau, 视野, ␠Método, ␠Giul, 절차, cherche]; classes {'alphabetic': 350, 'mixed': 10}
- C6 (n=277): representatives [␠بلا, からの, 最常见的, ␠без, 就能够, 都是非常, 十几个, مناسبة, 第一家, ␠były]; target-extreme [就能够, いう, ␠após, 年之, 无缘, 第七届]; classes {'alphabetic': 273, 'mixed': 3, 'punctuation': 1}
- C7 (n=227): representatives [É, ␠Sé, ␠Э, è, ␠før, ␠É, ␠øns, CU, ␠rés, Ç]; target-extreme [␠È, ␠alf, Е, acyj, ␠Сан, ␠mê]; classes {'alphabetic': 221, 'mixed': 6}
- C8 (n=209): representatives [=<?=$, ␠{{$, ="<?=$, ＊, ´, ␠@$, ␠<?=$, ␠*&, ␠@{$, #{@]; target-extreme [,www, ％, ～, ᵘ, ª, @Api]; classes {'alphabetic': 22, 'mixed': 19, 'punctuation': 167, 'whitespace': 1}
- C9 (n=195): representatives [␠החל, ␠وإ, ␠הא, ␠התק, �, �, �, ␠הח, ␠اللا, �]; target-extreme [�, 笫, ␠الاخ, �, เผยแ, תח]; classes {'alphabetic': 138, 'mixed': 2, 'punctuation': 55}
- C10 (n=106): representatives [␠retrieve, Writes, ␠Tells, Fetching, ␠Returning, ␠данный, generate, ␠Adds, Returned, ␠Skipping]; target-extreme [Introduced, leting, Fetching, Displayed, ␠Creating, ␠Fetch]; classes {'alphabetic': 97, 'mixed': 9}

Strongest intercommunity connections:

- C0 to C2: 1443 token edges; mean cosine 0.129543
- C1 to C2: 971 token edges; mean cosine 0.130349
- C0 to C1: 942 token edges; mean cosine 0.122336
- C2 to C5: 657 token edges; mean cosine 0.130258
- C2 to C3: 646 token edges; mean cosine 0.125741
- C1 to C3: 499 token edges; mean cosine 0.125863
- C2 to C7: 390 token edges; mean cosine 0.135018
- C1 to C9: 384 token edges; mean cosine 0.134090
- C0 to C5: 384 token edges; mean cosine 0.126052
- C1 to C5: 349 token edges; mean cosine 0.128528
- C1 to C8: 346 token edges; mean cosine 0.134089
- C2 to C6: 342 token edges; mean cosine 0.131580
- C1 to C4: 330 token edges; mean cosine 0.134725
- C1 to C6: 321 token edges; mean cosine 0.130277
- C2 to C4: 321 token edges; mean cosine 0.126917

## State 04 — block_3_output

Paired positive_head: membership Jaccard 0.914447; edge Jaccard 0.800733; shared tokens 5665.
Paired negative_tail: membership Jaccard 0.927893; edge Jaccard 0.831358; shared tokens 5765.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5742
- Directed 10-NN edges: 57420
- Undirected edges: 40936
- Communities: 11
- Modularity: 0.569445

All communities:

- C0 (n=1136): representatives [ak, ol, ain, ick, ap, ik, ants, ok, ines, ot]; target-extreme [иков, oints, ight, ountain, inki, oves]; classes {'alphabetic': 1118, 'mixed': 16, 'punctuation': 2}
- C1 (n=911): representatives [␠contractors, ␠photographer, ␠microphone, ␠government, ␠material, ␠goalkeeper, ␠participants, ␠photographers, ␠prices, ␠distributor]; target-extreme [␠valve, ␠Spare, ␠Contractor, ␠Decorating, ␠vaccine, ␠wastewater]; classes {'alphabetic': 859, 'mixed': 52}
- C2 (n=798): representatives [");\r\n, ")\r\n, "))\r\n, "));\n, )))\r\n, ');\r\n\r\n, ')\r\n\r\n, ])\r\n, ))\n, ));\r\n]; target-extreme [␠');\n, ],\n, )';\n, "],\n, ）\r\n, '),\r\n]; classes {'alphabetic': 20, 'mixed': 6, 'punctuation': 749, 'whitespace': 23}
- C3 (n=787): representatives [␠difference, ␠information, ␠misinformation, ␠report, 建議, ␠sampling, ␠transform, ␠symptoms, ␠negotiations, ␠transformations]; target-extreme [␠intervention, ␠variance, plaint, ��态, ␠instruct, ␠imbalance]; classes {'alphabetic': 757, 'mixed': 29, 'punctuation': 1}
- C4 (n=743): representatives [痦, 嵝, 턔, ␠fontSize, 铏, ␠spriteBatch, ␠нагрузк, strncmp, ␠pinMode, ␠kutje]; target-extreme [xDA, скоп, 眼科, ␠outFile, ␠underline, strncmp]; classes {'alphabetic': 641, 'mixed': 83, 'punctuation': 19}
- C5 (n=556): representatives [だと思います, ␠think, ないので, ようになりました, それでも, 드립니다, ␠المواطنين, になると, だったので, ␠оборудования]; target-extreme [ますが, _barang, 不會, ␠изделия, ので, ␠Конечно]; classes {'alphabetic': 522, 'mixed': 28, 'punctuation': 6}
- C6 (n=381): representatives [␠cut, ␠stripped, ␠painting, ␠pouring, ␠painted, ␠paint, ␠scratched, ␠pushed, ␠drop, ␠sitting]; target-extreme [␠standby, ainting, ␠choke, Speaking, ␠leaned, ␠scratched]; classes {'alphabetic': 374, 'mixed': 7}
- C7 (n=259): representatives [␠line, ␠written, \tsignal, \twrite, ␠height, ␠wrote, ␠lines, \timage, )r, ␠writes]; target-extreme [overwrite, 0, \tap, \twidth, \tMatrix, \tdf]; classes {'alphabetic': 167, 'mixed': 78, 'numeric': 8, 'punctuation': 6}
- C8 (n=74): representatives [␠Malaysia, ␠Palestinians, ␠Rohingya, ␠Monsanto, ␠Pakistan, ␠Taliban, ␠Montgomery, ␠Yellowstone, ␠North, ␠Turkey]; target-extreme [Scotland, ␠PayPal, North, Trump, ␠Eastern, ␠Malaysia]; classes {'alphabetic': 73, 'mixed': 1}
- C9 (n=68): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 4, 'punctuation': 2, 'whitespace': 62}
- C10 (n=29): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠生, ��, ␠对, ␠�]; classes {'alphabetic': 9, 'punctuation': 20}

Strongest intercommunity connections:

- C1 to C3: 1339 token edges; mean cosine 0.136375
- C0 to C1: 1021 token edges; mean cosine 0.130589
- C1 to C4: 800 token edges; mean cosine 0.122330
- C4 to C5: 713 token edges; mean cosine 0.127782
- C0 to C3: 690 token edges; mean cosine 0.129578
- C3 to C6: 639 token edges; mean cosine 0.136696
- C1 to C6: 621 token edges; mean cosine 0.134421
- C0 to C4: 591 token edges; mean cosine 0.121268
- C3 to C5: 556 token edges; mean cosine 0.134046
- C3 to C4: 511 token edges; mean cosine 0.120787
- C0 to C5: 501 token edges; mean cosine 0.133334
- C1 to C5: 457 token edges; mean cosine 0.131587
- C0 to C6: 430 token edges; mean cosine 0.137394
- C0 to C7: 395 token edges; mean cosine 0.137776
- C4 to C6: 266 token edges; mean cosine 0.120315

#### negative_tail

- Nodes: 6066
- Directed 10-NN edges: 60660
- Undirected edges: 43612
- Communities: 11
- Modularity: 0.476421

All communities:

- C0 (n=1318): representatives [\tdes, גרסה, ␠profes, профессиона, ␠получа, _done, ␠plethora, _Settings, ␠RECE, ␠sécur]; target-extreme [rapid, leting, ␠assh, _gap, ␠ciné, _CUR]; classes {'alphabetic': 821, 'mixed': 497}
- C1 (n=901): representatives [しっかりと, ␠işle, 诠释, هة, ␠일이, からの, ␠çalış, тверж, 最常见的, ␠بلا]; target-extreme [acyj, 就能够, łoż, ␠tù, 史上最, 深化]; classes {'alphabetic': 896, 'mixed': 5}
- C2 (n=877): representatives [㧬, ✽, 쨌, ᶅ, 🏦, /ayushman, CloseOperation, 뗄, 倻, PreferredGap]; target-extreme [�, 쐬, ʝ, établ, 🤬, 䢼]; classes {'alphabetic': 644, 'mixed': 23, 'punctuation': 210}
- C3 (n=756): representatives [삻, Hugh, ␠Carrie, ␠sala, ␠Copa, ␠AHL, ␠Mari, ␠Clubs, 퓼, ␠volcano]; target-extreme [␠פר, ␠Сан, ␠alf, _af, 天府, .nom]; classes {'alphabetic': 726, 'mixed': 29, 'punctuation': 1}
- C4 (n=701): representatives [GeneratedValue, BootApplication, .destroyAllWindows, @NgModule, .UseVisualStyleBackColor, ␠OnCollision, ␠WPARAM, .setBackgroundResource, .CompareTag, .menuStrip]; target-extreme [\brief, .asset, /renderer, ,www, /banner, _ESCAPE]; classes {'alphabetic': 324, 'mixed': 367, 'punctuation': 10}
- C5 (n=471): representatives [␠É, É, ␠والأ, ␠والإ, �, ␠�, 𝑖, è, ␠وإ, ␠Sé]; target-extreme [␠È, È, 𝒸, ː, ␠mê, เผยแ]; classes {'alphabetic': 385, 'mixed': 23, 'punctuation': 62, 'whitespace': 1}
- C6 (n=253): representatives [а, ␠of, ์, ing, s, �, ed, es, ся, 了]; target-extreme [␠of, _of, ␠OF, ␠with, import, ␠for]; classes {'alphabetic': 191, 'mixed': 29, 'punctuation': 32, 'whitespace': 1}
- C7 (n=238): representatives [(template, (ed, .Section, (run, (candidate, (IP, (clean, (loss, (div, ␠fetching]; target-extreme [Fetching, (pg, Ctx, (object, ␠Fetch, ␠ctx]; classes {'alphabetic': 44, 'mixed': 194}
- C8 (n=234): representatives [area, Pago, ereço, usuario, הצלחת, ␠éxito, ␠succès, ␠clases, ␠succes, ␠cosas]; target-extreme [הצלחת, .Success, ␠Método, cherche, iveau, ␠apellido]; classes {'alphabetic': 218, 'mixed': 16}
- C9 (n=163): representatives [␠[[], ␠{{$, ␠​, ␠[&, =<?=$, ＊, <?=$, ␠*&, $time, )const]; target-extreme [␠{{{, ％, ＿, ‧, }$/, ～]; classes {'alphabetic': 2, 'mixed': 13, 'punctuation': 148}
- C10 (n=154): representatives [母校, 灾区, 故乡, 樱花, ␠그리스, 湖, 上海, 脱贫攻坚, 神州, 祖国]; target-extreme [夏, 市委, 庄, 场馆, 风云, 财税]; classes {'alphabetic': 153, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C3: 1670 token edges; mean cosine 0.131899
- C0 to C1: 1202 token edges; mean cosine 0.131716
- C0 to C4: 1180 token edges; mean cosine 0.124094
- C2 to C4: 1109 token edges; mean cosine 0.138987
- C1 to C2: 1068 token edges; mean cosine 0.135024
- C1 to C3: 665 token edges; mean cosine 0.129771
- C2 to C5: 663 token edges; mean cosine 0.140619
- C0 to C2: 615 token edges; mean cosine 0.131195
- C0 to C7: 587 token edges; mean cosine 0.131940
- C1 to C5: 558 token edges; mean cosine 0.135915
- C2 to C3: 533 token edges; mean cosine 0.131919
- C3 to C4: 443 token edges; mean cosine 0.126980
- C0 to C5: 442 token edges; mean cosine 0.133762
- C1 to C8: 426 token edges; mean cosine 0.134631
- C0 to C8: 425 token edges; mean cosine 0.129955

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6118
- Directed 10-NN edges: 61180
- Undirected edges: 43585
- Communities: 10
- Modularity: 0.560197

All communities:

- C0 (n=1130): representatives [ak, ick, ants, ol, ain, ik, ot, ap, ine, ok]; target-extreme [иков, oints, ountain, ight, oves, inki]; classes {'alphabetic': 1113, 'mixed': 13, 'punctuation': 4}
- C1 (n=1007): representatives [␠cut, ␠line, ␠report, ␠information, 建議, ␠written, ␠material, ␠transform, ␠stripped, ␠holes]; target-extreme [␠standby, ␠variance, overwrite, ␠valve, ␠choke, ainting]; classes {'alphabetic': 977, 'mixed': 29, 'punctuation': 1}
- C2 (n=876): representatives [␠microphone, 嵝, 痦, 턔, ␠fontSize, 铏, strncmp, ␠spriteBatch, ␠kutje, ␠нагрузк]; target-extreme [xDA, 眼科, скоп, ␠outFile, ␠underline, _vote]; classes {'alphabetic': 747, 'mixed': 110, 'punctuation': 19}
- C3 (n=837): representatives [␠contractors, ␠photographer, ␠difference, ␠distributor, ␠cooker, ␠government, ␠contractor, ␠transformations, ␠goalkeeper, ␠photographers]; target-extreme [␠intervention, _barang, ��态, ␠Decorating, ␠Contractor, ␠imbalance]; classes {'alphabetic': 804, 'mixed': 32, 'punctuation': 1}
- C4 (n=822): representatives [");\r\n, ")\r\n, "))\r\n, "));\n, ])\r\n, ')\r\n\r\n, )))\r\n, ))\n, ));\r\n, ');\r\n\r\n]; target-extreme [␠');\n, ],\n, )';\n, ）\r\n, "],\n, '),\r\n]; classes {'alphabetic': 23, 'mixed': 15, 'punctuation': 761, 'whitespace': 23}
- C5 (n=571): representatives [だと思います, ␠think, ないので, 드립니다, それでも, だったので, になると, ようになりました, ですので, ␠unfortunately]; target-extreme [ますが, ␠Конечно, 不會, ␠congratulations, ␠intimidate, ので]; classes {'alphabetic': 560, 'mixed': 10, 'punctuation': 1}
- C6 (n=416): representatives [␠granite, ␠particles, ␠vinegar, ␠meat, ␠plant, ␠spiral, ␠tissue, ␠smartphone, ␠batteries, ␠Malaysia]; target-extreme [␠wastewater, Scotland, ␠monsters, ␠Darling, ␠mortar, ␠PayPal]; classes {'alphabetic': 406, 'mixed': 10}
- C7 (n=352): representatives [\twrite, \tsignal, \tdata, \timage, \tboard, \treset, DA, \theight, ␠T, DM]; target-extreme [\tap, \twidth, \tdf, \tMatrix, \tsignal, ␠Right]; classes {'alphabetic': 238, 'mixed': 109, 'punctuation': 5}
- C8 (n=77): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, \t\t\t\t, \t\t\t]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, 0, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠]; classes {'alphabetic': 6, 'numeric': 8, 'punctuation': 2, 'whitespace': 61}
- C9 (n=30): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不, ␠�, ␠生]; target-extreme [␠�, ␠�, ␠生, ��, ␠对, ␠�]; classes {'alphabetic': 10, 'punctuation': 20}

Strongest intercommunity connections:

- C1 to C3: 1515 token edges; mean cosine 0.140456
- C0 to C1: 1003 token edges; mean cosine 0.136645
- C2 to C3: 865 token edges; mean cosine 0.126358
- C0 to C3: 810 token edges; mean cosine 0.126676
- C1 to C2: 774 token edges; mean cosine 0.125050
- C1 to C6: 771 token edges; mean cosine 0.138096
- C2 to C5: 743 token edges; mean cosine 0.130114
- C0 to C2: 697 token edges; mean cosine 0.121757
- C1 to C5: 672 token edges; mean cosine 0.136826
- C3 to C6: 638 token edges; mean cosine 0.132668
- C3 to C5: 563 token edges; mean cosine 0.133548
- C0 to C6: 561 token edges; mean cosine 0.132393
- C0 to C7: 530 token edges; mean cosine 0.135480
- C0 to C5: 468 token edges; mean cosine 0.134776
- C2 to C6: 420 token edges; mean cosine 0.125207

#### negative_tail

- Nodes: 5912
- Directed 10-NN edges: 59120
- Undirected edges: 42612
- Communities: 9
- Modularity: 0.482467

All communities:

- C0 (n=1121): representatives [\tdes, ␠profes, ␠получа, _done, _Settings, ␠RECE, ␠Ult, _gap, ␠conna, тверж]; target-extreme [rapid, /renderer, leting, _gap, .nom, _af]; classes {'alphabetic': 560, 'mixed': 561}
- C1 (n=1061): representatives [㧬, 삻, しっかりと, גרסה, 诠释, 母校, 缜, からの, ␠일이, 最常见的]; target-extreme [就能够, 夏, ␠tù, 天府, iveau, 深化]; classes {'alphabetic': 1050, 'mixed': 9, 'punctuation': 2}
- C2 (n=856): representatives [профессиона, ␠plethora, Hugh, area, ␠sala, ␠Clubs, ␠Carrie, ␠Mari, ␠liber, ␠volcano]; target-extreme [␠Сан, ␠alf, ␠assh, ␠affili, ␠compreh, Hôtel]; classes {'alphabetic': 834, 'mixed': 22}
- C3 (n=784): representatives [GeneratedValue, BootApplication, .destroyAllWindows, @NgModule, .UseVisualStyleBackColor, ␠OnCollision, 쨌, ᶅ, ␠WPARAM, SectionsIn]; target-extreme [\brief, .asset, 쐬, ␠csvfile, 顼, 遘]; classes {'alphabetic': 454, 'mixed': 317, 'punctuation': 13}
- C4 (n=675): representatives [␠işle, 🏦, ﯭ, ␠eskorte, ἃ, 🉑, ﯦ, �, 💨, �]; target-extreme [�, 𝒸, ʝ, 🤬, เผยแ, ␠işle]; classes {'alphabetic': 424, 'mixed': 7, 'punctuation': 244}
- C5 (n=579): representatives [هة, ␠sécur, ␠ciné, é, ␠É, è, É, ␠øns, ␠clases, ␠é]; target-extreme [␠È, הצלחת, .Success, acyj, łoż, È]; classes {'alphabetic': 555, 'mixed': 22, 'punctuation': 2}
- C6 (n=395): representatives [✽, (template, ␠[[], (ed, (run, ␠*&, ␠{{$, (clean, ＊, (candidate]; target-extreme [import, class, ,www, ⊔, ␠to, (pg]; classes {'alphabetic': 46, 'mixed': 184, 'punctuation': 164, 'whitespace': 1}
- C7 (n=264): representatives [а, ␠of, ์, ing, �, es, ed, for, s, 了]; target-extreme [␠of, _of, ␠OF, ␠with, ưa, �]; classes {'alphabetic': 211, 'mixed': 21, 'punctuation': 31, 'whitespace': 1}
- C8 (n=177): representatives [␠والإ, ␠بلا, ␠والأ, ␠وإ, ในการ, ␠המק, ␠بالإ, ␠הא, ␠ס, ␠החל]; target-extreme [␠פר, いう, ␠الاخ, תח, ␠giải, пре]; classes {'alphabetic': 175, 'mixed': 2}

Strongest intercommunity connections:

- C0 to C2: 1683 token edges; mean cosine 0.131009
- C1 to C2: 1106 token edges; mean cosine 0.133596
- C0 to C3: 1035 token edges; mean cosine 0.123690
- C3 to C4: 1025 token edges; mean cosine 0.140162
- C1 to C3: 965 token edges; mean cosine 0.133708
- C1 to C4: 880 token edges; mean cosine 0.135433
- C0 to C1: 880 token edges; mean cosine 0.129117
- C1 to C5: 841 token edges; mean cosine 0.135382
- C2 to C5: 761 token edges; mean cosine 0.135573
- C0 to C6: 589 token edges; mean cosine 0.128126
- C4 to C5: 513 token edges; mean cosine 0.140402
- C3 to C6: 509 token edges; mean cosine 0.129560
- C0 to C5: 500 token edges; mean cosine 0.128668
- C2 to C3: 484 token edges; mean cosine 0.126973
- C2 to C4: 438 token edges; mean cosine 0.133085

## State 05 — block_4_output

Paired positive_head: membership Jaccard 0.922504; edge Jaccard 0.820429; shared tokens 6440.
Paired negative_tail: membership Jaccard 0.924626; edge Jaccard 0.819162; shared tokens 5876.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6880
- Directed 10-NN edges: 68800
- Undirected edges: 48605
- Communities: 10
- Modularity: 0.571502

All communities:

- C0 (n=1578): representatives [␠contractors, ␠transformations, ␠photographers, ␠employees, ␠batteries, ␠prices, ␠concentrations, ␠participants, ␠goalkeeper, ␠Distribution]; target-extreme [␠intervention, ␠plunge, 眼科, ␠Contractor, ␠wastewater, irthday]; classes {'alphabetic': 1523, 'mixed': 55}
- C1 (n=1269): representatives [ik, ain, ified, inger, ick, ants, ap, ments, ok, ol]; target-extreme [иков, oints, perature, ��态, inki, wish]; classes {'alphabetic': 1249, 'mixed': 17, 'punctuation': 3}
- C2 (n=979): representatives [业内人士, ですね, ить, ␠المواطنين, 드립니다, になりました, していました, っています, ようになりました, ывают]; target-extreme [实在, 不會, ␠денег, ␠услуги, orgt, _barang]; classes {'alphabetic': 967, 'mixed': 12}
- C3 (n=860): representatives [뤗, 턔, 痦, ␠fontSize, ␠bgColor, 嵝, 읩, 礞, strncmp, ␠assertThat]; target-extreme [xDA, ␠outFile, скоп, 胖, ␠PayPal, -contained]; classes {'alphabetic': 719, 'mixed': 109, 'punctuation': 32}
- C4 (n=776): representatives [␠cut, ␠difference, ␠vaccinated, ␠write, ␠stripped, ␠written, ␠coated, ␠worried, ␠debating, ␠painted]; target-extreme [␠advise, overwrite, ␠disagree, ␠choke, ␠shocked, Speaking]; classes {'alphabetic': 764, 'mixed': 11, 'punctuation': 1}
- C5 (n=724): representatives [');\r\n\r\n, ");\r\n, "))\r\n, .", ))\r\n, ")\r\n, ])\r\n, ");\r\n\r\n, )))\r\n, ')\r\n\r\n]; target-extreme [␠');\n, ␠'');\n\n, ],\n, "],\n, "]}\n, ],\r\n]; classes {'alphabetic': 7, 'mixed': 23, 'punctuation': 674, 'whitespace': 20}
- C6 (n=282): representatives [␠Portsmouth, ␠Birmingham, ington, ␠millennials, ␠Palestinians, ␠brown, ␠Sacramento, ␠Pittsburgh, ␠Singapore, ␠Liverpool]; target-extreme [␠street, Scotland, dashboard, 华盛顿, ␠Cardinals, ongyang]; classes {'alphabetic': 280, 'mixed': 2}
- C7 (n=175): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ,k, =, [, ␠[, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, )r]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 35, 'mixed': 44, 'numeric': 7, 'punctuation': 9, 'whitespace': 80}
- C8 (n=173): representatives [␠image, ␠�, ␠不, ␠weight, \theight, ␠�, ␠�, \tdata, \timage, \tcontrol]; target-extreme [\tMatrix, \tsignal, ␠�, \tap, ��, \tboard]; classes {'alphabetic': 107, 'mixed': 43, 'punctuation': 23}
- C9 (n=64): representatives [␠Unfortunately, ␠probably, Despite, ␠particularly, ␠perhaps, ␠unfortunately, Nevertheless, ␠Nevertheless, ␠certainly, ␠accordingly]; target-extreme [␠although, Instead, ␠Meanwhile, Indeed, ␠probably, ␠Nonetheless]; classes {'alphabetic': 60, 'mixed': 4}

Strongest intercommunity connections:

- C0 to C1: 1652 token edges; mean cosine 0.134531
- C0 to C4: 1622 token edges; mean cosine 0.143691
- C0 to C3: 1136 token edges; mean cosine 0.126666
- C2 to C3: 997 token edges; mean cosine 0.127849
- C0 to C2: 932 token edges; mean cosine 0.133754
- C1 to C2: 847 token edges; mean cosine 0.136214
- C1 to C3: 779 token edges; mean cosine 0.122138
- C1 to C4: 714 token edges; mean cosine 0.136813
- C2 to C4: 622 token edges; mean cosine 0.138660
- C0 to C6: 539 token edges; mean cosine 0.131915
- C3 to C4: 442 token edges; mean cosine 0.125145
- C1 to C6: 393 token edges; mean cosine 0.134883
- C3 to C6: 265 token edges; mean cosine 0.126605
- C0 to C8: 257 token edges; mean cosine 0.136068
- C2 to C6: 225 token edges; mean cosine 0.128195

#### negative_tail

- Nodes: 6179
- Directed 10-NN edges: 61790
- Undirected edges: 44354
- Communities: 9
- Modularity: 0.489651

All communities:

- C0 (n=1201): representatives [␠profes, ␠получа, профессиона, Hugh, ␠Mari, ␠Carrie, ␠splendid, ␠Clubs, ␠utter, ␠univers]; target-extreme [␠alf, ␠Elder, ␠получа, ␠Сан, ␠Método, ␠Mile]; classes {'alphabetic': 1176, 'mixed': 25}
- C1 (n=1183): representatives [㧬, 삻, 🍱, ご�, ␠işle, ᶅ, /ayushman, ✽, ﭩ, 뗄]; target-extreme [쐬, 夏, 🤬, ␠még, ⓤ, 建军]; classes {'alphabetic': 921, 'mixed': 8, 'punctuation': 254}
- C2 (n=1072): representatives [␠بلا, ␠yaygın, からの, ␠일이, ␠dzięki, ␠É, ␠sécur, ␠הא, 最常见的, ␠попу]; target-extreme [␠È, 史上最, È, .Success, ␠الاخ, établ]; classes {'alphabetic': 1055, 'mixed': 16, 'punctuation': 1}
- C3 (n=1046): representatives [\tdes, _done, (template, _Settings, (run, (ed, ␠NUM, -field, -str, _fields]; target-extreme [/high, _gap, /renderer, .asset, .div, /commons]; classes {'alphabetic': 282, 'mixed': 764}
- C4 (n=829): representatives [GeneratedValue, BootApplication, .destroyAllWindows, .UseVisualStyleBackColor, ␠WPARAM, ␠RelayCommand, ␠buttonWithType, ␠StatelessWidget, .setBackgroundResource, ␠OnCollision]; target-extreme [\brief, ␠ctx, @Api, ␠Поч, ,www, .alibaba]; classes {'alphabetic': 428, 'mixed': 387, 'punctuation': 14}
- C5 (n=369): representatives [诠释, 创新, 提升, 家族, 深入推进, 邻里, イベント, نتشر, 合, 层出不穷]; target-extreme [天府, 加快, 诠释, 解释, 复习, 庄]; classes {'alphabetic': 364, 'mixed': 5}
- C6 (n=287): representatives [␠[[], 𝑎, ="<?=$, ȃ, =<?=$, 𝑨, ℎ, ␠​, ={`/, ␠*&]; target-extreme [⊔, ː, ́, ʝ, 𝑎, {']; classes {'alphabetic': 75, 'mixed': 14, 'numeric': 1, 'punctuation': 197}
- C7 (n=182): representatives [␠of, а, �, ing, es, ся, ์, ь, 了, ая]; target-extreme [␠of, _of, class, ␠with, ␠OF, ␠for]; classes {'alphabetic': 133, 'mixed': 14, 'punctuation': 34, 'whitespace': 1}
- C8 (n=10): representatives [퓼, 䓫, 젡, Cumhurba, Cumhurbaş, �, ␠오�, �, 맍, 關�]; target-extreme [Cumhurbaş, �, Cumhurba, �, 젡, 關�]; classes {'alphabetic': 6, 'mixed': 2, 'punctuation': 2}

Strongest intercommunity connections:

- C0 to C3: 1804 token edges; mean cosine 0.130479
- C0 to C2: 1603 token edges; mean cosine 0.131342
- C1 to C2: 1537 token edges; mean cosine 0.134443
- C1 to C4: 1461 token edges; mean cosine 0.136347
- C3 to C4: 1282 token edges; mean cosine 0.122855
- C0 to C1: 1066 token edges; mean cosine 0.131110
- C0 to C4: 756 token edges; mean cosine 0.127994
- C1 to C5: 639 token edges; mean cosine 0.131117
- C2 to C5: 612 token edges; mean cosine 0.130124
- C2 to C3: 609 token edges; mean cosine 0.127596
- C0 to C5: 522 token edges; mean cosine 0.129137
- C2 to C4: 520 token edges; mean cosine 0.128414
- C1 to C3: 446 token edges; mean cosine 0.125813
- C1 to C6: 419 token edges; mean cosine 0.142936
- C2 to C7: 342 token edges; mean cosine 0.136611

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6541
- Directed 10-NN edges: 65410
- Undirected edges: 46192
- Communities: 13
- Modularity: 0.569445

All communities:

- C0 (n=1512): representatives [␠contractors, ␠transformations, ␠Conservation, ␠prices, ␠granite, ␠concentrations, ␠Distribution, ␠commentary, ␠homeowner, ␠difference]; target-extreme [␠intervention, perature, ��态, ␠денег, ␠Contractor, ␠wastewater]; classes {'alphabetic': 1428, 'mixed': 83, 'punctuation': 1}
- C1 (n=994): representatives [ik, ain, ick, ified, ants, ap, inger, ok, ments, ol]; target-extreme [иков, oints, inki, wish, aken, inks]; classes {'alphabetic': 981, 'mixed': 11, 'punctuation': 2}
- C2 (n=829): representatives [␠cut, ␠vaccinated, ␠write, ␠stripped, ␠transform, 建議, ␠written, ␠disagreement, ␠report, ␠disgusting]; target-extreme [␠advise, overwrite, ␠plunge, ␠disagree, ␠choke, ␠standby]; classes {'alphabetic': 820, 'mixed': 9}
- C3 (n=770): representatives [뤗, 턔, 痦, 业内人士, ␠fontSize, 읩, strncmp, ␠misdemean, 嵝, 礞]; target-extreme [眼科, xDA, ␠outFile, ␠drawback, скоп, ניווט]; classes {'alphabetic': 670, 'mixed': 72, 'punctuation': 28}
- C4 (n=663): representatives [');\r\n\r\n, ");\r\n, .", "))\r\n, ])\r\n, ))\r\n, ")\r\n, )))\r\n, ')\r\n\r\n, '\r\n]; target-extreme [␠');\n, ␠'');\n\n, ],\n, ␠')\n, "],\n, "]}\n]; classes {'alphabetic': 4, 'mixed': 2, 'punctuation': 651, 'whitespace': 6}
- C5 (n=650): representatives [ですね, 드립니다, ようになりました, っています, していました, になりました, ␠المواطنين, ␠الجميع, することは, 说实话]; target-extreme [实在, 不會, ␠услуги, orgt, ります, מסוגל]; classes {'alphabetic': 647, 'mixed': 3}
- C6 (n=361): representatives [DM, GS, DP, =, \theight, ␠PN, [, MD, \tdata, ,k]; target-extreme [\tMatrix, 0, \tap, ␠PN, PN, hat]; classes {'alphabetic': 256, 'mixed': 91, 'numeric': 8, 'punctuation': 6}
- C7 (n=261): representatives [␠photographers, ␠participants, ␠employees, ␠goalkeeper, ␠government, ␠officer, 学生们, ␠manufacturers, ␠constituency, 加盟商]; target-extreme [␠neighbors, ␠Cardinals, 学生们, ␠manufacturers, 生产商, Trump]; classes {'alphabetic': 259, 'mixed': 2}
- C8 (n=180): representatives [␠Portsmouth, ␠Birmingham, ington, ␠Sacramento, ␠Pittsburgh, ␠Taliban, ␠Montgomery, ␠Monsanto, ␠Wilmington, داعش]; target-extreme [华盛顿, Scotland, ␠PayPal, lington, olson, ongyang]; classes {'alphabetic': 180}
- C9 (n=119): representatives [␠don, ␠Unfortunately, ␠probably, ␠according, ␠particularly, ␠perhaps, ␠weren, ␠unfortunately, "What, Nevertheless]; target-extreme [␠although, Instead, ␠Meanwhile, Indeed, ␠Конечно, ␠probably]; classes {'alphabetic': 97, 'mixed': 20, 'punctuation': 2}
- C10 (n=112): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t]; classes {'alphabetic': 3, 'mixed': 1, 'punctuation': 18, 'whitespace': 90}
- C11 (n=54): representatives [␠brown, ␠tighten, ␠Brown, green, ␠lower, strength, ␠strengthen, ␠tightened, ␠stronger, ␠heightened]; target-extreme [␠tightened, orizontal, ␠strong, ␠weaker, ␠darker, ␠brighter]; classes {'alphabetic': 52, 'mixed': 2}
- C12 (n=36): representatives [␠�, ␠不, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠控, ␠�]; target-extreme [␠�, ��, ␠�, ␠主, ␠�, ␠生]; classes {'alphabetic': 13, 'punctuation': 23}

Strongest intercommunity connections:

- C0 to C2: 1721 token edges; mean cosine 0.139086
- C0 to C1: 1331 token edges; mean cosine 0.130393
- C0 to C3: 1055 token edges; mean cosine 0.125383
- C3 to C5: 847 token edges; mean cosine 0.131225
- C0 to C7: 766 token edges; mean cosine 0.141987
- C1 to C2: 626 token edges; mean cosine 0.137262
- C0 to C5: 557 token edges; mean cosine 0.129440
- C1 to C5: 531 token edges; mean cosine 0.133993
- C1 to C3: 518 token edges; mean cosine 0.123825
- C2 to C5: 497 token edges; mean cosine 0.136318
- C2 to C3: 464 token edges; mean cosine 0.126260
- C1 to C6: 455 token edges; mean cosine 0.134075
- C0 to C6: 347 token edges; mean cosine 0.129527
- C0 to C8: 318 token edges; mean cosine 0.126556
- C5 to C7: 273 token edges; mean cosine 0.137330

#### negative_tail

- Nodes: 6052
- Directed 10-NN edges: 60520
- Undirected edges: 43386
- Communities: 10
- Modularity: 0.478479

All communities:

- C0 (n=1306): representatives [\tdes, _done, ␠Clubs, _Settings, ␠tweak, (template, ␠일이, (run, (ed, -str]; target-extreme [/high, /renderer, _gap, .asset, 视野, .div]; classes {'alphabetic': 528, 'mixed': 777, 'punctuation': 1}
- C1 (n=1175): representatives [㧬, GeneratedValue, 🍱, .destroyAllWindows, BootApplication, ␠işle, .UseVisualStyleBackColor, /ayushman, ᶅ, ␠buttonWithType]; target-extreme [쐬, \brief, .alibaba, 遘, 新冠, 暄]; classes {'alphabetic': 807, 'mixed': 288, 'punctuation': 80}
- C2 (n=1042): representatives [␠profes, ␠получа, профессиона, ␠Mari, Hugh, ␠Carrie, ␠conna, ␠univers, ␠Anna, ␠liber]; target-extreme [␠alf, ␠Elder, ␠получа, ␠Сан, ␠Mile, ␠jos]; classes {'alphabetic': 1008, 'mixed': 34}
- C3 (n=766): representatives [诠释, ␠splendid, ␠trụ, ␠medically, �, 创新, 提升, 捂, ␠auditory, ся]; target-extreme [夏, .Success, 天府, 诠释, 建军, 절차]; classes {'alphabetic': 717, 'mixed': 13, 'punctuation': 36}
- C4 (n=676): representatives [何度も, ␠بلا, ␠yaygın, からの, ␠הא, してくれ, ␠בהם, ␠dzięki, 最常见的, と考え]; target-extreme [史上最, ␠még, ␠الاخ, ␠פר, いう, łoż]; classes {'alphabetic': 668, 'mixed': 8}
- C5 (n=292): representatives [✽, 🏦, ﯭ, 💨, 큦, ␠eskorte, ﰀ, 🏛, 📺, ✬]; target-extreme [ː, 🤬, ⓤ, ʝ, ✽, ᑯ]; classes {'alphabetic': 170, 'mixed': 1, 'punctuation': 121}
- C6 (n=254): representatives [="<?=$, ␠[[], =<?=$, ␠​, ={`/, #{@, ␠[&, ◇, >{{$, <?=$]; target-extreme [⊔, ́, @Api, ,www, <Real, {']; classes {'alphabetic': 20, 'mixed': 46, 'punctuation': 188}
- C7 (n=217): representatives [삻, ご�, 퓼, �, �, 𝑎, ე, �, ℎ, ȃ]; target-extreme [เผยแ, �, �, 𝑎, �, �]; classes {'alphabetic': 135, 'mixed': 10, 'numeric': 1, 'punctuation': 71}
- C8 (n=198): representatives [␠sécur, è, ␠É, É, Pago, ␠é, ␠cré, ␠Sé, ␠ciné, teste]; target-extreme [␠È, È, établ, ␠Método, ␠velocidad, ␠siè]; classes {'alphabetic': 193, 'mixed': 5}
- C9 (n=126): representatives [␠of, а, ์, ing, es, ь, 了, s, ␠on, ая]; target-extreme [␠of, _of, class, ␠with, ␠OF, ␠for]; classes {'alphabetic': 103, 'mixed': 16, 'punctuation': 6, 'whitespace': 1}

Strongest intercommunity connections:

- C0 to C2: 1808 token edges; mean cosine 0.129982
- C0 to C1: 1482 token edges; mean cosine 0.124162
- C2 to C3: 1021 token edges; mean cosine 0.129407
- C1 to C2: 943 token edges; mean cosine 0.130637
- C1 to C3: 921 token edges; mean cosine 0.130679
- C2 to C4: 903 token edges; mean cosine 0.130793
- C0 to C3: 886 token edges; mean cosine 0.129145
- C1 to C5: 853 token edges; mean cosine 0.142321
- C3 to C4: 839 token edges; mean cosine 0.129558
- C1 to C4: 745 token edges; mean cosine 0.134904
- C0 to C4: 516 token edges; mean cosine 0.126626
- C1 to C7: 446 token edges; mean cosine 0.141870
- C2 to C8: 393 token edges; mean cosine 0.132820
- C1 to C6: 329 token edges; mean cosine 0.136789
- C4 to C8: 306 token edges; mean cosine 0.136361

## State 06 — block_5_output

Paired positive_head: membership Jaccard 0.904050; edge Jaccard 0.776216; shared tokens 5625.
Paired negative_tail: membership Jaccard 0.926148; edge Jaccard 0.826335; shared tokens 5869.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6160
- Directed 10-NN edges: 61600
- Undirected edges: 43559
- Communities: 12
- Modularity: 0.574630

All communities:

- C0 (n=1365): representatives [␠transformations, ␠valves, ␠concentrations, ␠tariffs, ␠cracks, ␠millennials, ␠downside, ␠thermostat, ␠discrepancy, ␠transform]; target-extreme [␠intervention, ␠stain, ␠imbalance, piece, ␠holes, ␠positions]; classes {'alphabetic': 1307, 'mixed': 57, 'punctuation': 1}
- C1 (n=1075): representatives [ik, ants, ac, ить, ются, ments, ap, ick, ington, ita]; target-extreme [oints, arf, oningen, traction, formed, inski]; classes {'alphabetic': 1058, 'mixed': 15, 'numeric': 1, 'punctuation': 1}
- C2 (n=961): representatives [턔, 痦, نطق, ␠kutje, ␠openFileDialog, .DropDownStyle, INFRINGEMENT, ␠urządzenia, ␠projectName, ␠hardcoded]; target-extreme [inki, ␠outFile, _barang, xDA, illance, IsEmpty]; classes {'alphabetic': 816, 'mixed': 104, 'punctuation': 41}
- C3 (n=887): representatives [');\r\n\r\n, .", ]))\r\n, ");\r\n, ')\r\n\r\n, ")\r\n, ])\r\n, "))\r\n, ");\r\n\r\n, ))\r\n]; target-extreme [],\n, ']\r\n, ?'\n\n, ';\r\n\r\n, ␠');\n, ...\n]; classes {'alphabetic': 23, 'mixed': 13, 'punctuation': 824, 'whitespace': 27}
- C4 (n=499): representatives [\ttimeout, ␠write, ␠height, \twrite, \tleft, \tsignal, \tframe, HB, )r, ␠pr]; target-extreme [\tMatrix, 棵树, overwrite, [s, \tsignal, \tap]; classes {'alphabetic': 337, 'mixed': 160, 'punctuation': 2}
- C5 (n=476): representatives [ようになりました, っている, ␠الأخرى, していました, だったので, 願意, ␠שלנו, することは, ってしまった, があるので]; target-extreme [实在, ␠please, 站着, 好吗, 定了, 戳]; classes {'alphabetic': 467, 'mixed': 7, 'punctuation': 2}
- C6 (n=468): representatives [說話, ␠think, ␠placed, ␠stripped, ␠slipped, ␠utilize, ␠washed, ␠scratched, ␠attacking, ␠soaked]; target-extreme [␠instruct, ␠remind, standing, ␠indicative, oused, ␠tipped]; classes {'alphabetic': 458, 'mixed': 10}
- C7 (n=128): representatives [␠Portsmouth, ␠gypsum, ␠Wellington, ␠granite, ␠Princeton, ␠Wilmington, smouth, ␠Montgomery, ␠Newcastle, ␠limestone]; target-extreme [osphate, 丹麦, lington, osaic, 졵, ␠adidas]; classes {'alphabetic': 125, 'mixed': 3}
- C8 (n=95): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠]; classes {'alphabetic': 6, 'numeric': 2, 'punctuation': 5, 'whitespace': 82}
- C9 (n=82): representatives [␠girl, 学生们, ␠child, 巨头, ␠Children, ␠Students, 加盟商, ␠girls, ␠kid, 年轻人]; target-extreme [学生们, ␠jeunes, ␠stu, 胖, udents, 小伙子]; classes {'alphabetic': 81, 'mixed': 1}
- C10 (n=73): representatives [␠brown, ␠gray, green, ␠long, ␠strong, ␠North, ␠White, ␠Brown, ␠black, ␠white]; target-extreme [␠northwest, ␠gray, ␠darker, utely, ␠strong, HITE]; classes {'alphabetic': 70, 'mixed': 3}
- C11 (n=51): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不]; target-extreme [␠�, ␠�, ␠�, ␠生, ␠�, ␠�]; classes {'alphabetic': 19, 'mixed': 1, 'punctuation': 31}

Strongest intercommunity connections:

- C0 to C2: 1333 token edges; mean cosine 0.124940
- C0 to C1: 1289 token edges; mean cosine 0.131423
- C0 to C6: 1203 token edges; mean cosine 0.137671
- C2 to C5: 772 token edges; mean cosine 0.130587
- C1 to C2: 710 token edges; mean cosine 0.120157
- C1 to C4: 682 token edges; mean cosine 0.135580
- C0 to C4: 590 token edges; mean cosine 0.133032
- C0 to C5: 508 token edges; mean cosine 0.128291
- C1 to C5: 485 token edges; mean cosine 0.134644
- C2 to C4: 447 token edges; mean cosine 0.124290
- C1 to C6: 432 token edges; mean cosine 0.136843
- C2 to C6: 409 token edges; mean cosine 0.124449
- C5 to C6: 296 token edges; mean cosine 0.135913
- C0 to C7: 249 token edges; mean cosine 0.126845
- C2 to C3: 231 token edges; mean cosine 0.133518

#### negative_tail

- Nodes: 6179
- Directed 10-NN edges: 61790
- Undirected edges: 44382
- Communities: 10
- Modularity: 0.484275

All communities:

- C0 (n=1249): representatives [\tdes, ␠volcano, efully, ␠splendid, ␠sala, _Settings, _done, ␠Showing, Companies, (template]; target-extreme [/renderer, /banner, Producer, Opera, Modes, (template]; classes {'alphabetic': 851, 'mixed': 398}
- C1 (n=928): representatives [␠profes, ␠получа, ␠liber, ␠oxid, ␠Jenna, ␠ciné, ␠Lola, と考え, ␠immedi, ␠univers]; target-extreme [␠alf, ␠ly, ␠assh, ␠Giul, /pop, Chron]; classes {'alphabetic': 885, 'mixed': 41, 'punctuation': 2}
- C2 (n=836): representatives [母校, 诠释, 创新, علام, 花, 公共文化, 车, 提升, 戏曲, 옷]; target-extreme [�, 收集, 聊天, ␠ancestral, 萤, 夏]; classes {'alphabetic': 815, 'mixed': 6, 'punctuation': 15}
- C3 (n=832): representatives [.destroyAllWindows, GeneratedValue, BootApplication, ␠RelayCommand, @NgModule, .UseVisualStyleBackColor, ␠WPARAM, .setBackgroundResource, ␠OnCollision, ␠referencedColumnName]; target-extreme [(Text, /INFO, ␠MSG, =models, .bukkit, Jvm]; classes {'alphabetic': 427, 'mixed': 395, 'punctuation': 10}
- C4 (n=770): representatives [㧬, 🍱, ␠işle, ✽, ﯭ, 🏦, ᶅ, 💨, /ayushman, ﭮ]; target-extreme [⊔, �, ␠még, 🌶, 쫙, ✽]; classes {'alphabetic': 557, 'mixed': 13, 'punctuation': 200}
- C5 (n=575): representatives [ทราบ, ␠بلا, 気軽に, からの, ␠일이, 第一家, 最好不要, ␠successes, ␠dzięki, ␠המשפחה]; target-extreme [הצלחת, ␠succès, _success, .Success, 可不是, bruar]; classes {'alphabetic': 549, 'mixed': 26}
- C6 (n=489): representatives [а, 𝑎, 𝑨, ing, ␠of, ␠É, ﾞ, �, ์, ａ]; target-extreme [␠of, _of, ␠OF, �, ː, �]; classes {'alphabetic': 362, 'mixed': 35, 'numeric': 3, 'punctuation': 88, 'whitespace': 1}
- C7 (n=329): representatives [.Act, CCI, _CMD, _Ad, _pl, ␠App, _ERROR, Acc, .FR, _ASS]; target-extreme [.div, .app, _ASS, _HOST, /div, -cond]; classes {'alphabetic': 59, 'mixed': 270}
- C8 (n=164): representatives ["=>$, ="<?=$, ={`/, }());\n, =<?=$, <?=$, "><?=$, )const, ",$, >{{$]; target-extreme [={`/, ␠;\n\n\n, ={(), ([^, ="<?=$, .auth]; classes {'alphabetic': 14, 'mixed': 32, 'punctuation': 118}
- C9 (n=7): representatives [דוגמה, ␠пример, EXAMPLE, ␠örnek, ␠example, ␠exemp, Examples]; target-extreme [␠örnek, דוגמה, EXAMPLE, ␠example, ␠exemp, Examples]; classes {'alphabetic': 7}

Strongest intercommunity connections:

- C0 to C1: 1758 token edges; mean cosine 0.131579
- C0 to C3: 1346 token edges; mean cosine 0.128422
- C0 to C2: 1058 token edges; mean cosine 0.132771
- C3 to C4: 1038 token edges; mean cosine 0.137951
- C2 to C4: 852 token edges; mean cosine 0.131641
- C1 to C2: 803 token edges; mean cosine 0.128689
- C0 to C7: 787 token edges; mean cosine 0.127392
- C1 to C5: 687 token edges; mean cosine 0.134544
- C0 to C5: 662 token edges; mean cosine 0.132614
- C2 to C5: 652 token edges; mean cosine 0.131554
- C1 to C4: 634 token edges; mean cosine 0.132336
- C4 to C5: 544 token edges; mean cosine 0.133737
- C1 to C7: 519 token edges; mean cosine 0.133584
- C1 to C3: 519 token edges; mean cosine 0.128007
- C4 to C6: 503 token edges; mean cosine 0.140589

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5687
- Directed 10-NN edges: 56870
- Undirected edges: 40234
- Communities: 11
- Modularity: 0.572739

All communities:

- C0 (n=1400): representatives [␠contractors, ␠transformations, ␠valves, ␠tariffs, ␠stripped, ␠concentrations, ␠thermostat, ␠write, ␠cracks, ␠discrepancy]; target-extreme [␠intervention, ␠stain, ␠remind, ␠imbalance, ␠instruct, piece]; classes {'alphabetic': 1359, 'mixed': 39, 'punctuation': 2}
- C1 (n=1053): representatives [ik, ants, ap, ick, ac, ments, ita, il, ington, ites]; target-extreme [oints, arf, oningen, formed, traction, иков]; classes {'alphabetic': 1028, 'mixed': 23, 'numeric': 1, 'punctuation': 1}
- C2 (n=834): representatives [');\r\n\r\n, .", ");\r\n, ')\r\n\r\n, ]))\r\n, ")\r\n, ])\r\n, ");\r\n\r\n, "))\r\n, "));\n]; target-extreme [],\n, ']\r\n, ?'\n\n, ␠');\n, ';\r\n\r\n, ␠')\n]; classes {'alphabetic': 26, 'mixed': 10, 'punctuation': 772, 'whitespace': 26}
- C3 (n=768): representatives [턔, 痦, نطق, ␠spriteBatch, ␠openFileDialog, ␠downside, ␠kutje, .DropDownStyle, lığını, INFRINGEMENT]; target-extreme [实在, ␠outFile, inki, 棵树, overwrite, xDA]; classes {'alphabetic': 631, 'mixed': 99, 'punctuation': 38}
- C4 (n=696): representatives [ить, ようになりました, していました, ␠الأخرى, だったので, ␠think, 願意, ␠שלנו, することは, ␠urządzenia]; target-extreme [␠please, 站着, 好吗, 定了, _barang, ␠אישית]; classes {'alphabetic': 680, 'mixed': 14, 'punctuation': 2}
- C5 (n=391): representatives [\ttimeout, \twrite, \tleft, HB, \tframe, \tsignal, ␠height, GS, (ib, ␠pr]; target-extreme [\tMatrix, [s, \tsignal, \tap, ␠TN, (decoded]; classes {'alphabetic': 239, 'mixed': 148, 'punctuation': 4}
- C6 (n=337): representatives [␠Portsmouth, ␠millennials, ␠gypsum, ␠girl, 学生们, 树脂, ␠child, ␠Wellington, ␠работник, ␠granite]; target-extreme [␠street, lington, 学生们, 丹麦, 霉素, ␠wastewater]; classes {'alphabetic': 331, 'mixed': 6}
- C7 (n=89): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t␠␠␠␠␠␠␠␠␠␠␠␠, \t\t␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠]; classes {'alphabetic': 8, 'mixed': 1, 'numeric': 2, 'punctuation': 3, 'whitespace': 75}
- C8 (n=50): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不]; target-extreme [␠�, ␠�, ␠�, ␠�, ␠�, ␠生]; classes {'alphabetic': 18, 'mixed': 2, 'punctuation': 30}
- C9 (n=43): representatives [␠gray, ␠brown, ␠black, ␠White, ␠long, ␠strong, ␠Brown, Green, ␠early, ␠lower]; target-extreme [␠gray, ␠darker, ␠strong, ␠brown, ␠softer, -white]; classes {'alphabetic': 40, 'mixed': 3}
- C10 (n=26): representatives [說話, ␠speaks, ␠speak, ␠talk, ␠spoke, ␠speakers, Speak, Speaking, ␠spoken, ␠Speak]; target-extreme [Speaking, ␠Speaking, ␠speak, ␠Freak, 喉咙, ␠talk]; classes {'alphabetic': 26}

Strongest intercommunity connections:

- C0 to C1: 1525 token edges; mean cosine 0.135588
- C0 to C3: 1022 token edges; mean cosine 0.122651
- C0 to C4: 990 token edges; mean cosine 0.130209
- C3 to C4: 894 token edges; mean cosine 0.124853
- C0 to C6: 721 token edges; mean cosine 0.129088
- C1 to C4: 700 token edges; mean cosine 0.132952
- C1 to C3: 591 token edges; mean cosine 0.119119
- C1 to C5: 544 token edges; mean cosine 0.135688
- C1 to C6: 496 token edges; mean cosine 0.131307
- C3 to C5: 413 token edges; mean cosine 0.124326
- C0 to C5: 401 token edges; mean cosine 0.134799
- C3 to C6: 364 token edges; mean cosine 0.120874
- C4 to C6: 314 token edges; mean cosine 0.124877
- C2 to C3: 231 token edges; mean cosine 0.128504
- C2 to C5: 177 token edges; mean cosine 0.157343

#### negative_tail

- Nodes: 6027
- Directed 10-NN edges: 60270
- Undirected edges: 43220
- Communities: 8
- Modularity: 0.489587

All communities:

- C0 (n=1498): representatives [_Settings, ␠Showing, _done, ␠passwords, Companies, ␠Sends, ␠retrieve, (template, ␠contexts, ␠preached]; target-extreme [/renderer, /banner, Modes, Producer, Opera, .div]; classes {'alphabetic': 715, 'mixed': 783}
- C1 (n=1068): representatives [㧬, .destroyAllWindows, GeneratedValue, 🍱, BootApplication, ␠RelayCommand, .UseVisualStyleBackColor, @NgModule, ␠işle, ␠OnCollision]; target-extreme [/INFO, .bukkit, Jvm, 荼, 鬘, .PropTypes]; classes {'alphabetic': 739, 'mixed': 255, 'punctuation': 74}
- C2 (n=888): representatives [efully, ␠получа, ␠splendid, ทราบ, ␠cruel, ␠بلا, ␠일이, からの, علام, 気軽に]; target-extreme [הצלחת, ␠succès, ␠assh, _success, ␠még, 可不是]; classes {'alphabetic': 865, 'mixed': 19, 'punctuation': 4}
- C3 (n=841): representatives [␠volcano, ␠profes, ␠sala, ␠tavern, Hugh, ␠liber, ␠AHL, ␠Jenna, ␠vodka, ␠Lola]; target-extreme [/pop, ␠Giul, bruar, ␠Alter, ␠Curry, ␠Elder]; classes {'alphabetic': 806, 'mixed': 32, 'punctuation': 3}
- C4 (n=786): representatives [母校, ␠colleges, 花, 诠释, 创新, 车, 公共文化, ␠berries, 提升, 戏曲]; target-extreme [␠alf, �, 收集, ␠ancestral, 聊天, 萤]; classes {'alphabetic': 772, 'mixed': 11, 'punctuation': 3}
- C5 (n=407): representatives [𝑎, 𝑨, ␠É, "=>$, ℎ, ="<?=$, è, ȃ, ␠​, =<?=$]; target-extreme [ː, ␠È, ّ, è, ܢ, È]; classes {'alphabetic': 171, 'mixed': 52, 'numeric': 3, 'punctuation': 181}
- C6 (n=289): representatives [а, ing, ␠of, ﾞ, ␠EE, �, ์, e, s, ся]; target-extreme [␠of, _of, ␠OF, �, �, import]; classes {'alphabetic': 221, 'mixed': 27, 'punctuation': 40, 'whitespace': 1}
- C7 (n=250): representatives [🏦, ✽, ﯭ, 💨, ﰀ, 쿽, 🍔, 💵, ⨭, ☫]; target-extreme [⊔, 🌶, 쫙, ʝ, ✽, 🏍]; classes {'alphabetic': 118, 'mixed': 2, 'punctuation': 130}

Strongest intercommunity connections:

- C0 to C3: 1687 token edges; mean cosine 0.130754
- C0 to C1: 1551 token edges; mean cosine 0.126215
- C0 to C2: 1025 token edges; mean cosine 0.130165
- C2 to C4: 991 token edges; mean cosine 0.130762
- C0 to C4: 960 token edges; mean cosine 0.129169
- C1 to C2: 959 token edges; mean cosine 0.133636
- C2 to C3: 952 token edges; mean cosine 0.132216
- C1 to C4: 853 token edges; mean cosine 0.129570
- C3 to C4: 788 token edges; mean cosine 0.129604
- C1 to C7: 667 token edges; mean cosine 0.141834
- C1 to C3: 639 token edges; mean cosine 0.131478
- C1 to C5: 557 token edges; mean cosine 0.138109
- C0 to C6: 343 token edges; mean cosine 0.131851
- C2 to C6: 339 token edges; mean cosine 0.136023
- C0 to C5: 330 token edges; mean cosine 0.124546

## State 07 — block_6_output

Paired positive_head: membership Jaccard 0.909869; edge Jaccard 0.792845; shared tokens 5845.
Paired negative_tail: membership Jaccard 0.900554; edge Jaccard 0.762405; shared tokens 5687.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5971
- Directed 10-NN edges: 59710
- Undirected edges: 42479
- Communities: 11
- Modularity: 0.561964

All communities:

- C0 (n=1356): representatives [␠think, ␠misinformation, ␠transformations, ␠laser, ␠take, ␠house, ␠placed, ␠negotiations, ␠scratched, ␠pushed]; target-extreme [␠intervention, ␠instruct, ␠remind, ␠scratched, ␠knife, ␠holes]; classes {'alphabetic': 1300, 'mixed': 56}
- C1 (n=1032): representatives [ants, ine, ik, вать, ments, ton, ick, ают, ark, ains]; target-extreme [oints, kes, иков, arf, ита, zik]; classes {'alphabetic': 1019, 'mixed': 10, 'punctuation': 3}
- C2 (n=936): representatives [だったので, であれば, てしまいました, ␠açıklama, になっています, っている, ないので, ってる, してしまう, ようになりました]; target-extreme [ますが, _barang, ␠please, став, 实在, عون]; classes {'alphabetic': 922, 'mixed': 11, 'punctuation': 3}
- C3 (n=795): representatives [뤗, 턔, \ttimeout, نطق, ␠openFileDialog, 痦, ␠kutje, .isSelected, .tableLayoutPanel, 圙]; target-extreme [overwrite, ␠outFile, .DropDownStyle, IsEmpty, ␠progressBar, ultipart]; classes {'alphabetic': 647, 'mixed': 110, 'punctuation': 38}
- C4 (n=656): representatives [');\r\n\r\n, ")\r\n, .", ");\r\n, ]))\r\n, ])\r\n, ))\r\n, ');\r\n, ')\r\n\r\n, ……\n\n]; target-extreme ["],\n, ␠');\n, ';\r\n\r\n, ']\r\n, ],\n, '),\r\n]; classes {'alphabetic': 13, 'mixed': 19, 'numeric': 2, 'punctuation': 614, 'whitespace': 8}
- C5 (n=490): representatives [␠Portsmouth, ington, ␠المواطنين, ␠millennials, ␠policymakers, ␠employees, constitutional, smouth, 老爷子, داعش]; target-extreme [␠lieutenant, ␠rebels, orth, 学生们, ␠House, ␠stu]; classes {'alphabetic': 480, 'mixed': 10}
- C6 (n=487): representatives [ﳈ, \tcolor, \tleft, \theight, ␠long, \treset, GS, \twidth, \tposition, \tboard]; target-extreme [\tMatrix, \tsignal, piece, *k, \tboard, -data]; classes {'alphabetic': 310, 'mixed': 171, 'punctuation': 5, 'whitespace': 1}
- C7 (n=80): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠, \t\t\t\t\t\t, \t\t\t\t\t\t\t, \t\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, 0, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t]; classes {'alphabetic': 3, 'mixed': 1, 'numeric': 1, 'punctuation': 4, 'whitespace': 71}
- C8 (n=49): representatives [␠dignity, ␠optics, itics, istics, atics, iatrics, arity, ␠purity, ortality, ␠Engineering]; target-extreme [idity, rightness, electronics, iagnostics, ynamics, 꿱]; classes {'alphabetic': 45, 'mixed': 4}
- C9 (n=47): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠生, ␠�, ␠主, ␠�]; classes {'alphabetic': 16, 'mixed': 1, 'punctuation': 30}
- C10 (n=43): representatives [說話, ␠speak, ␠speaks, ␠speaking, ␠stood, ␠spoke, ␠четы, ␠stand, 三四, 5]; target-extreme [standing, 给我们, ␠stood, ␠Speaking, Speaking, Speak]; classes {'alphabetic': 42, 'numeric': 1}

Strongest intercommunity connections:

- C0 to C1: 1386 token edges; mean cosine 0.134930
- C2 to C3: 1112 token edges; mean cosine 0.126108
- C0 to C2: 1094 token edges; mean cosine 0.132031
- C0 to C5: 1065 token edges; mean cosine 0.133830
- C0 to C3: 992 token edges; mean cosine 0.126276
- C1 to C2: 825 token edges; mean cosine 0.130647
- C0 to C6: 666 token edges; mean cosine 0.132756
- C1 to C5: 592 token edges; mean cosine 0.129575
- C1 to C6: 575 token edges; mean cosine 0.130138
- C1 to C3: 563 token edges; mean cosine 0.119820
- C2 to C5: 505 token edges; mean cosine 0.132511
- C3 to C5: 481 token edges; mean cosine 0.125885
- C3 to C6: 418 token edges; mean cosine 0.124110
- C2 to C6: 210 token edges; mean cosine 0.123614
- C5 to C6: 188 token edges; mean cosine 0.127155

#### negative_tail

- Nodes: 6253
- Directed 10-NN edges: 62530
- Undirected edges: 44605
- Communities: 11
- Modularity: 0.487219

All communities:

- C0 (n=1277): representatives [␠LAW, ␠SECOND, _done, _rel, _Settings, ␠RECE, _RUN, _cluster, (template, _review]; target-extreme [/banner, /renderer, ␠פר, .EN, _valid, URRED]; classes {'alphabetic': 575, 'mixed': 702}
- C1 (n=1098): representatives [профессиона, ␠sessions, ␠splendid, ␠manuscripts, 母校, ␠preached, ␠contexts, ␠pseudo, ␠AHL, ␠simulation]; target-extreme [␠Elder, Modes, Producer, Domain, ␠advoc, ␠Archer]; classes {'alphabetic': 1046, 'mixed': 52}
- C2 (n=756): representatives [.destroyAllWindows, BootApplication, ␠RelayCommand, OptionsItemSelected, ␠OnCollision, .setBackgroundResource, ␠referencedColumnName, ␠WPARAM, .LinearLayoutManager, ␠PropertyChangedEventArgs]; target-extreme [␠ctx, הצלחת, =models, .BorderFactory, Jvm, _stdio]; classes {'alphabetic': 450, 'mixed': 295, 'punctuation': 11}
- C3 (n=743): representatives [㧬, 🍱, ibNameOrNil, ᶅ, ␠işle, 🏦, /ayushman, 뗄, 뺍, ✽]; target-extreme [�, ␠alf, 떴, 🧁, 萤, �]; classes {'alphabetic': 561, 'mixed': 8, 'punctuation': 174}
- C4 (n=576): representatives [תחילת, ␠получа, ␠일이, からの, ␠بلا, と考え, ␠cioè, ␠dzięki, 最常见的, 就能够]; target-extreme [␠쉽게, 天府, ␠بلا, ␠még, 年之, 史上最]; classes {'alphabetic': 570, 'mixed': 3, 'numeric': 1, 'punctuation': 2}
- C5 (n=571): representatives [诠释, 新, 创新, 提升, 深入推进, ␠successes, 研究, 休闲, 车, 体]; target-extreme [␠succès, 收集, ␠giải, 夏, 传, 盧]; classes {'alphabetic': 558, 'mixed': 11, 'punctuation': 2}
- C6 (n=524): representatives [а, ␠Э, ␠of, ing, 𝑎, �, ე, 𝐇, e, ℎ]; target-extreme [␠of, _of, ␠OF, �, ␠with, �]; classes {'alphabetic': 440, 'mixed': 39, 'punctuation': 44, 'whitespace': 1}
- C7 (n=359): representatives [Hugh, ␠Lauren, ␠Jenna, ␠авг, ␠Sandra, ␠Denn, ␠Franz, ␠Benn, ␠Manning, ␠Seth]; target-extreme [Fx, ␠Romero, ␠ly, ␠Bij, Brian, ␠Petra]; classes {'alphabetic': 350, 'mixed': 9}
- C8 (n=264): representatives [=<?=$, ="<?=$, (":/, }());\n, ˇ, "><?=$, :)];\n, ␠Skipping, ´, ={`/]; target-extreme [⊔, ّ, ː, ={(), ,www, )$_]; classes {'alphabetic': 49, 'mixed': 14, 'numeric': 1, 'punctuation': 200}
- C9 (n=53): representatives [<Unit, class, <Event, define, <Task, <Real, .enum, <Element, exports, _ENUM]; target-extreme [class, <Car, <Course, <Real, module, define]; classes {'alphabetic': 18, 'mixed': 35}
- C10 (n=32): representatives [␠Showing, _Show, Shows, .show, shows, .shows, -show, ␠Show, SHOW, sending]; target-extreme [Shows, .send, zeigt, .shows, .hide, _Show]; classes {'alphabetic': 24, 'mixed': 8}

Strongest intercommunity connections:

- C0 to C1: 2077 token edges; mean cosine 0.131691
- C0 to C2: 1136 token edges; mean cosine 0.124279
- C2 to C3: 1092 token edges; mean cosine 0.137018
- C1 to C5: 1039 token edges; mean cosine 0.131685
- C1 to C2: 828 token edges; mean cosine 0.128554
- C1 to C3: 781 token edges; mean cosine 0.133344
- C1 to C4: 752 token edges; mean cosine 0.133790
- C3 to C4: 610 token edges; mean cosine 0.133577
- C1 to C7: 610 token edges; mean cosine 0.131185
- C0 to C7: 582 token edges; mean cosine 0.131630
- C3 to C6: 507 token edges; mean cosine 0.135619
- C0 to C6: 478 token edges; mean cosine 0.131797
- C4 to C5: 473 token edges; mean cosine 0.129027
- C4 to C6: 443 token edges; mean cosine 0.142949
- C3 to C5: 439 token edges; mean cosine 0.127332

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6298
- Directed 10-NN edges: 62980
- Undirected edges: 44768
- Communities: 10
- Modularity: 0.561979

All communities:

- C0 (n=1251): representatives [␠misinformation, ␠transformations, ␠take, ␠participation, ␠material, ␠transform, ␠placed, ␠symptoms, constitutional, ␠pouring]; target-extreme [␠intervention, ␠instruct, overwrite, ␠remind, ␠scratched, ␠knife]; classes {'alphabetic': 1187, 'mixed': 64}
- C1 (n=1002): representatives [ants, ik, ments, ton, ick, ified, ter, ark, ley, il]; target-extreme [oints, kes, arf, ault, plaint, zik]; classes {'alphabetic': 988, 'mixed': 12, 'punctuation': 2}
- C2 (n=857): representatives [뤗, 턔, ␠açıklama, نطق, ␠모습, 痦, 圙, .tableLayoutPanel, INFRINGEMENT, .DropDownStyle]; target-extreme [_barang, 实在, .DropDownStyle, 겤, departureday, 퓬]; classes {'alphabetic': 783, 'mixed': 43, 'punctuation': 31}
- C3 (n=841): representatives [ington, ␠Portsmouth, ␠laser, ␠employees, ␠spiral, sticks, ␠millennials, smouth, ␠Director, stein]; target-extreme [␠lieutenant, ␠street, orth, ␠mortar, ␠stu, ␠Continent]; classes {'alphabetic': 811, 'mixed': 30}
- C4 (n=708): representatives [\ttimeout, ﳈ, ␠spriteBatch, ␠openFileDialog, .isSelected, \tcolor, \tleft, ␠projectName, \theight, (parseFloat]; target-extreme [\tMatrix, \tsignal, ␠outFile, ␠Thickness, IsEmpty, ␠progressBar]; classes {'alphabetic': 467, 'mixed': 239, 'punctuation': 2}
- C5 (n=673): representatives [');\r\n\r\n, .", ");\r\n, ")\r\n, ]))\r\n, ')\r\n\r\n, ');\r\n, '}}>, ))\r\n, ));\r\n\r\n]; target-extreme ["],\n, ␠');\n, ';\r\n\r\n, ']\r\n, ␠'');\n\n, '),\r\n]; classes {'alphabetic': 7, 'mixed': 15, 'punctuation': 643, 'whitespace': 8}
- C6 (n=659): representatives [であれば, だったので, になっています, ␠think, それでも, してしまう, てしまいました, ってる, っている, ␠الجميع]; target-extreme [ますが, ␠please, だったので, ␠Nhận, 定了, 站着]; classes {'alphabetic': 646, 'mixed': 12, 'punctuation': 1}
- C7 (n=175): representatives [вать, ают, ита, ались, ивают, ивать, ␠сообщил, ций, ились, بدأ]; target-extreme [став, عون, иков, ита, ева, еры]; classes {'alphabetic': 173, 'mixed': 2}
- C8 (n=87): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t\t\t\t]; target-extreme [0, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t]; classes {'alphabetic': 5, 'mixed': 1, 'numeric': 6, 'punctuation': 2, 'whitespace': 73}
- C9 (n=45): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不]; target-extreme [␠�, ␠�, ␠生, ␠�, ␠主, ␠�]; classes {'alphabetic': 14, 'punctuation': 31}

Strongest intercommunity connections:

- C0 to C3: 1544 token edges; mean cosine 0.135042
- C0 to C1: 1140 token edges; mean cosine 0.136174
- C1 to C3: 1068 token edges; mean cosine 0.130906
- C2 to C6: 940 token edges; mean cosine 0.133220
- C0 to C2: 909 token edges; mean cosine 0.128054
- C2 to C3: 821 token edges; mean cosine 0.127627
- C0 to C4: 768 token edges; mean cosine 0.131111
- C0 to C6: 743 token edges; mean cosine 0.136257
- C2 to C4: 684 token edges; mean cosine 0.124064
- C1 to C4: 656 token edges; mean cosine 0.128357
- C3 to C4: 550 token edges; mean cosine 0.124658
- C1 to C2: 532 token edges; mean cosine 0.124178
- C1 to C7: 401 token edges; mean cosine 0.140072
- C3 to C6: 382 token edges; mean cosine 0.131116
- C1 to C6: 361 token edges; mean cosine 0.131221

#### negative_tail

- Nodes: 5749
- Directed 10-NN edges: 57490
- Undirected edges: 40921
- Communities: 9
- Modularity: 0.481265

All communities:

- C0 (n=1189): representatives [␠Showing, ␠sessions, ␠manuscripts, _rel, _done, ␠SECOND, _Settings, _cluster, ROSS, Repo]; target-extreme [/banner, /renderer, ␠פר, .EN, -prom, URRED]; classes {'alphabetic': 552, 'mixed': 636, 'punctuation': 1}
- C1 (n=1133): representatives [㧬, 🍱, תחילת, ␠işle, ibNameOrNil, 🏦, ᶅ, 뗄, /ayushman, ✽]; target-extreme [␠alf, הצלחת, ả, 떴, ␠쉽게, ␠még]; classes {'alphabetic': 942, 'mixed': 17, 'punctuation': 174}
- C2 (n=943): representatives [профессиона, Hugh, ␠splendid, ␠preached, ␠AHL, ␠ciné, ␠RECE, ␠insecurity, 戏曲, ␠FIFA]; target-extreme [Fx, ␠Romero, ␠ly, ␠Elder, Opera, ␠advoc]; classes {'alphabetic': 931, 'mixed': 12}
- C3 (n=842): representatives [.destroyAllWindows, BootApplication, ␠RelayCommand, ␠OnCollision, .setBackgroundResource, ␠referencedColumnName, ␠WPARAM, .LinearLayoutManager, SectionsIn, ]init]; target-extreme [␠ctx, =models, .BorderFactory, ={(), Jvm, _stdio]; classes {'alphabetic': 373, 'mixed': 376, 'punctuation': 93}
- C4 (n=531): representatives [诠释, 深入推进, 创新, 新, 提升, 網絡, 车, 研究, 体, 灯]; target-extreme [�, 收集, ␠giải, 天府, 夏, 传]; classes {'alphabetic': 518, 'mixed': 6, 'punctuation': 7}
- C5 (n=464): representatives [а, ␠Э, ე, 𝐇, ์, ﾞ, e, �, ing, ȃ]; target-extreme [⊔, ّ, �, �, ␠È, ː]; classes {'alphabetic': 303, 'mixed': 20, 'punctuation': 141}
- C6 (n=407): representatives [␠بلا, 最常见的, ␠cioè, 就能够, ␠بنفس, 第一家, ␠без, ␠اللا, 都是非常, 两款]; target-extreme [␠بلا, 年之, 史上最, 可不是, 第七届, ␠بن]; classes {'alphabetic': 394, 'mixed': 12, 'numeric': 1}
- C7 (n=137): representatives [␠of, ␠Algorithms, for, 论, 問題, דוגמה, ␠For, ␠Criteria, of, 关键词]; target-extreme [␠of, _of, ␠OF, ␠with, of, ␠for]; classes {'alphabetic': 112, 'mixed': 21, 'punctuation': 3, 'whitespace': 1}
- C8 (n=103): representatives [␠medically, ␠wholly, ␠dramatically, ␠successes, ␠roughly, ␠wrongly, ␠succès, ␠consciously, ␠טלפון, רופא]; target-extreme [␠succès, 口碑, _success, ␠correctamente, ␠aggressively, ␠velocidad]; classes {'alphabetic': 93, 'mixed': 10}

Strongest intercommunity connections:

- C0 to C2: 1777 token edges; mean cosine 0.131190
- C0 to C3: 1458 token edges; mean cosine 0.124565
- C1 to C3: 1331 token edges; mean cosine 0.133673
- C1 to C2: 1220 token edges; mean cosine 0.131720
- C1 to C4: 894 token edges; mean cosine 0.129465
- C1 to C6: 815 token edges; mean cosine 0.134445
- C0 to C1: 724 token edges; mean cosine 0.126834
- C1 to C5: 697 token edges; mean cosine 0.138445
- C2 to C4: 559 token edges; mean cosine 0.127763
- C2 to C3: 552 token edges; mean cosine 0.127103
- C2 to C6: 466 token edges; mean cosine 0.131584
- C0 to C4: 428 token edges; mean cosine 0.127877
- C2 to C5: 367 token edges; mean cosine 0.130244
- C5 to C6: 324 token edges; mean cosine 0.141386
- C0 to C6: 298 token edges; mean cosine 0.126395

## State 08 — block_7_output

Paired positive_head: membership Jaccard 0.877899; edge Jaccard 0.730108; shared tokens 5299.
Paired negative_tail: membership Jaccard 0.873373; edge Jaccard 0.731518; shared tokens 4966.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5805
- Directed 10-NN edges: 58050
- Undirected edges: 41278
- Communities: 12
- Modularity: 0.576090

All communities:

- C0 (n=1060): representatives [턔, dzić, 痦, ␠spriteBatch, .SelectedIndexChanged, .localScale, .DropDownStyle, .tableLayoutPanel, .SelectedIndex, 保驾护]; target-extreme [عون, primaryKey, 퓬, ␠ShoppingCart, .arange, .DropDownStyle]; classes {'alphabetic': 861, 'mixed': 151, 'punctuation': 48}
- C1 (n=1012): representatives [␠stripped, ␠transformations, ␠placed, ␠slipped, ␠negotiations, ␠participation, ␠sucking, ␠participant, ␠soaked, ␠snatch]; target-extreme [overwrite, ␠intervention, ␠instruct, uplicates, ␠remind, plaint]; classes {'alphabetic': 985, 'mixed': 26, 'punctuation': 1}
- C2 (n=935): representatives [ton, ak, son, ay, ants, ter, ine, ains, ik, ita]; target-extreme [kes, oints, inki, wish, traction, ␠cate]; classes {'alphabetic': 926, 'mixed': 9}
- C3 (n=633): representatives [');\r\n\r\n, ")\r\n, ");\r\n, ).\n\n\n\n, "))\r\n, ));\n\n, ');\r\n, ");\r\n\r\n, ))\r\n, ')\r\n]; target-extreme ["],\n, `\r\n, ],\n, '),\r\n, ';\r\n\r\n, ');\r\n\r\n]; classes {'alphabetic': 2, 'mixed': 4, 'punctuation': 597, 'whitespace': 30}
- C4 (n=616): representatives [␠kitchen, ␠laser, ␠prices, ␠report, ␠apartment, ␠valve, ␠coils, ␠spiral, ␠transform, ␠edge]; target-extreme [␠knife, ␠lieutenant, 쟙, 值, ␠street, oningen]; classes {'alphabetic': 576, 'mixed': 38, 'punctuation': 2}
- C5 (n=554): representatives [になると, ␠think, ってる, ␠الأخرى, ようになりました, ␠لذلك, ␠gdyż, ␠شيء, してしまう, ␠estaba]; target-extreme [␠please, 定了, 实在, 不會, ますが, 给我们]; classes {'alphabetic': 532, 'mixed': 5, 'punctuation': 17}
- C6 (n=421): representatives [ﳈ, ]), '}}>, '), .', )),, .\, ?’, .\", ’.]; target-extreme [`)., *k, "|, +m, ']:, .(]; classes {'alphabetic': 39, 'mixed': 127, 'punctuation': 254, 'whitespace': 1}
- C7 (n=168): representatives [␠millennials, ␠Portsmouth, ␠policymakers, ␠employees, ␠student, 学生们, ␠Student, ␠immigrants, 老板, ␠rebels]; target-extreme [␠rebels, ␠Starbucks, ␠father, 学生们, ␠stu, \tperson]; classes {'alphabetic': 165, 'mixed': 3}
- C8 (n=155): representatives [ются, ают, вать, ить, ывают, лись, дается, ались, ивают, ции]; target-extreme [␠entrar, ących, ragen, ались, еры, reiben]; classes {'alphabetic': 153, 'mixed': 1, 'punctuation': 1}
- C9 (n=131): representatives [\ttimeout, \tboard, \tposition, ␠height, \twidth, \tds, \tsignal, \tcolor, \ttable, \tvertices]; target-extreme [\tsignal, \tMatrix, \tdirection, \tdf, \tdc, dating]; classes {'alphabetic': 117, 'mixed': 14}
- C10 (n=77): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, 0]; classes {'alphabetic': 1, 'mixed': 1, 'numeric': 6, 'punctuation': 6, 'whitespace': 63}
- C11 (n=43): representatives [␠speak, ␠speaking, ␠speaks, 說話, ␠talk, ␠sitting, ␠spoke, ␠speakers, ␠stood, ␠narrator]; target-extreme [卧, ␠speaks, Speaking, 躺, ␠Speaking, Speak]; classes {'alphabetic': 43}

Strongest intercommunity connections:

- C1 to C4: 1394 token edges; mean cosine 0.133160
- C0 to C1: 966 token edges; mean cosine 0.124666
- C2 to C4: 894 token edges; mean cosine 0.131668
- C1 to C2: 871 token edges; mean cosine 0.131078
- C0 to C5: 841 token edges; mean cosine 0.133240
- C0 to C2: 617 token edges; mean cosine 0.121854
- C0 to C4: 584 token edges; mean cosine 0.122617
- C1 to C5: 550 token edges; mean cosine 0.134188
- C3 to C6: 485 token edges; mean cosine 0.246173
- C2 to C8: 388 token edges; mean cosine 0.144096
- C0 to C8: 266 token edges; mean cosine 0.137326
- C1 to C7: 263 token edges; mean cosine 0.133138
- C2 to C5: 262 token edges; mean cosine 0.131930
- C0 to C6: 249 token edges; mean cosine 0.130083
- C0 to C7: 249 token edges; mean cosine 0.127453

#### negative_tail

- Nodes: 5308
- Directed 10-NN edges: 53080
- Undirected edges: 37946
- Communities: 8
- Modularity: 0.475574

All communities:

- C0 (n=1313): representatives [\tdes, תחילת, Air, _done, area, ␠Running, ␠HEALTH, ROSS, generate, _freq]; target-extreme [_ASS, _BUFFER, URRED, hpp, _valid, .EN]; classes {'alphabetic': 605, 'mixed': 707, 'punctuation': 1}
- C1 (n=974): representatives [GeneratedValue, 🍱, .destroyAllWindows, גרסה, ␠işle, профессиона, OptionsItemSelected, ␠WPARAM, .setBackgroundResource, ᶅ]; target-extreme [␠حر, เผยแ, 🉑, אפליק, 建军, 🧁]; classes {'alphabetic': 689, 'mixed': 155, 'punctuation': 130}
- C2 (n=935): representatives [efully, 攻势, ␠manuscripts, ␠yaygın, ␠fodder, ␠insecurity, 옷, ␠unpredictable, ␠berries, ␠promising]; target-extreme [收集, 提升, 有效地, ␠ancestral, 重心, ␠Elder]; classes {'alphabetic': 918, 'mixed': 17}
- C3 (n=679): representatives [אני, Hugh, ␠médec, انيا, è, ␠Sandra, ␠immedi, ␠É, ␠ciné, ␠univers]; target-extreme [␠alf, ␠È, È, è, hv, Hôtel]; classes {'alphabetic': 668, 'mixed': 11}
- C4 (n=490): representatives [ე, ␠ס, モ, ␠Ав, ␠Э, 놐, ﺎ, ␠авг, ℎ, ȃ]; target-extreme [ّ, ː, �, ܢ, ␠פר, ưa]; classes {'alphabetic': 452, 'mixed': 13, 'punctuation': 25}
- C5 (n=427): representatives [а, ์, ing, �, ␠of, es, e, ed, �, �]; target-extreme [␠of, _of, ␠OF, of, �, ␠with]; classes {'alphabetic': 319, 'mixed': 18, 'punctuation': 90}
- C6 (n=330): representatives [␠بلا, 最常见的, ␠vielleicht, 真的很, からの, ␠hätte, 这么大, ␠새로, ␠før, 多地]; target-extreme [␠succès, ␠még, ␠Wenn, ␠På, ␠بلا, ␠семь]; classes {'alphabetic': 316, 'mixed': 13, 'punctuation': 1}
- C7 (n=160): representatives [=<?=$, ="<?=$, ／, "><?=$, ␠​, ˇ, 〜, ␠@{$, ´, ␠^{\n]; target-extreme [⊔, ␠^{\n, ˇ, ([^, ª, 〜]; classes {'alphabetic': 13, 'mixed': 26, 'punctuation': 121}

Strongest intercommunity connections:

- C0 to C2: 1567 token edges; mean cosine 0.128924
- C1 to C2: 1273 token edges; mean cosine 0.131019
- C0 to C1: 1251 token edges; mean cosine 0.125598
- C0 to C3: 1113 token edges; mean cosine 0.128661
- C2 to C3: 962 token edges; mean cosine 0.131429
- C1 to C3: 729 token edges; mean cosine 0.129754
- C1 to C4: 663 token edges; mean cosine 0.134648
- C2 to C6: 599 token edges; mean cosine 0.134271
- C2 to C5: 523 token edges; mean cosine 0.132878
- C3 to C4: 511 token edges; mean cosine 0.134376
- C4 to C5: 506 token edges; mean cosine 0.148066
- C1 to C6: 413 token edges; mean cosine 0.131496
- C3 to C6: 379 token edges; mean cosine 0.130224
- C0 to C4: 379 token edges; mean cosine 0.126908
- C0 to C6: 365 token edges; mean cosine 0.130062

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5530
- Directed 10-NN edges: 55300
- Undirected edges: 39390
- Communities: 9
- Modularity: 0.577577

All communities:

- C0 (n=1367): representatives [␠laser, ␠stripped, ␠placed, ␠negotiations, ␠prices, ␠apartment, ␠valve, ␠filmmaker, ␠coils, ␠report]; target-extreme [␠intervention, overwrite, ␠instruct, ␠knife, ␠remind, ␠standby]; classes {'alphabetic': 1320, 'mixed': 46, 'punctuation': 1}
- C1 (n=1013): representatives [턔, dzić, 룁, ␠spriteBatch, 痦, .SelectedIndexChanged, \ttimeout, 保驾护, .tableLayoutPanel, ␠kutje]; target-extreme [primaryKey, 얐, ␠reimburse, oningen, 퓬, .arange]; classes {'alphabetic': 827, 'mixed': 137, 'punctuation': 49}
- C2 (n=900): representatives [ton, ak, ine, son, ants, ay, ik, ter, ains, ita]; target-extreme [kes, عون, oints, traction, ␠cate, frac]; classes {'alphabetic': 880, 'mixed': 20}
- C3 (n=800): representatives [');\r\n\r\n, ");\r\n, ")\r\n, ));\n\n, "))\r\n, ).\n\n\n\n, ')\r\n\r\n, ﳈ, ])\r\n, ))\r\n]; target-extreme ["],\n, `\r\n, ],\n, ';\r\n\r\n, ');\r\n\r\n, '),\r\n]; classes {'alphabetic': 22, 'mixed': 20, 'punctuation': 744, 'whitespace': 14}
- C4 (n=560): representatives [になると, ってる, ␠think, してしまう, ようになりました, ␠estaba, ␠الأخرى, てしまった, ␠لذلك, だったので]; target-extreme [␠please, 定了, 实在, ますが, 不會, ماذا]; classes {'alphabetic': 540, 'mixed': 6, 'punctuation': 14}
- C5 (n=369): representatives [ington, ␠Portsmouth, ␠goalkeeper, ␠millennials, ␠king, ␠student, ␠director, ␠policymakers, ␠Student, ␠employees]; target-extreme [␠lieutenant, ␠Starbucks, ␠Knight, 雕像, ␠king, ␠coalition]; classes {'alphabetic': 364, 'mixed': 4, 'punctuation': 1}
- C6 (n=254): representatives [\tboard, )$, \tds, \tcolor, \tposition, \tsignal, \twidth, ␠[, \ttable, \theight]; target-extreme [\tsignal, \tMatrix, *k, +m, 'order, *t]; classes {'alphabetic': 118, 'mixed': 130, 'punctuation': 6}
- C7 (n=165): representatives [ются, ают, ивают, дается, ить, ались, лись, aría, ␠сообщил, ились]; target-extreme [␠entrar, ących, ragen, ались, иков, еры]; classes {'alphabetic': 164, 'mixed': 1}
- C8 (n=102): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, \t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, \t\t\t\t\t\t\t]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, 0, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 2, 'mixed': 1, 'numeric': 6, 'punctuation': 20, 'whitespace': 73}

Strongest intercommunity connections:

- C0 to C2: 1396 token edges; mean cosine 0.132431
- C0 to C1: 1262 token edges; mean cosine 0.124156
- C0 to C5: 919 token edges; mean cosine 0.132664
- C1 to C4: 905 token edges; mean cosine 0.131148
- C0 to C4: 689 token edges; mean cosine 0.132744
- C1 to C2: 574 token edges; mean cosine 0.118376
- C2 to C5: 525 token edges; mean cosine 0.127157
- C1 to C5: 415 token edges; mean cosine 0.124536
- C2 to C7: 382 token edges; mean cosine 0.141689
- C0 to C6: 332 token edges; mean cosine 0.138201
- C2 to C6: 319 token edges; mean cosine 0.135427
- C1 to C3: 274 token edges; mean cosine 0.129710
- C1 to C7: 268 token edges; mean cosine 0.134324
- C2 to C4: 267 token edges; mean cosine 0.128651
- C1 to C6: 252 token edges; mean cosine 0.126085

#### negative_tail

- Nodes: 5344
- Directed 10-NN edges: 53440
- Undirected edges: 38033
- Communities: 9
- Modularity: 0.466221

All communities:

- C0 (n=1064): representatives [\tdes, _done, Air, ␠HEALTH, ROSS, _freq, _rel, (ed, ␠LOG, _fields]; target-extreme [_BUFFER, _ASS, hpp, URRED, _valid, Poss]; classes {'alphabetic': 451, 'mixed': 613}
- C1 (n=987): representatives [🍱, ␠işle, /ayushman, ᶅ, 母校, ␠получа, 攻势, ✽, תושבי, 💨]; target-extreme [�, ⊔, 🉑, ␠حر, เผยแ, אפליק]; classes {'alphabetic': 802, 'mixed': 9, 'punctuation': 176}
- C2 (n=881): representatives [␠manuscripts, ␠insecurity, ␠fodder, area, Hugh, אני, ␠unpredictable, тверж, ␠preached, 戏曲]; target-extreme [Hôtel, ␠Giul, ␠ancestral, ␠ciné, ␠Juli, ␠Romero]; classes {'alphabetic': 867, 'mixed': 13, 'punctuation': 1}
- C3 (n=785): representatives [а, ์, ing, ␠ס, e, �, è, ␠Ав, ე, es]; target-extreme [␠of, _of, ␠OF, ّ, of, ␠alf]; classes {'alphabetic': 622, 'mixed': 39, 'punctuation': 124}
- C4 (n=604): representatives [GeneratedValue, .destroyAllWindows, профессиона, .setBackgroundResource, ␠WPARAM, /filepath, MeshPro, ␠referencedColumnName, ␠GUIStyle, NSSet]; target-extreme [␠^{\n, /banner, _SECONDS, ␠epub, .bukkit, .Framework]; classes {'alphabetic': 277, 'mixed': 256, 'punctuation': 71}
- C5 (n=456): representatives [创新, 诠释, ␠эффектив, 提升, مناسبة, ␠reviews, 体, 水, 研究, ␠enjoyable]; target-extreme [收集, �, 提升, 盧, 天府, 传]; classes {'alphabetic': 449, 'mixed': 6, 'punctuation': 1}
- C6 (n=384): representatives [efully, ␠بلا, 最常见的, ␠vielleicht, ␠wholly, からの, ␠medically, ␠excessively, 真的很, ␠새로]; target-extreme [␠succès, ␠még, ␠Wenn, ␠쉽게, ␠plainly, ␠På]; classes {'alphabetic': 367, 'mixed': 17}
- C7 (n=138): representatives [תחילת, ␠Showing, ␠Running, ␠promising, generate, ␠Ends, ␠Tells, ␠unpack, ␠breaks, ␠Removing]; target-extreme [Compatible, Introduced, zeigt, ␠Tried, leting, תחילת]; classes {'alphabetic': 125, 'mixed': 13}
- C8 (n=45): representatives [␠médec, ␠dém, דוגמה, ␠cré, ␠меди, ␠Méd, ␠géné, ␠méth, ␠prés, ␠rés]; target-extreme [␠gén, ␠géné, ␠пример, EXAMPLE, ␠epid, ␠örnek]; classes {'alphabetic': 43, 'mixed': 2}

Strongest intercommunity connections:

- C0 to C2: 1382 token edges; mean cosine 0.128639
- C1 to C2: 1149 token edges; mean cosine 0.132563
- C1 to C4: 1125 token edges; mean cosine 0.131483
- C1 to C3: 1101 token edges; mean cosine 0.135496
- C0 to C4: 1068 token edges; mean cosine 0.123145
- C1 to C5: 728 token edges; mean cosine 0.129187
- C2 to C3: 620 token edges; mean cosine 0.126874
- C2 to C5: 606 token edges; mean cosine 0.127727
- C0 to C3: 596 token edges; mean cosine 0.128493
- C0 to C1: 561 token edges; mean cosine 0.125894
- C1 to C6: 556 token edges; mean cosine 0.132065
- C2 to C6: 539 token edges; mean cosine 0.132348
- C2 to C4: 508 token edges; mean cosine 0.125806
- C3 to C5: 426 token edges; mean cosine 0.128457
- C3 to C6: 393 token edges; mean cosine 0.130621

## State 09 — block_8_output

Paired positive_head: membership Jaccard 0.812068; edge Jaccard 0.610712; shared tokens 5168.
Paired negative_tail: membership Jaccard 0.837296; edge Jaccard 0.662820; shared tokens 4719.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5336
- Directed 10-NN edges: 53360
- Undirected edges: 37558
- Communities: 10
- Modularity: 0.570124

All communities:

- C0 (n=950): representatives [␠kitchen, ␠apartment, 业内人士, ␠misinformation, ␠laser, ␠negotiations, 卧室, ␠participants, Participants, ␠shark]; target-extreme [쟙, ␠street, ␠categorical, ␠Starbucks, ␠intervention, ␠услуги]; classes {'alphabetic': 900, 'mixed': 50}
- C1 (n=930): representatives [son, ley, ors, ys, inger, ются, ok, ton, ster, ают]; target-extreme [uplicates, kes, oints, orted, kas, station]; classes {'alphabetic': 916, 'mixed': 10, 'numeric': 2, 'punctuation': 2}
- C2 (n=862): representatives [룁, .getOrElse, ␠openFileDialog, 痦, dzić, 签约仪式, .tableLayoutPanel, .DropDownStyle, ␠kutje, 饻]; target-extreme [overwrite, .DropDownStyle, ␠goalkeeper, ␠dazz, 퓬, inactive]; classes {'alphabetic': 701, 'mixed': 128, 'punctuation': 33}
- C3 (n=781): representatives [␠cracks, ␠soaked, ␠located, ␠valve, ␠stripped, ␠placed, ␠slipped, sticks, ␠throat, ␠stimulated]; target-extreme [␠choke, ainting, ␠shake, ␠brake, ␠knife, ␠instruct]; classes {'alphabetic': 760, 'mixed': 21}
- C4 (n=774): representatives [');\r\n\r\n, ")\r\n, ).\n\n\n\n, "))\r\n, ));\n\n, ');\r\n, ));\r\n\r\n, ]))\r\n, ')\r\n\r\n, ");\r\n\r\n]; target-extreme ["],\n, ␠');\n, ],\n, '),\r\n, ␠')\n, ');\r\n\r\n]; classes {'alphabetic': 4, 'mixed': 20, 'numeric': 2, 'punctuation': 709, 'whitespace': 39}
- C5 (n=425): representatives [してしまう, であれば, をしている, ってしまう, ってしまった, それでも, ␠ולכן, だったので, することは, ␠شيء]; target-extreme [␠please, מסוגל, 定了, ␠�, ␠شيء, 参与到]; classes {'alphabetic': 394, 'mixed': 6, 'punctuation': 25}
- C6 (n=411): representatives [\ttimeout, DA, \tboard, \theight, pm, TC, SA, RS, \tposition, +self]; target-extreme [\tMatrix, ��态, frac, *t, ␠stu, \treset]; classes {'alphabetic': 277, 'mixed': 134}
- C7 (n=82): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t, \telse, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 10, 'mixed': 5, 'numeric': 1, 'punctuation': 3, 'whitespace': 63}
- C8 (n=61): representatives [␠Portsmouth, smouth, ␠Singapore, ␠Buckley, ␠غزة, ␠North, West, ␠Plymouth, Liverpool, ␠Wales]; target-extreme [celona, lington, ␠northeast, North, ␠Orth, ␠Huntington]; classes {'alphabetic': 60, 'mixed': 1}
- C9 (n=60): representatives [ﳈ, ␠don, 𝄴, ␠weren, ␠cuatro, 셢, ␠float, ␠doesn, ␠didn, ␠wasn]; target-extreme [␠didn, 옭, ␠don, March, 깢, 섥]; classes {'alphabetic': 58, 'mixed': 1, 'punctuation': 1}

Strongest intercommunity connections:

- C0 to C3: 1496 token edges; mean cosine 0.132040
- C0 to C2: 1060 token edges; mean cosine 0.124127
- C0 to C1: 1020 token edges; mean cosine 0.127208
- C1 to C3: 782 token edges; mean cosine 0.134623
- C1 to C2: 676 token edges; mean cosine 0.123820
- C2 to C3: 675 token edges; mean cosine 0.125296
- C2 to C5: 569 token edges; mean cosine 0.126223
- C1 to C6: 521 token edges; mean cosine 0.133335
- C0 to C5: 497 token edges; mean cosine 0.129214
- C2 to C6: 441 token edges; mean cosine 0.125862
- C3 to C5: 428 token edges; mean cosine 0.133512
- C1 to C5: 321 token edges; mean cosine 0.131781
- C0 to C6: 304 token edges; mean cosine 0.123188
- C3 to C6: 241 token edges; mean cosine 0.128967
- C2 to C4: 199 token edges; mean cosine 0.126509

#### negative_tail

- Nodes: 5165
- Directed 10-NN edges: 51650
- Undirected edges: 36685
- Communities: 9
- Modularity: 0.472640

All communities:

- C0 (n=1231): representatives [_Settings, _done, Concurrency, Air, ␠RECE, .AR, ␠Running, ␠TEST, ␠TEMP, ␠univers]; target-extreme [_ASS, _BUFFER, .EN, _WR, Introduced, .mock]; classes {'alphabetic': 651, 'mixed': 580}
- C1 (n=1017): representatives [גרסה, ␠RelayCommand, ␠OnCollision, ␠WPARAM, .setBackgroundResource, /ayushman, ᶅ, DidAppear, ␠referencedColumnName, 뗄]; target-extreme [ᑯ, 媪, .ManyToManyField, 上年, .bukkit, �]; classes {'alphabetic': 714, 'mixed': 172, 'punctuation': 131}
- C2 (n=937): representatives [תחילת, コスト, ␠işle, ␠получа, ␠splendid, 攻势, علام, ␠manuscripts, ␠yaygın, 最常见的]; target-extreme [加快, 有效地, 收集, 财税, ␠plainly, 處理]; classes {'alphabetic': 921, 'mixed': 16}
- C3 (n=853): representatives [а, ์, 놐, ␠בהם, ing, ␠ס, ე, ا, ␠trotz, ␠منها]; target-extreme [␠פר, ّ, ː, �, ე, เผยแ]; classes {'alphabetic': 792, 'mixed': 28, 'punctuation': 33}
- C4 (n=411): representatives [אני, Hugh, バリ, area, 金陵, ␠Sandra, ␠Angola, ␠Buddha, ␠Jenna, ␠Zambia]; target-extreme [␠Tex, ␠Giul, ␠الروسي, 天府, 建军, Ali]; classes {'alphabetic': 403, 'mixed': 8}
- C5 (n=351): representatives [✽, 𝑎, 𝐇, ა, ␠​, 𝐀, 𝑨, î, ȃ, ā]; target-extreme [␠alf, ␠È, ␠gén, ␠=&, ª, ὁ]; classes {'alphabetic': 188, 'mixed': 27, 'numeric': 1, 'punctuation': 135}
- C6 (n=302): representatives [�, �, 体, 凡本网注, �, �, ﾞ, �, �, �]; target-extreme [�, 传, �, 盧, �, �]; classes {'alphabetic': 212, 'mixed': 4, 'punctuation': 86}
- C7 (n=48): representatives [␠of, .of, ␠for, for, ␠de, ␠at, of, ␠для, ␠about, ␠For]; target-extreme [␠of, _of, ␠OF, ␠with, ␠Of, ␠for]; classes {'alphabetic': 40, 'mixed': 8}
- C8 (n=15): representatives [.models, (models, =models, .controllers, \models, .Model, \Entity, .Domain, ␠requests, .db]; target-extreme [=models, .controllers, .Model, .models, .bean, .db]; classes {'alphabetic': 1, 'mixed': 14}

Strongest intercommunity connections:

- C0 to C2: 1476 token edges; mean cosine 0.127830
- C0 to C1: 1350 token edges; mean cosine 0.122798
- C1 to C2: 1295 token edges; mean cosine 0.130605
- C2 to C3: 1110 token edges; mean cosine 0.130223
- C1 to C3: 845 token edges; mean cosine 0.129236
- C0 to C3: 778 token edges; mean cosine 0.124240
- C0 to C4: 770 token edges; mean cosine 0.125229
- C3 to C5: 591 token edges; mean cosine 0.146890
- C1 to C5: 588 token edges; mean cosine 0.133927
- C3 to C4: 557 token edges; mean cosine 0.129270
- C2 to C4: 556 token edges; mean cosine 0.127639
- C3 to C6: 506 token edges; mean cosine 0.139264
- C1 to C4: 506 token edges; mean cosine 0.127771
- C2 to C6: 429 token edges; mean cosine 0.131376
- C1 to C6: 316 token edges; mean cosine 0.127188

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6196
- Directed 10-NN edges: 61960
- Undirected edges: 43762
- Communities: 10
- Modularity: 0.573993

All communities:

- C0 (n=1175): representatives [␠kitchen, ␠misinformation, ␠apartment, ␠laser, 卧室, ␠cracks, ␠throat, ␠officer, ␠vaccine, ␠downside]; target-extreme [쟙, ␠choke, ␠street, ␠categorical, ␠Starbucks, ainting]; classes {'alphabetic': 1116, 'mixed': 58, 'punctuation': 1}
- C1 (n=1043): representatives [룁, 业内人士, \ttimeout, .getOrElse, 痦, dzić, ␠openFileDialog, نطق, 嵝, 签约仪式]; target-extreme [.DropDownStyle, ␠ShoppingCart, ␠dazz, 퓬, IsEmpty, 얐]; classes {'alphabetic': 856, 'mixed': 143, 'punctuation': 44}
- C2 (n=993): representatives [son, ys, ley, ors, ments, inger, ine, ok, oy, ster]; target-extreme [oints, uplicates, kes, orted, kas, oods]; classes {'alphabetic': 981, 'mixed': 12}
- C3 (n=821): representatives [');\r\n\r\n, ")\r\n, ));\n\n, "))\r\n, ).\n\n\n\n, ');\r\n, ]))\r\n, ')\r\n\r\n, '}}>, ));\r\n\r\n]; target-extreme ["],\n, ␠');\n, ],\n, '),\r\n, ');\r\n\r\n, ␠')\n]; classes {'alphabetic': 6, 'mixed': 15, 'numeric': 2, 'punctuation': 757, 'whitespace': 41}
- C4 (n=695): representatives [␠participants, ␠negotiations, ␠stripped, ␠think, ␠participation, ␠slipped, ␠sucking, Participants, ␠located, ␠placed]; target-extreme [␠intervention, ␠instruct, ␠Speaking, distinct, inactive, ␠indicative]; classes {'alphabetic': 673, 'mixed': 22}
- C5 (n=691): representatives [してしまう, ают, であれば, をしている, ются, дается, ␠ולכן, 드립니다, ␠لذلك, それでも]; target-extreme [␠please, מסוגל, 参与到, oningen, 定了, ␠شيء]; classes {'alphabetic': 679, 'mixed': 12}
- C6 (n=533): representatives [(indexPath, SA, TS, +self, (dateTime, TD, \theight, \tboard, pm, DA]; target-extreme [overwrite, frac, *t, ␠услуги, \tMatrix, \treset]; classes {'alphabetic': 334, 'mixed': 194, 'punctuation': 5}
- C7 (n=105): representatives [ﳈ, ␠don, ␠�, ␠�, 𝄴, ␠�, ␠�, ␠long, ␠�, ␠�]; target-extreme [␠�, ␠didn, 깢, ␠don, ␠�, 옭]; classes {'alphabetic': 77, 'mixed': 1, 'punctuation': 27}
- C8 (n=74): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t\t\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, 0]; classes {'alphabetic': 3, 'mixed': 1, 'numeric': 3, 'punctuation': 4, 'whitespace': 63}
- C9 (n=66): representatives [␠Portsmouth, smouth, ␠Stuttgart, ␠Buckley, 洛杉矶, Liverpool, ␠Singapore, ␠Ikea, ␠Wilmington, 谷歌]; target-extreme [␠Gates, lington, celona, ␠Huntington, Scotland, ␠ASE]; classes {'alphabetic': 66}

Strongest intercommunity connections:

- C0 to C4: 1482 token edges; mean cosine 0.138207
- C0 to C2: 1343 token edges; mean cosine 0.133332
- C0 to C1: 1108 token edges; mean cosine 0.125330
- C1 to C5: 1005 token edges; mean cosine 0.131500
- C2 to C5: 655 token edges; mean cosine 0.136801
- C1 to C4: 651 token edges; mean cosine 0.129256
- C2 to C4: 629 token edges; mean cosine 0.135157
- C0 to C5: 628 token edges; mean cosine 0.128156
- C1 to C2: 603 token edges; mean cosine 0.123096
- C1 to C6: 595 token edges; mean cosine 0.127826
- C2 to C6: 572 token edges; mean cosine 0.135487
- C4 to C5: 565 token edges; mean cosine 0.136119
- C0 to C6: 509 token edges; mean cosine 0.128976
- C1 to C3: 223 token edges; mean cosine 0.133409
- C4 to C6: 223 token edges; mean cosine 0.129127

#### negative_tail

- Nodes: 5190
- Directed 10-NN edges: 51900
- Undirected edges: 36667
- Communities: 9
- Modularity: 0.474925

All communities:

- C0 (n=1224): representatives [גרסה, תחילת, コスト, _done, Air, ␠manuscripts, Concurrency, area, ␠Running, ␠TEMP]; target-extreme [_BUFFER, _ASS, ␠Tried, .EN, _WR, ␠TEMP]; classes {'alphabetic': 608, 'mixed': 616}
- C1 (n=1001): representatives [␠RelayCommand, ␠işle, ␠WPARAM, ␠OnCollision, /ayushman, .setBackgroundResource, ✽, ᶅ, ␠yaygın, SectionsIn]; target-extreme [เผยแ, ᑯ, 媪, .ManyToManyField, .bukkit, �]; classes {'alphabetic': 722, 'mixed': 133, 'punctuation': 146}
- C2 (n=675): representatives [攻势, 最常见的, ␠rapid, からの, ␠fodder, ␠wholly, 创新, 诠释, 艰辛, 多地]; target-extreme [加快, 收集, 有效地, 财税, ␠plainly, 處理]; classes {'alphabetic': 651, 'mixed': 22, 'punctuation': 2}
- C3 (n=664): representatives [์, エネ, �, 凡本网注, �, �, �, �, ﾞ, ี]; target-extreme [�, 传, �, �, 번, 盧]; classes {'alphabetic': 562, 'mixed': 14, 'punctuation': 88}
- C4 (n=453): representatives [Hugh, אני, ␠Sandra, 金陵, ␠Buddha, ␠Jenna, ␠Angola, zano, ␠Manning, ␠Giul]; target-extreme [␠Tex, ␠Giul, ␠Kara, 天府, ␠الروسي, ␠район]; classes {'alphabetic': 445, 'mixed': 7, 'punctuation': 1}
- C5 (n=403): representatives [␠بلا, バリ, ␠בהם, ␠vielleicht, ␠ס, ␠각종, 伊利, ␠בדרך, ␠בגלל, ␠практичес]; target-extreme [␠פר, ␠alf, ␠الز, ␠Wenn, ␠ט, ␠Ра]; classes {'alphabetic': 394, 'mixed': 5, 'punctuation': 4}
- C6 (n=399): representatives [а, 놐, 𝑎, ე, ␠ciné, ing, 𝑨, ا, и, ა]; target-extreme [ّ, ː, \xff, ␠È, ე, Hôtel]; classes {'alphabetic': 358, 'mixed': 14, 'numeric': 1, 'punctuation': 26}
- C7 (n=243): representatives [␠of, ␠​, (":/, ␠[&, ／, =<?=$, ´, ="<?=$, ={`/, ˆ]; target-extreme [␠of, _of, ␠with, ␠OF, ␠Of, ␠to]; classes {'alphabetic': 80, 'mixed': 32, 'punctuation': 131}
- C8 (n=128): representatives [علام, صحف, ␠univers, 戏曲, ␠communic, ␠преж, ␠حر, ␠immedi, حف, طائر]; target-extreme [␠حر, ␠продук, ␠announc, ␠вой, ビジ, ␠advoc]; classes {'alphabetic': 125, 'mixed': 3}

Strongest intercommunity connections:

- C0 to C1: 1270 token edges; mean cosine 0.123256
- C0 to C2: 1085 token edges; mean cosine 0.124410
- C1 to C2: 837 token edges; mean cosine 0.128031
- C0 to C4: 787 token edges; mean cosine 0.123572
- C2 to C3: 738 token edges; mean cosine 0.129228
- C1 to C3: 658 token edges; mean cosine 0.127663
- C1 to C5: 560 token edges; mean cosine 0.130224
- C3 to C6: 554 token edges; mean cosine 0.143935
- C0 to C3: 516 token edges; mean cosine 0.123460
- C3 to C5: 492 token edges; mean cosine 0.134294
- C0 to C5: 485 token edges; mean cosine 0.126664
- C1 to C6: 477 token edges; mean cosine 0.135287
- C2 to C5: 467 token edges; mean cosine 0.129400
- C1 to C4: 456 token edges; mean cosine 0.127639
- C2 to C4: 409 token edges; mean cosine 0.125134

## State 10 — block_9_output

Paired positive_head: membership Jaccard 0.845058; edge Jaccard 0.671195; shared tokens 4925.
Paired negative_tail: membership Jaccard 0.830908; edge Jaccard 0.654721; shared tokens 4796.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5377
- Directed 10-NN edges: 53770
- Undirected edges: 38270
- Communities: 10
- Modularity: 0.564845

All communities:

- C0 (n=1064): representatives [ments, ik, son, ap, ak, ine, ter, ains, ington, ton]; target-extreme [IVE, oints, ewn, arf, став, kes]; classes {'alphabetic': 1039, 'mixed': 22, 'numeric': 1, 'punctuation': 2}
- C1 (n=956): representatives [떘, .EditorButton, 룁, .getOrElse, .urlencoded, ␠openFileDialog, ␠CGRectMake, 卧室, .localScale, ␠AssemblyProduct]; target-extreme [屉, ␠ShoppingCart, ␠קישורים, ␠reun, inactive, ␠зарегистри]; classes {'alphabetic': 780, 'mixed': 147, 'punctuation': 29}
- C2 (n=784): representatives [␠kitchen, ␠stripped, ␠apartment, ␠cracks, ␠сообщил, ␠sit, ␠placed, \twrite, ␠slipped, ␠refrigerator]; target-extreme [overwrite, ␠street, ␠trenches, ␠knife, ␠choke, ainting]; classes {'alphabetic': 756, 'mixed': 28}
- C3 (n=766): representatives [');\r\n\r\n, "))\r\n, ).\n\n\n\n, ));\n\n, ");\r\n, ")\r\n, ])\r\n, ))\r\n, '\r\n, ')\r\n\r\n]; target-extreme [],\n, ␠')\n, ␠'';\r\n, "],\n, ␠');\n, ],\r\n]; classes {'alphabetic': 19, 'mixed': 17, 'punctuation': 716, 'whitespace': 14}
- C4 (n=648): representatives [业内人士, ␠المواطنين, rarian, ␠participation, ␠الأخرى, ␠coordinates, ␠jurisdiction, intendent, 学生们, إجراءات]; target-extreme [␠intervention, _barang, osphate, ␠lieutenant, ␠Starbucks, plaint]; classes {'alphabetic': 628, 'mixed': 19, 'punctuation': 1}
- C5 (n=369): representatives [することは, 드립니다, それでも, ␠�, ってしまう, になると, ですので, ␠�, の中で, してしまう]; target-extreme [定了, ␠please, ␠incarcerated, ␠�, 特意, ␠�]; classes {'alphabetic': 334, 'mixed': 3, 'punctuation': 32}
- C6 (n=328): representatives [\ttimeout, SA, CP, TS, pd, MD, \theight, NBC, getWidth, MT]; target-extreme [/items, \tMatrix, cmb, \twidth, PN, \tsetTimeout]; classes {'alphabetic': 245, 'mixed': 83}
- C7 (n=285): representatives [ются, ают, дается, aría, ались, ивают, ции, 願意, ␠شيء, цию]; target-extreme [␠entrar, מסוגל, عون, кладыва, ␠לעמוד, דים]; classes {'alphabetic': 283, 'numeric': 1, 'punctuation': 1}
- C8 (n=90): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠, ␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠\n]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, -----------\n, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠\t]; classes {'alphabetic': 3, 'punctuation': 21, 'whitespace': 66}
- C9 (n=87): representatives [␠Portsmouth, smouth, ␠Montgomery, ␠Stuttgart, ␠العراقي, ␠Arlington, ␠Singapore, ␠Huntington, ␠Wilmington, ␠Yellowstone]; target-extreme [␠northeast, 쟙, oningen, xford, orth, ␠North]; classes {'alphabetic': 86, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C2: 1072 token edges; mean cosine 0.133144
- C2 to C4: 1031 token edges; mean cosine 0.129846
- C0 to C4: 887 token edges; mean cosine 0.124715
- C1 to C4: 846 token edges; mean cosine 0.123829
- C1 to C2: 789 token edges; mean cosine 0.125361
- C0 to C1: 772 token edges; mean cosine 0.119540
- C0 to C7: 615 token edges; mean cosine 0.136573
- C0 to C6: 553 token edges; mean cosine 0.130878
- C1 to C6: 398 token edges; mean cosine 0.127258
- C2 to C5: 382 token edges; mean cosine 0.132707
- C1 to C5: 372 token edges; mean cosine 0.125151
- C4 to C5: 346 token edges; mean cosine 0.130063
- C1 to C7: 344 token edges; mean cosine 0.124190
- C4 to C7: 333 token edges; mean cosine 0.128000
- C5 to C7: 285 token edges; mean cosine 0.132825

#### negative_tail

- Nodes: 5078
- Directed 10-NN edges: 50780
- Undirected edges: 35978
- Communities: 10
- Modularity: 0.463510

All communities:

- C0 (n=1292): representatives [␠получа, ␠Showing, _Settings, Companies, _done, Concurrency, ␠preached, ␠promising, ␠rapid, Air]; target-extreme [處理, Introduced, -cond, -prom, /banner, ␠TEMP]; classes {'alphabetic': 755, 'mixed': 536, 'punctuation': 1}
- C1 (n=1023): representatives [␠RelayCommand, תחילת, ␠işle, ␠WPARAM, 攻势, ✽, 母校, 뗄, ᶅ, .setBackgroundResource]; target-extreme [␠még, 建军, ␠alanı, 🉑, ␠yoğun, .bukkit]; classes {'alphabetic': 775, 'mixed': 105, 'punctuation': 143}
- C2 (n=667): representatives [Hugh, 퓼, ␠Xperia, ␠Ski, Jimmy, ␠Ав, ␠Jenna, ␠Sandra, ␠авг, انيا]; target-extreme [␠Farm, Ali, ␠Romero, 摩托, Hôtel, ␠vodka]; classes {'alphabetic': 639, 'mixed': 28}
- C3 (n=573): representatives [创新, 艰辛, 热议, 诠释, �, 提升, 创意, 研发, مناسبة, 体]; target-extreme [上年, 纺织, ␠lửa, 净, 庄, ␠kiện]; classes {'alphabetic': 539, 'mixed': 15, 'punctuation': 19}
- C4 (n=560): representatives [からの, ␠일이, ␠بلا, 真的很, 最常见的, ␠ס, ␠hầu, ␠الاحت, ␠sistemas, ␠succès]; target-extreme [␠الز, ␠פר, 第七届, ␠theres, ␠succès, ␠семь]; classes {'alphabetic': 535, 'mixed': 21, 'numeric': 1, 'punctuation': 3}
- C5 (n=441): representatives [𝐈, а, 𝑎, ์, バリ, 𝑖, モ, 𝐀, и, у]; target-extreme [�, �, �, �, ّ, ्�]; classes {'alphabetic': 274, 'mixed': 8, 'numeric': 1, 'punctuation': 157, 'whitespace': 1}
- C6 (n=288): representatives [␠[[], (template, (ed, (run, (seq, <Props, ␠(~, (Local, (Op, "><?=$]; target-extreme [:YES, Test, ,eg, ␠%=, ={(), (void]; classes {'alphabetic': 31, 'mixed': 193, 'punctuation': 64}
- C7 (n=94): representatives [␠univers, ␠immedi, ␠compar, ␠phenomen, ␠atmos, ␠Ult, ␠spont, ␠pne, ␠communic, ␠summar]; target-extreme [␠продук, .scenes, ␠lingu, ␠immedi, ␠univers, ␠slic]; classes {'alphabetic': 91, 'mixed': 3}
- C8 (n=74): representatives [␠of, (of, ␠for, for, 的, ␠About, ␠about, ␠For, Of, _of]; target-extreme [␠of, ␠with, ␠OF, _of, ␠for, ␠Of]; classes {'alphabetic': 56, 'mixed': 17, 'punctuation': 1}
- C9 (n=66): representatives [efully, ␠excessively, ␠bodily, ␠massively, ␠extensively, ␠verbally, ␠huge, 急速, ␠physical, ␠Essential]; target-extreme [有效地, ␠correctamente, 肉体, Mass, ␠plainly, 过度]; classes {'alphabetic': 62, 'mixed': 4}

Strongest intercommunity connections:

- C0 to C1: 1246 token edges; mean cosine 0.126557
- C0 to C2: 1221 token edges; mean cosine 0.127928
- C0 to C3: 988 token edges; mean cosine 0.129068
- C1 to C3: 887 token edges; mean cosine 0.128098
- C1 to C4: 886 token edges; mean cosine 0.133120
- C0 to C4: 817 token edges; mean cosine 0.128380
- C1 to C2: 709 token edges; mean cosine 0.129201
- C0 to C6: 668 token edges; mean cosine 0.128026
- C3 to C4: 635 token edges; mean cosine 0.126333
- C1 to C5: 570 token edges; mean cosine 0.136531
- C2 to C4: 528 token edges; mean cosine 0.128265
- C2 to C3: 479 token edges; mean cosine 0.125002
- C4 to C5: 379 token edges; mean cosine 0.133320
- C1 to C6: 378 token edges; mean cosine 0.127829
- C3 to C5: 333 token edges; mean cosine 0.126318

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5376
- Directed 10-NN edges: 53760
- Undirected edges: 38244
- Communities: 11
- Modularity: 0.576937

All communities:

- C0 (n=918): representatives [son, ments, ik, ine, ter, ains, ley, <tool_call>, ide, ok]; target-extreme [oints, arf, IVE, ewn, став, ourses]; classes {'alphabetic': 909, 'mixed': 7, 'numeric': 1, 'punctuation': 1}
- C1 (n=783): representatives [');\r\n\r\n, ")\r\n, ).\n\n\n\n, ));\n\n, "))\r\n, ");\r\n, ')\r\n\r\n, ));\r\n, ')\r\n, ])\r\n]; target-extreme [␠')\n, ],\n, "],\n, ␠');\n, ␠'';\r\n, ],\r\n]; classes {'alphabetic': 8, 'mixed': 28, 'punctuation': 733, 'whitespace': 14}
- C2 (n=776): representatives [ются, 业内人士, ают, ␠المواطنين, дается, ались, 드립니다, ␠الجميع, ␠الأخرى, してしまう]; target-extreme [定了, _barang, ␠incarcerated, ␠please, מסוגל, ␠entrar]; classes {'alphabetic': 767, 'mixed': 8, 'punctuation': 1}
- C3 (n=694): representatives [␠participation, ␠placed, ␠stripped, ␠jurisdiction, ␠overl, ␠slipped, ␠scratched, ␠frame, ␠unsett, ␠stimulated]; target-extreme [overwrite, ␠intervention, ␠choke, ainting, ␠instruct, ␠bargain]; classes {'alphabetic': 679, 'mixed': 15}
- C4 (n=665): representatives [떘, pushViewController, .urlencoded, .getOrElse, ␠CGRectMake, \ttimeout, ␠openFileDialog, .localScale, ␠AssemblyProduct, .eulerAngles]; target-extreme [␠ShoppingCart, \tMatrix, ␠loadData, fontsize, inactive, onedDateTime]; classes {'alphabetic': 501, 'mixed': 162, 'punctuation': 2}
- C5 (n=616): representatives [␠kitchen, 卧室, ␠apartment, ␠cracks, istrates, rarian, ␠cupboard, ␠coordinates, ␠policymakers, intendent]; target-extreme [␠street, ␠trenches, ␠lieutenant, osphate, ␠Starbucks, 쟙]; classes {'alphabetic': 583, 'mixed': 31, 'punctuation': 2}
- C6 (n=484): representatives [.EditorButton, 룁, 턔, 嵝, 圙, ␠kutje, ␠zobowią, ␠нагрузк, 돠, 聍]; target-extreme [屉, ␠קישורים, oningen, ␠reun, ␠зарегистри, 卧]; classes {'alphabetic': 445, 'mixed': 16, 'punctuation': 23}
- C7 (n=181): representatives [CP, pm, MD, NBC, pd, MB, MT, HT, TC, TL]; target-extreme [/T, PN, cmb, ␠CFR, xDA, KB]; classes {'alphabetic': 131, 'mixed': 49, 'punctuation': 1}
- C8 (n=119): representatives [␠Portsmouth, ington, ␠Wellington, stein, smouth, kinson, ␠Stuttgart, ␠Mitchell, instein, ␠Montgomery]; target-extreme [lington, ␠northeast, leston, orth, ␠northeastern, xford]; classes {'alphabetic': 119}
- C9 (n=94): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [-----------\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, 0, ␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠]; classes {'alphabetic': 3, 'numeric': 1, 'punctuation': 22, 'whitespace': 68}
- C10 (n=46): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠和, ␠�]; target-extreme [␠�, ␠�, ␠�, ␠�, ␠�, ␠商品]; classes {'alphabetic': 16, 'punctuation': 30}

Strongest intercommunity connections:

- C3 to C5: 948 token edges; mean cosine 0.132829
- C0 to C5: 751 token edges; mean cosine 0.126013
- C0 to C3: 739 token edges; mean cosine 0.131148
- C0 to C2: 734 token edges; mean cosine 0.132591
- C2 to C6: 676 token edges; mean cosine 0.128245
- C4 to C6: 657 token edges; mean cosine 0.126754
- C2 to C5: 641 token edges; mean cosine 0.129289
- C2 to C3: 634 token edges; mean cosine 0.131186
- C4 to C5: 519 token edges; mean cosine 0.120943
- C0 to C4: 500 token edges; mean cosine 0.121978
- C2 to C4: 479 token edges; mean cosine 0.123121
- C3 to C4: 449 token edges; mean cosine 0.126408
- C5 to C6: 348 token edges; mean cosine 0.122618
- C0 to C7: 340 token edges; mean cosine 0.133963
- C0 to C6: 327 token edges; mean cosine 0.120328

#### negative_tail

- Nodes: 5490
- Directed 10-NN edges: 54900
- Undirected edges: 38779
- Communities: 10
- Modularity: 0.459333

All communities:

- C0 (n=1138): representatives [תחילת, ␠işle, ␠RelayCommand, ␠WPARAM, ✽, 攻势, 母校, ﯭ, 뗄, ␠GUIStyle]; target-extreme [建军, 🉑, .bukkit, 摩托, ␠gı, ␠ApplicationController]; classes {'alphabetic': 840, 'mixed': 160, 'punctuation': 138}
- C1 (n=1067): representatives [␠Showing, _done, _Settings, Concurrency, (template, ␠preached, ROSS, ␠Running, (ed, _through]; target-extreme [Introduced, -cond, /banner, PROCESS, -prom, ␠alanı]; classes {'alphabetic': 456, 'mixed': 611}
- C2 (n=961): representatives [Air, 퓼, ␠compar, ␠aplic, ␠Ski, Hugh, אני, ␠авг, ␠univers, ␠liber]; target-extreme [␠Farm, ␠Tried, ␠Romero, ␠TEMP, Hôtel, ␠vodka]; classes {'alphabetic': 882, 'mixed': 78, 'punctuation': 1}
- C3 (n=594): representatives [efully, ␠terrible, 创新, ␠promising, ␠insecurity, ␠rapid, 提升, ␠immedi, ␠rigor, ␠recurrent]; target-extreme [處理, 纺织, 宣告, 敏捷, 重心, ␠correctamente]; classes {'alphabetic': 553, 'mixed': 41}
- C4 (n=503): representatives [𝐈, а, バリ, ␠ס, 𝑎, ␠of, ์, и, ностью, 𝑖]; target-extreme [␠of, _of, ␠with, ␠OF, �, ␠for]; classes {'alphabetic': 391, 'mixed': 30, 'numeric': 1, 'punctuation': 81}
- C5 (n=470): representatives [␠получа, ␠بلا, からの, ␠일이, 最常见的, 真的很, ␠без, 全球最大, ␠새로, مناسبة]; target-extreme [上年, ␠theres, 第七届, ␠семь, ␠kiện, ␠بلا]; classes {'alphabetic': 460, 'mixed': 8, 'numeric': 1, 'punctuation': 1}
- C6 (n=241): representatives [␠[[], ␠[&, <Props, ␠//!<, ◇, ’, ␠(~, =<?=$, ――, ´]; target-extreme [⊔, ␠=&, :YES, ={(), ␠%=, ª]; classes {'alphabetic': 20, 'mixed': 53, 'punctuation': 168}
- C7 (n=228): representatives [網絡, �, �, _web, 体, -network, 网络, \tnet, 樱花, 新]; target-extreme [␠lửa, 净, 매, 庄, 盧, 夏]; classes {'alphabetic': 189, 'mixed': 13, 'punctuation': 26}
- C8 (n=213): representatives [Companies, Processes, 戏曲, area, ␠ciné, 灾区, 禁区, -commerce, ␠successes, ␠sistemas]; target-extreme [␠succès, _success, Modes, ␠jogador, ␠velocidad, ␠clientes]; classes {'alphabetic': 198, 'mixed': 15}
- C9 (n=75): representatives [Ê, è, î, ␠É, ␠cré, Â, éné, ást, ␠é, ␠géné]; target-extreme [␠még, ␠quê, ␠È, ␠sû, ␠géné, ␠gén]; classes {'alphabetic': 75}

Strongest intercommunity connections:

- C1 to C2: 1670 token edges; mean cosine 0.126422
- C0 to C1: 1114 token edges; mean cosine 0.122897
- C1 to C3: 999 token edges; mean cosine 0.126541
- C0 to C2: 998 token edges; mean cosine 0.129745
- C0 to C3: 841 token edges; mean cosine 0.129296
- C2 to C3: 773 token edges; mean cosine 0.130357
- C0 to C5: 751 token edges; mean cosine 0.132009
- C0 to C4: 589 token edges; mean cosine 0.135292
- C3 to C5: 518 token edges; mean cosine 0.130544
- C2 to C5: 417 token edges; mean cosine 0.128571
- C1 to C5: 416 token edges; mean cosine 0.126266
- C2 to C4: 395 token edges; mean cosine 0.129946
- C2 to C8: 393 token edges; mean cosine 0.131246
- C1 to C8: 391 token edges; mean cosine 0.128091
- C4 to C5: 386 token edges; mean cosine 0.134463

## State 11 — block_10_output

Paired positive_head: membership Jaccard 0.824155; edge Jaccard 0.629197; shared tokens 5193.
Paired negative_tail: membership Jaccard 0.837786; edge Jaccard 0.662709; shared tokens 5206.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6103
- Directed 10-NN edges: 61030
- Undirected edges: 43240
- Communities: 9
- Modularity: 0.559891

All communities:

- C0 (n=1335): representatives [pushViewController, .getOrElse, ␠spriteBatch, ␠hashtable, ␠openFileDialog, ␠CGRectMake, ␠açıklama, INFRINGEMENT, .NumericUpDown, .DropDownList]; target-extreme [␠לעמוד, cmb, 码头, primaryKey, .tableLayoutPanel, .arange]; classes {'alphabetic': 1095, 'mixed': 212, 'numeric': 1, 'punctuation': 27}
- C1 (n=1174): representatives [␠write, ␠participants, ␠placed, ␠report, ␠written, ␠left, ␠water, ␠characteristic, 建議, ␠house]; target-extreme [overwrite, ␠intervention, ␠street, ␠lieutenant, ␠trenches, ␠knife]; classes {'alphabetic': 1116, 'mixed': 57, 'punctuation': 1}
- C2 (n=984): representatives [业内人士, ются, ают, вать, 說話, дается, ывают, ido, ␠think, ивают]; target-extreme [定了, ␠القرار, عون, ␠לדעת, wish, ␠please]; classes {'alphabetic': 966, 'mixed': 17, 'punctuation': 1}
- C3 (n=926): representatives [ak, ik, pe, son, ments, ton, ley, ire, ok, ait]; target-extreme [arf, kes, IVE, 옭, ewn, gregate]; classes {'alphabetic': 914, 'mixed': 10, 'numeric': 1, 'punctuation': 1}
- C4 (n=868): representatives [');\r\n\r\n, ));\n\n, ]))\r\n, "))\r\n, ).\n\n\n\n, ");\r\n, ));\n, ")\r\n, ));\r\n\r\n, }\n\n\n]; target-extreme []);\r\n\r\n, ␠'';\r\n, ␠')\n, ␠');\n, (',');\n, ␠{};\n]; classes {'alphabetic': 7, 'mixed': 4, 'punctuation': 843, 'whitespace': 14}
- C5 (n=430): representatives [CP, \tboard, (dateTime, PM, ,k, PN, ␠rp, (self, GS, SA]; target-extreme [\twidth, PN, *k, ␠CFR, /T, mc]; classes {'alphabetic': 294, 'mixed': 135, 'punctuation': 1}
- C6 (n=197): representatives [떘, ␠Portsmouth, smouth, ington, داعش, sticks, ␠thermostat, ␠Palestinians, ␠North, ␠غزة]; target-extreme [lington, 쟙, ␠Alban, ␠North, orth, ␠gps]; classes {'alphabetic': 193, 'mixed': 4}
- C7 (n=119): representatives [\t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, -------------\n]; target-extreme [␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠\r\n, -----------\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\n]; classes {'alphabetic': 6, 'punctuation': 36, 'whitespace': 77}
- C8 (n=70): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠实]; target-extreme [␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; classes {'alphabetic': 34, 'mixed': 2, 'punctuation': 34}

Strongest intercommunity connections:

- C0 to C1: 1777 token edges; mean cosine 0.124290
- C0 to C2: 1640 token edges; mean cosine 0.126764
- C1 to C2: 1387 token edges; mean cosine 0.131238
- C1 to C3: 1301 token edges; mean cosine 0.129597
- C2 to C3: 918 token edges; mean cosine 0.136951
- C0 to C3: 830 token edges; mean cosine 0.118492
- C3 to C5: 603 token edges; mean cosine 0.132359
- C0 to C5: 512 token edges; mean cosine 0.125636
- C1 to C6: 385 token edges; mean cosine 0.126465
- C0 to C6: 363 token edges; mean cosine 0.125989
- C1 to C5: 342 token edges; mean cosine 0.131620
- C3 to C6: 300 token edges; mean cosine 0.128157
- C0 to C4: 249 token edges; mean cosine 0.122836
- C2 to C4: 184 token edges; mean cosine 0.137376
- C2 to C6: 184 token edges; mean cosine 0.129007

#### negative_tail

- Nodes: 5727
- Directed 10-NN edges: 57270
- Undirected edges: 41161
- Communities: 10
- Modularity: 0.472014

All communities:

- C0 (n=1257): representatives [גרסה, ␠plethora, ␠apparel, _done, 攻势, Air, ␠Running, Companies, ␠preached, area]; target-extreme [處理, ␠Ride, .settings, -catching, 上年, ␠Farm]; classes {'alphabetic': 1009, 'mixed': 248}
- C1 (n=1025): representatives [.destroyAllWindows, ␠işle, ご�, 흣, ␠WPARAM, 🉑, DidAppear, ␠OnCollision, ✽, 𝐈]; target-extreme [🉑, ﱈ, 떴, ␠HttpServletResponse, _drvdata, 휭]; classes {'alphabetic': 744, 'mixed': 111, 'punctuation': 170}
- C2 (n=879): representatives [␠Lauren, ␠AHL, ␠Cameroon, ␠Xperia, ␠aplic, ␠HALF, ␠Aur, ␠Herr, ␠FIFA, ROSS]; target-extreme [␠Giul, ␠ARRAY, amura, 建军, 库里, ␠Meadows]; classes {'alphabetic': 857, 'mixed': 22}
- C3 (n=854): representatives [𬭶, ␠Showing, _RESET, .AR, ␠reloading, ␠TEST, -loaded, Dragging, (template, (ed]; target-extreme [_LOAD, -cond, ␠TEMP, :YES, ␠Relevant, -prom]; classes {'alphabetic': 315, 'mixed': 528, 'punctuation': 11}
- C4 (n=764): representatives [תחילת, efully, ␠terrible, 最常见的, ␠получа, ␠بلا, ␠일이, אני, 땐, からの]; target-extreme [␠még, 年之, -full, ␠بلا, ␠maior, 매]; classes {'alphabetic': 729, 'mixed': 33, 'numeric': 1, 'punctuation': 1}
- C5 (n=623): representatives [バリ, а, ​, 𝑖, 𝑎, e, ing, ์, �, ס]; target-extreme [�, �, �, �, ّ, �]; classes {'alphabetic': 464, 'mixed': 15, 'numeric': 1, 'punctuation': 142, 'whitespace': 1}
- C6 (n=122): representatives [提升, ␠losing, ␠Decre, 深入推进, ␠boosts, 显现, 加持, 全国, ␠Increase, -associated]; target-extreme [␠활용, 保证, 全面落实, ␠absent, ⽐, 提升]; classes {'alphabetic': 111, 'mixed': 10, 'punctuation': 1}
- C7 (n=100): representatives [=?",, ␠~/., =<?=$, ={`/, #{@, ','=',$, ="<?=$, ␠//!<, (":/, ␠"~/]; target-extreme [␠=&, ␠%=, #endregion, ={({, \tPy, ={()]; classes {'alphabetic': 3, 'mixed': 7, 'punctuation': 90}
- C8 (n=83): representatives [␠of, [OF, Of, 的, ␠For, ␠about, of, for, _of, ␠Of]; target-extreme [␠of, ␠for, _of, ␠with, ␠Of, ␠OF]; classes {'alphabetic': 61, 'mixed': 21, 'punctuation': 1}
- C9 (n=20): representatives [網絡, -network, 网络, \tnet, ネット, ␠networking, _net, NETWORK, 網路, ␠internet]; target-extreme [净, ネット, ␠networking, 絡, ␠сет, 联网]; classes {'alphabetic': 18, 'mixed': 2}

Strongest intercommunity connections:

- C0 to C3: 1834 token edges; mean cosine 0.128321
- C0 to C2: 1506 token edges; mean cosine 0.132555
- C0 to C4: 1223 token edges; mean cosine 0.132979
- C0 to C1: 1075 token edges; mean cosine 0.129518
- C2 to C3: 951 token edges; mean cosine 0.129139
- C1 to C4: 890 token edges; mean cosine 0.132178
- C1 to C2: 873 token edges; mean cosine 0.130812
- C1 to C5: 821 token edges; mean cosine 0.138701
- C1 to C3: 739 token edges; mean cosine 0.126525
- C2 to C4: 736 token edges; mean cosine 0.130301
- C4 to C5: 614 token edges; mean cosine 0.135679
- C2 to C5: 539 token edges; mean cosine 0.132651
- C3 to C4: 520 token edges; mean cosine 0.127667
- C0 to C5: 471 token edges; mean cosine 0.129263
- C0 to C6: 337 token edges; mean cosine 0.135184

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5391
- Directed 10-NN edges: 53910
- Undirected edges: 38127
- Communities: 10
- Modularity: 0.564063

All communities:

- C0 (n=1131): representatives [떘, ␠hashtable, 說話, ␠think, ␠participants, \twrite, ␠placed, ␠participant, ␠cracks, ␠policymakers]; target-extreme [overwrite, ␠intervention, ␠street, ␠lieutenant, 码头, ␠trenches]; classes {'alphabetic': 1078, 'mixed': 53}
- C1 (n=913): representatives [业内人士, ются, вать, ␠المواطنين, ments, ido, ывают, ивают, داعش, ようになりました]; target-extreme [␠לעמוד, 定了, ␠القرار, عون, מסוגל, ␠לדעת]; classes {'alphabetic': 891, 'mixed': 18, 'numeric': 1, 'punctuation': 3}
- C2 (n=873): representatives [son, ik, ton, ama, ake, ley, ut, ank, ind, ati]; target-extreme [lington, arf, kes, 옭, inki, IVE]; classes {'alphabetic': 856, 'mixed': 16, 'numeric': 1}
- C3 (n=819): representatives [');\r\n\r\n, ).\n\n\n\n, ));\n\n, ");\r\n, ]))\r\n, ")\r\n, "))\r\n, ));\n, ));\r\n, ')\r\n\r\n]; target-extreme []);\r\n\r\n, ␠')\n, ␠'';\r\n, ␠');\n, (',');\n, ],\r\n]; classes {'alphabetic': 9, 'mixed': 6, 'punctuation': 792, 'whitespace': 12}
- C4 (n=666): representatives [pushViewController, ␠openFileDialog, .getOrElse, ␠spriteBatch, ␠CGRectMake, INFRINGEMENT, ␠IPAddress, strncmp, .NumericUpDown, textbox]; target-extreme [cmb, primaryKey, .tableLayoutPanel, ␠loadData, .arange, ␠קישורים]; classes {'alphabetic': 479, 'mixed': 183, 'punctuation': 4}
- C5 (n=543): representatives [␠açıklama, 潲, ␠kvinn, 卧室, 铏, ␠kutje, ␠предназ, 歃, 돠, ␠предназначен]; target-extreme [␠knife, 퓬, 一对一, 댓, 屉, 謀]; classes {'alphabetic': 517, 'mixed': 6, 'punctuation': 20}
- C6 (n=191): representatives [\tboard, 。（, ,k, \ttable, (od, ␠positions, (std, .(, \twidth, \theight]; target-extreme [\twidth, *k, /T, (pb, ):(, (std]; classes {'alphabetic': 73, 'mixed': 100, 'punctuation': 18}
- C7 (n=118): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, -------------\n]; target-extreme [␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠\n, -----------\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\n]; classes {'alphabetic': 5, 'punctuation': 40, 'whitespace': 73}
- C8 (n=82): representatives [␠Portsmouth, smouth, North, gomery, ␠North, oklyn, Seattle, ␠Washington, ␠Winnipeg, ␠Coat]; target-extreme [쟙, ␠North, emory, ␠northeast, celona, North]; classes {'alphabetic': 80, 'mixed': 2}
- C9 (n=55): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; classes {'alphabetic': 24, 'punctuation': 31}

Strongest intercommunity connections:

- C0 to C1: 1340 token edges; mean cosine 0.129225
- C0 to C2: 1278 token edges; mean cosine 0.126024
- C0 to C4: 938 token edges; mean cosine 0.120242
- C1 to C5: 924 token edges; mean cosine 0.126754
- C1 to C2: 879 token edges; mean cosine 0.130034
- C0 to C5: 832 token edges; mean cosine 0.123069
- C4 to C5: 794 token edges; mean cosine 0.123618
- C1 to C4: 513 token edges; mean cosine 0.122681
- C2 to C4: 441 token edges; mean cosine 0.121950
- C2 to C5: 350 token edges; mean cosine 0.117414
- C0 to C6: 254 token edges; mean cosine 0.134733
- C4 to C6: 245 token edges; mean cosine 0.126972
- C2 to C6: 227 token edges; mean cosine 0.130791
- C1 to C3: 190 token edges; mean cosine 0.127307
- C3 to C4: 171 token edges; mean cosine 0.135215

#### negative_tail

- Nodes: 5693
- Directed 10-NN edges: 56930
- Undirected edges: 40631
- Communities: 9
- Modularity: 0.486544

All communities:

- C0 (n=1049): representatives [𬭶, _done, ␠AHL, area, _runs, _RESET, _Settings, .AR, ROSS, ␠TEST]; target-extreme [-cond, _LOAD, .settings, ␠TEMP, ␠ARRAY, -prom]; classes {'alphabetic': 346, 'mixed': 703}
- C1 (n=976): representatives [גרסה, .destroyAllWindows, /ayushman, ␠WPARAM, ✽, 母校, ご�, 딯, DidAppear, ␠יצ]; target-extreme [🉑, ␠HttpServletResponse, Hôtel, 떴, 휭, ␠imgUrl]; classes {'alphabetic': 723, 'mixed': 103, 'punctuation': 150}
- C2 (n=871): representatives [␠plethora, ␠Cameroon, 攻势, ␠apparel, Air, ␠일이, Companies, ␠rapid, ␠tech, ␠volcano]; target-extreme [處理, 净, ␠Farm, 收集, 敏捷, liquid]; classes {'alphabetic': 847, 'mixed': 23, 'punctuation': 1}
- C3 (n=705): representatives [𝐈, バリ, а, 𝑎, ์, e, 𝑖, ing, ␠ס, es]; target-extreme [�, �, �, �, �, ёр]; classes {'alphabetic': 585, 'mixed': 25, 'numeric': 1, 'punctuation': 93, 'whitespace': 1}
- C4 (n=674): representatives [תחילת, efully, 最常见的, ␠بلا, אני, からの, ␠slightly, 真的很, ␠без, ␠wholly]; target-extreme [␠még, ␠maior, 年之, ␠بلا, 上年, ␠Relevant]; classes {'alphabetic': 659, 'mixed': 13, 'punctuation': 2}
- C5 (n=658): representatives [␠Lauren, ␠Copa, ␠Jenna, 莉, ␠Madden, ␠Cosby, ␠Herr, maj, ␠Sandra, ␠recurrent]; target-extreme [hero, ␠Giul, 库里, ␠Meadows, ␠Pep, ␠Romero]; classes {'alphabetic': 639, 'mixed': 19}
- C6 (n=475): representatives [␠получа, ␠Running, ␠preached, ␠promising, -founded, ␠reloading, ␠Holds, ␠Riding, -loaded, ␠univers]; target-extreme [␠Ride, -catching, ␠Ends, ␠Recording, Shows, Introduced]; classes {'alphabetic': 410, 'mixed': 64, 'punctuation': 1}
- C7 (n=212): representatives [​, ␠[[], ','=',$, =?",, =<?=$, ␠~/., #{@, ـ, �, <Props]; target-extreme [ّ, :YES, ː, ␠=&, ␠%=, ={()]; classes {'alphabetic': 14, 'mixed': 28, 'numeric': 1, 'punctuation': 169}
- C8 (n=73): representatives [␠of, 的, ␠For, Of, of, ␠Of, for, _of, .of, ␠for]; target-extreme [␠of, ␠for, _of, ␠with, ␠Of, ␠OF]; classes {'alphabetic': 55, 'mixed': 17, 'punctuation': 1}

Strongest intercommunity connections:

- C0 to C6: 1005 token edges; mean cosine 0.129656
- C1 to C2: 990 token edges; mean cosine 0.130600
- C0 to C2: 990 token edges; mean cosine 0.127956
- C2 to C5: 886 token edges; mean cosine 0.133590
- C0 to C1: 873 token edges; mean cosine 0.126351
- C2 to C6: 868 token edges; mean cosine 0.133507
- C1 to C4: 851 token edges; mean cosine 0.131469
- C2 to C4: 843 token edges; mean cosine 0.131425
- C1 to C3: 796 token edges; mean cosine 0.135362
- C0 to C5: 785 token edges; mean cosine 0.129265
- C3 to C4: 599 token edges; mean cosine 0.134944
- C1 to C5: 531 token edges; mean cosine 0.129951
- C3 to C5: 511 token edges; mean cosine 0.134033
- C2 to C3: 511 token edges; mean cosine 0.130070
- C0 to C4: 506 token edges; mean cosine 0.128297

## State 12 — block_11_output

Paired positive_head: membership Jaccard 0.812396; edge Jaccard 0.605411; shared tokens 4863.
Paired negative_tail: membership Jaccard 0.841823; edge Jaccard 0.672543; shared tokens 5189.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5074
- Directed 10-NN edges: 50740
- Undirected edges: 35875
- Communities: 10
- Modularity: 0.538393

All communities:

- C0 (n=958): representatives [ik, вать, ются, ants, ut, ments, ati, ul, ton, ались]; target-extreme [distinct, arf, plaint, nat, frac, cych]; classes {'alphabetic': 950, 'mixed': 8}
- C1 (n=704): representatives [ようになりました, 說話, ␠kennenlernen, ␠características, になりました, の中で, ␠eigentlich, それでも, ですので, っていく]; target-extreme [מסוגל, 変わって, 定了, ␠embark, ␠umiejętności, ␠remind]; classes {'alphabetic': 690, 'mixed': 14}
- C2 (n=673): representatives [␠Portsmouth, ␠kitchen, 业内人士, 卧室, ␠cupboard, smouth, ington, ␠apartment, ␠Wellington, ␠الانتخابات]; target-extreme [␠lieutenant, oningen, useum, lington, ␠street, عون]; classes {'alphabetic': 665, 'mixed': 8}
- C3 (n=630): representatives [pushViewController, ␠spriteBatch, .getOrElse, ␠hashtable, INFRINGEMENT, ␠CGRectMake, ␠thermostat, .JComboBox, ␠UIControl, ␠serialVersionUID]; target-extreme [.CompareTo, .writeFile, ␠thermostat, 一对一, ␠timetable, .arange]; classes {'alphabetic': 433, 'mixed': 189, 'punctuation': 8}
- C4 (n=578): representatives [떘, 턔, 룁, 뀌, 歃, 琟, 엮, 돠, ␠kutje, ␠misdemean]; target-extreme [퓬, 겤, 码头, 镚, 屉, 맜]; classes {'alphabetic': 544, 'mixed': 12, 'punctuation': 22}
- C5 (n=477): representatives [));\n\n, ).\n\n\n\n, "))\r\n, ");\r\n, ');\r\n\r\n, ));\r\n, ));\n, "));\n, ))\r\n, ")\r\n]; target-extreme [],\n, (',');\n, ␠')\n, ],\r\n, }",\n, '),\r\n]; classes {'alphabetic': 3, 'mixed': 4, 'punctuation': 468, 'whitespace': 2}
- C6 (n=459): representatives [␠slipped, ␠constituency, ␠cracks, ␠characteristic, ␠stimulated, ␠legislation, ␠recommendations, ␠scratched, ␠jurisdiction, ␠soak]; target-extreme [␠intervention, ␠trenches, ␠indicative, ␠scratched, ␠Disorder, ␠hang]; classes {'alphabetic': 429, 'mixed': 27, 'punctuation': 3}
- C7 (n=381): representatives [CP, DM, MD, GS, (indexPath, LT, ␠rp, (dateTime, AC, ␠LT]; target-extreme [cmb, /T, *k, iap, PN, \tap]; classes {'alphabetic': 246, 'mixed': 132, 'punctuation': 3}
- C8 (n=116): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠North, ␠␠␠␠␠␠␠␠, North, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, south, ␠😀, ␠␠␠␠␠␠]; target-extreme [␠northeast, ␠␠␠␠␠␠␠␠␠\n, ␠North, ␠␠␠␠␠␠␠␠␠␠␠␠\t, North, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t]; classes {'alphabetic': 42, 'mixed': 2, 'numeric': 1, 'punctuation': 25, 'whitespace': 46}
- C9 (n=98): representatives [\twrite, ␠�, ␠writes, ␠�, ␠�, ␠�, ␠wrote, \troot, ␠�, \telse]; target-extreme [overwrite, \twidth, ␠�, ␠�, ␠�, ␠underline]; classes {'alphabetic': 70, 'mixed': 3, 'punctuation': 24, 'whitespace': 1}

Strongest intercommunity connections:

- C0 to C2: 970 token edges; mean cosine 0.126747
- C3 to C4: 835 token edges; mean cosine 0.125627
- C2 to C6: 772 token edges; mean cosine 0.126524
- C0 to C1: 727 token edges; mean cosine 0.130354
- C1 to C4: 689 token edges; mean cosine 0.125864
- C1 to C2: 679 token edges; mean cosine 0.126226
- C1 to C6: 663 token edges; mean cosine 0.129911
- C0 to C6: 612 token edges; mean cosine 0.129961
- C2 to C3: 598 token edges; mean cosine 0.123357
- C2 to C4: 593 token edges; mean cosine 0.123146
- C0 to C7: 580 token edges; mean cosine 0.134179
- C0 to C3: 514 token edges; mean cosine 0.117298
- C1 to C3: 412 token edges; mean cosine 0.120721
- C0 to C4: 398 token edges; mean cosine 0.122436
- C3 to C7: 370 token edges; mean cosine 0.121333

#### negative_tail

- Nodes: 5481
- Directed 10-NN edges: 54810
- Undirected edges: 38839
- Communities: 9
- Modularity: 0.481535

All communities:

- C0 (n=1203): representatives [␠plethora, ␠apparel, Companies, ␠получа, ␠sessions, ␠trucks, ␠Running, 母校, Training, ␠rapid]; target-extreme [處理, 净, 建军, 纺织, ␠succès, _FIRE]; classes {'alphabetic': 1081, 'mixed': 122}
- C1 (n=828): representatives [.destroyAllWindows, }}">{{$, /ayushman, ␠işle, ␠OnCollision, .setBackgroundResource, 倻, DidAppear, /filepath, ␠thỏa]; target-extreme [:YES, 🉑, _drvdata, ={({, ␠ApplicationController, ={()]; classes {'alphabetic': 308, 'mixed': 353, 'punctuation': 167}
- C2 (n=734): representatives [_done, ␠Showing, ␠TEST, ␠RECE, ROSS, ␠Ав, ␠immedi, ␠retrieve, ␠TEMP, _freq]; target-extreme [Test, ␠TEMP, .EN, ␠ARRAY, _SYS, .shows]; classes {'alphabetic': 415, 'mixed': 319}
- C3 (n=719): representatives [а, 𝑎, レ, ing, и, ์, ا, area, ἃ, e]; target-extreme [ả, 매, �, ␠الز, Æ, 的]; classes {'alphabetic': 667, 'mixed': 22, 'numeric': 1, 'punctuation': 29}
- C4 (n=668): representatives [efully, תחילת, ␠일이, ␠بلا, ␠במיוחד, 最常见的, 额外, אני, 真的很, からの]; target-extreme [第七届, Hôtel, ␠maior, ␠без, ␠ample, ␠بلا]; classes {'alphabetic': 653, 'mixed': 13, 'numeric': 1, 'punctuation': 1}
- C5 (n=632): representatives [Hugh, ␠Carrie, ␠Cameroon, ␠Lauren, ␠AHL, ␠FIFA, ␠Xperia, ␠авг, ␠Aur, ␠Jenna]; target-extreme [␠Romero, ␠inexp, ␠Jed, ␠bella, ␠Jenna, ␠Ago]; classes {'alphabetic': 617, 'mixed': 15}
- C6 (n=316): representatives [💨, 🧤, ✽, 딯, ᶅ, 🍔, אפליק, ﯭ, ₶, �]; target-extreme [떴, ␠még, ﱈ, 🆓, אפליק, 䢼]; classes {'alphabetic': 200, 'mixed': 5, 'punctuation': 111}
- C7 (n=195): representatives [�, �, �, �, �, �, ␠biên, ﾞ, �, �]; target-extreme [�, �, �, �, �, 牢]; classes {'alphabetic': 120, 'mixed': 2, 'punctuation': 73}
- C8 (n=186): representatives [␠of, ;;;;;;;;, „, ´, ␠​, ”, 〜, ـ, ـــــ, (of]; target-extreme [␠of, ␠with, ّ, ␠for, ␠OF, ␠on]; classes {'alphabetic': 68, 'mixed': 33, 'punctuation': 84, 'whitespace': 1}

Strongest intercommunity connections:

- C0 to C2: 1619 token edges; mean cosine 0.129259
- C0 to C4: 1203 token edges; mean cosine 0.130330
- C0 to C5: 1028 token edges; mean cosine 0.131239
- C1 to C2: 974 token edges; mean cosine 0.124946
- C0 to C1: 947 token edges; mean cosine 0.125927
- C3 to C4: 665 token edges; mean cosine 0.136613
- C2 to C5: 645 token edges; mean cosine 0.129787
- C1 to C6: 643 token edges; mean cosine 0.133145
- C0 to C3: 551 token edges; mean cosine 0.128667
- C3 to C5: 545 token edges; mean cosine 0.132453
- C1 to C4: 503 token edges; mean cosine 0.129509
- C2 to C4: 501 token edges; mean cosine 0.128707
- C2 to C3: 404 token edges; mean cosine 0.125358
- C4 to C5: 401 token edges; mean cosine 0.131965
- C3 to C6: 384 token edges; mean cosine 0.134343

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5775
- Directed 10-NN edges: 57750
- Undirected edges: 40854
- Communities: 10
- Modularity: 0.558182

All communities:

- C0 (n=1257): representatives [␠kitchen, 卧室, ␠apartment, ␠slipped, 說話, ␠cupboard, ␠authoritarian, ␠características, ␠الانتخابات, ␠cracks]; target-extreme [overwrite, ␠lieutenant, ␠intervention, distinct, ␠indicative, ␠trenches]; classes {'alphabetic': 1216, 'mixed': 41}
- C1 (n=960): representatives [떘, ik, ются, ants, ut, 읩, ались, ments, sing, aría]; target-extreme [oningen, plaint, arf, iap, nat, inki]; classes {'alphabetic': 950, 'mixed': 10}
- C2 (n=729): representatives [pushViewController, ␠ucfirst, ␠spriteBatch, ␠CGRectMake, .getOrElse, ␠hashtable, INFRINGEMENT, ␠AssemblyProduct, ␠UIControl, ␠serialVersionUID]; target-extreme [.CompareTo, .writeFile, ␠thermostat, .arange, ␠fread, .tableLayoutPanel]; classes {'alphabetic': 497, 'mixed': 228, 'punctuation': 4}
- C3 (n=712): representatives [.EditorButton, 룁, 턔, 嵝, 痦, 뀌, 엮, 돠, 歃, ␠fkk]; target-extreme [퓬, 겤, ␠umiejętności, 镚, 码头, ␠كلمة]; classes {'alphabetic': 664, 'mixed': 16, 'punctuation': 32}
- C4 (n=685): representatives [вать, 业内人士, ようになりました, dzić, になると, дается, ивают, の中で, それでも, 的年轻人]; target-extreme [عون, מסוגל, 定了, 変わって, cych, ących]; classes {'alphabetic': 681, 'mixed': 4}
- C5 (n=591): representatives ["))\r\n, ).\n\n\n\n, ");\r\n, ));\n\n, ');\r\n\r\n, ));\r\n, ])\n, "));\n, ))\r\n, ")\r\n]; target-extreme [],\n, (',');\n, ␠')\n, ],\r\n, "],\n, ().\n]; classes {'alphabetic': 7, 'mixed': 3, 'punctuation': 578, 'whitespace': 3}
- C6 (n=529): representatives [GS, DM, LT, (indexPath, MD, CP, \twrite, (rt, \tboard, PN]; target-extreme [cmb, /T, *k, \tap, PN, rk]; classes {'alphabetic': 357, 'mixed': 169, 'numeric': 1, 'punctuation': 2}
- C7 (n=182): representatives [␠Portsmouth, smouth, ington, ␠Wellington, ␠Scarborough, ␠North, North, oklyn, ␠Bundesliga, ␠Singapore]; target-extreme [lington, ␠northeast, xford, 一对一, leston, ␠North]; classes {'alphabetic': 180, 'mixed': 2}
- C8 (n=75): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, -------------\n, ␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠\r\n]; target-extreme [␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠\t\t\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\n]; classes {'alphabetic': 1, 'punctuation': 23, 'whitespace': 51}
- C9 (n=55): representatives [␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠不, ␠下, ␠和]; target-extreme [␠�, ��态, ␠�, ␠�, ␠�, ␠�]; classes {'alphabetic': 26, 'mixed': 2, 'punctuation': 26, 'whitespace': 1}

Strongest intercommunity connections:

- C0 to C1: 1469 token edges; mean cosine 0.130747
- C2 to C3: 1086 token edges; mean cosine 0.128340
- C0 to C4: 1082 token edges; mean cosine 0.129836
- C0 to C2: 936 token edges; mean cosine 0.123563
- C3 to C4: 885 token edges; mean cosine 0.129758
- C1 to C4: 745 token edges; mean cosine 0.135530
- C0 to C3: 745 token edges; mean cosine 0.126021
- C1 to C6: 716 token edges; mean cosine 0.132858
- C1 to C2: 556 token edges; mean cosine 0.119868
- C2 to C6: 523 token edges; mean cosine 0.124421
- C2 to C4: 441 token edges; mean cosine 0.125489
- C1 to C3: 394 token edges; mean cosine 0.119531
- C0 to C6: 377 token edges; mean cosine 0.124136
- C0 to C7: 340 token edges; mean cosine 0.128249
- C1 to C7: 280 token edges; mean cosine 0.127770

#### negative_tail

- Nodes: 5872
- Directed 10-NN edges: 58720
- Undirected edges: 41428
- Communities: 11
- Modularity: 0.488148

All communities:

- C0 (n=1182): representatives [␠plethora, ␠apparel, ␠sessions, Companies, ␠volcano, 攻势, Training, 母校, ␠reviews, 创新]; target-extreme [處理, 收集, 纺织, Hôtel, ␠Farm, 儿童]; classes {'alphabetic': 1159, 'mixed': 23}
- C1 (n=1155): representatives [␠Showing, _done, ␠Running, (ed, ␠TEST, -work, -Day, _cluster, _Settings, ␠RECE]; target-extreme [Test, ␠inexp, ␠ARRAY, ␠TEMP, _scr, _FIRE]; classes {'alphabetic': 590, 'mixed': 565}
- C2 (n=764): representatives [/ayushman, ␠işle, תחילת, 💨, ␠יצ, ✽, ␠일이, ﯭ, 倻, ␠thỏa]; target-extreme [�, 떴, 摩托, 🉑, 옙, .bukkit]; classes {'alphabetic': 599, 'mixed': 12, 'numeric': 1, 'punctuation': 152}
- C3 (n=539): representatives [␠OnCollision, 🧤, .setBackgroundResource, DidAppear, ␠получа, /filepath, ␠GUIStyle, ␠MaterialPageRoute, ]init, ␠buttonWithType]; target-extreme [:YES, _drvdata, ␠ApplicationController, MethodInfo, CompleteListener, /banner]; classes {'alphabetic': 280, 'mixed': 244, 'punctuation': 15}
- C4 (n=519): representatives [а, ␠of, ์, и, 𝑎, ing, e, е, レ, ℎ]; target-extreme [␠of, ␠with, ّ, ␠for, ␠OF, 的]; classes {'alphabetic': 450, 'mixed': 37, 'numeric': 1, 'punctuation': 31}
- C5 (n=502): representatives [␠Carrie, ␠Cameroon, ␠Lauren, ␠авг, ␠FIFA, 球, ␠Copa, ␠Jenna, ␠Sandra, Johnny]; target-extreme [␠Romero, ␠Jed, ␠Jenna, ␠Ago, ␠bella, ␠Giul]; classes {'alphabetic': 490, 'mixed': 12}
- C6 (n=478): representatives [efully, ␠بلا, からの, אני, ␠данный, 真的很, 庞大的, 但实际上, ␠без, роме]; target-extreme [第七届, ␠maior, ␠بلا, ␠семь, ␠без, .Simple]; classes {'alphabetic': 467, 'mixed': 11}
- C7 (n=272): representatives [}}">{{$, ␠{{$, „, {{$, ␠[&, ="<?=$, #{@, =<?=$, "><?=$, <?=$]; target-extreme [={({, ={(), {{$, Ј, (:, ;;;;;;;;]; classes {'alphabetic': 28, 'mixed': 14, 'punctuation': 229, 'whitespace': 1}
- C8 (n=268): representatives [花, �, �, �, �, �, �, ﾞ, �, �]; target-extreme [�, �, �, �, 净, 매]; classes {'alphabetic': 199, 'punctuation': 69}
- C9 (n=153): representatives [É, ␠lä, ␠É, ré, ␠é, ␠Méd, ␠cré, è, Á, ␠géné]; target-extreme [ả, ␠الز, Æ, ␠Pep, ␠még, ô]; classes {'alphabetic': 153}
- C10 (n=40): representatives [area, ␠tarea, ␠succès, attività, エリア, ␠Success, ␠Idea, ␠success, _SUCCESS, _success]; target-extreme [␠succès, attività, ␠fame, עיון, ␠success, successfully]; classes {'alphabetic': 35, 'mixed': 5}

Strongest intercommunity connections:

- C0 to C1: 1909 token edges; mean cosine 0.130157
- C1 to C3: 1058 token edges; mean cosine 0.123497
- C0 to C2: 927 token edges; mean cosine 0.129043
- C0 to C5: 867 token edges; mean cosine 0.131730
- C2 to C3: 773 token edges; mean cosine 0.130662
- C0 to C6: 754 token edges; mean cosine 0.131650
- C1 to C5: 648 token edges; mean cosine 0.132021
- C0 to C3: 616 token edges; mean cosine 0.124675
- C2 to C4: 548 token edges; mean cosine 0.143087
- C1 to C2: 514 token edges; mean cosine 0.126159
- C2 to C6: 501 token edges; mean cosine 0.136275
- C1 to C6: 445 token edges; mean cosine 0.127490
- C0 to C8: 428 token edges; mean cosine 0.135462
- C1 to C4: 375 token edges; mean cosine 0.127277
- C4 to C6: 338 token edges; mean cosine 0.139364

## State 13 — block_12_output

Paired positive_head: membership Jaccard 0.863165; edge Jaccard 0.703633; shared tokens 4832.
Paired negative_tail: membership Jaccard 0.852388; edge Jaccard 0.693628; shared tokens 4533.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5215
- Directed 10-NN edges: 52150
- Undirected edges: 36775
- Communities: 10
- Modularity: 0.538080

All communities:

- C0 (n=1165): representatives [떘, ␠kitchen, ␠cupboard, 卧室, ␠cooker, sticks, ␠apartment, osterone, ␠refrigerator, ␠scratched]; target-extreme [overwrite, distinct, ␠indicative, ␠lieutenant, ␠timetable, ␠intervention]; classes {'alphabetic': 1114, 'mixed': 51}
- C1 (n=1106): representatives [.EditorButton, 턔, 룁, ␠spriteBatch, 嵝, .getOrElse, ␠açıklama, 읩, INFRINGEMENT, ␠모습]; target-extreme [cmb, 特意, .CompareTo, 퓬, ␠fread, .writeFile]; classes {'alphabetic': 943, 'mixed': 132, 'punctuation': 31}
- C2 (n=868): representatives [ik, ito, ants, <tool_call>, ait, ut, ok, ister, av, ments]; target-extreme [irse, iap, arf, wish, nat, ood]; classes {'alphabetic': 863, 'mixed': 5}
- C3 (n=689): representatives [ются, 业内人士, していました, дается, してしまう, aría, になると, ались, ようになりました, ывают]; target-extreme [␠לעמוד, cych, 定了, 不會, dać, ␠לדעת]; classes {'alphabetic': 677, 'mixed': 9, 'punctuation': 3}
- C4 (n=570): representatives [븓, (rt, ID, \twrite, ␠�, _dx, _id, pm, MD, GS]; target-extreme [/T, fontsize, ewn, rk, *k, (sprite]; classes {'alphabetic': 383, 'mixed': 167, 'punctuation': 19, 'whitespace': 1}
- C5 (n=532): representatives ["))\r\n, ));\n\n, ');\r\n\r\n, ).\n\n\n\n, ")\r\n, ])\n, '))\n, ')\r\n\r\n, ));\r\n, ,"]; target-extreme [(',');\n, ␠')\n, ],\n, `\r\n, ],\r\n, "],\n]; classes {'alphabetic': 30, 'mixed': 18, 'punctuation': 478, 'whitespace': 6}
- C6 (n=128): representatives [smouth, ington, ␠Wellington, North, داعش, ␠North, ␠Charlottesville, ␠Scarborough, ␠Singapore, instein]; target-extreme [oningen, xford, lington, ␠northeast, leston, ␠Goa]; classes {'alphabetic': 126, 'mixed': 2}
- C7 (n=74): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, -----------\n]; classes {'alphabetic': 4, 'numeric': 1, 'punctuation': 22, 'whitespace': 47}
- C8 (n=44): representatives [book, ␠comments, ␠wrote, 发布了, ␠commented, ␠unveiled, 丛书, ␠publié, ␠posted, ␠Published]; target-extreme [␠CFR, /comments, ␠publié, 책, ␠tome, ␠책]; classes {'alphabetic': 42, 'mixed': 2}
- C9 (n=39): representatives [ﱊ, 퓲, 옭, 쥉, 뻅, 끍, 㟁, 깢, 뺃, 셢]; target-extreme [ﳫ, 𬭤, 옭, ﱊ, 넖, 䓨]; classes {'alphabetic': 37, 'punctuation': 2}

Strongest intercommunity connections:

- C0 to C1: 1390 token edges; mean cosine 0.123159
- C0 to C2: 1341 token edges; mean cosine 0.124313
- C1 to C3: 1287 token edges; mean cosine 0.128996
- C0 to C3: 1004 token edges; mean cosine 0.127165
- C2 to C3: 817 token edges; mean cosine 0.131252
- C1 to C4: 760 token edges; mean cosine 0.123873
- C2 to C4: 674 token edges; mean cosine 0.128724
- C0 to C4: 643 token edges; mean cosine 0.125659
- C1 to C2: 600 token edges; mean cosine 0.118294
- C0 to C6: 270 token edges; mean cosine 0.123572
- C3 to C4: 262 token edges; mean cosine 0.122210
- C2 to C6: 211 token edges; mean cosine 0.127115
- C1 to C6: 191 token edges; mean cosine 0.124041
- C4 to C5: 165 token edges; mean cosine 0.142520
- C1 to C5: 157 token edges; mean cosine 0.122475

#### negative_tail

- Nodes: 4800
- Directed 10-NN edges: 48000
- Undirected edges: 33888
- Communities: 9
- Modularity: 0.479754

All communities:

- C0 (n=957): representatives [_done, ␠Running, ␠comparing, _Settings, ␠RECE, ␠unsupported, ROSS, -Day, ␠HALF, ␠liber]; target-extreme [␠TEMP, _LOAD, -buffer, ␠Creating, ␠inexp, ␠Sole]; classes {'alphabetic': 524, 'mixed': 433}
- C1 (n=907): representatives [␠بلا, а, ing, ์, ␠Ав, и, ␠Пар, �, �, ␠cré]; target-extreme [�, �, �, ␠الز, у, Æ]; classes {'alphabetic': 778, 'mixed': 15, 'numeric': 1, 'punctuation': 113}
- C2 (n=803): representatives [␠sessions, ␠insecurity, ␠trucks, ␠volcano, 攻势, ␠curriculum, Concurrency, ␠successes, 创新, truth]; target-extreme [␠Farm, 處理, 纺织, 建军, 敏捷, 净]; classes {'alphabetic': 775, 'mixed': 28}
- C3 (n=510): representatives [삻, efully, ␠plethora, 最常见的, 庞大的, ␠במיוחד, ␠קשה, אני, ␠Highly, ␠fodder]; target-extreme [第七届, 连载, ␠lief, ␠вся, 有效地, ␠még]; classes {'alphabetic': 488, 'mixed': 21, 'punctuation': 1}
- C4 (n=503): representatives [.destroyAllWindows, ␠WPARAM, ␠OnCollision, .setBackgroundResource, ␠buttonWithType, DidAppear, ␠HttpServletResponse, ]init, ␠Models, ␠jsonResponse]; target-extreme [.Automation, ␠ApplicationController, :YES, .setBackgroundResource, .bukkit, /banner]; classes {'alphabetic': 250, 'mixed': 243, 'punctuation': 10}
- C5 (n=396): representatives [␠Carrie, ␠Jimmy, ␠Jenna, ␠Angola, ␠Hannah, ␠Macedonia, Johnny, ␠Herr, ␠Sandra, ␠Cair]; target-extreme [␠Curry, ␠Romero, ␠Jed, ,eg, ␠Bott, ␠Manning]; classes {'alphabetic': 389, 'mixed': 7}
- C6 (n=361): representatives [␠işle, 母校, ♋, ␠получа, 💨, 🍔, 🉑, ᶅ, ␠алк, ␠ład]; target-extreme [떴, 🉑, ﱈ, ␠gı, 🏪, ﮦ]; classes {'alphabetic': 254, 'mixed': 2, 'punctuation': 105}
- C7 (n=240): representatives [␠of, =<?=$, <?=$, "><?=$, #{@, 的, ="<?=$, {{$, ={(), ={`/]; target-extreme [␠of, ␠for, ␠with, ␠OF, 的, ␠to]; classes {'alphabetic': 61, 'mixed': 30, 'numeric': 1, 'punctuation': 147, 'whitespace': 1}
- C8 (n=123): representatives [area, Tests, ␠Ass, ␠tarea, ␠predictions, ␠Demo, ␠Prediction, דוגמה, Testing, ␠Problem]; target-extreme [␠Problem, Test, EXAMPLE, ␠пример, ␠Acceler, ␠Mass]; classes {'alphabetic': 106, 'mixed': 17}

Strongest intercommunity connections:

- C0 to C2: 1221 token edges; mean cosine 0.132064
- C0 to C4: 950 token edges; mean cosine 0.122027
- C2 to C3: 775 token edges; mean cosine 0.130821
- C0 to C3: 700 token edges; mean cosine 0.130033
- C1 to C6: 670 token edges; mean cosine 0.131434
- C1 to C3: 659 token edges; mean cosine 0.129645
- C1 to C2: 642 token edges; mean cosine 0.127133
- C0 to C1: 623 token edges; mean cosine 0.128036
- C1 to C5: 592 token edges; mean cosine 0.131168
- C2 to C4: 508 token edges; mean cosine 0.122624
- C0 to C5: 493 token edges; mean cosine 0.127009
- C4 to C6: 471 token edges; mean cosine 0.129592
- C2 to C5: 456 token edges; mean cosine 0.126485
- C2 to C6: 357 token edges; mean cosine 0.129054
- C3 to C6: 353 token edges; mean cosine 0.133401

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5215
- Directed 10-NN edges: 52150
- Undirected edges: 36856
- Communities: 10
- Modularity: 0.554250

All communities:

- C0 (n=1192): representatives [떘, ␠kitchen, 읩, rarian, ␠cupboard, ␠refrigerator, ␠apartment, ␠cooker, sticks, ␠scratched]; target-extreme [overwrite, ␠indicative, ␠lieutenant, plaint, distinct, ␠intervention]; classes {'alphabetic': 1146, 'mixed': 46}
- C1 (n=833): representatives [ются, ␠açıklama, дается, iquer, aría, ались, ивают, になると, それでも, ывают]; target-extreme [␠לעמוד, oningen, irse, 定了, cych, ␠patiënt]; classes {'alphabetic': 821, 'mixed': 11, 'punctuation': 1}
- C2 (n=748): representatives [ik, ants, ito, <tool_call>, ut, ait, av, ok, ton, ab]; target-extreme [rk, ewn, iap, rax, ood, oints]; classes {'alphabetic': 740, 'mixed': 8}
- C3 (n=723): representatives [pushViewController, ␠spriteBatch, .dateTimePicker, 业内人士, .getOrElse, ␠CGRectMake, ␠모습, .tableLayoutPanel, INFRINGEMENT, strncmp]; target-extreme [fontsize, .CompareTo, 特意, .writeFile, ␠timetable, .tableLayoutPanel]; classes {'alphabetic': 579, 'mixed': 141, 'punctuation': 3}
- C4 (n=596): representatives [.EditorButton, 턔, 룁, 嵝, .DropDownStyle, معاي, 洨, ␠kutje, 鲱, 铏]; target-extreme [퓬, 骺, QRSTUV, 屉, 댓, 镚]; classes {'alphabetic': 546, 'mixed': 15, 'punctuation': 35}
- C5 (n=529): representatives ["))\r\n, ');\r\n\r\n, ");\r\n, ));\n\n, ])\n, ));\r\n, ")\r\n, "));\n, ).\n\n\n\n, '))\n]; target-extreme [(',');\n, ␠')\n, ],\n, "],\n, `\r\n, ],\r\n]; classes {'alphabetic': 3, 'mixed': 11, 'punctuation': 507, 'whitespace': 8}
- C6 (n=365): representatives [(indexPath, pm, \twrite, (rt, GS, LT, _dx, ␠xt, (dateTime, DM]; target-extreme [cmb, /T, (sprite, *k, (al, (com]; classes {'alphabetic': 216, 'mixed': 146, 'punctuation': 3}
- C7 (n=108): representatives [smouth, ington, ␠Wellington, ␠Stuttgart, North, ␠Montgomery, ␠Scarborough, ␠Charlottesville, ␠North, ␠Singapore]; target-extreme [lington, xford, ␠northeast, ␠Goa, 쟙, North]; classes {'alphabetic': 107, 'mixed': 1}
- C8 (n=78): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠\n, -----------\n, =========\n]; classes {'alphabetic': 3, 'numeric': 1, 'punctuation': 23, 'whitespace': 51}
- C9 (n=43): representatives [␠�, ␠�, ␠�, ␠�, ␠和, ␠不, ␠�, ␠下, ␠�, ␠修改]; target-extreme [␠�, ␠�, >Delete, ��态, ␠修改, ␠�]; classes {'alphabetic': 19, 'mixed': 3, 'punctuation': 20, 'whitespace': 1}

Strongest intercommunity connections:

- C0 to C2: 1229 token edges; mean cosine 0.124899
- C0 to C3: 1160 token edges; mean cosine 0.122869
- C0 to C1: 1050 token edges; mean cosine 0.127015
- C3 to C4: 985 token edges; mean cosine 0.127273
- C1 to C2: 797 token edges; mean cosine 0.130488
- C1 to C3: 752 token edges; mean cosine 0.126552
- C1 to C4: 735 token edges; mean cosine 0.128325
- C0 to C4: 610 token edges; mean cosine 0.122276
- C2 to C6: 505 token edges; mean cosine 0.129030
- C3 to C6: 445 token edges; mean cosine 0.122946
- C2 to C3: 380 token edges; mean cosine 0.118117
- C0 to C6: 363 token edges; mean cosine 0.125376
- C2 to C4: 263 token edges; mean cosine 0.118345
- C0 to C7: 232 token edges; mean cosine 0.123121
- C2 to C7: 157 token edges; mean cosine 0.129477

#### negative_tail

- Nodes: 5051
- Directed 10-NN edges: 50510
- Undirected edges: 35693
- Communities: 10
- Modularity: 0.481353

All communities:

- C0 (n=910): representatives [\tdes, _done, _Settings, ␠RECE, ␠TEST, ␠promising, ␠TEMP, ␠HALF, -Day, ROSS]; target-extreme [-buffer, ␠TEMP, ␠Tried, _LOAD, _FIRE, ␠Blocks]; classes {'alphabetic': 377, 'mixed': 531, 'punctuation': 2}
- C1 (n=827): representatives [.destroyAllWindows, 삻, ␠işle, ␠OnCollision, .setBackgroundResource, ␠WPARAM, 所提供之, 母校, DidAppear, ␠buttonWithType]; target-extreme [떴, 🉑, �, ␠inexp, 建军, ␠correctamente]; classes {'alphabetic': 564, 'mixed': 162, 'punctuation': 101}
- C2 (n=791): representatives [␠Jimmy, ␠Carrie, ␠Jenna, ␠Herr, ␠Drug, ␠Ав, RE, ␠Bod, ␠sugar, ␠liber]; target-extreme [␠Curry, 敏捷, ␠Romero, ␠PRES, ␠Jed, ␠Ride]; classes {'alphabetic': 776, 'mixed': 14, 'punctuation': 1}
- C3 (n=603): representatives [а, ␠of, ing, ์, е, �, и, ე, �, 的]; target-extreme [␠of, ␠for, ␠with, �, ␠OF, 的]; classes {'alphabetic': 464, 'mixed': 28, 'numeric': 2, 'punctuation': 108, 'whitespace': 1}
- C4 (n=588): representatives [␠volcano, ␠fodder, 提升, 戏曲, ␠Macedonia, ␠Angola, 热议, ␠Zambia, 休闲, 体]; target-extreme [␠Farm, 纺织, 重心, ␠Baseball, 保证, 提升]; classes {'alphabetic': 582, 'mixed': 5, 'punctuation': 1}
- C5 (n=493): representatives [␠sessions, ␠Running, ␠comparing, ␠curriculum, ␠colleges, 创新, ␠Models, ␠Surgery, ␠reviews, Training]; target-extreme [處理, ␠Creating, ␠clientes, Uses, _testing, .integration]; classes {'alphabetic': 442, 'mixed': 50, 'punctuation': 1}
- C6 (n=399): representatives [最常见的, ␠במיוחד, ␠بلا, אני, ␠일이, 就能够, からの, Pago, ␠без, 真的很]; target-extreme [␠الز, ␠без, ␠семь, ␠بلا, 第七届, ␠вся]; classes {'alphabetic': 390, 'mixed': 8, 'punctuation': 1}
- C7 (n=219): representatives [␠plethora, efully, ␠insecurity, 攻势, ␠successes, ␠motivational, 庞大的, ␠Highly, truth, ␠perseverance]; target-extreme [净, ␠motivational, ␠succès, ␠Sicher, 肉体, ␠brisk]; classes {'alphabetic': 211, 'mixed': 8}
- C8 (n=207): representatives [=<?=$, "><?=$, ="<?=$, #{@, ={`/, {{$, <?=$, ␠//!<, „, ␠{$]; target-extreme [옙, (:, ="<?=$, {{$, ={(), ="?]; classes {'alphabetic': 16, 'mixed': 28, 'punctuation': 163}
- C9 (n=14): representatives [␠век, ␠monday, ␠sábado, ␠Jahr, ␠дня, ␠miesią, ␠Friday, ␠Saturday, ␠Copyright, ␠Thursday]; target-extreme [␠дня, ␠miesią, weekday, ␠sábado, Saturday, _week]; classes {'alphabetic': 13, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C1: 1043 token edges; mean cosine 0.123157
- C0 to C2: 1008 token edges; mean cosine 0.130094
- C0 to C5: 989 token edges; mean cosine 0.131495
- C4 to C5: 715 token edges; mean cosine 0.131978
- C1 to C2: 671 token edges; mean cosine 0.127119
- C2 to C4: 613 token edges; mean cosine 0.128262
- C1 to C3: 573 token edges; mean cosine 0.130965
- C1 to C4: 562 token edges; mean cosine 0.125667
- C1 to C6: 541 token edges; mean cosine 0.131889
- C2 to C5: 522 token edges; mean cosine 0.129187
- C2 to C3: 469 token edges; mean cosine 0.133208
- C1 to C5: 458 token edges; mean cosine 0.125959
- C3 to C4: 408 token edges; mean cosine 0.126922
- C3 to C6: 389 token edges; mean cosine 0.137470
- C0 to C4: 386 token edges; mean cosine 0.125273

## State 14 — block_13_output

Paired positive_head: membership Jaccard 0.877748; edge Jaccard 0.728880; shared tokens 5629.
Paired negative_tail: membership Jaccard 0.886795; edge Jaccard 0.747024; shared tokens 6118.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6047
- Directed 10-NN edges: 60470
- Undirected edges: 42911
- Communities: 8
- Modularity: 0.542405

All communities:

- C0 (n=1252): representatives [ются, ants, ik, ak, ают, ut, ments, ok, ich, ister]; target-extreme [irse, wish, ewn, iap, arf, frac]; classes {'alphabetic': 1237, 'mixed': 13, 'numeric': 1, 'punctuation': 1}
- C1 (n=1096): representatives [pushViewController, ␠ucfirst, ␠CGRectMake, .getOrElse, ␠hashtable, ␠openFileDialog, .tableLayoutPanel, ␠electrodes, \tstrcat, ␠scaleFactor]; target-extreme [overwrite, distinct, fontsize, .writeFile, ␠timetable, .tableLayoutPanel]; classes {'alphabetic': 854, 'mixed': 238, 'punctuation': 4}
- C2 (n=1019): representatives [␠kitchen, 业内人士, istrates, smouth, ␠scratched, ␠disgusting, ␠priests, 卧室, ␠apartment, ␠Commander]; target-extreme [␠intervention, ␠street, oningen, ␠scratched, ␠trenches, plemented]; classes {'alphabetic': 997, 'mixed': 22}
- C3 (n=884): representatives [.EditorButton, 룁, 턔, więt, 嵝, .visitMethodInsn, 漦, ␠spriteBatch, hevik, 圙]; target-extreme [퓬, QRSTUV, ǳ, 턔, 𬭤, 𐤔]; classes {'alphabetic': 790, 'mixed': 45, 'punctuation': 49}
- C4 (n=763): representatives [になると, はずです, ってしまいます, ␠report, それでも, ようになりました, していました, することは, ␠شيء, تغيير]; target-extreme [␠לעמוד, 不會, ␠although, מסוגל, 特意, ␠никогда]; classes {'alphabetic': 736, 'mixed': 12, 'punctuation': 15}
- C5 (n=641): representatives [');\r\n\r\n, "))\r\n, ")\r\n, ");\r\n, ));\n\n, ).\n\n\n\n, ))\r\n, ));\r\n\r\n, ));\r\n, '\r\n]; target-extreme [(',');\n, }");\r\n, ␠')\n, ]);\r\n\r\n, `\r\n, ],\n]; classes {'alphabetic': 3, 'mixed': 23, 'punctuation': 608, 'whitespace': 7}
- C6 (n=329): representatives [CP, ␠rp, LT, PD, ␠don, \tboard, ␠maxX, \telse, CD, NBC]; target-extreme [cmb, /T, ␠elif, *k, xF, ␠AFP]; classes {'alphabetic': 222, 'mixed': 105, 'punctuation': 2}
- C7 (n=63): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\n]; target-extreme [␠␠␠␠\t\t\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\n, -----------\n, ----------\n, ␠␠␠␠␠␠\r\n]; classes {'alphabetic': 2, 'punctuation': 14, 'whitespace': 47}

Strongest intercommunity connections:

- C1 to C2: 1726 token edges; mean cosine 0.128641
- C0 to C2: 1484 token edges; mean cosine 0.127950
- C1 to C3: 1354 token edges; mean cosine 0.131542
- C0 to C1: 1128 token edges; mean cosine 0.124070
- C2 to C4: 1036 token edges; mean cosine 0.128393
- C0 to C4: 943 token edges; mean cosine 0.130544
- C3 to C4: 938 token edges; mean cosine 0.131310
- C1 to C4: 776 token edges; mean cosine 0.126207
- C2 to C3: 692 token edges; mean cosine 0.126976
- C1 to C6: 578 token edges; mean cosine 0.128147
- C0 to C6: 556 token edges; mean cosine 0.131460
- C0 to C3: 531 token edges; mean cosine 0.120743
- C2 to C6: 168 token edges; mean cosine 0.121294
- C5 to C6: 146 token edges; mean cosine 0.139518
- C4 to C6: 146 token edges; mean cosine 0.128246

#### negative_tail

- Nodes: 6378
- Directed 10-NN edges: 63780
- Undirected edges: 44904
- Communities: 9
- Modularity: 0.501723

All communities:

- C0 (n=1292): representatives [삻, \tdes, (result, ␠Running, _done, _Dep, ␠RECE, ␠TEMP, ␠HALF, ROSS]; target-extreme [.settings, -full, /name, ?q, -produ, -cond]; classes {'alphabetic': 508, 'mixed': 784}
- C1 (n=1051): representatives [.destroyAllWindows, ␠işle, .setBackgroundResource, профессиона, ␠OnCollision, ✽, ␠WPARAM, 💨, ␠ład, 母校]; target-extreme [떴, ␠inexp, .bukkit, Jvm, �, ␠механиз]; classes {'alphabetic': 756, 'mixed': 157, 'punctuation': 138}
- C2 (n=844): representatives [攻势, 戏曲, ␠trucks, 创新, 提升, 休闲, 艰辛, 车, 热议, 流]; target-extreme [纺织, ␠Farm, 매, 牢, ␠giải, 宣告]; classes {'alphabetic': 840, 'mixed': 3, 'punctuation': 1}
- C3 (n=790): representatives [␠Carrie, Hugh, ␠Zambia, ␠ponder, ␠Macedonia, ␠Lauren, ␠Jenna, ␠Пар, zano, ␠Jimmy]; target-extreme [␠Curry, ␠Romero, ␠Bott, Berry, \tPy, ␠Kara]; classes {'alphabetic': 771, 'mixed': 19}
- C4 (n=723): representatives [␠comparing, ␠sessions, ␠simulation, Companies, ␠curriculum, ␠straightforward, ␠insecurity, ␠perseverance, -commerce, Concurrency]; target-extreme [␠clientes, EXAMPLE, 重心, _testing, ␠Lightweight, ネット]; classes {'alphabetic': 672, 'mixed': 51}
- C5 (n=650): representatives [а, ์, и, ا, ing, ь, 了, �, �, е]; target-extreme [�, ␠الز, у, Æ, ّ, �]; classes {'alphabetic': 515, 'mixed': 12, 'punctuation': 123}
- C6 (n=605): representatives [␠במיוחד, 最常见的, ほとんど, ␠positively, ␠successes, אני, ␠без, 真的很, 庞大的, 更具]; target-extreme [␠семь, ␠succès, /banner, ␠além, ␠correctamente, 第七届]; classes {'alphabetic': 580, 'mixed': 24, 'numeric': 1}
- C7 (n=293): representatives [=<?=$, ="<?=$, ␠{{$, "><?=$, {{$, #{@, ␠​, ~, ={()=>, ><?=$]; target-extreme [␠$($, ␠=&, ={(), $$, {, ((*]; classes {'alphabetic': 23, 'mixed': 32, 'numeric': 1, 'punctuation': 235, 'whitespace': 2}
- C8 (n=130): representatives [␠of, Pago, 的, ␠cultura, ␠negócio, ␠pessoas, ␠for, ␠about, ␠For, Nama]; target-extreme [␠of, ␠for, ␠with, ␠OF, ␠to, _of]; classes {'alphabetic': 118, 'mixed': 12}

Strongest intercommunity connections:

- C0 to C4: 1508 token edges; mean cosine 0.131420
- C0 to C1: 1288 token edges; mean cosine 0.125887
- C0 to C3: 1181 token edges; mean cosine 0.130991
- C2 to C4: 971 token edges; mean cosine 0.133704
- C1 to C2: 900 token edges; mean cosine 0.129773
- C1 to C5: 837 token edges; mean cosine 0.137372
- C3 to C4: 779 token edges; mean cosine 0.130541
- C1 to C3: 737 token edges; mean cosine 0.131928
- C1 to C6: 693 token edges; mean cosine 0.134962
- C1 to C4: 674 token edges; mean cosine 0.131833
- C2 to C6: 598 token edges; mean cosine 0.133165
- C2 to C3: 556 token edges; mean cosine 0.131146
- C2 to C5: 535 token edges; mean cosine 0.134397
- C0 to C2: 522 token edges; mean cosine 0.126198
- C4 to C6: 496 token edges; mean cosine 0.136342

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5995
- Directed 10-NN edges: 59950
- Undirected edges: 42653
- Communities: 10
- Modularity: 0.553429

All communities:

- C0 (n=1115): representatives [ются, ak, ants, ik, ают, ments, ut, av, act, ton]; target-extreme [wish, irse, ewn, عون, arf, frac]; classes {'alphabetic': 1104, 'mixed': 10, 'numeric': 1}
- C1 (n=1037): representatives [.EditorButton, 턔, 룁, 嵝, więt, .visitMethodInsn, hevik, 圙, .TabStop, igrationBuilder]; target-extreme [퓬, QRSTUV, ␠לעמוד, ǳ, 턔, 𐤔]; classes {'alphabetic': 963, 'mixed': 26, 'punctuation': 48}
- C2 (n=968): representatives [␠kitchen, istrates, ␠disgusting, ␠report, ␠scratched, ␠cupboard, ␠apartment, ␠policymakers, ␠electrodes, ␠cooker]; target-extreme [␠intervention, ␠street, ␠scratched, plemented, distinct, ␠trenches]; classes {'alphabetic': 948, 'mixed': 20}
- C3 (n=906): representatives [pushViewController, ␠ucfirst, ␠spriteBatch, ␠CGRectMake, .getOrElse, ␠hashtable, [SerializeField, .dateTimePicker, ␠openFileDialog, .tableLayoutPanel]; target-extreme [overwrite, fontsize, .writeFile, .tableLayoutPanel, fontSize, .CompareTo]; classes {'alphabetic': 650, 'mixed': 254, 'punctuation': 2}
- C4 (n=645): representatives [');\r\n\r\n, "))\r\n, ");\r\n, ).\n\n\n\n, ));\n\n, ")\r\n, ));\r\n, ))\r\n, ));\r\n\r\n, '\r\n]; target-extreme [(',');\n, ␠')\n, }");\r\n, ]);\r\n\r\n, ],\n, `\r\n]; classes {'alphabetic': 2, 'mixed': 8, 'punctuation': 628, 'whitespace': 7}
- C5 (n=619): representatives [业内人士, になると, ってしまいます, ようになりました, 签约仪式, それでも, ␠القادم, はずです, aría, ␠شيء]; target-extreme [不會, מסוגל, 特意, ␠timetable, season, سياسات]; classes {'alphabetic': 611, 'mixed': 8}
- C6 (n=421): representatives [<tool_call>, CP, 븓, ␠rp, ID, PD, LT, )p, ni, PN]; target-extreme [cmb, /T, *k, ␠AFP, rk, xF]; classes {'alphabetic': 299, 'mixed': 120, 'punctuation': 2}
- C7 (n=138): representatives [smouth, ␠Montgomery, igslist, داعش, Seattle, ␠Scarborough, ottesville, ␠Singapore, gomery, ␠Plymouth]; target-extreme [oningen, 쟙, ␠Augustine, xford, 겤, atchewan]; classes {'alphabetic': 137, 'mixed': 1}
- C8 (n=109): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠don, \tint, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, \twidth]; target-extreme [␠although, ␠elif, ␠␠␠␠\t\t\n, ␠␠␠␠␠␠␠␠␠\n, -----------\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 35, 'punctuation': 29, 'whitespace': 45}
- C9 (n=37): representatives [␠�, ␠�, ␠新, ␠�, ␠和, left, ␠�, ␠生, ␠�, ␠上]; target-extreme [␠�, ␠�, ��态, left, ␠�, ��]; classes {'alphabetic': 16, 'mixed': 3, 'punctuation': 18}

Strongest intercommunity connections:

- C0 to C2: 1437 token edges; mean cosine 0.129146
- C1 to C3: 1337 token edges; mean cosine 0.130454
- C2 to C3: 1062 token edges; mean cosine 0.125550
- C1 to C5: 958 token edges; mean cosine 0.132705
- C1 to C2: 891 token edges; mean cosine 0.126801
- C2 to C5: 844 token edges; mean cosine 0.128684
- C0 to C5: 706 token edges; mean cosine 0.131484
- C0 to C3: 689 token edges; mean cosine 0.119245
- C0 to C6: 675 token edges; mean cosine 0.129543
- C0 to C1: 653 token edges; mean cosine 0.121169
- C3 to C6: 517 token edges; mean cosine 0.121925
- C3 to C5: 433 token edges; mean cosine 0.123801
- C2 to C6: 294 token edges; mean cosine 0.122184
- C2 to C7: 249 token edges; mean cosine 0.124351
- C1 to C6: 235 token edges; mean cosine 0.121975

#### negative_tail

- Nodes: 6639
- Directed 10-NN edges: 66390
- Undirected edges: 46675
- Communities: 9
- Modularity: 0.503620

All communities:

- C0 (n=1202): representatives [\tdes, (result, _done, _Dep, ␠TEMP, ␠RECE, ␠LAW, ␠HALF, -Day, _Ad]; target-extreme [␠inexp, .settings, -full, -produ, ␠ARRAY, -cond]; classes {'alphabetic': 457, 'mixed': 745}
- C1 (n=1081): representatives [␠comparing, ␠Running, ␠sessions, ␠curriculum, ␠straightforward, Companies, ␠simulation, ␠insecurity, ␠perseverance, ␠scenarios]; target-extreme [␠clientes, ␠семь, 纺织, 重心, Uses, EXAMPLE]; classes {'alphabetic': 1010, 'mixed': 71}
- C2 (n=1014): representatives [삻, ␠Carrie, Hugh, ␠volcano, ␠Macedonia, ␠Zambia, ␠Jenna, ␠Lauren, ␠Angola, אני]; target-extreme [␠Curry, ␠Farm, ␠Romero, \tPy, ?q, ␠Bott]; classes {'alphabetic': 987, 'mixed': 27}
- C3 (n=1006): representatives [а, ์, e, ing, и, �, е, 了, チェ, �]; target-extreme [�, ␠الز, у, ّ, Æ, �]; classes {'alphabetic': 860, 'mixed': 10, 'numeric': 2, 'punctuation': 133, 'whitespace': 1}
- C4 (n=967): representatives [.destroyAllWindows, .setBackgroundResource, профессиона, ␠OnCollision, ✽, ␠WPARAM, ␠получа, 🏦, ␠ład, ␠yaygın]; target-extreme [떴, .bukkit, Jvm, �, /name, /banner]; classes {'alphabetic': 634, 'mixed': 194, 'punctuation': 139}
- C5 (n=780): representatives [攻势, ␠במיוחד, ␠بلا, 最常见的, 提升, 庞大的, 更具, ほとんど, 気軽に, ␠без]; target-extreme [敏捷, 宣告, 牢, 过度, ␠além, 市委]; classes {'alphabetic': 767, 'mixed': 13}
- C6 (n=323): representatives [=<?=$, ="<?=$, {{$, ␠{{$, "><?=$, ´, #{@, ~, ]))), ␠(~]; target-extreme [␠$($, ={(), $$, ـ, {, ␠=&]; classes {'alphabetic': 46, 'mixed': 27, 'numeric': 1, 'punctuation': 248, 'whitespace': 1}
- C7 (n=138): representatives [␠successes, ␠positively, ␠datos, ␠pessoas, ␠Success, ␠succès, attività, \tsuccess, ␠gỗ, idade]; target-extreme [␠succès, ␠correctamente, ␠дня, ␠brisk, attività, ␠confidently]; classes {'alphabetic': 133, 'mixed': 5}
- C8 (n=128): representatives [␠of, ␠السيارات, ␠de, ␠الإيراني, הייתי, ␠for, ␠For, ␠é, ’est, ␠on]; target-extreme [␠of, ␠for, ␠with, ␠OF, ␠to, _of]; classes {'alphabetic': 108, 'mixed': 20}

Strongest intercommunity connections:

- C0 to C1: 1577 token edges; mean cosine 0.130128
- C0 to C2: 1321 token edges; mean cosine 0.132856
- C1 to C2: 1229 token edges; mean cosine 0.131973
- C0 to C4: 1182 token edges; mean cosine 0.125645
- C1 to C5: 1071 token edges; mean cosine 0.133091
- C1 to C4: 1015 token edges; mean cosine 0.130221
- C3 to C4: 954 token edges; mean cosine 0.134240
- C2 to C4: 860 token edges; mean cosine 0.128794
- C2 to C3: 804 token edges; mean cosine 0.134262
- C3 to C5: 778 token edges; mean cosine 0.136638
- C4 to C5: 773 token edges; mean cosine 0.131231
- C1 to C3: 648 token edges; mean cosine 0.131484
- C0 to C3: 544 token edges; mean cosine 0.129022
- C0 to C5: 448 token edges; mean cosine 0.131802
- C2 to C5: 438 token edges; mean cosine 0.130604

## State 15 — block_14_output

Paired positive_head: membership Jaccard 0.877897; edge Jaccard 0.726915; shared tokens 5493.
Paired negative_tail: membership Jaccard 0.860584; edge Jaccard 0.697285; shared tokens 5537.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5791
- Directed 10-NN edges: 57910
- Undirected edges: 41408
- Communities: 9
- Modularity: 0.537173

All communities:

- C0 (n=1315): representatives [猫咪, ␠kitchen, ailer, sensor, ␠kittens, istrates, ␠apartment, ␠cupboard, osterone, ␠priests]; target-extreme [overwrite, ␠lieutenant, ␠intervention, ␠scratched, ␠street, ␠strapped]; classes {'alphabetic': 1230, 'mixed': 85}
- C1 (n=1126): representatives [pushViewController, ␠şikay, ␠wyśw, ␠ucfirst, .EditorButton, ␠spriteBatch, 嵝, .visitMethodInsn, 漦, ␠CGRectMake]; target-extreme [␠swal, ␠ransom, ␠לעמוד, \tstrncpy, 😳, ␠radioButton]; classes {'alphabetic': 911, 'mixed': 161, 'punctuation': 54}
- C2 (n=728): representatives [ak, ain, ik, ton, ut, ans, ister, av, ek, ama]; target-extreme [wish, rax, 码, kas, kes, lac]; classes {'alphabetic': 719, 'mixed': 8, 'punctuation': 1}
- C3 (n=721): representatives [ются, になると, ывают, ようになりました, дается, ␠القادم, ивают, ינים, ались, からない]; target-extreme [irse, 不會, cych, عون, ␠entrar, season]; classes {'alphabetic': 706, 'mixed': 15}
- C4 (n=552): representatives [');\r\n\r\n, "))\r\n, ));\n\n, ")\r\n, ')\r\n\r\n, ));\r\n\r\n, ));\r\n, '\r\n, '))\n, ');\r\n]; target-extreme [}");\r\n, "]}\n, (',');\n, ␠')\n, ␠␠␠␠\t\t\n, ␠');\n\n]; classes {'alphabetic': 2, 'mixed': 4, 'punctuation': 507, 'whitespace': 39}
- C5 (n=530): representatives [뤗, 㨳, 떘, 룁, więt, 턔, 馧, 띱, 圙, 믈]; target-extreme [myśl, 𐤔, tridge, 퓬, distinct, ameleon]; classes {'alphabetic': 513, 'mixed': 9, 'punctuation': 8}
- C6 (n=504): representatives [CP, 𝑽, \tds, (ds, _cf, (indexPath, MD, \tcp, ID, LT]; target-extreme [cmb, *k, (sprite, /T, [l, fontsize]; classes {'alphabetic': 315, 'mixed': 186, 'numeric': 1, 'punctuation': 2}
- C7 (n=205): representatives [getWidth, actionDate, ␠setDate, ␠不, ␠mName, DateTime, AGES, ␠setTime, createdAt, ␠loadData]; target-extreme [␠timetable, ␠getColor, /items, ␠createDate, dating, ␠tableName]; classes {'alphabetic': 162, 'mixed': 32, 'punctuation': 11}
- C8 (n=110): representatives [smouth, ington, ␠Turkish, ␠Stuttgart, داعش, ␠Cincinnati, ␠Montgomery, gomery, ␠Austrian, ottesville]; target-extreme [oningen, 쟙, ␠Augustine, ␠Snyder, xford, North]; classes {'alphabetic': 109, 'mixed': 1}

Strongest intercommunity connections:

- C1 to C5: 1611 token edges; mean cosine 0.137779
- C0 to C2: 1162 token edges; mean cosine 0.127482
- C0 to C1: 1099 token edges; mean cosine 0.125887
- C0 to C5: 922 token edges; mean cosine 0.130351
- C1 to C3: 880 token edges; mean cosine 0.128744
- C0 to C3: 847 token edges; mean cosine 0.124595
- C3 to C5: 675 token edges; mean cosine 0.132426
- C2 to C3: 669 token edges; mean cosine 0.131506
- C2 to C6: 554 token edges; mean cosine 0.135851
- C1 to C6: 455 token edges; mean cosine 0.126434
- C0 to C6: 450 token edges; mean cosine 0.122071
- C2 to C5: 424 token edges; mean cosine 0.127119
- C0 to C7: 375 token edges; mean cosine 0.123941
- C1 to C7: 354 token edges; mean cosine 0.125370
- C1 to C2: 301 token edges; mean cosine 0.120295

#### negative_tail

- Nodes: 5661
- Directed 10-NN edges: 56610
- Undirected edges: 39355
- Communities: 13
- Modularity: 0.485821

All communities:

- C0 (n=1174): representatives [삻, _done, .setBackgroundResource, ␠WPARAM, ␠OnCollision, ✽, /filepath, .getSystemService, ␠CONT, ROSS]; target-extreme [Jvm, -cond, /name, .bukkit, 🉑, .settings]; classes {'alphabetic': 576, 'mixed': 578, 'punctuation': 20}
- C1 (n=1121): representatives [攻势, ␠insecurity, ␠exclusion, Companies, ␠promising, ␠preached, ␠TEST, ␠accessibility, ␠activism, ␠일이]; target-extreme [宣告, 齐聚, ⽐, 过度, ␠Lightweight, _testing]; classes {'alphabetic': 1048, 'mixed': 72, 'punctuation': 1}
- C2 (n=900): representatives [Hugh, ␠Carrie, 戏曲, ␠liber, ␠Jenna, ␠Herr, ␠Пар, ␠Hannah, ␠Angola, ␠pne]; target-extreme [␠Curry, ␠Bott, ␠Johnny, Berry, Jerry, ␠Tex]; classes {'alphabetic': 879, 'mixed': 21}
- C3 (n=671): representatives [а, и, ing, e, ا, ์, i, е, ␠É, 了]; target-extreme [у, Æ, ся, ␠sû, 매, ␠الز]; classes {'alphabetic': 576, 'mixed': 23, 'punctuation': 70, 'whitespace': 2}
- C4 (n=506): representatives [␠بلا, ␠cioè, ␠без, 更具, ␠jede, ␠وذلك, ␠две, 協助, ␠notamment, ␠Simple]; target-extreme [␠без, ␠correctamente, EXAMPLE, 協助, ␠succès, ␠még]; classes {'alphabetic': 482, 'mixed': 23, 'punctuation': 1}
- C5 (n=270): representatives [=<?=$, ␠[&, ]))), {{$, ␠{{$, ~, ([&, ="<?=$, ={()=>, =[],]; target-extreme [$$, ={(), ％, ␠=&, ([&, {]; classes {'alphabetic': 10, 'mixed': 26, 'punctuation': 232, 'whitespace': 2}
- C6 (n=269): representatives [�, ﾞ, �, �, �, 流, �, 型, �, �]; target-extreme [�, 净, 牢, �, �, �]; classes {'alphabetic': 218, 'mixed': 1, 'punctuation': 50}
- C7 (n=227): representatives [␠получа, ␠univers, ILI, Appro, ␠предоставля, ␠appro, ␠immedi, ␠atmos, ␠наз, бро]; target-extreme [␠inexp, ␠механиз, ␠выполня, ␠DECL, ␠appro, Poss]; classes {'alphabetic': 207, 'mixed': 20}
- C8 (n=176): representatives [💨, 🏦, 💵, 🏭, ≜, 🏩, ﯭ, 쐉, 📺, ]; target-extreme [摩托, 떴, ✾, 🆓, ✗, 🏪]; classes {'alphabetic': 76, 'mixed': 2, 'numeric': 1, 'punctuation': 97}
- C9 (n=124): representatives [第一家, 金陵, 第七届, 全国, 万人次, 十几个, 百分之, REST, -mile, 八大]; target-extreme [万人次, ␠семь, 第七届, 几张, 上年, 笫]; classes {'alphabetic': 116, 'mixed': 7, 'numeric': 1}
- C10 (n=100): representatives [CCI, ␠mongo, ␠App, ACC, ␠PPC, .dev, ␠Azure, ␠EMP, .models, 中国移动]; target-extreme [.vis, .http, ␠PPC, ␠HTTP, ␠SEC, .db]; classes {'alphabetic': 65, 'mixed': 35}
- C11 (n=98): representatives [␠of, ␠shows, ␠about, Shows, _Show, ␠For, ␠de, ␠up, for, ␠return]; target-extreme [␠of, ␠for, ␠with, ␠OF, ␠to, import]; classes {'alphabetic': 79, 'mixed': 18, 'punctuation': 1}
- C12 (n=25): representatives [客户, ␠customer, Users, ␠клиент, .product, ␠clientes, 顾客, ␠Customers, CLIENT, ␠Guests]; target-extreme [␠clientes, Users, /User, ␠клиент, ␠Visitors, .product]; classes {'alphabetic': 17, 'mixed': 8}

Strongest intercommunity connections:

- C0 to C1: 1694 token edges; mean cosine 0.127197
- C0 to C2: 1161 token edges; mean cosine 0.128968
- C1 to C2: 1020 token edges; mean cosine 0.128027
- C1 to C4: 884 token edges; mean cosine 0.131019
- C0 to C3: 633 token edges; mean cosine 0.126488
- C2 to C3: 619 token edges; mean cosine 0.130630
- C0 to C4: 582 token edges; mean cosine 0.128187
- C0 to C7: 481 token edges; mean cosine 0.128668
- C3 to C4: 450 token edges; mean cosine 0.133216
- C1 to C6: 442 token edges; mean cosine 0.134642
- C1 to C7: 441 token edges; mean cosine 0.129392
- C2 to C7: 410 token edges; mean cosine 0.130953
- C3 to C6: 394 token edges; mean cosine 0.145180
- C1 to C3: 391 token edges; mean cosine 0.125314
- C2 to C4: 374 token edges; mean cosine 0.129646

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5959
- Directed 10-NN edges: 59590
- Undirected edges: 42767
- Communities: 7
- Modularity: 0.546699

All communities:

- C0 (n=1331): representatives [㨳, pushViewController, ␠şikay, ␠wyśw, 룁, ␠ucfirst, .EditorButton, 턔, ␠spriteBatch, .visitMethodInsn]; target-extreme [myśl, 𐤔, ␠swal, 퓬, ␠ransom, 턔]; classes {'alphabetic': 1166, 'mixed': 101, 'punctuation': 64}
- C1 (n=1292): representatives [␠kitchen, ␠priests, ␠apartment, ␠kittens, ␠cupboard, ␠scratched, 卧室, osterone, ␠deprived, ␠report]; target-extreme [␠lieutenant, ␠intervention, ␠scratched, ␠street, distinct, ␠timetable]; classes {'alphabetic': 1215, 'mixed': 77}
- C2 (n=1226): representatives [뤗, 떘, ak, ain, ton, son, ik, 읩, ut, av]; target-extreme [oningen, عون, ameleon, wish, tridge, kas]; classes {'alphabetic': 1193, 'mixed': 32, 'punctuation': 1}
- C3 (n=710): representatives [ются, になると, ようになりました, дается, ивают, からない, ␠شيء, であれば, malıdır, ␠الأخرى]; target-extreme [irse, 不會, cych, ␠entrar, ␠לעמוד, ällt]; classes {'alphabetic': 696, 'mixed': 13, 'punctuation': 1}
- C4 (n=578): representatives [');\r\n\r\n, "))\r\n, ));\n\n, ));\r\n, ")\r\n, ));\r\n\r\n, ')\r\n\r\n, '))\r\n, ','');\n, ');\r\n]; target-extreme [}");\r\n, "]}\n, (',');\n, ␠')\n, ␠␠␠␠\t\t\n, ]);\r\n\r\n]; classes {'alphabetic': 6, 'mixed': 13, 'punctuation': 538, 'whitespace': 21}
- C5 (n=495): representatives [\tds, CP, (indexPath, DP, TD, \ttypedef, (ds, _cf, MD, PD]; target-extreme [[l, (sprite, fontsize, *k, /T, DK]; classes {'alphabetic': 310, 'mixed': 170, 'numeric': 1, 'punctuation': 14}
- C6 (n=327): representatives [.getOrElse, strncmp, actionDate, getWidth, ␠setDate, ␠memcpy, ␠richTextBox, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠dataGridView, textbox]; target-extreme [overwrite, cmb, \tstrncpy, onedDateTime, ␠getColor, ␠radioButton]; classes {'alphabetic': 202, 'mixed': 96, 'punctuation': 9, 'whitespace': 20}

Strongest intercommunity connections:

- C1 to C2: 2013 token edges; mean cosine 0.129788
- C0 to C1: 1288 token edges; mean cosine 0.127690
- C0 to C3: 1194 token edges; mean cosine 0.132370
- C0 to C2: 1044 token edges; mean cosine 0.127970
- C2 to C3: 890 token edges; mean cosine 0.128699
- C1 to C3: 870 token edges; mean cosine 0.126168
- C2 to C5: 797 token edges; mean cosine 0.131665
- C0 to C6: 779 token edges; mean cosine 0.133696
- C0 to C5: 493 token edges; mean cosine 0.126499
- C1 to C5: 479 token edges; mean cosine 0.125103
- C1 to C6: 447 token edges; mean cosine 0.122998
- C2 to C6: 341 token edges; mean cosine 0.121713
- C5 to C6: 297 token edges; mean cosine 0.127456
- C3 to C6: 211 token edges; mean cosine 0.125438
- C3 to C5: 194 token edges; mean cosine 0.123172

#### negative_tail

- Nodes: 6310
- Directed 10-NN edges: 63100
- Undirected edges: 43924
- Communities: 11
- Modularity: 0.493840

All communities:

- C0 (n=1001): representatives [삻, _done, ␠CONT, .AR, ␠TEMP, ROSS, -work, .COMP, _Settings, ␠HALF]; target-extreme [/name, .settings, Shows, -loss, _acc, .att]; classes {'alphabetic': 381, 'mixed': 620}
- C1 (n=937): representatives [Hugh, ␠Carrie, ␠airline, ␠Melania, ␠Jenna, 戏曲, ␠promising, ␠Herr, ␠Ends, ␠Angola]; target-extreme [␠Curry, ␠Johnny, ␠Bott, Jerry, ␠Finland, ␠Giul]; classes {'alphabetic': 916, 'mixed': 21}
- C2 (n=811): representatives [␠insecurity, Companies, ␠TEST, ␠experimentation, 協助, Training, ␠accessibility, ␠organizational, ␠motivational, Tests]; target-extreme [净, 过度, ⽐, 万人次, ␠clientes, ␠Farm]; classes {'alphabetic': 773, 'mixed': 36, 'punctuation': 2}
- C3 (n=791): representatives [.setBackgroundResource, ␠WPARAM, ␠OnCollision, .getSystemService, /filepath, ✽, 💨, ␠HttpServletResponse, ␠StatelessWidget, DidAppear]; target-extreme [Jvm, 摩托, 🉑, .bukkit, ␠gı, .Automation]; classes {'alphabetic': 524, 'mixed': 146, 'punctuation': 121}
- C4 (n=678): representatives [а, ing, и, e, i, ا, е, ์, é, Á]; target-extreme [у, ␠sû, ся, Æ, ّ, ␠الز]; classes {'alphabetic': 630, 'mixed': 17, 'punctuation': 31}
- C5 (n=609): representatives [␠exclusion, ␠RECE, ␠liber, ␠получа, ␠thỏa, ␠yaygın, 准备, ␠продук, ␠турист, ␠automobile]; target-extreme [␠inexp, -cond, ␠pard, ␠механиз, ␠продук, ␠выполня]; classes {'alphabetic': 579, 'mixed': 29, 'punctuation': 1}
- C6 (n=471): representatives [␠بلا, 更具, ␠без, ␠وذلك, ␠cioè, ほとんど, ␠две, ␠jede, 就能, ␠pessoas]; target-extreme [␠семь, ␠без, 第七届, ␠jede, 几张, ␠بلا]; classes {'alphabetic': 458, 'mixed': 12, 'numeric': 1}
- C7 (n=323): representatives [=<?=$, ~,, ]))), ␠{{$, ={()=>, ␠[&, ≜, ~, ="<?=$, =[],]; target-extreme [$$, ={(), ％, {, ([&, ␠$($]; classes {'alphabetic': 23, 'mixed': 15, 'numeric': 1, 'punctuation': 280, 'whitespace': 4}
- C8 (n=313): representatives [攻势, ␠straightforward, ␠일이, ␠positively, area, ␠Elementary, ␠areas, ␠Simple, ␠hypothetical, ␠slightly]; target-extreme [␠Lightweight, ␠correctamente, Uses, .Simple, EXAMPLE, ␠brisk]; classes {'alphabetic': 293, 'mixed': 20}
- C9 (n=249): representatives [�, �, �, �, �, ﾞ, �, �, �, �]; target-extreme [�, 宣告, �, 牢, �, �]; classes {'alphabetic': 170, 'mixed': 2, 'punctuation': 77}
- C10 (n=127): representatives [␠of, ␠preached, 的, for, ␠Making, ␠return, ␠about, ␠For, ␠up, ho]; target-extreme [␠of, ␠for, ␠with, ␠OF, ␠to, import]; classes {'alphabetic': 113, 'mixed': 12, 'punctuation': 2}

Strongest intercommunity connections:

- C0 to C1: 1040 token edges; mean cosine 0.129709
- C0 to C5: 913 token edges; mean cosine 0.131164
- C0 to C3: 867 token edges; mean cosine 0.122031
- C1 to C5: 825 token edges; mean cosine 0.132418
- C2 to C3: 747 token edges; mean cosine 0.130363
- C0 to C2: 732 token edges; mean cosine 0.127767
- C2 to C5: 729 token edges; mean cosine 0.131436
- C1 to C2: 668 token edges; mean cosine 0.129526
- C1 to C3: 580 token edges; mean cosine 0.128373
- C1 to C4: 561 token edges; mean cosine 0.133275
- C3 to C5: 524 token edges; mean cosine 0.128863
- C2 to C8: 518 token edges; mean cosine 0.132639
- C2 to C6: 477 token edges; mean cosine 0.131991
- C4 to C6: 459 token edges; mean cosine 0.139359
- C4 to C5: 436 token edges; mean cosine 0.135657

## State 16 — block_15_output

Paired positive_head: membership Jaccard 0.870476; edge Jaccard 0.720357; shared tokens 5484.
Paired negative_tail: membership Jaccard 0.874981; edge Jaccard 0.716649; shared tokens 5739.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5945
- Directed 10-NN edges: 59450
- Undirected edges: 42323
- Communities: 10
- Modularity: 0.544069

All communities:

- C0 (n=1512): representatives [떘, ␠transformations, 猫咪, ␠kitchen, ␠priests, características, ␠cut, ␠deprived, sensor, ␠distributor]; target-extreme [␠scratched, overwrite, ␠lieutenant, ␠spoon, ␠intervention, ␠strapped]; classes {'alphabetic': 1448, 'mixed': 64}
- C1 (n=1054): representatives [㨳, ␠şikay, 룁, ␠wyśw, więt, .EditorButton, 턔, 漦, ␠açıklama, 圙]; target-extreme [屉, 𐤔, 퓬, ␠לעמוד, מסוגל, 닢]; classes {'alphabetic': 988, 'mixed': 8, 'punctuation': 58}
- C2 (n=941): representatives [ются, ak, ik, ain, <tool_call>, ton, son, ut, ka, дается]; target-extreme [irse, kes, wish, عون, oningen, oods]; classes {'alphabetic': 926, 'mixed': 11, 'punctuation': 4}
- C3 (n=737): representatives [pushViewController, ␠spriteBatch, .visitMethodInsn, igrationBuilder, .ToolStripButton, .RemoveAt, .DropDownStyle, .TabStop, ␠CGRectMake, .getOrElse]; target-extreme [␠swal, \tstrncpy, \tImGui, .DropDownStyle, ␠subscribe, ␠radioButton]; classes {'alphabetic': 503, 'mixed': 231, 'punctuation': 3}
- C4 (n=554): representatives [になると, を持っている, ってる, ようになりました, んでいる, することは, てしまった, 学生们, ␠شيء, だったので]; target-extreme [␠patiënt, 不會, ␠küçük, ␠entrar, ␠publié, 人たち]; classes {'alphabetic': 541, 'mixed': 13}
- C5 (n=549): representatives [\tds, (ds, \tcp, \tfs, CP, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \tdf, sr, PD, \tdp]; target-extreme [*k, cmb, /T, \tboard, (sprite, ␠kne]; classes {'alphabetic': 325, 'mixed': 194, 'numeric': 1, 'punctuation': 13, 'whitespace': 16}
- C6 (n=418): representatives [');\r\n\r\n, "))\r\n, ')\r\n\r\n, '))\r\n, ))\r\n, ');\r\n, ")\r\n, ));\r\n\r\n, '\r\n, }")\n]; target-extreme [}");\r\n, 。”\n\n, ␠')\n, (',');\n, ␠');\n, "]}\n]; classes {'alphabetic': 3, 'mixed': 8, 'punctuation': 391, 'whitespace': 16}
- C7 (n=121): representatives [␠Portsmouth, ington, smouth, ␠Cincinnati, 特朗普, ␠Snapchat, instein, ␠Montgomery, ␠brown, ␠Scarborough]; target-extreme [tridge, ameleon, uffman, xford, ␠Tumblr, ␠Augustine]; classes {'alphabetic': 117, 'mixed': 4}
- C8 (n=34): representatives [␠不, ␠�, ␠�, ␠�, ␠remove, ␠和, ␠生, ␠�, ␠下, ␠�]; target-extreme [␠�, ␠删除, ␠�, ␠�, ␠生, ␠商品]; classes {'alphabetic': 13, 'mixed': 5, 'punctuation': 16}
- C9 (n=25): representatives [丛书, DOI, book, ␠ISBN, ␠isbn, öffent, ␠thumbs, ␠DOI, ␠Ebook, ␠책]; target-extreme [␠thumbs, doi, ␠ebook, 丛书, öffent, ␠eBook]; classes {'alphabetic': 24, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C2: 1495 token edges; mean cosine 0.127663
- C1 to C3: 1358 token edges; mean cosine 0.132104
- C0 to C1: 1136 token edges; mean cosine 0.129953
- C0 to C3: 1101 token edges; mean cosine 0.125156
- C0 to C4: 933 token edges; mean cosine 0.128781
- C1 to C4: 867 token edges; mean cosine 0.135416
- C1 to C2: 683 token edges; mean cosine 0.126983
- C2 to C4: 617 token edges; mean cosine 0.132728
- C2 to C5: 594 token edges; mean cosine 0.134544
- C0 to C5: 530 token edges; mean cosine 0.127100
- C3 to C5: 515 token edges; mean cosine 0.124711
- C3 to C4: 412 token edges; mean cosine 0.128718
- C2 to C3: 354 token edges; mean cosine 0.120126
- C0 to C7: 299 token edges; mean cosine 0.131696
- C1 to C5: 282 token edges; mean cosine 0.126845

#### negative_tail

- Nodes: 6323
- Directed 10-NN edges: 63230
- Undirected edges: 44034
- Communities: 11
- Modularity: 0.508139

All communities:

- C0 (n=1423): representatives [_done, ROSS, Concurrency, _Dep, ␠CONT, _Settings, -work, .AR, _Ad, Companies]; target-extreme [.settings, ␠Creating, ␠Auxiliary, ␠inexp, Adj, -cond]; classes {'alphabetic': 742, 'mixed': 681}
- C1 (n=1070): representatives [␠işle, efully, .setBackgroundResource, ␠RelayCommand, .getSystemService, 攻势, 母校, ✽, ␠Melania, ␠получа]; target-extreme [Jvm, 牢, .bukkit, 摩托, 🉑, ␠alf]; classes {'alphabetic': 795, 'mixed': 136, 'punctuation': 139}
- C2 (n=1021): representatives [␠insecurity, area, ␠Reduction, 创新, ␠joints, ␠experimentation, 提升, 影视, 加持, ␠accessibility]; target-extreme [支援, ␠Uses, 定律, 污染, ␠clientes, 處理]; classes {'alphabetic': 1005, 'mixed': 16}
- C3 (n=891): representatives [а, ي, ا, �, и, ์, �, Á, e, �]; target-extreme [�, у, �, Æ, ся, �]; classes {'alphabetic': 784, 'mixed': 23, 'punctuation': 83, 'whitespace': 1}
- C4 (n=794): representatives [Hugh, ␠Carrie, ␠stark, ␠Herr, Jimmy, Johnny, ␠Ends, ␠Ghana, ␠Sandra, ␠Anthony]; target-extreme [␠Farm, ␠Betty, ␠Manning, Johnny, ␠Bij, ␠Finland]; classes {'alphabetic': 779, 'mixed': 15}
- C5 (n=493): representatives [␠بلا, ␠במיוחד, 最常见的, ␠без, 更具, ␠две, ␠positively, ␠اللا, ␠speeds, ␠succès]; target-extreme [␠без, .Simple, ␠igual, 过度, ␠correctamente, ずっと]; classes {'alphabetic': 479, 'mixed': 13, 'punctuation': 1}
- C6 (n=351): representatives [="<?=$, =<?=$, ={()=>, }());\n, $$, ␠[&, ␠},\n\n\n, ␠{{$, "><?=$, ]; target-extreme [$$, ={(), ّ, ％, Ј, 〜]; classes {'alphabetic': 33, 'mixed': 24, 'numeric': 2, 'punctuation': 285, 'special': 1, 'whitespace': 6}
- C7 (n=112): representatives [␠of, 的, ␠up, ␠behind, ␠de, ␠about, for, with, ␠neben, ␠on]; target-extreme [␠of, ␠for, ␠with, ␠OF, with, import]; classes {'alphabetic': 93, 'mixed': 19}
- C8 (n=77): representatives [␠terrible, 庞大的, 这么大, ␠huge, ␠Azure, ␠countless, ␠Dirty, 巨额, huge, ␠Awesome]; target-extreme [净, azor, ␠battered, ␠ample, .AWS, ネット]; classes {'alphabetic': 71, 'mixed': 6}
- C9 (n=46): representatives [万人次, esterday, 第七届, million, 百分之, 万元, 十万, 萬, 百亿, ␠triệu]; target-extreme [第七届, ␠семь, 万人次, 百分之, weekday, ␠tỉ]; classes {'alphabetic': 42, 'mixed': 3, 'numeric': 1}
- C10 (n=45): representatives [␠adjacent, �, �, �, ␠adjoining, �, ␠adjacency, �, �, �]; target-extreme [�, �, ␠adjacent, ␠adjoining, 笫, Adjacent]; classes {'alphabetic': 19, 'punctuation': 26}

Strongest intercommunity connections:

- C0 to C2: 1442 token edges; mean cosine 0.131942
- C0 to C1: 1383 token edges; mean cosine 0.125523
- C0 to C4: 1281 token edges; mean cosine 0.130410
- C1 to C2: 1262 token edges; mean cosine 0.130255
- C1 to C3: 946 token edges; mean cosine 0.133187
- C2 to C3: 771 token edges; mean cosine 0.133175
- C1 to C4: 725 token edges; mean cosine 0.129147
- C2 to C4: 713 token edges; mean cosine 0.129427
- C3 to C4: 622 token edges; mean cosine 0.131150
- C2 to C5: 610 token edges; mean cosine 0.135766
- C1 to C5: 599 token edges; mean cosine 0.133942
- C3 to C5: 579 token edges; mean cosine 0.137418
- C0 to C3: 512 token edges; mean cosine 0.123599
- C0 to C5: 496 token edges; mean cosine 0.132831
- C1 to C6: 359 token edges; mean cosine 0.132585

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5839
- Directed 10-NN edges: 58390
- Undirected edges: 41670
- Communities: 10
- Modularity: 0.539274

All communities:

- C0 (n=1284): representatives [떘, ␠transformations, 猫咪, ␠kitchen, ␠priests, ␠deprived, 卧室, ␠underscores, ␠scratched, sensor]; target-extreme [␠lieutenant, ␠scratched, ␠intervention, ␠spoon, ␠twilight, ameleon]; classes {'alphabetic': 1234, 'mixed': 50}
- C1 (n=1092): representatives [㨳, ␠şikay, ␠wyśw, 룁, 턔, .EditorButton, więt, 漦, 圙, ␠açıklama]; target-extreme [屉, 퓬, 𐤔, ␠לעמוד, 닢, 鲎]; classes {'alphabetic': 1015, 'mixed': 17, 'punctuation': 60}
- C2 (n=793): representatives [ются, ak, son, ik, <tool_call>, ton, дается, ut, ek, ka]; target-extreme [irse, wish, kes, عون, oods, ␠cate]; classes {'alphabetic': 774, 'mixed': 17, 'punctuation': 2}
- C3 (n=727): representatives [pushViewController, ␠spriteBatch, .visitMethodInsn, igrationBuilder, .TabStop, .ToolStripButton, .DropDownStyle, .RemoveAt, ␠CGRectMake, .titleLabel]; target-extreme [␠swal, \tstrncpy, \tImGui, .DropDownStyle, INFRINGEMENT, ␠AUTHORS]; classes {'alphabetic': 483, 'mixed': 244}
- C4 (n=598): representatives [になると, を持っている, características, ようになりました, だったので, 学生们, することは, ␠شيء, ␠모습, داعش]; target-extreme [不會, ␠patiënt, ␠entrar, season, ␠küçük, ␠publié]; classes {'alphabetic': 586, 'mixed': 12}
- C5 (n=460): representatives ["))\r\n, ');\r\n\r\n, ))\r\n, ')\r\n\r\n, }")\n, ));\r\n, "))\n, ');\r\n, ")\r\n, '\r\n]; target-extreme [}");\r\n, 。”\n\n, ␠')\n, (',');\n, "]}\n, ␠');\n]; classes {'alphabetic': 5, 'mixed': 4, 'numeric': 1, 'punctuation': 421, 'whitespace': 29}
- C6 (n=432): representatives [\tds, (ds, \tfs, \tcp, CP, MD, PD, \tdf, [l, ␠dm]; target-extreme [*k, cmb, (sprite, /T, [l, rk]; classes {'alphabetic': 267, 'mixed': 163, 'punctuation': 2}
- C7 (n=289): representatives [␠cut, ␠don, ␠slipped, ␠notifying, ␠reacted, ␠stimulated, ␠washed, umbed, ␠report, ␠overl]; target-extreme [overwrite, plemented, ␠cry, ␠tipped, ␠instruct, ␠although]; classes {'alphabetic': 279, 'mixed': 10}
- C8 (n=125): representatives [␠Portsmouth, ington, smouth, raham, ␠Snapchat, ␠Cincinnati, 特朗普, instein, ␠Scarborough, ␠Montgomery]; target-extreme [oningen, tridge, xford, 쟙, ompson, ␠Snape]; classes {'alphabetic': 123, 'mixed': 2}
- C9 (n=39): representatives [␠проис, ␠�, ␠�, ␠不, ␠和, ␠�, ␠生, ␠�, ␠�, ␠�]; target-extreme [␠生命周期, ��态, ␠�, ␠生, ␠�, ␠�]; classes {'alphabetic': 18, 'mixed': 2, 'punctuation': 18, 'whitespace': 1}

Strongest intercommunity connections:

- C1 to C3: 1316 token edges; mean cosine 0.133004
- C0 to C2: 1188 token edges; mean cosine 0.127705
- C1 to C4: 1102 token edges; mean cosine 0.135427
- C0 to C3: 990 token edges; mean cosine 0.124764
- C0 to C1: 987 token edges; mean cosine 0.129908
- C0 to C7: 758 token edges; mean cosine 0.135345
- C0 to C4: 679 token edges; mean cosine 0.127118
- C2 to C4: 618 token edges; mean cosine 0.132197
- C1 to C2: 597 token edges; mean cosine 0.126327
- C2 to C6: 534 token edges; mean cosine 0.127536
- C3 to C6: 423 token edges; mean cosine 0.126565
- C2 to C3: 387 token edges; mean cosine 0.120194
- C3 to C4: 361 token edges; mean cosine 0.123757
- C0 to C6: 330 token edges; mean cosine 0.125274
- C0 to C8: 305 token edges; mean cosine 0.129254

#### negative_tail

- Nodes: 5975
- Directed 10-NN edges: 59750
- Undirected edges: 41680
- Communities: 10
- Modularity: 0.506850

All communities:

- C0 (n=1252): representatives [_done, ROSS, Concurrency, ␠CONT, _Dep, .AR, ␠HALF, /filepath, ␠получа, area]; target-extreme [␠Auxiliary, ␠Creating, .settings, ␠inexp, .Flag, -cond]; classes {'alphabetic': 643, 'mixed': 609}
- C1 (n=931): representatives [母校, ␠Melania, ␠insecurity, ␠thỏa, 创新, 提升, 戏曲, 接力, 安全, 庞大的]; target-extreme [摩托, ␠clientes, 定律, 上年, 處理, 宣告]; classes {'alphabetic': 920, 'mixed': 8, 'punctuation': 3}
- C2 (n=879): representatives [а, и, ␠of, ا, ي, ์, e, ing, Á, ışı]; target-extreme [␠of, ␠for, ␠with, у, ␠OF, with]; classes {'alphabetic': 814, 'mixed': 37, 'punctuation': 27, 'whitespace': 1}
- C3 (n=775): representatives [␠terrible, Hugh, ␠Carrie, ␠promising, Jimmy, Johnny, ␠Sandra, ␠Miche, ␠Jenna, ␠Herr]; target-extreme [␠Farm, ␠Manning, Johnny, ␠Betty, ␠Bij, ␠Curry]; classes {'alphabetic': 764, 'mixed': 11}
- C4 (n=627): representatives [␠RelayCommand, .setBackgroundResource, ✽, .getSystemService, 💨, ␠HttpServletResponse, ␠AssemblyCompany, 💵, 🏦, 🏭]; target-extreme [Jvm, .bukkit, 🉑, 떴, _testing, azor]; classes {'alphabetic': 338, 'mixed': 156, 'punctuation': 133}
- C5 (n=548): representatives [תחילת, ␠بلا, 最常见的, ␠일이, 更具, ␠positively, אני, からの, ␠две, роме]; target-extreme [第七届, .Simple, ␠семь, ずっと, ␠без, ␠igual]; classes {'alphabetic': 527, 'mixed': 19, 'numeric': 1, 'punctuation': 1}
- C6 (n=363): representatives [=<?=$, ="<?=$, $$, ␠!, ␠{{$, ={()=>, "><?=$, ,$, {{$, ␠[&]; target-extreme [$$, import, ={(), Ј, ％, ␠import]; classes {'alphabetic': 50, 'mixed': 31, 'numeric': 3, 'punctuation': 274, 'whitespace': 5}
- C7 (n=292): representatives [�, 凡本网注, �, �, �, �, �, �, �, �]; target-extreme [�, �, �, 牢, �, 净]; classes {'alphabetic': 205, 'mixed': 1, 'punctuation': 86}
- C8 (n=260): representatives [␠perseverance, ␠accessibility, ␠experimentation, ␠scenarios, ␠joints, ␠Labs, ␠Surgery, ␠fluid, ␠networking, ␠activism]; target-extreme [支援, ␠Uses, ␠proven, ␠выполня, ␠mud, ␠networking]; classes {'alphabetic': 247, 'mixed': 13}
- C9 (n=48): representatives [␠shows, Shows, _Show, ␠journée, show, -show, .send, .show, ␠Projects, SHOW]; target-extreme [␠Shows, SHOW, Shows, .send, (show, ␠дня]; classes {'alphabetic': 36, 'mixed': 12}

Strongest intercommunity connections:

- C0 to C3: 1234 token edges; mean cosine 0.128699
- C0 to C4: 944 token edges; mean cosine 0.123254
- C0 to C1: 928 token edges; mean cosine 0.127671
- C1 to C5: 822 token edges; mean cosine 0.134117
- C1 to C3: 737 token edges; mean cosine 0.128448
- C1 to C4: 728 token edges; mean cosine 0.125345
- C2 to C5: 698 token edges; mean cosine 0.139637
- C0 to C2: 657 token edges; mean cosine 0.130404
- C1 to C2: 652 token edges; mean cosine 0.128777
- C0 to C5: 617 token edges; mean cosine 0.132234
- C0 to C8: 617 token edges; mean cosine 0.130547
- C2 to C3: 566 token edges; mean cosine 0.130056
- C1 to C8: 553 token edges; mean cosine 0.135498
- C2 to C7: 513 token edges; mean cosine 0.144610
- C1 to C7: 478 token edges; mean cosine 0.135655

## State 17 — block_16_output

Paired positive_head: membership Jaccard 0.848951; edge Jaccard 0.679010; shared tokens 5463.
Paired negative_tail: membership Jaccard 0.853996; edge Jaccard 0.688014; shared tokens 5621.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6000
- Directed 10-NN edges: 60000
- Undirected edges: 42706
- Communities: 10
- Modularity: 0.545602

All communities:

- C0 (n=991): representatives [ются, ak, ik, ments, <tool_call>, ut, ton, дается, man, og]; target-extreme [wish, kes, tridge, irse, otoxic, wróci]; classes {'alphabetic': 973, 'mixed': 13, 'punctuation': 5}
- C1 (n=961): representatives [뤗, 떘, 읩, ␠underscores, ␠kitchen, istrates, ␠apartment, ␠concentrations, ␠priests, ␠kittens]; target-extreme [␠lieutenant, ␠twilight, ␠timetable, ␠shadow, ␠monkey, codes]; classes {'alphabetic': 906, 'mixed': 53, 'punctuation': 2}
- C2 (n=870): representatives [业内人士, maktad, ␠açıklama, を持っている, características, を与え, ␠kutje, になると, ようになりました, ␠yayg]; target-extreme [מסוגל, ␠לעמוד, ällt, oningen, myśl, илас]; classes {'alphabetic': 850, 'mixed': 14, 'punctuation': 6}
- C3 (n=785): representatives [.EditorButton, ␠spriteBatch, .visitMethodInsn, imizeBox, .getOrElse, .DropDownStyle, .TabStop, THOOK, ␠hashtable, .ToolStripButton]; target-extreme [overwrite, .DropDownStyle, textbox, ␠ShoppingCart, ␠loadData, ␠getColor]; classes {'alphabetic': 532, 'mixed': 251, 'punctuation': 2}
- C4 (n=700): representatives [␠cut, ␠transformations, sticks, ␠sucking, ␠measurements, ␠soaked, ␠scratched, ␠report, ␠reacted, ␠soak]; target-extreme [␠strapped, piece, ␠subscribe, plemented, ␠interfer, ␠ransom]; classes {'alphabetic': 681, 'mixed': 19}
- C5 (n=652): representatives [␠şikay, 턔, 룁, więt, 漦, 馧, 믈, 닢, igrationBuilder, 폈]; target-extreme [𐤔, 屉, 댓, صند, 둡, 簟]; classes {'alphabetic': 602, 'mixed': 5, 'punctuation': 45}
- C6 (n=470): representatives [\tds, CP, \tfs, (ds, (bs, MD, (song, MT, (dateTime, mt]; target-extreme [cmb, fm, \tboard, *k, (com, mts]; classes {'alphabetic': 292, 'mixed': 176, 'numeric': 1, 'punctuation': 1}
- C7 (n=450): representatives [');\r\n\r\n, "))\r\n, ))\r\n, ")\r\n, ]))\r\n, ));\r\n\r\n, ')\r\n\r\n, ');\r\n, }")\n, '))\r\n]; target-extreme [}");\r\n, ␠')\n, (',');\n, 。”\n\n, ␠');\n, "]}\n]; classes {'alphabetic': 5, 'mixed': 3, 'punctuation': 424, 'whitespace': 18}
- C8 (n=72): representatives [␠don, ␠不, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠�, ␠␠␠␠␠␠␠␠\t\t, ␠doesn, ␠�, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠although, ␠doesn, ␠don, ␠elif, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠�]; classes {'alphabetic': 31, 'mixed': 2, 'punctuation': 19, 'whitespace': 20}
- C9 (n=49): representatives [␠Portsmouth, smouth, ␠Cincinnati, ␠Singapore, ␠Plymouth, ␠Scarborough, גרמנ, ␠Eastern, ipeg, ␠Winnipeg]; target-extreme [xford, ␠Malaysia, Scotland, foundland, ␠Winnipeg, ␠northeastern]; classes {'alphabetic': 49}

Strongest intercommunity connections:

- C1 to C4: 1248 token edges; mean cosine 0.131479
- C0 to C1: 1198 token edges; mean cosine 0.126895
- C2 to C5: 1133 token edges; mean cosine 0.134407
- C3 to C5: 933 token edges; mean cosine 0.134607
- C1 to C3: 872 token edges; mean cosine 0.126372
- C1 to C2: 841 token edges; mean cosine 0.130224
- C0 to C2: 786 token edges; mean cosine 0.129572
- C2 to C3: 775 token edges; mean cosine 0.129420
- C0 to C4: 685 token edges; mean cosine 0.131889
- C0 to C6: 669 token edges; mean cosine 0.133540
- C2 to C4: 593 token edges; mean cosine 0.128405
- C1 to C5: 566 token edges; mean cosine 0.131595
- C3 to C6: 431 token edges; mean cosine 0.125924
- C3 to C4: 413 token edges; mean cosine 0.128256
- C1 to C6: 385 token edges; mean cosine 0.125717

#### negative_tail

- Nodes: 6300
- Directed 10-NN edges: 63000
- Undirected edges: 43770
- Communities: 11
- Modularity: 0.501340

All communities:

- C0 (n=1183): representatives [_done, ␠curriculum, ␠Running, 攻势, ␠Assurance, _Settings, Concurrency, -work, ␠insecurity, ␠perseverance]; target-extreme [␠Farm, ␠Auxiliary, ␠Creating, 敏捷, 資源, ␠Ride]; classes {'alphabetic': 879, 'mixed': 304}
- C1 (n=879): representatives [а, ا, 车, �, и, �, �, ์, 凡本网注, e]; target-extreme [�, у, 牢, 瓜, �, フレ]; classes {'alphabetic': 744, 'mixed': 20, 'punctuation': 115}
- C2 (n=870): representatives [✽, ␠Melania, אני, ␠بلا, ✬, 戏曲, ␠thỏa, אפליק, ␠GUIStyle, 🉑]; target-extreme [🐀, ␠продук, ␠alf, ␠выполня, 摩托, ␠الز]; classes {'alphabetic': 698, 'mixed': 8, 'numeric': 1, 'punctuation': 163}
- C3 (n=812): representatives [ROSS, _Pro, _Dep, ␠RECE, ␠LAW, ␠Herr, ␠Miche, ␠Пар, _Ad, _Off]; target-extreme [␠Bij, ␠DECL, ␠inexp, ␠appro, ␠TELE, ␠PPC]; classes {'alphabetic': 570, 'mixed': 242}
- C4 (n=538): representatives [efully, ␠במיוחד, 體驗, ␠succès, からの, ␠été, ␠две, 不能, ␠sogar, さら]; target-extreme [␠example, ␠Và, 过度, 而出, תם, Adjacent]; classes {'alphabetic': 509, 'mixed': 28, 'punctuation': 1}
- C5 (n=523): representatives [.setBackgroundResource, ␠OnCollision, ␠HttpServletResponse, ␠MaterialPageRoute, ␠AppCompatActivity, DidAppear, ␠Xperia, _drvdata, ␠الاحت, @Inject]; target-extreme [Jvm, .bukkit, .Automation, azor, _customize, ␠Manga]; classes {'alphabetic': 269, 'mixed': 254}
- C6 (n=523): representatives [␠일이, ␠TEST, area, 创新, 提升, 创意, イベント, 加持, ␠ciné, 研发]; target-extreme [␠район, 古今, 形容, ␠clientes, 支援, 事故]; classes {'alphabetic': 505, 'mixed': 16, 'numeric': 1, 'punctuation': 1}
- C7 (n=402): representatives [␠Macedonia, ␠Carrie, ␠Angola, ␠Jenna, ␠Archer, ␠Ghana, Johnny, ␠Sandra, zano, ␠Georgia]; target-extreme [Johnny, ␠Curry, ␠Giul, ␠Finland, ␠Ferrari, ␠Madison]; classes {'alphabetic': 397, 'mixed': 5}
- C8 (n=322): representatives [=<?=$, ="<?=$, ␠{{$, {{$, }}}, >{{$, "><?=$, ␠_______,, ␠@{$, ~]; target-extreme [$$, ّ, {, ː, 〜, ـ]; classes {'alphabetic': 16, 'mixed': 23, 'numeric': 2, 'punctuation': 277, 'whitespace': 4}
- C9 (n=137): representatives [␠of, ␠Behind, 的, ␠без, ␠up, ␠behind, ␠about, for, ␠neben, ␠de]; target-extreme [␠of, ␠for, import, ␠with, ␠to, 的]; classes {'alphabetic': 109, 'mixed': 26, 'punctuation': 2}
- C10 (n=111): representatives [á, É, é, ␠É, Á, ␠é, â, ité, í, ␠À]; target-extreme [Æ, ␠sû, ␠Я, ␠È, ␠géné, ␠gén]; classes {'alphabetic': 106, 'mixed': 2, 'punctuation': 3}

Strongest intercommunity connections:

- C0 to C3: 1290 token edges; mean cosine 0.127418
- C0 to C6: 992 token edges; mean cosine 0.132959
- C1 to C2: 976 token edges; mean cosine 0.134904
- C0 to C5: 907 token edges; mean cosine 0.122625
- C0 to C2: 735 token edges; mean cosine 0.129098
- C0 to C4: 720 token edges; mean cosine 0.133383
- C2 to C4: 592 token edges; mean cosine 0.134720
- C2 to C5: 587 token edges; mean cosine 0.125612
- C0 to C7: 582 token edges; mean cosine 0.130186
- C3 to C5: 577 token edges; mean cosine 0.124035
- C2 to C6: 559 token edges; mean cosine 0.129742
- C1 to C6: 557 token edges; mean cosine 0.136166
- C2 to C3: 554 token edges; mean cosine 0.129600
- C1 to C4: 479 token edges; mean cosine 0.133530
- C0 to C1: 477 token edges; mean cosine 0.130214

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5898
- Directed 10-NN edges: 58980
- Undirected edges: 42131
- Communities: 9
- Modularity: 0.546598

All communities:

- C0 (n=1206): representatives [뤗, ␠şikay, CppCodeGenWriteBarrier, .EditorButton, 턔, 룁, więt, .visitMethodInsn, ␠spriteBatch, 漦]; target-extreme [屉, .DropDownStyle, 𐤔, ␠לעמוד, oningen, myśl]; classes {'alphabetic': 1012, 'mixed': 141, 'punctuation': 53}
- C1 (n=978): representatives [␠microphone, ␠hashtable, 읩, ␠Portsmouth, ␠transformations, ␠kitchen, ␠underscores, ␠priests, ␠cupboard, istrates]; target-extreme [␠lieutenant, ␠twilight, tridge, ameleon, ␠drawback, ␠shadow]; classes {'alphabetic': 904, 'mixed': 73, 'punctuation': 1}
- C2 (n=861): representatives [ak, ются, ut, ik, ton, man, ington, og, ek, ston]; target-extreme [wish, kes, piece, ␠cate, irse, ood]; classes {'alphabetic': 850, 'mixed': 8, 'punctuation': 3}
- C3 (n=774): representatives [业内人士, を持っている, дается, を与え, ようになりました, características, になると, quisar, ивают, んでいる]; target-extreme [מסוגל, ällt, wróci, 好吗, cych, ␠patiënt]; classes {'alphabetic': 757, 'mixed': 17}
- C4 (n=663): representatives [<tool_call>, \tds, CP, (ds, \tfs, 𝑽, 븓, (song, (dateTime, (indexPath]; target-extreme [cmb, yp, fm, *k, (com, \tboard]; classes {'alphabetic': 449, 'mixed': 212, 'numeric': 1, 'punctuation': 1}
- C5 (n=636): representatives [떘, ␠cut, ␠misdemean, ␠scratched, ␠reacted, ␠soaked, ␠deleting, ␠dragged, ␠clipped, ␠stimulated]; target-extreme [overwrite, ␠strapped, ␠ransom, plemented, ␠bargain, umbling]; classes {'alphabetic': 611, 'mixed': 25}
- C6 (n=456): representatives ["))\r\n, ');\r\n\r\n, ")\r\n, ))\r\n, ));\r\n\r\n, ]))\r\n, '))\r\n, ])\n, ');\r\n, }")\n]; target-extreme [}");\r\n, ␠')\n, (',');\n, ␠');\n, 。”\n\n, "]}\n]; classes {'alphabetic': 4, 'mixed': 1, 'punctuation': 432, 'whitespace': 19}
- C7 (n=244): representatives [textbox, ␠dataGridView, ␠mName, getWidth, ␠richTextBox, tableName, ␠minLength, ␠rowIndex, .IsChecked, actionDate]; target-extreme [textbox, ␠loadData, ␠getColor, ␠getEmail, fontSize, ␠ShoppingCart]; classes {'alphabetic': 192, 'mixed': 52}
- C8 (n=80): representatives [␠don, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠不, ␠�, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠�, ␠doesn, ␠didn]; target-extreme [␠although, ␠生命周期, ␠doesn, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠don, ␠elif]; classes {'alphabetic': 35, 'mixed': 2, 'punctuation': 24, 'whitespace': 19}

Strongest intercommunity connections:

- C0 to C3: 1372 token edges; mean cosine 0.133734
- C1 to C2: 1177 token edges; mean cosine 0.130891
- C0 to C1: 1151 token edges; mean cosine 0.128624
- C1 to C5: 1149 token edges; mean cosine 0.131875
- C2 to C4: 825 token edges; mean cosine 0.131303
- C1 to C3: 699 token edges; mean cosine 0.127377
- C2 to C5: 644 token edges; mean cosine 0.130176
- C2 to C3: 636 token edges; mean cosine 0.130404
- C0 to C7: 597 token edges; mean cosine 0.138565
- C1 to C4: 592 token edges; mean cosine 0.126438
- C3 to C5: 524 token edges; mean cosine 0.126857
- C0 to C4: 524 token edges; mean cosine 0.124798
- C0 to C5: 522 token edges; mean cosine 0.126236
- C0 to C2: 467 token edges; mean cosine 0.123770
- C4 to C5: 301 token edges; mean cosine 0.126049

#### negative_tail

- Nodes: 5903
- Directed 10-NN edges: 59030
- Undirected edges: 41051
- Communities: 11
- Modularity: 0.491827

All communities:

- C0 (n=920): representatives [_Settings, ␠curriculum, ROSS, ␠Running, _Pro, _Dep, ␠hypothetical, ␠LAW, ␠TEST, -work]; target-extreme [␠DECL, ␠TELE, ␠Creating, ␠inexp, /authentication, ␠PPC]; classes {'alphabetic': 450, 'mixed': 470}
- C1 (n=918): representatives [␠Carrie, ␠Macedonia, 戏曲, ␠Herr, ␠Angola, ␠Miche, ␠Jenna, Pago, ␠preached, ␠Пар]; target-extreme [␠Farm, Johnny, ␠Curry, ␠alf, ␠Ago, ␠Giul]; classes {'alphabetic': 902, 'mixed': 16}
- C2 (n=914): representatives [攻势, ␠insecurity, 提升, ␠business, ␠scenarios, ␠agriculture, ␠Ensure, ␠experimentation, ␠succès, 體驗]; target-extreme [資源, ␠Auxiliary, ␠район, 支援, 牢, ␠clientes]; classes {'alphabetic': 883, 'mixed': 29, 'numeric': 1, 'punctuation': 1}
- C3 (n=783): representatives [а, é, и, ا, ე, Á, á, É, ␠É, e]; target-extreme [у, ّ, Æ, ␠Bij, ː, ␠sû]; classes {'alphabetic': 726, 'mixed': 33, 'punctuation': 24}
- C4 (n=619): representatives [_done, .setBackgroundResource, ␠OnCollision, ␠Melania, Concurrency, ␠HttpServletResponse, אפליק, ␠perseverance, ␠thỏa, ␠AppCompatActivity]; target-extreme [Jvm, .bukkit, ␠продук, ␠выполня, ␠механиз, azor]; classes {'alphabetic': 389, 'mixed': 226, 'punctuation': 4}
- C5 (n=477): representatives [✽, 🉑, 🏭, ✬, 🍔, 🏩, 쭘, �, �, �]; target-extreme [🐀, 摩托, ⊔, �, Ј, ␠gı]; classes {'alphabetic': 286, 'mixed': 3, 'punctuation': 187, 'whitespace': 1}
- C6 (n=332): representatives [=<?=$, ="<?=$, "><?=$, #{@, ␠{{$, {{$, $$$, $$, <?=$, „]; target-extreme [$$, {, 〜, ـ, ␠%, ={()]; classes {'alphabetic': 31, 'mixed': 24, 'numeric': 3, 'punctuation': 272, 'whitespace': 2}
- C7 (n=293): representatives [␠במיוחד, אני, ␠일이, からの, ␠بلا, роме, さら, ␠две, ␠sogar, ␠السيارات]; target-extreme [␠proven, תם, ずっと, 更, さら, ␠بلا]; classes {'alphabetic': 274, 'mixed': 19}
- C8 (n=264): representatives [车, �, ์, �, �, 湖, ﾞ, �, 凡本网注, �]; target-extreme [�, 瓜, 形容, �, �, �]; classes {'alphabetic': 208, 'mixed': 3, 'punctuation': 53}
- C9 (n=254): representatives [␠promising, ␠Elementary, ␠motivational, ␠medically, ␠immedi, ␠verbally, ␠recurrent, 这么大, ␠sexual, ␠Simple]; target-extreme [.Simple, Simple, 过度, _valid, ␠hero, Adjacent]; classes {'alphabetic': 238, 'mixed': 16}
- C10 (n=129): representatives [␠of, 的, ␠Behind, ␠about, ␠neben, for, ␠de, ␠behind, ␠for, define]; target-extreme [␠of, ␠for, import, _of, ␠with, 的]; classes {'alphabetic': 93, 'mixed': 32, 'punctuation': 3, 'whitespace': 1}

Strongest intercommunity connections:

- C0 to C1: 1142 token edges; mean cosine 0.129097
- C0 to C4: 1081 token edges; mean cosine 0.120955
- C1 to C2: 940 token edges; mean cosine 0.130937
- C0 to C2: 885 token edges; mean cosine 0.127709
- C2 to C4: 724 token edges; mean cosine 0.125247
- C1 to C3: 617 token edges; mean cosine 0.131579
- C1 to C4: 593 token edges; mean cosine 0.126296
- C3 to C5: 578 token edges; mean cosine 0.132342
- C4 to C5: 573 token edges; mean cosine 0.126986
- C2 to C3: 523 token edges; mean cosine 0.127201
- C0 to C3: 493 token edges; mean cosine 0.130121
- C2 to C9: 477 token edges; mean cosine 0.134179
- C2 to C8: 445 token edges; mean cosine 0.135748
- C2 to C7: 434 token edges; mean cosine 0.130155
- C0 to C9: 416 token edges; mean cosine 0.130302

## State 18 — block_17_output

Paired positive_head: membership Jaccard 0.871327; edge Jaccard 0.707892; shared tokens 5634.
Paired negative_tail: membership Jaccard 0.843083; edge Jaccard 0.656182; shared tokens 5491.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5876
- Directed 10-NN edges: 58760
- Undirected edges: 41904
- Communities: 10
- Modularity: 0.554535

All communities:

- C0 (n=1294): representatives [떘, ␠underscores, ␠kitchen, ␠cut, 卧室, ␠slipped, ␠priests, ␠apartment, ␠DVDs, ␠soaked]; target-extreme [␠strapped, 雕像, overwrite, ameleon, ␠scratched, otoxic]; classes {'alphabetic': 1240, 'mixed': 54}
- C1 (n=1193): representatives [␠şikay, 룁, ␠wyśw, 턔, więt, .EditorButton, 痦, ␠spriteBatch, 圙, .DropDownStyle]; target-extreme [.DropDownStyle, 骺, ␠לעמוד, 屉, ␠ShoppingCart, 댓]; classes {'alphabetic': 1068, 'mixed': 59, 'punctuation': 66}
- C2 (n=1025): representatives [son, ían, ik, ok, ton, ak, ys, man, ka, ывают]; target-extreme [irse, wish, kes, عون, oningen, kas]; classes {'alphabetic': 999, 'mixed': 22, 'punctuation': 4}
- C3 (n=679): representatives [\tds, (ds, CP, DP, (song, _cf, ␠don, \tfs, \tlbl, (dateTime]; target-extreme [_HC, fm, |string, \tboard, (ts, (com]; classes {'alphabetic': 431, 'mixed': 246, 'punctuation': 2}
- C4 (n=607): representatives [になると, それでも, 业内人士, características, だったので, ␠모습, を与え, することは, していました, ␠некоторые]; target-extreme [מסוגל, ماذا, 实在, 不會, ␠Nevertheless, 偏偏]; classes {'alphabetic': 593, 'mixed': 14}
- C5 (n=494): representatives [');\r\n\r\n, "))\r\n, ]))\r\n, ")\r\n, ");\r\n\r\n, ))\r\n, '))\r\n, '))\n, ));\r\n\r\n, ));\n]; target-extreme [}");\r\n, (',');\n, ␠?>">\n, 。”\n\n, ␠",";\n, ␠')\n]; classes {'alphabetic': 4, 'mixed': 4, 'punctuation': 465, 'whitespace': 21}
- C6 (n=450): representatives [.RemoveAt, .getOrElse, ␠CGRectMake, strncmp, .IsChecked, textbox, ␠dataGridView, ␠WINAPI, .numberOfLines, ␠sscanf]; target-extreme [cmb, ␠newcom, .IsNotNull, textbox, \tstrncpy, \tNSString]; classes {'alphabetic': 293, 'mixed': 152, 'punctuation': 5}
- C7 (n=85): representatives [␠Portsmouth, smouth, داعش, ␠Scarborough, oklyn, ␠Indonesian, benhavn, ottesville, derabad, Seattle]; target-extreme [xford, ␠Snape, foundland, derabad, ␠Rohingya, ␠Victorian]; classes {'alphabetic': 84, 'mixed': 1}
- C8 (n=25): representatives [␠不, ␠�, ␠�, ␠�, ␠和, ␠�, ␠�, ␠下, ␠是否, ␠是]; target-extreme [␠�, ␠生命周期, ␠商品, ␠和, ␠�, ␠�]; classes {'alphabetic': 10, 'punctuation': 15}
- C9 (n=24): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, \t␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t]; target-extreme [\t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ▎, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\t]; classes {'numeric': 1, 'punctuation': 2, 'whitespace': 21}

Strongest intercommunity connections:

- C0 to C2: 1607 token edges; mean cosine 0.128533
- C0 to C1: 1186 token edges; mean cosine 0.125423
- C1 to C4: 1056 token edges; mean cosine 0.134500
- C1 to C6: 933 token edges; mean cosine 0.134947
- C1 to C2: 891 token edges; mean cosine 0.125696
- C2 to C3: 803 token edges; mean cosine 0.132637
- C0 to C4: 779 token edges; mean cosine 0.127127
- C2 to C4: 673 token edges; mean cosine 0.130332
- C0 to C3: 668 token edges; mean cosine 0.125063
- C0 to C6: 600 token edges; mean cosine 0.123656
- C3 to C6: 516 token edges; mean cosine 0.128749
- C1 to C3: 463 token edges; mean cosine 0.126634
- C2 to C6: 319 token edges; mean cosine 0.119076
- C4 to C6: 202 token edges; mean cosine 0.125579
- C0 to C7: 173 token edges; mean cosine 0.133059

#### negative_tail

- Nodes: 6390
- Directed 10-NN edges: 63900
- Undirected edges: 44575
- Communities: 11
- Modularity: 0.488962

All communities:

- C0 (n=1026): representatives [_done, ␠ticker, ␠Clubs, _Settings, _RO, ROSS, _Pro, ␠TEST, ␠RECE, ␠Ав]; target-extreme [␠Ult, ␠PRES, -full, ␠Bullet, /name, ␠DECL]; classes {'alphabetic': 411, 'mixed': 615}
- C1 (n=785): representatives [␠получа, ✽, אפליק, ␠Пар, ␠турист, 🉑, ␠liber, ␠بلا, アクセ, ✬]; target-extreme [摩托, ␠alf, ␠продук, ␠inexp, 芦, 🐀]; classes {'alphabetic': 623, 'mixed': 7, 'punctuation': 155}
- C2 (n=662): representatives [а, ا, Á, ステ, ์, �, ე, ing, レ, パ]; target-extreme [�, у, ␠TELE, ␠الز, �, Æ]; classes {'alphabetic': 552, 'mixed': 28, 'numeric': 2, 'punctuation': 80}
- C3 (n=658): representatives [␠curriculum, ␠Assurance, ␠Running, Concurrency, Companies, ␠airline, ␠insecurity, ␠Activities, ␠experimentation, ␠FIFA]; target-extreme [␠Farm, ␠район, ␠Equality, ␠Familie, ␠Joint, ␠Installed]; classes {'alphabetic': 627, 'mixed': 30, 'punctuation': 1}
- C4 (n=598): representatives [␠perseverance, 攻势, ␠Ensure, 艰辛, ␠motivational, 提升, -safe, 安全, 接力, ␠preached]; target-extreme [␠lief, ␠Creating, 提升, 资源, 支援, 敏捷]; classes {'alphabetic': 579, 'mixed': 19}
- C5 (n=551): representatives [efully, ␠במיוחד, ␠terrible, ␠rapid, ␠hypothetical, ␠auditory, ␠Elementary, ␠السيارات, ␠positively, ␠merciless]; target-extreme [␠Auxiliary, ␠proven, Simple, 笫, ␠example, 第七届]; classes {'alphabetic': 533, 'mixed': 17, 'numeric': 1}
- C6 (n=487): representatives [Hugh, ␠Angola, ␠Carrie, ␠Jimmy, ␠Macedonia, ␠Sandra, Jimmy, ␠Jenna, Pago, ␠Billy]; target-extreme [␠Curry, ␠Manning, Johnny, ␠Johnny, ␠Giul, ␠Madison]; classes {'alphabetic': 484, 'mixed': 3}
- C7 (n=459): representatives [␠Jud, ␠Bor, ␠Bra, ␠Herr, ␠Tra, ␠Guerr, ␠Bod, ␠Poz, ␠Tur, ␠Brid]; target-extreme [␠Bij, ␠Afr, ␠Bott, Br, Arr, ␠appro]; classes {'alphabetic': 447, 'mixed': 12}
- C8 (n=402): representatives [=<?=$, ␠of, 的, ␠{$, ␠​, ␠{{$, ’est, ´, ␠case, ']; target-extreme [␠of, ␠for, ␠OF, ␠to, _of, ␠with]; classes {'alphabetic': 131, 'mixed': 36, 'punctuation': 230, 'whitespace': 5}
- C9 (n=382): representatives [.setBackgroundResource, ␠referencedColumnName, ␠HttpServletResponse, ␠MaterialPageRoute, AffineTransform, DidAppear, ␠doInBackground, _drvdata, .coroutines, IconModule]; target-extreme [.bukkit, Jvm, javax, (EFFECT, ␠HTTP, azor]; classes {'alphabetic': 221, 'mixed': 159, 'punctuation': 2}
- C10 (n=380): representatives [凡本网注, 影视, 游艇, ␠ciné, 湖, 水域, 新, 佳, 石油, 羅]; target-extreme [形容, 古今, 瓜, 매, 庄, 盧]; classes {'alphabetic': 374, 'mixed': 5, 'punctuation': 1}

Strongest intercommunity connections:

- C0 to C3: 908 token edges; mean cosine 0.129035
- C3 to C4: 825 token edges; mean cosine 0.133694
- C1 to C2: 753 token edges; mean cosine 0.137608
- C0 to C9: 680 token edges; mean cosine 0.121112
- C0 to C1: 679 token edges; mean cosine 0.128413
- C0 to C5: 669 token edges; mean cosine 0.134056
- C0 to C7: 630 token edges; mean cosine 0.136703
- C4 to C5: 580 token edges; mean cosine 0.134218
- C1 to C4: 551 token edges; mean cosine 0.129662
- C1 to C3: 542 token edges; mean cosine 0.132409
- C0 to C4: 514 token edges; mean cosine 0.128165
- C3 to C6: 510 token edges; mean cosine 0.132508
- C3 to C5: 480 token edges; mean cosine 0.132085
- C6 to C7: 466 token edges; mean cosine 0.138565
- C1 to C5: 437 token edges; mean cosine 0.132659

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6224
- Directed 10-NN edges: 62240
- Undirected edges: 44611
- Communities: 10
- Modularity: 0.560727

All communities:

- C0 (n=1229): representatives [㨳, pushViewController, ␠şikay, CppCodeGenWriteBarrier, 턔, .EditorButton, 룁, ␠wyśw, więt, 痦]; target-extreme [␠newcom, .DropDownStyle, 骺, 屉, myśl, ǳ]; classes {'alphabetic': 1087, 'mixed': 73, 'punctuation': 69}
- C1 (n=1133): representatives [猫咪, ␠underscores, ␠cut, ␠kitchen, 卧室, ␠priests, ␠soaked, ␠downside, ␠flakes, ␠caves]; target-extreme [雕像, overwrite, ␠strapped, ameleon, ␠lieutenant, thouse]; classes {'alphabetic': 1089, 'mixed': 44}
- C2 (n=1047): representatives [dzić, 业内人士, になると, だったので, características, それでも, дается, を与え, ␠모습, quisar]; target-extreme [מסוגל, ماذا, oningen, 实在, ␠לעמוד, ␠patiënt]; classes {'alphabetic': 1023, 'mixed': 24}
- C3 (n=1007): representatives [떘, son, ik, ton, ok, ak, ys, og, man, ka]; target-extreme [wish, irse, kas, kes, عون, otoxic]; classes {'alphabetic': 994, 'mixed': 10, 'punctuation': 3}
- C4 (n=634): representatives [\tds, (ds, (indexPath, ␠paddingTop, (song, \tlbl, CP, DP, sr, \tfs]; target-extreme [cmb, fm, _HC, |string, \tboard, \tcf]; classes {'alphabetic': 346, 'mixed': 286, 'punctuation': 2}
- C5 (n=523): representatives [');\r\n\r\n, "))\r\n, ");\r\n, ]))\r\n, ")\r\n, ");\r\n\r\n, ))\r\n, ));\n, ));\r\n, ));\r\n\r\n]; target-extreme [}");\r\n, (',');\n, ␠?>">\n, '),\r\n, ␠')\n, ␠",";\n]; classes {'alphabetic': 4, 'mixed': 7, 'punctuation': 508, 'whitespace': 4}
- C6 (n=424): representatives [.getOrElse, .RemoveAt, ␠CGRectMake, strncmp, textbox, ␠sscanf, .IsChecked, ␠setTime, ␠richTextBox, ␠dataGridView]; target-extreme [textbox, .IsNotNull, \tNSString, \tstrncpy, .lineEdit, primaryKey]; classes {'alphabetic': 292, 'mixed': 132}
- C7 (n=99): representatives [␠Portsmouth, smouth, ␠Italians, oklyn, ␠Scarborough, ␠Indonesian, derabad, ottesville, Chicago, ␠Singapore]; target-extreme [tridge, xford, ␠Snape, foundland, ␠Augustine, derabad]; classes {'alphabetic': 97, 'mixed': 2}
- C8 (n=73): representatives [␠don, ␠不, ␠�, ␠�, ␠�, ␠�, ␠doesn, ␠published, ␠wasn, ␠是]; target-extreme [␠商品, ␠don, ␠�, ␠twenties, ␠和, ␠publié]; classes {'alphabetic': 52, 'mixed': 2, 'punctuation': 19}
- C9 (n=55): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\n, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠\r\n, \t␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠\t\t\n, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\n, ▎, ␠␠␠␠␠␠␠␠\t\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 2, 'numeric': 1, 'punctuation': 15, 'whitespace': 37}

Strongest intercommunity connections:

- C0 to C2: 1590 token edges; mean cosine 0.133338
- C1 to C3: 1355 token edges; mean cosine 0.131328
- C1 to C2: 1139 token edges; mean cosine 0.127705
- C0 to C1: 1011 token edges; mean cosine 0.127674
- C2 to C3: 979 token edges; mean cosine 0.131105
- C0 to C6: 960 token edges; mean cosine 0.136666
- C0 to C3: 709 token edges; mean cosine 0.125825
- C3 to C4: 695 token edges; mean cosine 0.133761
- C1 to C6: 495 token edges; mean cosine 0.123511
- C1 to C4: 465 token edges; mean cosine 0.126435
- C4 to C6: 461 token edges; mean cosine 0.129762
- C0 to C4: 437 token edges; mean cosine 0.127869
- C2 to C6: 311 token edges; mean cosine 0.125837
- C3 to C6: 290 token edges; mean cosine 0.122163
- C2 to C4: 235 token edges; mean cosine 0.124526

#### negative_tail

- Nodes: 5614
- Directed 10-NN edges: 56140
- Undirected edges: 39039
- Communities: 13
- Modularity: 0.471387

All communities:

- C0 (n=836): representatives [_done, ␠получа, Concurrency, ✽, .setBackgroundResource, アクセ, אפליק, ␠HttpServletResponse, ␠referencedColumnName, ✬]; target-extreme [摩托, ␠продук, Jvm, 🐀, 建军, ␠механиз]; classes {'alphabetic': 548, 'mixed': 185, 'punctuation': 103}
- C1 (n=795): representatives [ROSS, _Settings, ␠Running, ␠Пар, ␠TEST, _Pro, ␠TEMP, .AR, ␠liber, ␠RECE]; target-extreme [␠TELE, ␠inexp, ␠Afr, ␠Creating, ␠Ult, ␠Retrie]; classes {'alphabetic': 469, 'mixed': 326}
- C2 (n=682): representatives [␠curriculum, ␠Assurance, ␠Clubs, ␠airline, ␠Activities, ␠accessibility, Companies, 攻势, ␠FIFA, 戏曲]; target-extreme [␠Farm, ␠Auxiliary, 定律, ␠район, ␠Joint, ␠Equality]; classes {'alphabetic': 584, 'mixed': 98}
- C3 (n=643): representatives [а, ا, Á, ステ, ing, �, ι, ि�, ა, ე]; target-extreme [у, ␠الز, Æ, а, フレ, �]; classes {'alphabetic': 575, 'mixed': 15, 'punctuation': 53}
- C4 (n=638): representatives [␠Jimmy, ␠Carrie, ␠Sandra, Jimmy, ␠Jenna, ␠Herr, Johnny, ␠Jud, ␠Archer, ␠auditory]; target-extreme [␠Curry, ␠lief, ␠Johnny, ␠Manning, Johnny, ␠Giul]; classes {'alphabetic': 615, 'mixed': 23}
- C5 (n=583): representatives [␠במיוחד, ␠terrible, ␠بلا, ␠promising, אני, からの, ␠recurrent, イベント, ␠منها, ␠две]; target-extreme [␠kiện, Simple, ␠example, ␠Nets, ␠Simple, ␠permet]; classes {'alphabetic': 548, 'mixed': 34, 'punctuation': 1}
- C6 (n=369): representatives [␠insecurity, ␠Ensure, 提升, 壮大, 深入推进, 嫌弃, 安全, 交通事故, 協助, 加持]; target-extreme [提升, 资源, 支援, 敏捷, 保证, ␠DECL]; classes {'alphabetic': 356, 'mixed': 13}
- C7 (n=311): representatives [=<?=$, â, $$, ´, ␠{{$, ー, „, []=$, ␠@{$, ']; target-extreme [␠to, ّ, $$, import, ％, 〜]; classes {'alphabetic': 48, 'mixed': 32, 'numeric': 2, 'punctuation': 225, 'whitespace': 4}
- C8 (n=294): representatives [์, �, �, �, �, �, �, ␠orch, 凡本网注, ﾞ]; target-extreme [�, ␠alf, �, �, 芦, �]; classes {'alphabetic': 241, 'mixed': 2, 'numeric': 1, 'punctuation': 50}
- C9 (n=174): representatives [␠contexts, アプリ, ␠App, ␠javafx, ␠javax, ␠Azure, 客户, -app, ␠ARRAY, 伊利]; target-extreme [.bukkit, javax, Arr, azor, ␠clientes, /name]; classes {'alphabetic': 96, 'mixed': 78}
- C10 (n=157): representatives [␠Macedonia, ␠Ghana, ␠Angola, ␠Georgia, ␠Sudan, ␠России, ␠gỗ, ␠Athen, Europe, ␠Romania]; target-extreme [␠Ago, ␠Familie, 古今, ञ, 上年, ␠Finland]; classes {'alphabetic': 154, 'mixed': 3}
- C11 (n=70): representatives [␠of, 的, ␠Behind, for, ␠de, ␠about, ␠from, ␠behind, of, Of]; target-extreme [␠of, ␠for, _of, ␠OF, 的, ␠with]; classes {'alphabetic': 54, 'mixed': 16}
- C12 (n=62): representatives [␠Nou, ␠Lou, ␠Su, ␠Ki, ␠Lu, ␠Aj, ␠Pou, ␠Dou, AJ, Fu]; target-extreme [␠Bij, Adj, ␠giải, ␠Chu, Fu, Ace]; classes {'alphabetic': 60, 'mixed': 2}

Strongest intercommunity connections:

- C0 to C1: 972 token edges; mean cosine 0.125654
- C0 to C2: 854 token edges; mean cosine 0.128788
- C1 to C2: 851 token edges; mean cosine 0.126355
- C1 to C4: 839 token edges; mean cosine 0.131628
- C2 to C4: 747 token edges; mean cosine 0.128171
- C0 to C5: 653 token edges; mean cosine 0.129155
- C0 to C3: 605 token edges; mean cosine 0.130787
- C2 to C6: 547 token edges; mean cosine 0.132165
- C0 to C4: 529 token edges; mean cosine 0.125042
- C1 to C5: 505 token edges; mean cosine 0.129871
- C2 to C5: 494 token edges; mean cosine 0.129001
- C1 to C3: 457 token edges; mean cosine 0.131753
- C3 to C5: 453 token edges; mean cosine 0.136257
- C3 to C8: 430 token edges; mean cosine 0.143961
- C5 to C6: 401 token edges; mean cosine 0.127866

## State 19 — block_18_output

Paired positive_head: membership Jaccard 0.852823; edge Jaccard 0.685971; shared tokens 5725.
Paired negative_tail: membership Jaccard 0.853430; edge Jaccard 0.687727; shared tokens 5549.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6439
- Directed 10-NN edges: 64390
- Undirected edges: 46213
- Communities: 10
- Modularity: 0.577972

All communities:

- C0 (n=1314): representatives [떘, ␠kitchen, ␠enamel, ␠Portsmouth, ␠underscores, ␠cracks, ␠transformations, ␠scratched, ␠drinkers, ␠granite]; target-extreme [␠strapped, overwrite, crafted, ␠interfer, ␠monkey, 雕像]; classes {'alphabetic': 1257, 'mixed': 56, 'punctuation': 1}
- C1 (n=1052): representatives [ik, son, ают, ok, ывают, man, ␠cut, el, ut, ak]; target-extreme [kas, kes, wish, ällt, irse, יצו]; classes {'alphabetic': 1037, 'mixed': 12, 'numeric': 1, 'punctuation': 2}
- C2 (n=1052): representatives [␠şikay, .EditorButton, 룁, 턔, :UIButtonTypeCustom, .TabStop, نطق, .DropDownStyle, 痦, 圙]; target-extreme [屉, .DropDownStyle, 댓, 😳, ␠çeş, ␠Tumblr]; classes {'alphabetic': 964, 'mixed': 23, 'punctuation': 65}
- C3 (n=888): representatives [\tds, CP, (ds, GS, \tcp, 𝑽, \tfs, (dateTime, MD, (song]; target-extreme [␠ShoppingCart, fm, ␠gps, _HC, *k, \tmat]; classes {'alphabetic': 514, 'mixed': 370, 'punctuation': 4}
- C4 (n=790): representatives [业内人士, それでも, をしている, になると, を持っている, していました, だったので, ␠يتعلق, ␠모습, ますが]; target-extreme [عون, ␠לעמוד, Instead, 偏偏, מסוגל, ␠realidad]; classes {'alphabetic': 774, 'mixed': 16}
- C5 (n=669): representatives [pushViewController, ␠spriteBatch, [SerializeField, .RemoveAt, .tabControl, ␠FindObjectOfType, .getOrElse, .dateTimePicker, .NumericUpDown, INFRINGEMENT]; target-extreme [cmb, textbox, |string, ␠tableName, .IsNotNull, primaryKey]; classes {'alphabetic': 443, 'mixed': 222, 'punctuation': 4}
- C6 (n=569): representatives [');\r\n\r\n, ");\r\n, "))\r\n, ")\r\n, ");\r\n\r\n, ]))\r\n, ')\r\n\r\n, ))\r\n, :";\r\n, ])\r\n]; target-extreme [}");\r\n, (',');\n, 。”\n\n, ␠",";\n, (",");\n, ␠␠␠␠\t\t\n]; classes {'alphabetic': 3, 'mixed': 4, 'punctuation': 519, 'whitespace': 43}
- C7 (n=37): representatives [NECT, ETERS, AGES, AKER, LETTE, ENDED, ENG, ROY, ERSION, UTERS]; target-extreme [ADING, ENDED, ␠AUTHORS, AGED, CTOR, configs]; classes {'alphabetic': 37}
- C8 (n=36): representatives [␠不, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠�, ␠生命周期, ␠和, ␠�]; classes {'alphabetic': 15, 'punctuation': 21}
- C9 (n=32): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t, ␠\t\t\t, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ▎]; classes {'punctuation': 3, 'whitespace': 29}

Strongest intercommunity connections:

- C0 to C1: 1506 token edges; mean cosine 0.130946
- C2 to C4: 1200 token edges; mean cosine 0.134756
- C0 to C2: 1128 token edges; mean cosine 0.128244
- C2 to C5: 1116 token edges; mean cosine 0.136922
- C0 to C4: 1005 token edges; mean cosine 0.128984
- C1 to C3: 901 token edges; mean cosine 0.134400
- C3 to C5: 833 token edges; mean cosine 0.130416
- C0 to C5: 795 token edges; mean cosine 0.125128
- C1 to C4: 771 token edges; mean cosine 0.133441
- C0 to C3: 742 token edges; mean cosine 0.125568
- C1 to C2: 618 token edges; mean cosine 0.125260
- C2 to C3: 363 token edges; mean cosine 0.125887
- C4 to C5: 355 token edges; mean cosine 0.127774
- C1 to C5: 221 token edges; mean cosine 0.123162
- C3 to C4: 202 token edges; mean cosine 0.129366

#### negative_tail

- Nodes: 6134
- Directed 10-NN edges: 61340
- Undirected edges: 42871
- Communities: 11
- Modularity: 0.492661

All communities:

- C0 (n=1292): representatives [␠curriculum, ␠apparel, ␠Assurance, 攻势, ␠Clubs, ␠ticker, ␠insecurity, ␠Running, ␠Activities, ␠currents]; target-extreme [␠Farm, 资源, ␠maturity, Army, ␠athletics, ␠Mines]; classes {'alphabetic': 1253, 'mixed': 39}
- C1 (n=1209): representatives [_done, ROSS, .AR, _Settings, ␠ALL, ␠RECE, Concurrency, ␠Accred, .FR, ␠Пар]; target-extreme [␠продук, ␠TELE, ␠Retrie, ␠lief, ␠appro, -full]; classes {'alphabetic': 629, 'mixed': 577, 'punctuation': 3}
- C2 (n=867): representatives [а, ا, ა, ing, и, ์, ␠данный, 𝑎, 𝐚, 𝑨]; target-extreme [�, �, у, フレ, 的, ː]; classes {'alphabetic': 728, 'mixed': 20, 'numeric': 1, 'punctuation': 117, 'whitespace': 1}
- C3 (n=847): representatives [📨, ␠OnCollision, ␠получа, ✬, ✽, ␠yaygın, ␠HttpServletResponse, ﯭ, אפליק, ␠thỏa]; target-extreme [.bukkit, Jvm, 建军, ␠inexp, ␠выполня, ⊔]; classes {'alphabetic': 634, 'mixed': 81, 'punctuation': 132}
- C4 (n=611): representatives [␠Carrie, ␠Macedonia, ␠Angola, ␠Jimmy, انيا, Jimmy, ␠Crawford, ␠Zambia, ␠Seth, ␠Jenna]; target-extreme [␠Bij, ␠Curry, ␠Giul, ␠Till, azor, ␠Madison]; classes {'alphabetic': 596, 'mixed': 15}
- C5 (n=454): representatives [area, 更具, 提升, ␠WILL, 提供, ␠Success, ␠Example, ␠effectively, ␠succès, ␠jede]; target-extreme [␠Và, 加快, attività, 特别, EXAMPLE, 引入]; classes {'alphabetic': 439, 'mixed': 14, 'punctuation': 1}
- C6 (n=384): representatives [␠terrible, ␠Ensure, 協助, ␠Support, ␠Provide, ␠Supports, ␠Loads, ␠Execute, ␠providing, ␠Ends]; target-extreme [␠Creating, 保证, Applications, 支援, ␠lends, ␠hero]; classes {'alphabetic': 339, 'mixed': 45}
- C7 (n=266): representatives [␠​, ␠!, ␠{{$, >>), ~, ´, ␠*@, $$, {{$, ■]; target-extreme [␠to, ␠%%, 〜, $$, ª, ‹]; classes {'alphabetic': 28, 'mixed': 16, 'punctuation': 219, 'special': 1, 'whitespace': 2}
- C8 (n=149): representatives [八大, ␠million, 乡村, 万人次, 第七, million, 农村, 老年, 万千瓦, 第七届]; target-extreme [␠район, 第七届, 笫, 上年, ␠Rural, ␠семь]; classes {'alphabetic': 146, 'mixed': 3}
- C9 (n=30): representatives [␠of, ␠de, for, ␠about, ␠on, ␠at, Of, of, _to, _of]; target-extreme [␠of, _of, ␠OF, ␠for, ␠with, -of]; classes {'alphabetic': 25, 'mixed': 5}
- C10 (n=25): representatives [␠géné, éné, ␠cré, ␠prés, ␠Méd, ␠Pré, ␠spéc, ␠gén, ␠Prä, ␠méd]; target-extreme [␠géné, ␠Prä, ␠Cré, ␠gén, ␠spéc, ␠Dess]; classes {'alphabetic': 25}

Strongest intercommunity connections:

- C0 to C1: 1824 token edges; mean cosine 0.130502
- C0 to C3: 1164 token edges; mean cosine 0.128486
- C1 to C3: 1113 token edges; mean cosine 0.123501
- C1 to C4: 1041 token edges; mean cosine 0.131393
- C0 to C6: 828 token edges; mean cosine 0.131752
- C0 to C4: 798 token edges; mean cosine 0.132262
- C0 to C5: 795 token edges; mean cosine 0.132468
- C2 to C3: 775 token edges; mean cosine 0.129166
- C1 to C6: 706 token edges; mean cosine 0.129095
- C0 to C2: 622 token edges; mean cosine 0.132921
- C1 to C2: 529 token edges; mean cosine 0.127385
- C2 to C5: 473 token edges; mean cosine 0.131898
- C2 to C4: 468 token edges; mean cosine 0.133861
- C3 to C5: 441 token edges; mean cosine 0.129697
- C3 to C4: 411 token edges; mean cosine 0.126463

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5999
- Directed 10-NN edges: 59990
- Undirected edges: 43103
- Communities: 10
- Modularity: 0.565603

All communities:

- C0 (n=1337): representatives [pushViewController, ␠şikay, .EditorButton, 룁, ␠spriteBatch, 턔, .TabStop, :UIButtonTypeCustom, [SerializeField, 痦]; target-extreme [␠לעמוד, 屉, ␠swal, .DropDownStyle, primaryKey, 댓]; classes {'alphabetic': 1098, 'mixed': 172, 'punctuation': 67}
- C1 (n=1336): representatives [떘, نطق, ␠kitchen, ␠cut, ␠underscores, ␠flakes, ␠granite, ␠cracks, ␠slipped, ␠drinkers]; target-extreme [␠strapped, 雕像, ␠choked, crafted, ␠lieutenant, thouse]; classes {'alphabetic': 1259, 'mixed': 76, 'punctuation': 1}
- C2 (n=1042): representatives [ik, ok, son, ают, el, man, ut, ались, ывают, дается]; target-extreme [عون, wish, kas, kes, ällt, irse]; classes {'alphabetic': 1026, 'mixed': 13, 'numeric': 1, 'punctuation': 2}
- C3 (n=766): representatives [CP, \tds, (ds, PD, \tfs, \tlbl, (indexPath, (dateTime, MD, _cf]; target-extreme [|string, *k, \tmat, fm, ␠gps, _HC]; classes {'alphabetic': 426, 'mixed': 339, 'punctuation': 1}
- C4 (n=596): representatives [になると, 业内人士, をしている, ␠يتعلق, それでも, はずです, していました, だったので, ␠모습, になりました]; target-extreme [Instead, 偏偏, מסוגל, 实在, ␠although, 好吗]; classes {'alphabetic': 586, 'mixed': 10}
- C5 (n=508): representatives [');\r\n\r\n, "))\r\n, ");\r\n, ));\n\n, ))\r\n, ]))\r\n, ")\r\n, ));\n, ));\r\n, ");\r\n\r\n]; target-extreme [}");\r\n, (',');\n, 。”\n\n, ␠",";\n, ],\n, (",");\n]; classes {'alphabetic': 2, 'mixed': 2, 'punctuation': 502, 'whitespace': 2}
- C6 (n=163): representatives [␠richTextBox, ␠dataGridView, ␠comboBox, ␠DropDownList, pictureBox, textbox, ␠pictureBox, ␠ComboBox, getWidth, comboBox]; target-extreme [cmb, textbox, overwrite, ␠tableName, .lineEdit, ␠radioButton]; classes {'alphabetic': 126, 'mixed': 37}
- C7 (n=109): representatives [␠Portsmouth, واشنطن, ington, ␠Scarborough, 特朗普, 星巴克, داعش, ␠photoshop, ␠Montgomery, ␠Indonesian]; target-extreme [␠ShoppingCart, xford, 运营商, lington, leston, ␠Victorian]; classes {'alphabetic': 109}
- C8 (n=107): representatives [␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠\r\n, "\r\n\r\n\r\n, ␠␠␠␠␠␠␠␠\n, ␠}\r\n\r\n\r\n\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ");\n\n\n]; target-extreme [␠␠␠␠\t\t\n, ␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠\t]; classes {'alphabetic': 2, 'punctuation': 43, 'whitespace': 62}
- C9 (n=35): representatives [␠�, ␠不, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�]; target-extreme [␠�, ␠�, ␠和, ␠�, ␠生命周期, ␠�]; classes {'alphabetic': 14, 'punctuation': 21}

Strongest intercommunity connections:

- C1 to C2: 1647 token edges; mean cosine 0.126266
- C0 to C1: 1488 token edges; mean cosine 0.125776
- C0 to C4: 1021 token edges; mean cosine 0.132191
- C0 to C2: 877 token edges; mean cosine 0.124426
- C1 to C3: 784 token edges; mean cosine 0.125024
- C2 to C3: 772 token edges; mean cosine 0.134354
- C2 to C4: 767 token edges; mean cosine 0.136086
- C1 to C4: 735 token edges; mean cosine 0.128669
- C0 to C3: 684 token edges; mean cosine 0.128001
- C0 to C6: 514 token edges; mean cosine 0.137773
- C1 to C6: 300 token edges; mean cosine 0.124621
- C1 to C7: 291 token edges; mean cosine 0.128630
- C3 to C6: 223 token edges; mean cosine 0.128940
- C0 to C7: 152 token edges; mean cosine 0.125822
- C2 to C7: 147 token edges; mean cosine 0.126200

#### negative_tail

- Nodes: 5917
- Directed 10-NN edges: 59170
- Undirected edges: 41247
- Communities: 12
- Modularity: 0.484265

All communities:

- C0 (n=1321): representatives [␠apparel, ␠curriculum, _done, ␠insecurity, ␠Clubs, ␠Assurance, ␠experimentation, ␠biodiversity, 攻势, ␠Running]; target-extreme [␠Farm, 资源, ␠maturity, ␠Creating, ␠Bullet, registration]; classes {'alphabetic': 1031, 'mixed': 290}
- C1 (n=828): representatives [␠получа, ✽, ﯭ, ␠HttpServletResponse, ␠yaygın, ␠GUIStyle, אפליק, 🏭, �, ␠thỏa]; target-extreme [.bukkit, ␠inexp, 摩托, 🐀, ␠выполня, ⊔]; classes {'alphabetic': 613, 'mixed': 88, 'punctuation': 127}
- C2 (n=673): representatives [а, ا, ␠of, ing, ა, ์, е, и, ि�, ი]; target-extreme [␠of, フレ, у, ␠for, ␠to, 的]; classes {'alphabetic': 612, 'mixed': 23, 'punctuation': 37, 'whitespace': 1}
- C3 (n=609): representatives [␠Accred, ␠Пар, ␠RECE, ␠orch, ␠Ав, ␠ASS, ␠Retrie, ␠Ult, ␠immedi, ␠Adv]; target-extreme [␠Bij, ␠TELE, ␠продук, ␠Retrie, ␠פר, ␠PRES]; classes {'alphabetic': 546, 'mixed': 63}
- C4 (n=468): representatives [𬭶, .AR, ␠ALL, ROSS, _br, ␠THR, .FR, ASSERT, _Tr, _Ad]; target-extreme [_of, ␠OF, Jvm, azor, _FIRE, -of]; classes {'alphabetic': 219, 'mixed': 249}
- C5 (n=424): representatives [␠Carrie, ␠Macedonia, ␠Angola, ␠Jimmy, Jimmy, ␠Crawford, انيا, ␠Jenna, ␠Sandra, ␠Archer]; target-extreme [␠Curry, ␠Giul, ␠Madison, ␠Serbia, ␠Petersburg, ␠Ride]; classes {'alphabetic': 418, 'mixed': 6}
- C6 (n=367): representatives [提升, ␠WILL, ␠Supports, 诠释, 酒业, 不能, ␠supporting, 也要, 深入推进, 協助]; target-extreme [加快, 支援, coverage, 引入, 協助, 过度]; classes {'alphabetic': 354, 'mixed': 13}
- C7 (n=348): representatives [�, �, �, �, 凡本网注, ﾞ, �, �, �, �]; target-extreme [�, �, 保证, �, �, �]; classes {'alphabetic': 266, 'mixed': 1, 'punctuation': 81}
- C8 (n=295): representatives [戏曲, 影视, ␠ciné, area, 灾区, ␠Media, 体育, ␠athletics, 全民健身, 旅游]; target-extreme [建军, Army, ␠район, ␠athletics, ␠hero, 纺织]; classes {'alphabetic': 278, 'mixed': 17}
- C9 (n=248): representatives [␠​, $$, ´, ␠{{$, ␠*@, }}, >$, {{$, ■, 〜]; target-extreme [␠%%, $$, 〜, ={(), ª, ‹]; classes {'alphabetic': 26, 'mixed': 23, 'punctuation': 197, 'whitespace': 2}
- C10 (n=226): representatives [␠terrible, ␠BIG, דוגמה, ␠GREAT, ␠Example, ␠officially, ␠BEST, ␠effectively, ␠huge, better]; target-extreme [特别, ␠Relevant, ␠Extra, Adj, ␠GREAT, EXAMPLE]; classes {'alphabetic': 211, 'mixed': 15}
- C11 (n=110): representatives [␠SECOND, ␠million, 八大, esterday, 万人次, 第七届, ␠Familie, 国家级, ␠הבוקר, 萬]; target-extreme [第七届, 笫, 上年, 百年, ␠Familie, 第七]; classes {'alphabetic': 107, 'mixed': 2, 'numeric': 1}

Strongest intercommunity connections:

- C0 to C1: 1007 token edges; mean cosine 0.125154
- C0 to C4: 993 token edges; mean cosine 0.124762
- C0 to C8: 866 token edges; mean cosine 0.132971
- C0 to C3: 860 token edges; mean cosine 0.131933
- C0 to C6: 744 token edges; mean cosine 0.131133
- C0 to C5: 629 token edges; mean cosine 0.128572
- C1 to C2: 595 token edges; mean cosine 0.132927
- C3 to C4: 577 token edges; mean cosine 0.130301
- C3 to C5: 522 token edges; mean cosine 0.133269
- C1 to C3: 522 token edges; mean cosine 0.128335
- C0 to C10: 518 token edges; mean cosine 0.130264
- C2 to C7: 429 token edges; mean cosine 0.141895
- C2 to C3: 421 token edges; mean cosine 0.132814
- C0 to C2: 420 token edges; mean cosine 0.129159
- C1 to C4: 419 token edges; mean cosine 0.123522

## State 20 — block_19_output

Paired positive_head: membership Jaccard 0.813656; edge Jaccard 0.623293; shared tokens 4838.
Paired negative_tail: membership Jaccard 0.817643; edge Jaccard 0.630726; shared tokens 4829.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5636
- Directed 10-NN edges: 56360
- Undirected edges: 40182
- Communities: 9
- Modularity: 0.531977

All communities:

- C0 (n=1150): representatives [쿅, 떘, 씯, 턔, 룁, ␠açıklama, 믈, نطق, maktad, 唷]; target-extreme [عون, 扈, ␠לעמוד, 哂, מחשב, 屉]; classes {'alphabetic': 1091, 'mixed': 25, 'punctuation': 34}
- C1 (n=1057): representatives [␠transformations, sensor, ␠kitchen, ␠cardboard, ␠sucking, -door, ␠slipped, ␠enamel, worm, sticks]; target-extreme [␠strapped, ␠dreaming, ␠raster, ␠twitch, ␠underline, _transform]; classes {'alphabetic': 1018, 'mixed': 39}
- C2 (n=985): representatives [<tool_call>, ak, ik, ain, son, ka, ok, ками, ch, ek]; target-extreme [码, kas, wish, ỡ, ących, heim]; classes {'alphabetic': 967, 'mixed': 15, 'punctuation': 3}
- C3 (n=728): representatives [␠spriteBatch, [SerializeField, ␠CGRectMake, .DropDownStyle, ␠hardcoded, GtkWidget, INFRINGEMENT, .TabStop, ␠openFileDialog, KeyListener]; target-extreme [.DropDownStyle, overwrite, codes, ␠tableName, textbox, ␠nrows]; classes {'alphabetic': 449, 'mixed': 276, 'punctuation': 3}
- C4 (n=717): representatives [CP, (ds, 𝑴, \tds, DM, 𝑽, PD, ␠VGA, (table, (df]; target-extreme [␠gps, fm, \tcom, _HC, \tmat, *k]; classes {'alphabetic': 446, 'mixed': 249, 'numeric': 2, 'punctuation': 4, 'whitespace': 16}
- C5 (n=521): representatives [赤ちゃん, を持っている, をしている, ってる, características, ␠شيء, それでも, ようになりました, นะคะ, していました]; target-extreme [crafted, ␠realidad, ␠although, てくる, 偏偏, Instead]; classes {'alphabetic': 508, 'mixed': 13}
- C6 (n=340): representatives [');\r\n\r\n, ')\r\n\r\n, "))\r\n, ")\r\n, ));\r\n\r\n, ))\r\n\r\n, ')\r\n, :";\r\n, ');\r\n, ";\r\n\r\n]; target-extreme [(',');\n, ')\r\n\r\n, 。”\n\n, (",");\n, ␠",";\n, }");\r\n]; classes {'alphabetic': 3, 'mixed': 12, 'punctuation': 299, 'whitespace': 26}
- C7 (n=111): representatives [واشنطن, ␠York, ␠Indonesian, 服务中心, ␠photoshop, 特朗普, ␠Snapchat, ␠Turkish, ␠Austrian, ␠Scarborough]; target-extreme [␠Tumblr, ␠Victorian, ␠Monsanto, xford, filtro, ␠foto]; classes {'alphabetic': 109, 'mixed': 2}
- C8 (n=27): representatives [␠�, ␠不, ␠�, ␠�, ␠�, ␠�, ␠�, ␠�, ␠控, ␠和]; target-extreme [␠商品, ␠和, ␠�, ␠म, ␠�, ␠�]; classes {'alphabetic': 12, 'punctuation': 15}

Strongest intercommunity connections:

- C0 to C1: 1457 token edges; mean cosine 0.129268
- C0 to C5: 1299 token edges; mean cosine 0.136325
- C0 to C3: 1265 token edges; mean cosine 0.128355
- C1 to C2: 1173 token edges; mean cosine 0.130717
- C1 to C3: 926 token edges; mean cosine 0.125489
- C2 to C4: 922 token edges; mean cosine 0.136011
- C0 to C2: 877 token edges; mean cosine 0.127614
- C3 to C4: 742 token edges; mean cosine 0.127037
- C2 to C5: 554 token edges; mean cosine 0.132183
- C1 to C5: 509 token edges; mean cosine 0.129060
- C0 to C4: 498 token edges; mean cosine 0.129549
- C1 to C4: 430 token edges; mean cosine 0.130028
- C2 to C3: 368 token edges; mean cosine 0.120673
- C3 to C5: 279 token edges; mean cosine 0.125163
- C0 to C7: 233 token edges; mean cosine 0.129538

#### negative_tail

- Nodes: 5153
- Directed 10-NN edges: 51530
- Undirected edges: 36229
- Communities: 11
- Modularity: 0.501604

All communities:

- C0 (n=1044): representatives [␠Clubs, ␠curriculum, Companies, ␠Showing, ␠Running, ␠fluids, 戏曲, ␠assistance, ␠Ensure, ␠insecurity]; target-extreme [␠maturity, ␠Uses, ␠Shows, Army, registration, ␠alumni]; classes {'alphabetic': 888, 'mixed': 156}
- C1 (n=686): representatives [攻势, 准备, 凡本网注, 提升, 艰辛, ␠business, 灾区, ␠case, 安全, 接力]; target-extreme [引入, 前列, ␠Ninth, 国家战略, 资源, 经典的]; classes {'alphabetic': 683, 'mixed': 3}
- C2 (n=667): representatives [_done, ␠LAW, ROSS, .AR, ␠Ult, ␠FORWARD, ␠CONT, ␠Ав, ␠RECE, .FR]; target-extreme [/name, ␠TELE, ␠Afr, ␠affili, ␠Interr, .so]; classes {'alphabetic': 453, 'mixed': 213, 'punctuation': 1}
- C3 (n=667): representatives [📨, ␠마지, ✽, ハー, ✬, ﯭ, ␠yaygın, ⨭, ␠thỏa, ₶]; target-extreme [BootTest, ␠الز, ⊔, ␠lief, ⚡, ⌨]; classes {'alphabetic': 490, 'mixed': 11, 'punctuation': 166}
- C4 (n=505): representatives [а, ์, �, �, ing, ␠of, e, ا, á, ışı]; target-extreme [␠of, �, ␠to, �, у, �]; classes {'alphabetic': 414, 'mixed': 25, 'numeric': 1, 'punctuation': 65}
- C5 (n=463): representatives [␠Crawford, ␠Liberia, ␠Jenna, ␠surreal, Johnny, ␠Manning, ␠Seth, ␠Sandra, ␠Gunn, ␠Lorenzo]; target-extreme [␠Curry, ␠Bullet, ␠Manning, ␠Kara, ␠Lever, ␠Sudan]; classes {'alphabetic': 457, 'mixed': 6}
- C6 (n=389): representatives [␠OnCollision, MeshPro, ␠GUIStyle, DidAppear, entionPolicy, .getSystemService, ␠HttpServletResponse, AffineTransform, ␠ParameterDirection, ␠//</]; target-extreme [.bukkit, .twitter, DidAppear, /banner, Jvm, .repo]; classes {'alphabetic': 174, 'mixed': 203, 'punctuation': 12}
- C7 (n=377): representatives [␠במיוחד, 就會, 毅然, ␠sogar, 必然会, אני, 还是会, 都是非常, ␠medically, 就能够]; target-extreme [上下游, 特别, ␠MUST, EXAMPLE, .must, ␠Và]; classes {'alphabetic': 364, 'mixed': 13}
- C8 (n=283): representatives [}}, }}}, )const, >>), "))), ">{{$, ]=, ␠_______,, ()},, ␠*/)]; target-extreme [␠%%, ‹, ª, Ј, €, >Total]; classes {'alphabetic': 26, 'mixed': 16, 'numeric': 1, 'punctuation': 236, 'special': 1, 'whitespace': 3}
- C9 (n=50): representatives [�, �, �, �, �, ␠szy, �, �, �, ␠vũ]; target-extreme [�, �, �, 반, �, �]; classes {'alphabetic': 20, 'punctuation': 30}
- C10 (n=22): representatives [nej, ␠Ej, ␠Moj, ␠مج, ␠j, ␠adjacent, ␠Haj, ej, ␠Adj, dj]; target-extreme [Adj, ␠Bij, ␠Ej, øj, ␠Mej, ␠Haj]; classes {'alphabetic': 21, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C1: 1174 token edges; mean cosine 0.131392
- C0 to C2: 1131 token edges; mean cosine 0.127101
- C0 to C5: 795 token edges; mean cosine 0.128473
- C2 to C5: 679 token edges; mean cosine 0.132245
- C0 to C6: 627 token edges; mean cosine 0.121905
- C3 to C6: 609 token edges; mean cosine 0.126535
- C1 to C3: 528 token edges; mean cosine 0.124992
- C1 to C7: 518 token edges; mean cosine 0.130336
- C0 to C3: 479 token edges; mean cosine 0.125238
- C2 to C6: 456 token edges; mean cosine 0.120911
- C3 to C4: 455 token edges; mean cosine 0.133860
- C0 to C7: 424 token edges; mean cosine 0.129120
- C2 to C3: 419 token edges; mean cosine 0.125711
- C2 to C4: 414 token edges; mean cosine 0.130047
- C1 to C2: 373 token edges; mean cosine 0.125191

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5148
- Directed 10-NN edges: 51480
- Undirected edges: 36629
- Communities: 10
- Modularity: 0.535021

All communities:

- C0 (n=1044): representatives [␠weighting, ␠kitchen, ␠cardboard, ␠cupboard, características, ␠slipped, ␠cooker, ␠scratched, agonal, ␠apartment]; target-extreme [␠strapped, ␠raster, ␠drawback, ␠twitch, ␠choked, _transform]; classes {'alphabetic': 1005, 'mixed': 38, 'punctuation': 1}
- C1 (n=903): representatives [ak, son, ik, ain, ok, ka, ch, man, ками, ut]; target-extreme [wish, 码, kas, \tmat, ỡ, otoxic]; classes {'alphabetic': 891, 'mixed': 10, 'punctuation': 2}
- C2 (n=795): representatives [␠açıklama, 赤ちゃん, それでも, นะคะ, ってる, していました, ␠모습, になると, ␠يتعلق, ␠بطريقة]; target-extreme [عون, ących, ␠realidad, ␠לעמוד, מחשב, ивают]; classes {'alphabetic': 770, 'mixed': 12, 'punctuation': 13}
- C3 (n=709): representatives [␠spriteBatch, [SerializeField, sensor, .DropDownStyle, INFRINGEMENT, ␠CGRectMake, GtkWidget, .TabStop, .getOrElse, ␠AssemblyProduct]; target-extreme [.DropDownStyle, overwrite, ␠tableName, ␠Tumblr, textbox, ␠nrows]; classes {'alphabetic': 489, 'mixed': 219, 'punctuation': 1}
- C4 (n=690): representatives [쿅, 떘, 씯, <tool_call>, 턔, نطق, 룁, 嵝, 믈, 砠]; target-extreme [crafted, ␠dreaming, 扈, 屉, 啐, صند]; classes {'alphabetic': 646, 'mixed': 17, 'punctuation': 27}
- C5 (n=453): representatives [(ds, \tds, CP, PD, DM, \tsignal, \tfs, \tcp, ␠VGA, cm]; target-extreme [␠gps, fm, \tcom, codes, _HC, ␠SV]; classes {'alphabetic': 326, 'mixed': 127}
- C6 (n=322): representatives [');\r\n\r\n, ')\r\n\r\n, "))\r\n, ")\r\n, ));\r\n\r\n, ';\r\n\r\n, ');\r\n, ";\r\n\r\n, ))\r\n\r\n, '))\r\n]; target-extreme [(',');\n, ')\r\n\r\n, ␠",";\n, 。”\n\n, '),\r\n, "'\n]; classes {'alphabetic': 5, 'mixed': 8, 'punctuation': 282, 'whitespace': 27}
- C7 (n=152): representatives [𝑽, +C, .getS, +x, 𝑩, <k, ,X, +S, +z, ﮑ]; target-extreme [*k, 𝘚, ,k, 𝑽, )y, 𝐤]; classes {'alphabetic': 49, 'mixed': 101, 'numeric': 1, 'punctuation': 1}
- C8 (n=64): representatives [␠don, ␠�, ␠�, ␠不, ␠doesn, ␠Don, ␠watching, ␠�, ␠�, ␠wasn]; target-extreme [␠although, Instead, ␠пом, ␠商品, 从, ␠�]; classes {'alphabetic': 49, 'mixed': 2, 'punctuation': 13}
- C9 (n=16): representatives [\t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'punctuation': 1, 'whitespace': 15}

Strongest intercommunity connections:

- C0 to C1: 1147 token edges; mean cosine 0.127197
- C2 to C4: 1110 token edges; mean cosine 0.132310
- C0 to C3: 1089 token edges; mean cosine 0.124447
- C0 to C4: 975 token edges; mean cosine 0.127334
- C0 to C2: 969 token edges; mean cosine 0.126444
- C3 to C4: 914 token edges; mean cosine 0.128798
- C1 to C5: 723 token edges; mean cosine 0.133642
- C1 to C2: 641 token edges; mean cosine 0.132301
- C1 to C4: 563 token edges; mean cosine 0.125698
- C3 to C5: 539 token edges; mean cosine 0.122968
- C2 to C3: 512 token edges; mean cosine 0.125038
- C1 to C3: 436 token edges; mean cosine 0.121970
- C0 to C5: 389 token edges; mean cosine 0.124078
- C4 to C5: 241 token edges; mean cosine 0.125855
- C5 to C7: 164 token edges; mean cosine 0.142216

#### negative_tail

- Nodes: 5582
- Directed 10-NN edges: 55820
- Undirected edges: 39241
- Communities: 10
- Modularity: 0.500206

All communities:

- C0 (n=957): representatives [␠curriculum, ␠Running, ␠insecurity, ␠assistance, ␠organizational, ␠accessibility, ␠preached, ␠Provide, ␠Elementary, 准备]; target-extreme [.bukkit, ␠maturity, Jvm, .repo, registration, ␠Uses]; classes {'alphabetic': 720, 'mixed': 237}
- C1 (n=917): representatives [␠LAW, .AR, ␠CONT, ␠FORWARD, ␠RECE, _Dep, .FR, ROSS, ␠Ав, ␠Ult]; target-extreme [␠TELE, /name, /banner, ␠ál, ␠Interr, ␠inexp]; classes {'alphabetic': 625, 'mixed': 292}
- C2 (n=897): representatives [␠OnCollision, ✽, 📨, ␠마지, ﯭ, ✬, DidAppear, ␠ParameterDirection, ␠GUIStyle, ᙳ]; target-extreme [␠الز, ⊔, BootTest, DidAppear, ⚡, ␠MaterialPageRoute]; classes {'alphabetic': 606, 'mixed': 106, 'punctuation': 185}
- C3 (n=777): representatives [␠Clubs, Companies, 攻势, ␠fluids, 戏曲, ␠imagery, ␠warfare, ␠auditory, 影视, ␠sexual]; target-extreme [␠Bullet, Army, ␠alumni, ␠Lever, 纺织, 比分]; classes {'alphabetic': 748, 'mixed': 29}
- C4 (n=707): representatives [ハー, а, ステ, �, е, и, á, ์, ing, ا]; target-extreme [�, �, у, ّ, а, �]; classes {'alphabetic': 584, 'mixed': 17, 'numeric': 1, 'punctuation': 105}
- C5 (n=644): representatives [␠במיוחד, انيا, 提升, אני, 就會, ␠notamment, ␠Awesome, ␠sogar, 壮大, 也会]; target-extreme [上下游, 引入, 前列, 国家战略, ␠MUST, ␠Ninth]; classes {'alphabetic': 631, 'mixed': 13}
- C6 (n=352): representatives [}}}, }}, ␠*)__, ␠case, )const, "))), >>), ]=, >{{$, ">{{$]; target-extreme [␠%%, ‹, ”, ª, €, {]; classes {'alphabetic': 38, 'mixed': 30, 'numeric': 1, 'punctuation': 278, 'special': 1, 'whitespace': 4}
- C7 (n=270): representatives [␠Crawford, ␠Liberia, ␠Hannah, ␠Sandra, ␠Jenna, ␠Seth, ␠Sanchez, ␠Rivera, ␠Gareth, Johnny]; target-extreme [␠Curry, ␠Manning, ␠Sudan, ␠Cassidy, ␠Kara, ␠Khan]; classes {'alphabetic': 269, 'mixed': 1}
- C8 (n=41): representatives [␠of, ␠de, ␠between, ␠from, 的, for, ␠OF, _to, _of, -of]; target-extreme [␠of, ␠to, 的, ␠OF, _of, ␠for]; classes {'alphabetic': 31, 'mixed': 10}
- C9 (n=20): representatives [␠Ej, ␠Moj, ␠مج, nej, ␠j, ␠Vij, 相邻, ␠aj, ej, ␠Adj]; target-extreme [Adj, ␠Bij, ␠Ej, ␠Mej, 相邻, ␠مج]; classes {'alphabetic': 20}

Strongest intercommunity connections:

- C0 to C3: 1644 token edges; mean cosine 0.128794
- C0 to C1: 1194 token edges; mean cosine 0.124167
- C1 to C3: 986 token edges; mean cosine 0.129393
- C0 to C5: 851 token edges; mean cosine 0.127350
- C0 to C2: 808 token edges; mean cosine 0.123733
- C1 to C2: 771 token edges; mean cosine 0.122696
- C2 to C4: 684 token edges; mean cosine 0.127087
- C1 to C4: 635 token edges; mean cosine 0.129599
- C3 to C5: 599 token edges; mean cosine 0.127679
- C4 to C5: 577 token edges; mean cosine 0.131370
- C2 to C3: 562 token edges; mean cosine 0.126170
- C2 to C5: 550 token edges; mean cosine 0.127578
- C1 to C5: 464 token edges; mean cosine 0.127274
- C3 to C4: 446 token edges; mean cosine 0.125924
- C0 to C4: 431 token edges; mean cosine 0.123726

## State 21 — block_20_output

Paired positive_head: membership Jaccard 0.799548; edge Jaccard 0.601363; shared tokens 5664.
Paired negative_tail: membership Jaccard 0.806303; edge Jaccard 0.616132; shared tokens 6115.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6567
- Directed 10-NN edges: 65670
- Undirected edges: 46523
- Communities: 9
- Modularity: 0.541581

All communities:

- C0 (n=1414): representatives [씯, ␠spriteBatch, 턔, 룁, ␠SelectListItem, [SerializeField, GtkWidget, 믈, نطق, .DropDownStyle]; target-extreme [🙇, .DropDownStyle, .IsNotNull, 댓, ␠richTextBox, ␠tableName]; classes {'alphabetic': 1167, 'mixed': 174, 'punctuation': 73}
- C1 (n=1338): representatives [떘, son, ol, ain, ad, em, ak, ik, um, ían]; target-extreme [kas, wish, kes, endum, acts, ␠cen]; classes {'alphabetic': 1311, 'mixed': 23, 'punctuation': 4}
- C2 (n=899): representatives [だと思います, をしている, ␠ngồi, ってる, ␠때문에, ␠شيء, していました, 得益于, ␠يحتاج, ってしまう]; target-extreme [␠كلمة, محاكم, 实在, 女装, ってくる, ␠책]; classes {'alphabetic': 885, 'mixed': 14}
- C3 (n=660): representatives [CP, \tds, ␠sc, CM, MD, FS, cs, \tlbl, CT, sn]; target-extreme [,k, ␠gps, fm, ␠ctl, \tcom, _nm]; classes {'alphabetic': 502, 'mixed': 154, 'punctuation': 4}
- C4 (n=620): representatives [agonal, ␠sum, ␠disgusting, ␠slipped, ␠transform, ␠altering, ␠transforms, ␠increases, ␠scratched, ␠pack]; target-extreme [␠strapped, ␠distracting, parameters, ␠underline, overwrite, crafted]; classes {'alphabetic': 563, 'mixed': 56, 'punctuation': 1}
- C5 (n=616): representatives [واشنطن, ␠kitchen, ␠electrodes, ␠cooker, ␠apartment, ␠pixels, ␠goalkeeper, ␠alimentos, ␠vinegar, ␠forehead]; target-extreme [Oak, ␠mats, Keywords, ␠resin, ␠Committee, ␠microscopic]; classes {'alphabetic': 602, 'mixed': 14}
- C6 (n=488): representatives [(ds, Component, (df, (table, (tree, (od, (fs, \treset, \tcolor, \tpath]; target-extreme [codes, ,axis, \tcolor, 码, =config, ␠raster]; classes {'alphabetic': 238, 'mixed': 249, 'punctuation': 1}
- C7 (n=373): representatives [');\r\n\r\n, "))\r\n, ");\r\n\r\n, ')\r\n\r\n, ")\r\n, ));\r\n\r\n, ";\r\n\r\n, ');\r\n, ))\r\n\r\n, ..."\n\n]; target-extreme [␠␠␠␠␠␠\r\n, ';\n\n\n\n, (",");\n, ]);\r\n\r\n, (',');\n, ')\r\n\r\n]; classes {'alphabetic': 3, 'mixed': 5, 'punctuation': 326, 'whitespace': 39}
- C8 (n=159): representatives [␠don, ␠according, ␠si, ␠不, ␠doesn, ␠didn, ␠từ, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [Instead, ␠don, ␠noch, ␠ei, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠пом]; classes {'alphabetic': 116, 'mixed': 11, 'punctuation': 10, 'whitespace': 22}

Strongest intercommunity connections:

- C0 to C2: 1665 token edges; mean cosine 0.134559
- C1 to C2: 978 token edges; mean cosine 0.133069
- C0 to C5: 914 token edges; mean cosine 0.127571
- C1 to C3: 906 token edges; mean cosine 0.137815
- C1 to C5: 867 token edges; mean cosine 0.128885
- C0 to C1: 861 token edges; mean cosine 0.124574
- C1 to C4: 834 token edges; mean cosine 0.131252
- C0 to C4: 709 token edges; mean cosine 0.125778
- C0 to C3: 666 token edges; mean cosine 0.127124
- C4 to C5: 652 token edges; mean cosine 0.128219
- C3 to C6: 621 token edges; mean cosine 0.140465
- C2 to C4: 606 token edges; mean cosine 0.129356
- C2 to C5: 581 token edges; mean cosine 0.129828
- C0 to C6: 563 token edges; mean cosine 0.127309
- C1 to C6: 504 token edges; mean cosine 0.130628

#### negative_tail

- Nodes: 6693
- Directed 10-NN edges: 66930
- Undirected edges: 47614
- Communities: 10
- Modularity: 0.484229

All communities:

- C0 (n=1700): representatives [␠retail, ␠LAW, ␠Clubs, ␠colleges, ␠apparel, ␠sessions, ␠experimentation, ␠airline, 母校, ␠curriculum]; target-extreme [␠Joint, ␠alumni, /name, Army, /authentication, .repo]; classes {'alphabetic': 1334, 'mixed': 366}
- C1 (n=1066): representatives [␠RTBU, ␠OnCollision, ␠thỏa, 采矿等, 明ら, ﯭ, ✽, ␠GUIStyle, 췐, ✬]; target-extreme [␠MaterialPageRoute, BootTest, ␠współpr, ⊔, ␠thỏa, ⚡]; classes {'alphabetic': 724, 'mixed': 162, 'punctuation': 180}
- C2 (n=1030): representatives [профессиона, ␠Traff, ␠RECE, ␠Crawford, ␠המקצועי, gee, ␠Retrie, ␠Herr, ␠hypoth, ␠Lynn]; target-extreme [␠TELE, ␠Lever, ␠Manning, ␠affili, olean, ␠PRES]; classes {'alphabetic': 967, 'mixed': 63}
- C3 (n=801): representatives [ハー, а, 𝑎, нный, ステ, ing, ์, у, �, и]; target-extreme [␠of, у, ａ, �, 𝑎, �]; classes {'alphabetic': 702, 'mixed': 20, 'numeric': 2, 'punctuation': 77}
- C4 (n=703): representatives [␠במיוחד, 攻势, 毅然, 壮大, 就能够, ␠בהם, 更具, ␠surely, 就會, ␠Testing]; target-extreme [前列, ␠Ninth, 第七届, /high, ␠MUST, 第一家]; classes {'alphabetic': 655, 'mixed': 47, 'punctuation': 1}
- C5 (n=557): representatives [␠sports, ␠Boxing, ␠FIFA, 公共文化, ␠motivational, ␠Ski, 戏曲, emia, ␠Golf, ␠Trade]; target-extreme [比分, ␠motivational, ␠Railway, UGC, ␠colleagues, ␠athletics]; classes {'alphabetic': 526, 'mixed': 31}
- C6 (n=343): representatives [␠//</, ␠*)__, ¯¯, >>), }());\n, ␠_______,, =?",, ))/(, ـ, "]; target-extreme [␠``(, ␠%%, {, ␠^{\n, =}, ]]; classes {'alphabetic': 19, 'mixed': 37, 'punctuation': 281, 'special': 1, 'whitespace': 5}
- C7 (n=259): representatives [.AR, /filepath, Ljava, .COMP, ␠Ret, _ret, _Pr, .coroutines, _FUN, _Dep]; target-extreme [.bukkit, .ret, _STA, /me, _barrier, _snd]; classes {'alphabetic': 78, 'mixed': 181}
- C8 (n=175): representatives [凡本网注, �, 明, 新, 保, �, �, 阜, ␠cover, �]; target-extreme [虎, 相邻, 遂, 盧, 반, 毕]; classes {'alphabetic': 137, 'mixed': 3, 'punctuation': 35}
- C9 (n=59): representatives [␠user, ␠Kunden, ␠customer, ␠venda, 客户, 万人次, ␠Clients, _Customer, 万千瓦, ␠clientes]; target-extreme [␠clientes, ␠tỷ, /User, \tclient, 万人次, ␠tỉ]; classes {'alphabetic': 54, 'mixed': 5}

Strongest intercommunity connections:

- C0 to C2: 1974 token edges; mean cosine 0.131407
- C0 to C5: 1574 token edges; mean cosine 0.134976
- C0 to C4: 1329 token edges; mean cosine 0.134084
- C0 to C1: 1219 token edges; mean cosine 0.126658
- C2 to C3: 903 token edges; mean cosine 0.131857
- C0 to C3: 730 token edges; mean cosine 0.127739
- C1 to C3: 725 token edges; mean cosine 0.131575
- C1 to C4: 708 token edges; mean cosine 0.129845
- C1 to C2: 651 token edges; mean cosine 0.127272
- C2 to C5: 625 token edges; mean cosine 0.130997
- C0 to C7: 596 token edges; mean cosine 0.125098
- C3 to C4: 579 token edges; mean cosine 0.134182
- C4 to C5: 523 token edges; mean cosine 0.130905
- C2 to C7: 507 token edges; mean cosine 0.128982
- C1 to C5: 473 token edges; mean cosine 0.128873

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6181
- Directed 10-NN edges: 61810
- Undirected edges: 43946
- Communities: 10
- Modularity: 0.543822

All communities:

- C0 (n=1305): representatives [ak, son, ain, em, ik, ían, ают, ok, ki, ac]; target-extreme [kas, ␠cen, zon, kes, man, kat]; classes {'alphabetic': 1280, 'mixed': 20, 'punctuation': 5}
- C1 (n=947): representatives [떘, 씯, 턔, 룁, ␠SelectListItem, 믈, ␠ngồi, ␠openFileDialog, 砠, نطق]; target-extreme [␠كلمة, 🙇, 女装, 镚, מלך, 츨]; classes {'alphabetic': 849, 'mixed': 34, 'punctuation': 64}
- C2 (n=851): representatives [をしている, してしまう, ␠때문에, ってる, ␠شيء, 得益于, それでも, していました, 贡献力量, ってしまう]; target-extreme [实在, محاكم, ってくる, عون, ␠realidad, 怎么看]; classes {'alphabetic': 842, 'mixed': 9}
- C3 (n=812): representatives [CP, \tds, (ds, Token, CM, (table, \tlbl, sn, (tree, \tcp]; target-extreme [codes, fm, ␠gps, (Keys, ,axis, ␠ctl]; classes {'alphabetic': 545, 'mixed': 265, 'punctuation': 2}
- C4 (n=666): representatives [␠electrodes, ␠kitchen, ␠apartment, sensor, واشنطن, ␠cooker, ␠artisans, ␠pixels, ␠balcony, 服务中心]; target-extreme [␠책, ␠mats, crafted, ␠raster, 雕像, 酱油]; classes {'alphabetic': 649, 'mixed': 16, 'punctuation': 1}
- C5 (n=612): representatives [pushViewController, ␠spriteBatch, [SerializeField, GtkWidget, .getOrElse, ␠CGRectMake, ␠XmlDocument, KeyListener, INFRINGEMENT, textbox]; target-extreme [␠tableName, .IsNotNull, ␠underline, overwrite, ␠estimator, ␠websocket]; classes {'alphabetic': 389, 'mixed': 221, 'punctuation': 2}
- C6 (n=413): representatives [agonal, ␠don, ␠disgusting, ␠according, ␠scratched, ␠slipped, ␠transforms, ␠handsome, ␠scrambled, ␠coated]; target-extreme [wish, Instead, ␠strapped, ␠distracting, parameters, ␠intervention]; classes {'alphabetic': 403, 'mixed': 10}
- C7 (n=412): representatives [');\r\n\r\n, "))\r\n, ");\r\n\r\n, ");\r\n, ")\r\n, ));\r\n\r\n, ";\r\n\r\n, ';\r\n\r\n, ))\r\n, >";\r\n]; target-extreme [␠␠␠␠␠␠\r\n, (',');\n, ')\r\n\r\n, ]);\r\n\r\n, (",");\n, ")\r\n\r\n]; classes {'alphabetic': 5, 'mixed': 7, 'punctuation': 359, 'whitespace': 41}
- C8 (n=126): representatives [+k, 𝑽, [k, +z, +C, ,k, +c, .getS, +x, +y]; target-extreme [,k, 𝐤, *k, [D, _Y, +x]; classes {'alphabetic': 47, 'mixed': 75, 'punctuation': 4}
- C9 (n=37): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠和, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t]; target-extreme [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠商品, ␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t, ␠�]; classes {'alphabetic': 9, 'punctuation': 8, 'whitespace': 20}

Strongest intercommunity connections:

- C1 to C2: 1345 token edges; mean cosine 0.134989
- C0 to C3: 1154 token edges; mean cosine 0.135969
- C1 to C5: 1085 token edges; mean cosine 0.131430
- C0 to C2: 1065 token edges; mean cosine 0.134614
- C0 to C4: 993 token edges; mean cosine 0.129821
- C1 to C4: 812 token edges; mean cosine 0.127084
- C3 to C5: 787 token edges; mean cosine 0.125812
- C0 to C1: 693 token edges; mean cosine 0.124735
- C0 to C6: 619 token edges; mean cosine 0.129192
- C4 to C5: 499 token edges; mean cosine 0.122384
- C0 to C5: 492 token edges; mean cosine 0.123273
- C2 to C4: 488 token edges; mean cosine 0.128048
- C4 to C6: 469 token edges; mean cosine 0.130008
- C2 to C6: 433 token edges; mean cosine 0.129555
- C2 to C5: 384 token edges; mean cosine 0.125558

#### negative_tail

- Nodes: 7006
- Directed 10-NN edges: 70060
- Undirected edges: 49585
- Communities: 9
- Modularity: 0.490332

All communities:

- C0 (n=1841): representatives [␠retail, ␠LAW, ␠Clubs, ␠manuscripts, ␠apparel, ␠sessions, ␠colleges, ␠tennis, ␠airline, ␠currents]; target-extreme [␠TELE, ␠alumni, ␠Joint, Army, ␠Buzz, /name]; classes {'alphabetic': 1400, 'mixed': 441}
- C1 (n=1275): representatives [␠RTBU, ␠thỏa, ␠OnCollision, ﯭ, профессиона, 明ら, ␠ParameterDirection, ✬, ␠GUIStyle, 췐]; target-extreme [␠MaterialPageRoute, ␠współpr, ⚡, 荼, BootTest, ␠Moż]; classes {'alphabetic': 879, 'mixed': 202, 'punctuation': 194}
- C2 (n=1024): representatives [␠במיוחד, 攻势, ␠rapid, 毅然, 艰辛, 壮大, 就能够, 更具, ␠rigor, مناسبة]; target-extreme [前列, 近视, 第七届, .Flag, ␠Ninth, 壮大]; classes {'alphabetic': 996, 'mixed': 27, 'punctuation': 1}
- C3 (n=942): representatives [␠Traff, ␠franch, .AR, ␠Ав, ␠utter, ␠hypoth, ␠immedi, ␠Herr, gee, ␠PROF]; target-extreme [␠الز, .ret, ␠наз, ␠PRES, 芦, ␠affili]; classes {'alphabetic': 766, 'mixed': 175, 'punctuation': 1}
- C4 (n=837): representatives [ハー, а, ステ, ا, ー, ์, �, �, ing, ␠of]; target-extreme [␠of, у, ａ, �, 𝑎, �]; classes {'alphabetic': 692, 'mixed': 24, 'numeric': 1, 'punctuation': 120}
- C5 (n=342): representatives [>>), }}, ␠[[], =?",, ', </, }());\n, ‟, ", */),]; target-extreme [␠``(, ”, {, ␠%%, ], =}]; classes {'alphabetic': 21, 'mixed': 31, 'punctuation': 285, 'special': 1, 'whitespace': 4}
- C6 (n=336): representatives [␠Carrie, ␠Liberia, ␠Crawford, ␠Lynn, ␠Russell, ␠Hannah, ␠Sandra, ␠Sudan, Johnny, ␠Hernandez]; target-extreme [␠Manning, ␠Ruth, ␠Bella, ␠Curry, ␠Coron, ␠Cassidy]; classes {'alphabetic': 331, 'mixed': 5}
- C7 (n=330): representatives [␠user, ␠business, -feira, ␠cultura, ␠jede, ␠før, ␠Kunden, 客户, ␠две, ␠бренд]; target-extreme [iação, ␠clientes, coverage, ␠colleagues, 节目, .cover]; classes {'alphabetic': 300, 'mixed': 29, 'punctuation': 1}
- C8 (n=79): representatives [␠media, ␠Testing, Testing, 试验, ␠testing, -help, Test, Tests, TestData, 求助]; target-extreme [Failed, azor, ␠Supported, _testing, imedia, Supported]; classes {'alphabetic': 53, 'mixed': 26}

Strongest intercommunity connections:

- C0 to C3: 2046 token edges; mean cosine 0.131101
- C0 to C2: 1910 token edges; mean cosine 0.134514
- C0 to C1: 1618 token edges; mean cosine 0.126370
- C1 to C2: 1048 token edges; mean cosine 0.130525
- C1 to C3: 900 token edges; mean cosine 0.128508
- C1 to C4: 886 token edges; mean cosine 0.134500
- C3 to C4: 826 token edges; mean cosine 0.133377
- C0 to C7: 729 token edges; mean cosine 0.131473
- C0 to C4: 710 token edges; mean cosine 0.130025
- C2 to C4: 701 token edges; mean cosine 0.130793
- C0 to C6: 643 token edges; mean cosine 0.134531
- C2 to C3: 632 token edges; mean cosine 0.128524
- C3 to C6: 523 token edges; mean cosine 0.133213
- C2 to C7: 516 token edges; mean cosine 0.131085
- C1 to C5: 457 token edges; mean cosine 0.140331

## State 22 — block_21_output

Paired positive_head: membership Jaccard 0.791926; edge Jaccard 0.601700; shared tokens 4963.
Paired negative_tail: membership Jaccard 0.807499; edge Jaccard 0.618668; shared tokens 5772.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 5637
- Directed 10-NN edges: 56370
- Undirected edges: 39959
- Communities: 11
- Modularity: 0.535837

All communities:

- C0 (n=1095): representatives [pe, em, ik, ain, ek, um, ok, ki, son, ido]; target-extreme [kas, 码, wish, ake, codes, man]; classes {'alphabetic': 1072, 'mixed': 21, 'punctuation': 2}
- C1 (n=1079): representatives [だと思います, 赤ちゃん, ␠때문에, ␠ngồi, ってる, นะคะ, だったので, とっても, とても, の中で]; target-extreme [实在, ␠책, 女装, -contained, ␠كلمة, นะคะ]; classes {'alphabetic': 1071, 'mixed': 8}
- C2 (n=879): representatives [떘, ␠spriteBatch, ␠SelectListItem, [SerializeField, GtkWidget, .dateTimePicker, SharedPointer, igrationBuilder, .getOrElse, .NumericUpDown]; target-extreme [Component, ␠doi, crafted, dataTable, ␠richTextBox, locator]; classes {'alphabetic': 647, 'mixed': 231, 'punctuation': 1}
- C3 (n=812): representatives [␠şikay, 씯, 턔, 룁, 믈, 砠, 唷, .DropDownStyle, maktad, 粿]; target-extreme [🙇, 댓, 侍, 捽, .DropDownStyle, 剁]; classes {'alphabetic': 743, 'mixed': 19, 'punctuation': 50}
- C4 (n=438): representatives [␠kitchen, ␠cardboard, ␠flakes, ␠apartment, 服务中心, ␠brown, ␠toddler, واشنطن, ␠huis, ␠Wohnung]; target-extreme [购物中心, ucken, ␠underline, ␠choke, 服务中心, ␠Goa]; classes {'alphabetic': 435, 'mixed': 3}
- C5 (n=377): representatives [\tds, ␠isi, CM, CT, SA, sn, ␠VB, MD, PM, ␠PD]; target-extreme [␠gps, \tcom, mts, \tap, ␠ctl, _HC]; classes {'alphabetic': 326, 'mixed': 50, 'punctuation': 1}
- C6 (n=371): representatives [(ds, (fs, \tlbl, (tree, (df, (Object, (table, (dateTime, (values, ,k]; target-extreme [cmb, (ts, (Keys, ,k, (ST, \tv]; classes {'alphabetic': 83, 'mixed': 283, 'punctuation': 5}
- C7 (n=278): representatives [');\r\n\r\n, ");\r\n, "))\r\n, ')\r\n\r\n, ');\r\n, ");\r\n\r\n, ]);\r\n, ")\r\n, ";\r\n\r\n, '\r\n\r\n]; target-extreme [")\r\n\r\n, ')\r\n\r\n, ("+, ().\n, ␠?>">\n, +="]; classes {'alphabetic': 1, 'mixed': 3, 'punctuation': 273, 'whitespace': 1}
- C8 (n=225): representatives [␠transform, ␠according, ␠recipe, ␠composition, ␠evolving, ␠transforms, ␠individual, ␠contained, ␠calculated, ␠pulling]; target-extreme [ventional, conv, ␠estimator, Instead, ␠descended, ␠intervention]; classes {'alphabetic': 220, 'mixed': 5}
- C9 (n=50): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠, ␠和, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠\t\n]; target-extreme [deviceId, ␠␠␠␠␠␠\r\n, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠是, \t\t\n\t\t\n\t\t\n, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'alphabetic': 7, 'punctuation': 7, 'whitespace': 36}
- C10 (n=33): representatives [😅, 🥳, 😱, ␠😀, ❕, 😪, 😳, 👹, 😣, 😤]; target-extreme [🥳, 😤, 😳, 🍄, 👹, 😣]; classes {'mixed': 1, 'punctuation': 32}

Strongest intercommunity connections:

- C1 to C3: 1398 token edges; mean cosine 0.130429
- C0 to C1: 1081 token edges; mean cosine 0.131931
- C2 to C3: 1051 token edges; mean cosine 0.130761
- C1 to C2: 840 token edges; mean cosine 0.124244
- C0 to C5: 716 token edges; mean cosine 0.136574
- C0 to C4: 691 token edges; mean cosine 0.129033
- C1 to C4: 683 token edges; mean cosine 0.128563
- C2 to C4: 616 token edges; mean cosine 0.125555
- C0 to C2: 611 token edges; mean cosine 0.119682
- C0 to C3: 548 token edges; mean cosine 0.124389
- C2 to C6: 518 token edges; mean cosine 0.132193
- C2 to C5: 447 token edges; mean cosine 0.125808
- C3 to C4: 403 token edges; mean cosine 0.126552
- C0 to C8: 380 token edges; mean cosine 0.132520
- C2 to C8: 343 token edges; mean cosine 0.127884

#### negative_tail

- Nodes: 6423
- Directed 10-NN edges: 64230
- Undirected edges: 45460
- Communities: 10
- Modularity: 0.486245

All communities:

- C0 (n=1581): representatives [␠LAW, ␠Clubs, ␠manuscripts, ␠colleges, профессиона, ␠Organisation, ␠insecurity, ␠apparel, ␠ticker, ␠authoritative]; target-extreme [␠alumni, Army, .repo, ␠contenders, _basic, ␠publicity]; classes {'alphabetic': 1180, 'mixed': 401}
- C1 (n=942): representatives [selectorMethod, ␠OnCollision, 明ら, ␠마지, ﯭ, ␠thỏa, ␠GUIStyle, 췐, 🕝, 母校]; target-extreme [␠MaterialPageRoute, DidAppear, ✀, ⊔, BootTest, ␠выполня]; classes {'alphabetic': 619, 'mixed': 132, 'punctuation': 191}
- C2 (n=851): representatives [␠internationally, 最常见的, ␠sogar, 就會, ␠Professional, ␠surely, ␠illegally, 毅然, роме, 前列]; target-extreme [␠Ninth, 权威, 旗下的, 没有必要, 主流, ␠igual]; classes {'alphabetic': 826, 'mixed': 23, 'punctuation': 2}
- C3 (n=827): representatives [а, ์, �, 𝑎, 𝑖, ␠of, ería, 𝖗, Í, �]; target-extreme [␠of, ␠for, ␠OF, 的, ａ, ␠уровне]; classes {'alphabetic': 740, 'mixed': 27, 'numeric': 1, 'punctuation': 59}
- C4 (n=805): representatives [␠profes, ␠Traff, .AR, ␠NEVER, ␠Ав, ␠immedi, ␠меди, ␠ciné, ␠evalu, _FUN]; target-extreme [␠TELE, /name, ␠Prest, .prof, ␠hypoth, ␠affili]; classes {'alphabetic': 564, 'mixed': 241}
- C5 (n=675): representatives [␠Liberia, ␠Crawford, ␠Dome, ␠Wall, ␠Russell, ␠Sandra, ␠Bro, ␠Hart, ␠Jimmy, ␠Wallet]; target-extreme [␠Buzz, ␠Bella, ␠Coron, ␠Cassidy, ␠Curry, ␠Manning]; classes {'alphabetic': 663, 'mixed': 12}
- C6 (n=350): representatives [␠sports, ␠tennis, ␠Boxing, ␠Trade, ␠surgical, ␠sexual, ␠FIFA, ␠Golf, 保险, ␠golf]; target-extreme [␠Joint, ␠fame, .sales, ␠Trade, Opera, ␠Foot]; classes {'alphabetic': 324, 'mixed': 26}
- C7 (n=333): representatives ["=>$, }}}, >>), ␠*)__, ),$, ´, }}, ¯¯, )], ()},]; target-extreme [=}, ّ, ␠``(, /=, ⽐, ª]; classes {'alphabetic': 28, 'mixed': 37, 'numeric': 1, 'punctuation': 261, 'special': 1, 'whitespace': 5}
- C8 (n=42): representatives [␠biggest, ␠bigger, ␠fullest, huge, better, ␠GREAT, ␠Better, ␠broader, .Big, ␠BIG]; target-extreme [huge, ␠biggest, -full, ␠GREAT, major, ␠huge]; classes {'alphabetic': 36, 'mixed': 6}
- C9 (n=17): representatives [␠áreas, ␠área, ␠врач, ␠alanı, ␠órgão, ␠energia, Area, .area, ␠categoria, AREA]; target-extreme [AREA, ␠área, ␠áreas, ␠ámbito, ␠visita, ␠alanı]; classes {'alphabetic': 15, 'mixed': 2}

Strongest intercommunity connections:

- C0 to C4: 1816 token edges; mean cosine 0.130086
- C0 to C2: 1296 token edges; mean cosine 0.132215
- C0 to C1: 1159 token edges; mean cosine 0.124312
- C0 to C6: 1109 token edges; mean cosine 0.136181
- C0 to C5: 1026 token edges; mean cosine 0.130079
- C4 to C5: 898 token edges; mean cosine 0.132981
- C0 to C3: 802 token edges; mean cosine 0.126499
- C1 to C2: 733 token edges; mean cosine 0.128253
- C1 to C3: 728 token edges; mean cosine 0.131870
- C2 to C3: 717 token edges; mean cosine 0.130453
- C1 to C4: 698 token edges; mean cosine 0.127432
- C3 to C4: 638 token edges; mean cosine 0.133333
- C2 to C4: 584 token edges; mean cosine 0.128739
- C3 to C5: 576 token edges; mean cosine 0.128112
- C1 to C7: 392 token edges; mean cosine 0.135591

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5593
- Directed 10-NN edges: 55930
- Undirected edges: 39732
- Communities: 8
- Modularity: 0.537033

All communities:

- C0 (n=1096): representatives [pe, ik, ka, em, ain, son, ek, el, ki, ien]; target-extreme [kas, mts, wish, man, ake, ␠cen]; classes {'alphabetic': 1082, 'mixed': 13, 'numeric': 1}
- C1 (n=901): representatives [␠şikay, 턔, 砠, ␠ngồi, 룁, 믈, 唷, .DropDownStyle, 馧, _kses]; target-extreme [🙇, 捽, 拈, 댓, 剁, 🥳]; classes {'alphabetic': 809, 'mixed': 13, 'punctuation': 79}
- C2 (n=802): representatives [だと思います, 赤ちゃん, ␠때문에, なかなか, นะคะ, とっても, だったので, ␠açıklama, してしまう, していました]; target-extreme [实在, -contained, ってくる, ␠пом, นะคะ, dıkları]; classes {'alphabetic': 787, 'mixed': 13, 'punctuation': 2}
- C3 (n=716): representatives [pushViewController, ␠spriteBatch, ␠SelectListItem, [SerializeField, .dateTimePicker, GtkWidget, .getOrElse, igrationBuilder, SharedPointer, .NumericUpDown]; target-extreme [crafted, -feedback, ␠doi, محاكم, ␠DatePicker, ␠richTextBox]; classes {'alphabetic': 502, 'mixed': 210, 'punctuation': 4}
- C4 (n=704): representatives [(ds, \tds, \tlbl, ␠isi, (df, (tree, sn, CM, (fs, \ttxt]; target-extreme [␠gps, cmb, ␠ctl, fm, (ts, \tcom]; classes {'alphabetic': 380, 'mixed': 301, 'punctuation': 8, 'whitespace': 15}
- C5 (n=631): representatives [떘, ␠kitchen, ␠cardboard, sensor, 服务中心, ␠apartment, ␠flakes, ␠huis, ␠apartments, ␠resin]; target-extreme [码, Component, codes, ␠책, 女装, ␠mats]; classes {'alphabetic': 612, 'mixed': 18, 'punctuation': 1}
- C6 (n=400): representatives [␠leaning, ␠transform, ␠grow, ␠released, ␠altering, ␠agréable, ␠transforms, ␠adaptation, ␠sending, ␠painstaking]; target-extreme [ventional, conv, ␠choke, ␠كلمة, ␠hang, ␠estimator]; classes {'alphabetic': 379, 'mixed': 21}
- C7 (n=343): representatives [');\r\n\r\n, ");\r\n, "))\r\n, ')\r\n\r\n, ");\r\n\r\n, ";\r\n\r\n, ';\r\n\r\n, ))\r\n\r\n, ');\r\n, ]);\r\n]; target-extreme [")\r\n\r\n, ("+, ')\r\n\r\n, +=", ().\n, "'\n]; classes {'alphabetic': 2, 'mixed': 5, 'punctuation': 316, 'whitespace': 20}

Strongest intercommunity connections:

- C1 to C2: 1284 token edges; mean cosine 0.132975
- C1 to C3: 1166 token edges; mean cosine 0.130857
- C0 to C4: 973 token edges; mean cosine 0.138910
- C0 to C2: 874 token edges; mean cosine 0.132773
- C0 to C5: 837 token edges; mean cosine 0.126832
- C3 to C5: 725 token edges; mean cosine 0.124786
- C3 to C4: 714 token edges; mean cosine 0.125738
- C0 to C1: 615 token edges; mean cosine 0.122720
- C1 to C5: 609 token edges; mean cosine 0.125281
- C2 to C3: 563 token edges; mean cosine 0.125598
- C2 to C5: 556 token edges; mean cosine 0.126281
- C5 to C6: 541 token edges; mean cosine 0.126340
- C0 to C6: 458 token edges; mean cosine 0.128273
- C0 to C3: 433 token edges; mean cosine 0.119417
- C2 to C6: 426 token edges; mean cosine 0.127224

#### negative_tail

- Nodes: 6497
- Directed 10-NN edges: 64970
- Undirected edges: 45930
- Communities: 10
- Modularity: 0.469209

All communities:

- C0 (n=1320): representatives [␠profes, ␠LAW, ␠Clubs, ␠Traff, ␠apparel, ␠ticker, .AR, ROSS, _Settings, ␠Dome]; target-extreme [␠TELE, /name, .prof, ␠Coron, .Flag, ␠Joint]; classes {'alphabetic': 840, 'mixed': 480}
- C1 (n=911): representatives [␠colleges, ␠insecurity, ␠Organisation, ␠sports, ␠industries, ␠fauna, ␠weddings, Companies, ␠Boxing, ␠areas]; target-extreme [Army, ␠feud, ␠solic, ␠publicity, ␠TRADE, ␠colleagues]; classes {'alphabetic': 874, 'mixed': 36, 'punctuation': 1}
- C2 (n=743): representatives [␠Crawford, ␠Liberia, ␠hypoth, ␠immedi, ␠FIFA, ␠Russell, ␠univers, ␠Sandra, ␠gramm, ␠evalu]; target-extreme [␠Buzz, ␠Curry, ␠Bella, ␠Cassidy, ␠hypoth, ␠Manning]; classes {'alphabetic': 723, 'mixed': 20}
- C3 (n=712): representatives [selectorMethod, 明ら, ﯭ, ␠GUIStyle, 传奇私服, ␠współpr, ✽, ✬, 🕝, �]; target-extreme [✀, ⊔, BootTest, 䢼, ␠Moż, ␠współpr]; classes {'alphabetic': 516, 'mixed': 11, 'punctuation': 185}
- C4 (n=707): representatives [а, ์, ␠of, роме, 𝑎, 𝖗, �, ე, �, á]; target-extreme [␠of, ␠for, 的, ␠OF, ａ, ␠to]; classes {'alphabetic': 625, 'mixed': 30, 'numeric': 1, 'punctuation': 51}
- C5 (n=704): representatives [母校, ␠glamour, ␠המקצועי, ␠internationally, ␠graduation, 最常见的, 行业发展, 全明星, ␠illegally, 都是非常]; target-extreme [␠alumni, _basic, huge, ␠Ninth, 权威, ␠fame]; classes {'alphabetic': 688, 'mixed': 15, 'punctuation': 1}
- C6 (n=692): representatives [␠OnCollision, ␠manuscripts, профессиона, ␠thỏa, ␠마지, ␠authoritative, DidAppear, MeshPro, Concurrency, .makeText]; target-extreme [DidAppear, .repo, ␠MaterialPageRoute, ␠contenders, .sales, /authentication]; classes {'alphabetic': 401, 'mixed': 285, 'punctuation': 6}
- C7 (n=328): representatives [}}}, ␠*)__, >>), ´, ¯¯, ]=], ‟, ␠*/), ـ, }}]; target-extreme [=}, ␠``(, ّ, /=, ␠%%, ⽐]; classes {'alphabetic': 24, 'mixed': 30, 'numeric': 1, 'punctuation': 268, 'special': 1, 'whitespace': 4}
- C8 (n=319): representatives [␠sogar, -month, ␠centro, ␠jede, ␠أيضا, тверж, דוגמה, ␠datos, -feira, ␠également]; target-extreme [␠уровне, ␠выполня, iação, ertura, ÖZ, ␠igual]; classes {'alphabetic': 309, 'mixed': 10}
- C9 (n=61): representatives [Training, ␠TESTING, Testing, ␠testing, ␠Test, rest, ␠analysis, 试验, ␠Prest, ␠sost]; target-extreme [␠Prest, _testing, Disk, ␠lessons, Latest, 訓練]; classes {'alphabetic': 52, 'mixed': 9}

Strongest intercommunity connections:

- C0 to C1: 1847 token edges; mean cosine 0.133323
- C0 to C2: 1431 token edges; mean cosine 0.131009
- C0 to C6: 1410 token edges; mean cosine 0.123817
- C1 to C5: 1028 token edges; mean cosine 0.132982
- C1 to C2: 865 token edges; mean cosine 0.132270
- C1 to C6: 850 token edges; mean cosine 0.128988
- C3 to C6: 831 token edges; mean cosine 0.130903
- C0 to C5: 784 token edges; mean cosine 0.131658
- C3 to C4: 637 token edges; mean cosine 0.133062
- C0 to C4: 631 token edges; mean cosine 0.126510
- C2 to C4: 545 token edges; mean cosine 0.129960
- C1 to C3: 513 token edges; mean cosine 0.128825
- C5 to C6: 490 token edges; mean cosine 0.126734
- C3 to C5: 456 token edges; mean cosine 0.129150
- C1 to C4: 451 token edges; mean cosine 0.128562

## State 23 — block_22_output

Paired positive_head: membership Jaccard 0.784516; edge Jaccard 0.580529; shared tokens 5239.
Paired negative_tail: membership Jaccard 0.784551; edge Jaccard 0.574579; shared tokens 5637.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 6060
- Directed 10-NN edges: 60600
- Undirected edges: 42693
- Communities: 11
- Modularity: 0.524248

All communities:

- C0 (n=1027): representatives [em, ik, ito, pe, ek, ka, ain, ad, ut, um]; target-extreme [kas, rk, ake, cea, igned, man]; classes {'alphabetic': 982, 'mixed': 42, 'numeric': 1, 'punctuation': 2}
- C1 (n=1024): representatives [턔, ␠wyśw, ␠ngồi, 믈, 砠, 唷, 😘, 铏, maktad, とはい]; target-extreme [␠schl, 侍, غل, 捽, 큠, محاكم]; classes {'alphabetic': 933, 'mixed': 8, 'punctuation': 83}
- C2 (n=1001): representatives [떘, 赤ちゃん, ␠kitchen, ␠flakes, sensor, ประเทศไทย, inté, ␠Cincinnati, سعيد, gan]; target-extreme [码, ayas, codes, ropsych, Ingredient, parameters]; classes {'alphabetic': 958, 'mixed': 43}
- C3 (n=698): representatives [␠spriteBatch, .visitMethodInsn, .dateTimePicker, ␠SelectListItem, [SerializeField, .getOrElse, GtkWidget, ␠POLITICO, KeyListener, ␠openFileDialog]; target-extreme [_transaksi, ␠DatePicker, ␠richTextBox, ␠eğlen, .drawImage, isEmpty]; classes {'alphabetic': 463, 'mixed': 227, 'punctuation': 8}
- C4 (n=683): representatives [(ds, cs, MD, (fs, ␠sc, sn, \tds, TL, ds, (tree]; target-extreme [cmb, fm, sn, ␠gps, _HC, ␠sd]; classes {'alphabetic': 404, 'mixed': 274, 'punctuation': 5}
- C5 (n=668): representatives [だと思います, นะคะ, 贡献力量, とっても, 保驾护航, しております, ってる, お願い, していました, ␠according]; target-extreme [实在, печат, ですよね, ␠për, ␠uống, ってくる]; classes {'alphabetic': 651, 'mixed': 12, 'punctuation': 5}
- C6 (n=509): representatives [␠disgusting, ␠switch, ␠don, ␠written, thinking, ␠transform, ␠report, ␠grow, ␠brown, ␠transforms]; target-extreme [␠ctl, ␠пом, ␠nostalgic, Instead, plemented, ␠stick]; classes {'alphabetic': 494, 'mixed': 15}
- C7 (n=221): representatives [');\r\n\r\n, ')\r\n\r\n, ");\r\n, ,', ")\r\n\r\n, ')\n\n\n, ');\r\n, ')\r\n, "\r\n\r\n\r\n, '\r\n\r\n]; target-extreme [.")\n, ')\r\n\r\n, ("+, .")\r\n, `)., ")\r\n\r\n]; classes {'alphabetic': 2, 'mixed': 2, 'punctuation': 190, 'whitespace': 27}
- C8 (n=189): representatives [дается, ают, iento, ías, ieren, ientos, iendo, aban, ählt, ßen]; target-extreme [ących, ucken, uesto, cheiden, acción, cych]; classes {'alphabetic': 189}
- C9 (n=24): representatives [jan, ␠months, March, ␠Jun, Jun, 一个小时, ␠hours, September, ␠Julian, 秋天]; target-extreme [season, Days, Wed, ␠months, jan, schedule]; classes {'alphabetic': 23, 'mixed': 1}
- C10 (n=16): representatives [Ẋ, Ṡ, ḣ, ṫ, ż, Ṛ, ṗ, Ṫ, ḷ, Ṁ]; target-extreme [Ṁ, ḷ, Ṫ, ḣ, Ṡ, Ẋ]; classes {'alphabetic': 16}

Strongest intercommunity connections:

- C1 to C3: 1158 token edges; mean cosine 0.129314
- C0 to C2: 1156 token edges; mean cosine 0.130673
- C1 to C5: 1099 token edges; mean cosine 0.133224
- C0 to C4: 1024 token edges; mean cosine 0.142028
- C2 to C3: 873 token edges; mean cosine 0.123125
- C1 to C2: 847 token edges; mean cosine 0.125912
- C2 to C6: 767 token edges; mean cosine 0.127296
- C0 to C6: 681 token edges; mean cosine 0.134984
- C2 to C5: 635 token edges; mean cosine 0.129239
- C0 to C1: 630 token edges; mean cosine 0.127899
- C3 to C4: 586 token edges; mean cosine 0.128758
- C5 to C6: 505 token edges; mean cosine 0.134982
- C0 to C8: 487 token edges; mean cosine 0.143484
- C2 to C4: 480 token edges; mean cosine 0.127393
- C3 to C5: 430 token edges; mean cosine 0.125618

#### negative_tail

- Nodes: 6645
- Directed 10-NN edges: 66450
- Undirected edges: 47015
- Communities: 9
- Modularity: 0.486917

All communities:

- C0 (n=1298): representatives [␠Clubs, ␠manuscripts, ␠colleges, ␠apparel, ␠cuffs, ␠weddings, ␠FIFA, 攻势, ␠automobiles, ␠artistic]; target-extreme [␠alumni, ␠Buzz, ␠fame, 重心, ␠Foot, ␠товаров]; classes {'alphabetic': 1215, 'mixed': 83}
- C1 (n=990): representatives [.AR, ␠Traff, ␠Restr, ␠Crawford, ␠Ав, ␠utter, ␠Liberia, ␠immedi, ␠Tele, ␠univers]; target-extreme [␠EFF, .prof, ␠Prest, ␠Gale, ␠Bella, ␠Cob]; classes {'alphabetic': 817, 'mixed': 173}
- C2 (n=964): representatives [профессиона, ␠CONT, ␠RECE, ␠Organisation, Companies, -founded, ROSS, -round, ␠Showing, ␠Directed]; target-extreme [Army, ␠TELE, ␠Lever, -loss, /authentication, URRED]; classes {'alphabetic': 700, 'mixed': 264}
- C3 (n=903): representatives [往往会, ␠המקצועי, ␠stricter, ␠internationally, ␠jede, 就會, 如果玩家, 都是非常, ␠sogar, 庞大的]; target-extreme [没有必要, 第七届, 旗下的, ␠từng, ␠Ninth, 一举]; classes {'alphabetic': 872, 'mixed': 30, 'punctuation': 1}
- C4 (n=899): representatives [␠WPARAM, ␠OnCollision, 明ら, ␠마지, ␠GUIStyle, ␠thỏa, ␠vazge, .ImageField, .MouseEventHandler, ✽]; target-extreme [DidAppear, ␠MaterialPageRoute, /general, hwnd, .Flag, _DEST]; classes {'alphabetic': 481, 'mixed': 400, 'punctuation': 18}
- C5 (n=768): representatives [𬭶, а, ์, �, �, 𝑎, اء, роме, �, 𝑖]; target-extreme [␠of, ␠уровне, ␠for, ａ, ␠OF, ␠géné]; classes {'alphabetic': 631, 'mixed': 30, 'numeric': 2, 'punctuation': 105}
- C6 (n=401): representatives [퓭, ✬, 䃎, אפליק, ﯦ, ﰀ, ﰿ, �, 넠, ﲟ]; target-extreme [꧁, �, 䢼, ✀, �, ⚡]; classes {'alphabetic': 223, 'mixed': 2, 'punctuation': 174, 'whitespace': 2}
- C7 (n=365): representatives [))==, }}}, })",, "=>$, )}, ␠//", ])),, ">',, ]=], >>)]; target-extreme [␠to, /name, ␠``(, =}, ={(), ++]=]; classes {'alphabetic': 19, 'mixed': 43, 'punctuation': 297, 'special': 1, 'whitespace': 5}
- C8 (n=57): representatives [␠user, ␠customer, 客户, ␠Kunden, ␠Area, ␠world, ustomer, 客户的, World, ␠clientes]; target-extreme [\Customer, ␠áreas, AREA, 客户, ␠área, 病人]; classes {'alphabetic': 44, 'mixed': 12, 'punctuation': 1}

Strongest intercommunity connections:

- C0 to C2: 1992 token edges; mean cosine 0.132150
- C0 to C1: 1537 token edges; mean cosine 0.133000
- C1 to C2: 1284 token edges; mean cosine 0.131999
- C2 to C4: 1265 token edges; mean cosine 0.125547
- C0 to C4: 1155 token edges; mean cosine 0.126520
- C0 to C3: 1107 token edges; mean cosine 0.130095
- C1 to C4: 870 token edges; mean cosine 0.125263
- C1 to C5: 848 token edges; mean cosine 0.130813
- C3 to C5: 763 token edges; mean cosine 0.131821
- C2 to C3: 712 token edges; mean cosine 0.131571
- C3 to C4: 680 token edges; mean cosine 0.128093
- C0 to C5: 628 token edges; mean cosine 0.127747
- C4 to C6: 591 token edges; mean cosine 0.132816
- C4 to C5: 541 token edges; mean cosine 0.128465
- C1 to C3: 524 token edges; mean cosine 0.128244

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 5857
- Directed 10-NN edges: 58570
- Undirected edges: 41271
- Communities: 11
- Modularity: 0.531318

All communities:

- C0 (n=1205): representatives [ito, pe, ik, ka, ek, el, ain, ki, ys, et]; target-extreme [kas, ących, rk, ayas, ucken, cea]; classes {'alphabetic': 1187, 'mixed': 18}
- C1 (n=914): representatives [sensor, ␠kitchen, ␠flakes, ␠disgusting, ␠switch, ␠transform, ␠toolkit, ␠painstaking, ␠written, ␠calculated]; target-extreme [码, codes, Ingredient, ␠mats, ␠translates, ␠intervention]; classes {'alphabetic': 859, 'mixed': 54, 'punctuation': 1}
- C2 (n=909): representatives [턔, 믈, 🐌, 砠, 唷, 😘, 铏, とはい, ␠meiden, 鳟]; target-extreme [␠schl, 큠, 슝, 捽, 🥳, ␠eğlen]; classes {'alphabetic': 809, 'mixed': 14, 'punctuation': 86}
- C3 (n=869): representatives [だと思います, ␠ngồi, นะคะ, 贡献力量, 赤ちゃん, 保驾护航, とっても, ってる, しております, だったので]; target-extreme [实在, печат, محاكم, ␠për, するために, _transaksi]; classes {'alphabetic': 856, 'mixed': 12, 'punctuation': 1}
- C4 (n=742): representatives [pushViewController, 떘, ␠spriteBatch, .visitMethodInsn, ␠SelectListItem, .dateTimePicker, [SerializeField, .getOrElse, KeyListener, .DropDownStyle]; target-extreme [cmb, ␠ctl, ␠DatePicker, ␠richTextBox, tmp, .drawImage]; classes {'alphabetic': 529, 'mixed': 206, 'punctuation': 7}
- C5 (n=631): representatives [(ds, ␠isi, sn, \tfs, (fs, \tds, (od, MD, (tree, ␠PD]; target-extreme [fm, ␠gps, sn, \tap, ␠sd, _HC]; classes {'alphabetic': 350, 'mixed': 278, 'punctuation': 3}
- C6 (n=264): representatives [␠Cincinnati, ␠Jamaica, ington, ␠Delhi, ประเทศไทย, ␠Italians, داعش, ␠Singapore, ␠huis, 服务中心]; target-extreme [服务中心, ␠Cincinnati, ␠francais, 巧克力, Seattle, thouse]; classes {'alphabetic': 262, 'mixed': 2}
- C7 (n=241): representatives [');\r\n\r\n, ')\r\n\r\n, ")\r\n\r\n, ')\n\n\n, ');\r\n, ,', ";\r\n, ")\n\n, .")\n, >\r\n\r\n\r\n]; target-extreme [.")\n, ')\r\n\r\n, ("+, ')\n\n, ")\r\n\r\n, .")\r\n]; classes {'alphabetic': 7, 'mixed': 4, 'punctuation': 203, 'whitespace': 27}
- C8 (n=41): representatives [␠don, ␠yet, ␠until, ␠Don, ␠since, ␠won, ␠having, ␠doing, ␠As, ␠upon]; target-extreme [␠пом, Instead, Having, ␠isn, ␠Having, ␠don]; classes {'alphabetic': 38, 'mixed': 3}
- C9 (n=26): representatives [omega, psi, epsilon, δ, tau, delta, rho, Psi, Omega, math]; target-extreme [◯, Δ, ␠Δ, Psi, glyph, symbol]; classes {'alphabetic': 22, 'mixed': 1, 'numeric': 1, 'punctuation': 2}
- C10 (n=15): representatives [Ṡ, Ẋ, ṫ, ḣ, Ṛ, Ṫ, Ṃ, Ċ, ṗ, Ṁ]; target-extreme [Ṁ, ḷ, Ṫ, ḣ, Ṡ, Ċ]; classes {'alphabetic': 15}

Strongest intercommunity connections:

- C2 to C3: 1316 token edges; mean cosine 0.131434
- C2 to C4: 1108 token edges; mean cosine 0.129849
- C0 to C1: 1083 token edges; mean cosine 0.128762
- C1 to C4: 943 token edges; mean cosine 0.123177
- C0 to C5: 911 token edges; mean cosine 0.141104
- C0 to C3: 905 token edges; mean cosine 0.133516
- C1 to C3: 755 token edges; mean cosine 0.127902
- C1 to C2: 725 token edges; mean cosine 0.126689
- C4 to C5: 630 token edges; mean cosine 0.127362
- C0 to C2: 620 token edges; mean cosine 0.125266
- C3 to C4: 606 token edges; mean cosine 0.125713
- C0 to C4: 426 token edges; mean cosine 0.122828
- C1 to C5: 413 token edges; mean cosine 0.125772
- C0 to C6: 399 token edges; mean cosine 0.131904
- C1 to C6: 362 token edges; mean cosine 0.124058

#### negative_tail

- Nodes: 6177
- Directed 10-NN edges: 61770
- Undirected edges: 43580
- Communities: 10
- Modularity: 0.491196

All communities:

- C0 (n=1106): representatives [␠franch, ␠Traff, ␠immedi, ␠Crawford, ␠aplic, ␠glamour, ␠utter, ␠Restr, ␠auditory, ␠hypoth]; target-extreme [␠Lever, ␠géné, ␠Gale, ␠Joint, ␠Foot, ␠Bella]; classes {'alphabetic': 1069, 'mixed': 37}
- C1 (n=1047): representatives [攻势, ␠stricter, ␠internationally, 母校, ␠jede, 影视, 行业发展, ␠две, ␠sogar, ␠أيضا]; target-extreme [␠alumni, ␠уровне, /authentication, ␠từng, ␠fame, 重心]; classes {'alphabetic': 1036, 'mixed': 10, 'punctuation': 1}
- C2 (n=882): representatives [␠apparel, ␠manuscripts, ␠colleges, ␠Clubs, ␠weddings, Companies, ␠frogs, ␠lowering, ␠forestry, ␠السيارات]; target-extreme [Army, ␠Buzz, .sales, ␠товаров, ␠probation, ␠contenders]; classes {'alphabetic': 839, 'mixed': 43}
- C3 (n=790): representatives [𬭶, .AR, ROSS, -round, ␠Directed, ␠Ав, ␠HALF, ␠NEVER, -founded, _Settings]; target-extreme [␠Prest, ␠EFF, .prof, ␠TELE, URRED, -loss]; classes {'alphabetic': 377, 'mixed': 413}
- C4 (n=768): representatives [明ら, ␠OnCollision, ␠WPARAM, ␠GUIStyle, ␠vazge, ␠thỏa, ␠마지, ✽, entionPolicy, DidAppear]; target-extreme [DidAppear, ␠announc, /general, .Menu, .repo, /name]; classes {'alphabetic': 377, 'mixed': 383, 'punctuation': 8}
- C5 (n=591): representatives [ﯭ, CppGuid, ␠�, ﰿ, 䃎, ﰀ, �, 넠, ﯱ, ␠współpr]; target-extreme [꧁, �, �, 䢼, ﻵ, ⚡]; classes {'alphabetic': 409, 'mixed': 10, 'punctuation': 172}
- C6 (n=574): representatives [а, 𝑎, ์, е, �, �, �, роме, ␠المتح, 𝑖]; target-extreme [␠of, ␠to, ａ, ␠for, ␠OF, �]; classes {'alphabetic': 503, 'mixed': 19, 'numeric': 1, 'punctuation': 51}
- C7 (n=374): representatives ["=>$, ␠*)__, }}}, 】,【, )}, })",, ␠//", =?",, ]=], )]]; target-extreme [␠``(, ”, =}, ={(), :-------------</, /=]; classes {'alphabetic': 29, 'mixed': 37, 'punctuation': 299, 'special': 1, 'whitespace': 8}
- C8 (n=31): representatives [␠world, World, ␠giới, Area, ␠áreas, ␠carta, ␠contrato, 的世界, ␠equipo, ␠área]; target-extreme [␠áreas, ␠área, AREA, 世界上最, .World, ␠Arte]; classes {'alphabetic': 27, 'mixed': 3, 'punctuation': 1}
- C9 (n=14): representatives [_Show, SHOW, zeigt, Show, >List, -show, ␠Shows, (show, >New, >Email]; target-extreme [-show, SHOW, ␠Shows, zeigt, >List, >Show]; classes {'alphabetic': 4, 'mixed': 10}

Strongest intercommunity connections:

- C0 to C2: 1680 token edges; mean cosine 0.132549
- C0 to C3: 1348 token edges; mean cosine 0.135013
- C1 to C2: 1347 token edges; mean cosine 0.131563
- C3 to C4: 1023 token edges; mean cosine 0.124099
- C0 to C1: 916 token edges; mean cosine 0.130238
- C2 to C4: 904 token edges; mean cosine 0.125397
- C2 to C3: 810 token edges; mean cosine 0.127228
- C0 to C4: 745 token edges; mean cosine 0.126378
- C4 to C5: 744 token edges; mean cosine 0.129077
- C1 to C4: 703 token edges; mean cosine 0.126205
- C1 to C6: 623 token edges; mean cosine 0.132232
- C1 to C3: 555 token edges; mean cosine 0.130388
- C1 to C5: 520 token edges; mean cosine 0.125417
- C0 to C6: 515 token edges; mean cosine 0.130434
- C5 to C6: 495 token edges; mean cosine 0.131692

## State 24 — block_23_output

Paired positive_head: membership Jaccard 0.815202; edge Jaccard 0.626642; shared tokens 6789.
Paired negative_tail: membership Jaccard 0.804680; edge Jaccard 0.609123; shared tokens 6258.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 7684
- Directed 10-NN edges: 76840
- Undirected edges: 54339
- Communities: 10
- Modularity: 0.526602

All communities:

- C0 (n=1607): representatives [ﰰ, ␠wyśw, ␠ngồi, .visitMethodInsn, نطق, 믈, 턔, 赤ちゃん, 唷, 馧]; target-extreme [큠, ␠për, ␠schl, محاكم, ⌯, ␠eğlen]; classes {'alphabetic': 1447, 'mixed': 24, 'punctuation': 136}
- C1 (n=1583): representatives [pushViewController, 떘, ␠spriteBatch, [SerializeField, ␠SelectListItem, .dateTimePicker, igrationBuilder, GtkWidget, SharedPointer, ␠XmlDocument]; target-extreme [cmb, 码, (il, parameters, .setCancelable, ␠ctl]; classes {'alphabetic': 1021, 'mixed': 555, 'punctuation': 7}
- C2 (n=1570): representatives [ito, em, ik, ad, pe, um, ap, ain, ka, se]; target-extreme [kas, zon, rk, cea, entin, ropsych]; classes {'alphabetic': 1539, 'mixed': 29, 'punctuation': 2}
- C3 (n=882): representatives [だと思います, นะคะ, características, とっても, になると, はずです, ってる, 保驾护航, 거든요, ␠isi]; target-extreme [实在, ących, ですよね, _transaksi, てくる, uesto]; classes {'alphabetic': 869, 'mixed': 11, 'punctuation': 2}
- C4 (n=599): representatives [␠think, ␠disgusting, ␠switch, ␠ask, ␠sit, ␠transform, ␠don, ␠until, ␠choose, ␠written]; target-extreme [Having, ␠пом, ␠hang, ␠distracting, ␠psyche, thanks]; classes {'alphabetic': 584, 'mixed': 15}
- C5 (n=528): representatives [␠Cincinnati, ประเทศไทย, ␠kitchen, ␠cabin, ␠brown, ␠Syracuse, ␠alimentos, ␠huis, ␠Barcelona, ␠yogurt]; target-extreme [Ingredient, 服务中心, ␠cousin, 副秘书长, ␠Produkt, 驾驶员]; classes {'alphabetic': 515, 'mixed': 12, 'punctuation': 1}
- C6 (n=476): representatives [␠sc, _y, \tcp, bc, sn, TL, ␠PD, CS, sd, PC]; target-extreme [␠gps, _HC, fm, (the, xm, sn]; classes {'alphabetic': 311, 'mixed': 156, 'punctuation': 9}
- C7 (n=316): representatives [');\r\n\r\n, ')\r\n\r\n, .\n\n\n, ');\r\n, ));\r\n, ")\r\n\r\n, );\r\n\r\n, ,', ")\r\n, ……\n\n]; target-extreme [")\r\n\r\n, ␠␠␠␠␠␠\r\n, ';\n\n\n\n, .")\n, .\r\n\r\n, ')\r\n\r\n]; classes {'alphabetic': 2, 'mixed': 5, 'punctuation': 263, 'whitespace': 46}
- C8 (n=73): representatives [␠months, 思, Jan, ␠YEAR, ␠septembre, 数, Jun, 个小时, ␠hours, ␠Jun]; target-extreme [season, ␠сентя, Days, six, 'clock, ␠Oct]; classes {'alphabetic': 70, 'mixed': 3}
- C9 (n=50): representatives [Ẋ, omega, psi, ḣ, ṡ, ␠ü, Psi, Γ, Ṡ, tau]; target-extreme [Ṫ, ◯, Ẋ, ḣ, ṗ, ␠ø]; classes {'alphabetic': 48, 'punctuation': 2}

Strongest intercommunity connections:

- C0 to C1: 1956 token edges; mean cosine 0.130303
- C0 to C3: 1721 token edges; mean cosine 0.137044
- C1 to C2: 1317 token edges; mean cosine 0.130583
- C2 to C3: 1071 token edges; mean cosine 0.140086
- C0 to C2: 933 token edges; mean cosine 0.128791
- C1 to C6: 911 token edges; mean cosine 0.134343
- C2 to C6: 886 token edges; mean cosine 0.146865
- C1 to C4: 876 token edges; mean cosine 0.131241
- C0 to C5: 863 token edges; mean cosine 0.132113
- C1 to C3: 768 token edges; mean cosine 0.126656
- C2 to C4: 732 token edges; mean cosine 0.141383
- C0 to C4: 724 token edges; mean cosine 0.132962
- C1 to C5: 690 token edges; mean cosine 0.126589
- C2 to C5: 624 token edges; mean cosine 0.136630
- C3 to C4: 605 token edges; mean cosine 0.136322

#### negative_tail

- Nodes: 6787
- Directed 10-NN edges: 67870
- Undirected edges: 47992
- Communities: 8
- Modularity: 0.504788

All communities:

- C0 (n=1495): representatives [␠trucks, ␠airline, ␠manuscripts, ␠colleges, ␠Clubs, ␠births, ␠tennis, ␠cuffs, 捐助, Companies]; target-extreme [␠Buzz, ␠alumni, ␠golf, ␠contenders, Army, ␠Trade]; classes {'alphabetic': 1445, 'mixed': 50}
- C1 (n=1162): representatives [𬭶, ␠LAW, -founded, ␠CONT, ROSS, ␠Directed, -round, -world, ␠Dome, _Settings]; target-extreme [␠Joint, ␠CROSS, -loss, /name, ␠Tops, URRED]; classes {'alphabetic': 546, 'mixed': 616}
- C2 (n=1027): representatives [␠במיוחד, ␠двух, ␠stricter, ␠lowering, ␠أيضا, ␠renewed, 更快, 举办的, ␠две, ␠current]; target-extreme [␠уровне, 没有必要, ␠Và, 主流, 一举, 第七届]; classes {'alphabetic': 985, 'mixed': 39, 'numeric': 1, 'punctuation': 2}
- C3 (n=938): representatives [明ら, ␠WPARAM, 퓭, �, ␠OnCollision, 펶, ␠마지, ␠GUIStyle, 嚆, ␠vazge]; target-extreme [␠MaterialPageRoute, ꧁, DidAppear, VERTISEMENT, 前列, �]; classes {'alphabetic': 655, 'mixed': 148, 'punctuation': 135}
- C4 (n=817): representatives [␠RECE, ␠Traff, ␠auditory, ␠immedi, ␠Restr, ␠Ав, ␠utter, ␠Retrie, ␠categor, ␠reint]; target-extreme [␠EFF, ␠Obst, ␠Lever, ␠laure, ␠Prest, ␠Cob]; classes {'alphabetic': 784, 'mixed': 33}
- C5 (n=511): representatives [а, ์, 𝑎, е, 𝑖, �, ิ, 𝒊, 𝖗, �]; target-extreme [␠of, 𝘦, ␠for, _of, ␠to, ａ]; classes {'alphabetic': 390, 'mixed': 32, 'punctuation': 89}
- C6 (n=446): representatives [}}}, )}, "=>$, )}), }}, ']}}</, ␠]), })",, )], ")}]; target-extreme [={(), =}, ّ, /List, ++]=, ()],]; classes {'alphabetic': 23, 'mixed': 61, 'punctuation': 354, 'special': 1, 'whitespace': 7}
- C7 (n=391): representatives [␠Crawford, ␠Liberia, ␠world, ␠Hart, ␠Bro, ␠Bra, ␠Manning, ␠Cobra, ␠Jehovah, Jimmy]; target-extreme [␠Gale, ␠Bella, ␠Бр, ␠Latter, ␠با, ␠Marr]; classes {'alphabetic': 373, 'mixed': 18}

Strongest intercommunity connections:

- C0 to C1: 1997 token edges; mean cosine 0.129332
- C0 to C2: 1485 token edges; mean cosine 0.128943
- C0 to C4: 1279 token edges; mean cosine 0.132935
- C1 to C4: 1204 token edges; mean cosine 0.131797
- C1 to C3: 943 token edges; mean cosine 0.123235
- C1 to C2: 905 token edges; mean cosine 0.128338
- C2 to C3: 857 token edges; mean cosine 0.130081
- C0 to C3: 816 token edges; mean cosine 0.127374
- C0 to C7: 730 token edges; mean cosine 0.130315
- C2 to C4: 670 token edges; mean cosine 0.130056
- C3 to C4: 587 token edges; mean cosine 0.131415
- C4 to C7: 578 token edges; mean cosine 0.134542
- C3 to C5: 531 token edges; mean cosine 0.135015
- C2 to C5: 519 token edges; mean cosine 0.132162
- C4 to C5: 455 token edges; mean cosine 0.129647

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 7433
- Directed 10-NN edges: 74330
- Undirected edges: 52302
- Communities: 11
- Modularity: 0.527979

All communities:

- C0 (n=1454): representatives [ik, ito, ka, se, pe, ki, ain, ek, ys, um]; target-extreme [kas, zon, ących, etas, cea, yan]; classes {'alphabetic': 1423, 'mixed': 31}
- C1 (n=1338): representatives [떘, תכנית, نطق, 赤ちゃん, sensor, ␠Cincinnati, ␠cabin, ␠flakes, ประเทศไทย, ␠huis]; target-extreme [Ingredient, entin, ropsych, محاكم, 服务中心, _transaksi]; classes {'alphabetic': 1272, 'mixed': 65, 'punctuation': 1}
- C2 (n=1204): representatives [ﰰ, ␠ngồi, 믈, 턔, 唷, 馧, 😘, 😼, 薅, 砠]; target-extreme [큠, ␠schl, ␠eğlen, 窍, 슝, ⌯]; classes {'alphabetic': 1066, 'mixed': 8, 'numeric': 1, 'punctuation': 129}
- C3 (n=815): representatives [(ds, \tlbl, (query, ␠isi, ␠PSU, (Object, ␠PD, ␠sc, _y, sn]; target-extreme [cmb, rk, ␠gps, (il, (the, _HC]; classes {'alphabetic': 456, 'mixed': 358, 'punctuation': 1}
- C4 (n=805): representatives [pushViewController, .visitMethodInsn, ␠spriteBatch, ␠SelectListItem, .dateTimePicker, igrationBuilder, SharedPointer, [SerializeField, .NumericUpDown, compileComponents]; target-extreme [␠për, overwrite, .setCancelable, ␠DatePicker, codes, ␠Produkt]; classes {'alphabetic': 512, 'mixed': 282, 'punctuation': 11}
- C5 (n=691): representatives [だと思います, นะคะ, とっても, になると, 贡献力量, はずです, 出てくる, 保驾护航, 거든요, と思って]; target-extreme [实在, ですよね, てくる, คน, ␠taste, と思って]; classes {'alphabetic': 679, 'mixed': 12}
- C6 (n=550): representatives [␠think, ␠disgusting, ␠ask, ␠sit, ␠written, ␠contradictory, ␠transform, ␠sum, ␠until, ␠choose]; target-extreme [Having, ␠suffer, \tget, ␠distracting, thanks, ␠stressing]; classes {'alphabetic': 531, 'mixed': 19}
- C7 (n=297): representatives [');\r\n\r\n, ')\r\n\r\n, ));\r\n\r\n, .\n\n\n, ));\r\n, ")\r\n\r\n, );\r\n\r\n, ');\r\n, "\r\n\r\n, ……\n\n]; target-extreme [")\r\n\r\n, ␠␠␠␠␠␠\r\n, .")\n, ';\n\n\n\n, .\r\n\r\n, ("+]; classes {'alphabetic': 1, 'mixed': 2, 'punctuation': 256, 'whitespace': 38}
- C8 (n=215): representatives [克, ␠brown, ␠المشكلة, 用, ␠cyan, 思, 热, 杀, 棉, ␠orange]; target-extreme [码, 凉, 悦, ␠uống, 坐, 职]; classes {'alphabetic': 206, 'mixed': 3, 'punctuation': 6}
- C9 (n=44): representatives [Ian, ␠Alan, Jun, Jan, ␠Claire, ␠Kevin, September, Alan, Michael, ␠Katherine]; target-extreme [ichael, Neil, leen, ␠сентя, ynthia, ␠Francis]; classes {'alphabetic': 44}
- C10 (n=20): representatives [psi, omega, Γ, tau, epsilon, Psi, δ, rho, ␠ν, ␠μ]; target-extreme [◯, Δ, Χ, ◎, δ, ␠Δ]; classes {'alphabetic': 17, 'punctuation': 3}

Strongest intercommunity connections:

- C1 to C2: 1533 token edges; mean cosine 0.131521
- C0 to C1: 1419 token edges; mean cosine 0.133114
- C2 to C4: 1160 token edges; mean cosine 0.131380
- C1 to C4: 1152 token edges; mean cosine 0.126719
- C0 to C3: 1070 token edges; mean cosine 0.140461
- C2 to C5: 997 token edges; mean cosine 0.135983
- C1 to C5: 985 token edges; mean cosine 0.134315
- C1 to C6: 939 token edges; mean cosine 0.132213
- C3 to C4: 822 token edges; mean cosine 0.130078
- C0 to C5: 715 token edges; mean cosine 0.137679
- C0 to C6: 673 token edges; mean cosine 0.138232
- C0 to C2: 641 token edges; mean cosine 0.128496
- C1 to C3: 573 token edges; mean cosine 0.125027
- C5 to C6: 501 token edges; mean cosine 0.137293
- C0 to C4: 494 token edges; mean cosine 0.124757

#### negative_tail

- Nodes: 7248
- Directed 10-NN edges: 72480
- Undirected edges: 51167
- Communities: 9
- Modularity: 0.492854

All communities:

- C0 (n=1804): representatives [␠trucks, ␠manuscripts, ␠Clubs, ␠LAW, -world, -round, -founded, ␠cuffs, ␠industries, Companies]; target-extreme [␠Joint, ␠Buzz, ␠golf, ␠alumni, Army, -loss]; classes {'alphabetic': 1492, 'mixed': 312}
- C1 (n=1186): representatives [␠Crawford, ␠Traff, ␠immedi, ␠auditory, ␠Ав, ␠utter, ␠univers, ␠orch, ␠Accred, ␠البريط]; target-extreme [␠Obst, ␠Gale, ␠Lever, ␠EFF, ␠Prest, ␠Bella]; classes {'alphabetic': 1138, 'mixed': 47, 'punctuation': 1}
- C2 (n=1143): representatives [明ら, ␠WPARAM, ␠OnCollision, ␠GUIStyle, �, 퓭, 嚆, ␠마지, 펶, ␠miệ]; target-extreme [꧁, ␠MaterialPageRoute, DidAppear, VERTISEMENT, 前列, 䢼]; classes {'alphabetic': 805, 'mixed': 186, 'punctuation': 152}
- C3 (n=981): representatives [␠במיוחד, ␠lowering, 如果玩家, ␠stricter, ␠أيضا, ␠renewed, ␠sogar, 将会, 更快, 举办的]; target-extreme [没有必要, 重心, 主流, ␠Và, ␠frontline, 一举]; classes {'alphabetic': 950, 'mixed': 30, 'punctuation': 1}
- C4 (n=633): representatives [␠CONT, ␠RECE, ROSS, ␠Restr, ␠current, _MOV, ␠HALF, ␠SPEED, .COMP, ␠Cont]; target-extreme [␠CROSS, .prof, URRED, _Height, /general, GREE]; classes {'alphabetic': 302, 'mixed': 331}
- C5 (n=600): representatives [𬭶, а, ์, 𝑎, е, �, ー, �, 了, 𝖗]; target-extreme [␠of, 𝘦, ａ, _of, ␠for, �]; classes {'alphabetic': 482, 'mixed': 22, 'numeric': 1, 'punctuation': 95}
- C6 (n=451): representatives [}}}, )}, }}, ␠*)__, ']}}</, )}), })",, ␠]), )], ␠//.]; target-extreme [={(), =}, ()],, :-------------</, ++]=, ␠``(]; classes {'alphabetic': 21, 'mixed': 60, 'punctuation': 361, 'special': 1, 'whitespace': 8}
- C7 (n=227): representatives [捐助, ␠user, انيا, ␠WORLD, ␠world, ␠media, ␠customer, ␠client, 客户, ␠России]; target-extreme [␠уровне, ␠áreas, 高层次, \Customer, 信念, .World]; classes {'alphabetic': 197, 'mixed': 30}
- C8 (n=223): representatives [␠двух, ␠first, ␠две, 两条, ␠NEVER, ␠primeiro, 第一位, ifth, ␠jede, ␠duas]; target-extreme [␠Monday, ␠toutes, 第七届, ␠różnych, ␠Ninth, 四级]; classes {'alphabetic': 189, 'mixed': 32, 'punctuation': 2}

Strongest intercommunity connections:

- C0 to C1: 2287 token edges; mean cosine 0.131445
- C0 to C3: 1582 token edges; mean cosine 0.129175
- C0 to C2: 1368 token edges; mean cosine 0.126003
- C0 to C4: 1314 token edges; mean cosine 0.128646
- C1 to C4: 1036 token edges; mean cosine 0.132318
- C2 to C3: 913 token edges; mean cosine 0.129599
- C1 to C2: 912 token edges; mean cosine 0.130016
- C1 to C3: 746 token edges; mean cosine 0.128962
- C2 to C5: 703 token edges; mean cosine 0.135834
- C0 to C7: 665 token edges; mean cosine 0.133197
- C1 to C5: 660 token edges; mean cosine 0.130173
- C2 to C4: 527 token edges; mean cosine 0.122399
- C3 to C5: 498 token edges; mean cosine 0.133785
- C0 to C5: 490 token edges; mean cosine 0.125229
- C3 to C4: 454 token edges; mean cosine 0.129636

## State 25 — block_24_output

Paired positive_head: membership Jaccard 0.813493; edge Jaccard 0.626759; shared tokens 6246.
Paired negative_tail: membership Jaccard 0.822009; edge Jaccard 0.638452; shared tokens 7186.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 7094
- Directed 10-NN edges: 70940
- Undirected edges: 49987
- Communities: 11
- Modularity: 0.517104

All communities:

- C0 (n=1539): representatives [pushViewController, ␠wyśw, ﰰ, .visitMethodInsn, ␠spriteBatch, 턔, ␠SelectListItem, 😼, UIImageView, 唷]; target-extreme [صيان, 큠, ⌯, ሴ, dsn, myśl]; classes {'alphabetic': 1248, 'mixed': 192, 'punctuation': 99}
- C1 (n=1165): representatives [ito, ad, se, pe, ain, ik, ki, ap, ka, ut]; target-extreme [zon, kas, rk, ucus, man, ake]; classes {'alphabetic': 1134, 'mixed': 30, 'numeric': 1}
- C2 (n=883): representatives [떘, sensor, ␠kitchen, ␠silicone, ␠flakes, ␠cabin, ␠cooker, ␠dataset, ␠garden, ␠Snapchat]; target-extreme [码, parameters, stack, tree, save, Ingredient]; classes {'alphabetic': 819, 'mixed': 62, 'punctuation': 2}
- C3 (n=879): representatives [␠cut, ␠think, ␠disgusting, sing, ␠identify, ␠ask, ␠grow, ring, ␠spray, cut]; target-extreme [ropsych, Having, standing, ␠asymmetric, ␠taste, ␠psyche]; classes {'alphabetic': 834, 'mixed': 44, 'punctuation': 1}
- C4 (n=874): representatives [だと思います, ␠ngồi, 赤ちゃん, นะคะ, とっても, 거든요, になると, と思って, 这样一来, それでも]; target-extreme [ですよね, 实在, season, محاكم, てくる, печат]; classes {'alphabetic': 863, 'mixed': 8, 'punctuation': 3}
- C5 (n=754): representatives [(ds, (query, q, \tlbl, sn, ␠sc, PC, (Object, sd, (df]; target-extreme [␠gps, sn, \tap, ␠yn, cmb, ␠sd]; classes {'alphabetic': 455, 'mixed': 297, 'punctuation': 2}
- C6 (n=368): representatives [ient, iendo, ificaciones, ías, дается, ucursal, ␠hizo, iento, ieren, ␠haben]; target-extreme [ących, _transaksi, ucken, ária, ␠realidad, uesto]; classes {'alphabetic': 358, 'mixed': 9, 'punctuation': 1}
- C7 (n=327): representatives [');\r\n\r\n, ");\r\n\r\n, ')\r\n\r\n, ");\r\n, );\r\n\r\n, ');\r\n, ")\r\n\r\n, .\n\n\n, ();\r\n\r\n, ␠␠␠␠␠␠␠␠\n]; target-extreme [")\r\n\r\n, ␠␠␠␠␠␠\r\n, ');\r\n, ')\r\n\r\n, ␠?>">\n, ';\n\n\n\n]; classes {'alphabetic': 5, 'mixed': 8, 'punctuation': 267, 'whitespace': 47}
- C8 (n=173): representatives [␠Portsmouth, ␠Cincinnati, ␠Syracuse, ␠Singapore, ␠Stuttgart, ريك, ␠Delhi, ␠Jamaica, ประเทศไทย, phis]; target-extreme [entin, xford, ælland, ␠Cincinnati, Neill, urnished]; classes {'alphabetic': 163, 'mixed': 9, 'punctuation': 1}
- C9 (n=88): representatives [思, 郁, 失, ␠dying, 痛, 碎, 懷, ␠Young, 产, 毒]; target-extreme [碎, young, 凉, 脏, 职, مق]; classes {'alphabetic': 86, 'mixed': 1, 'punctuation': 1}
- C10 (n=44): representatives [δ, Γ, Ẋ, ç, ḣ, ż, ␠Ç, ṫ, ñ, ␠ü]; target-extreme [Χ, ñ, Ẋ, Ṫ, δ, ┅]; classes {'alphabetic': 40, 'punctuation': 4}

Strongest intercommunity connections:

- C0 to C4: 1528 token edges; mean cosine 0.131035
- C0 to C2: 1239 token edges; mean cosine 0.126919
- C2 to C3: 1235 token edges; mean cosine 0.128083
- C1 to C5: 1100 token edges; mean cosine 0.141023
- C1 to C3: 1030 token edges; mean cosine 0.135448
- C1 to C2: 905 token edges; mean cosine 0.128544
- C0 to C3: 805 token edges; mean cosine 0.125672
- C1 to C6: 799 token edges; mean cosine 0.140978
- C3 to C4: 790 token edges; mean cosine 0.133269
- C0 to C5: 732 token edges; mean cosine 0.126718
- C2 to C4: 709 token edges; mean cosine 0.129369
- C0 to C1: 634 token edges; mean cosine 0.125632
- C2 to C5: 606 token edges; mean cosine 0.127701
- C1 to C4: 555 token edges; mean cosine 0.131255
- C4 to C6: 520 token edges; mean cosine 0.140857

#### negative_tail

- Nodes: 7794
- Directed 10-NN edges: 77940
- Undirected edges: 55196
- Communities: 9
- Modularity: 0.503922

All communities:

- C0 (n=1515): representatives [␠trucks, ␠Clubs, ␠births, ␠Dome, ␠tennis, ␠automobiles, ␠manuscripts, ␠perseverance, Companies, ␠weddings]; target-extreme [Army, ␠contenders, ␠golf, ␠alumni, /authentication, Applications]; classes {'alphabetic': 1442, 'mixed': 73}
- C1 (n=1290): representatives [␠OnCollision, �, 嚆, 明ら, ␠WPARAM, ␠vazge, ␠undisclosed, ␠thỏa, ␠마지, 퓭]; target-extreme [VERTISEMENT, ␠повер, <AudioSource, .Charting, ␠�, ␠الأمير]; classes {'alphabetic': 930, 'mixed': 212, 'punctuation': 148}
- C2 (n=1268): representatives [𬭶, ␠LAW, _Settings, ␠CONT, ␠RECE, ␠Directed, -founded, -world, ROSS, -round]; target-extreme [␠Joint, ␠EFF, ␠уровне, ␠CROSS, /name, .prof]; classes {'alphabetic': 518, 'mixed': 750}
- C3 (n=1011): representatives [攻势, ␠במיוחד, ␠двух, ␠areas, ␠world, 诠释, 两条, ␠أيضا, 第一位, ␠primeiro]; target-extreme [没有必要, 第七届, 一举, 接力, 祖国, 重心]; classes {'alphabetic': 964, 'mixed': 39, 'numeric': 3, 'punctuation': 5}
- C4 (n=785): representatives [␠Traff, ␠أمري, ␠auditory, ␠Restr, ␠Ав, ␠immedi, ␠cere, ␠milit, ␠Accred, ␠البريط]; target-extreme [␠Lever, Veter, ␠Bere, ␠alcanç, ␠Vers, ␠Obst]; classes {'alphabetic': 766, 'mixed': 19}
- C5 (n=546): representatives [)}, }}}, }}, ))], ))==, }), )}), }),, })",, "=>$]; target-extreme [=}, ␠=&, ={(), ␠&), ␠%=, ++]=]; classes {'alphabetic': 33, 'mixed': 89, 'punctuation': 415, 'special': 1, 'whitespace': 8}
- C6 (n=540): representatives [𝐈, а, ์, 𝑎, 🖏, 𝐚, 𝐑, 了, 𝖗, ever]; target-extreme [␠of, _of, �, ␠거, ␠to, �]; classes {'alphabetic': 386, 'mixed': 20, 'punctuation': 134}
- C7 (n=527): representatives [␠Crawford, 𝄕, ␠Miche, ␠Ле, ␠Rockefeller, ␠Bor, ␠Barr, ␠Cosby, ␠puff, ␠Gingrich]; target-extreme [␠Buzz, ␠Emerson, ␠Bella, ␠Jed, ␠Latter, ␠bolster]; classes {'alphabetic': 516, 'mixed': 9, 'punctuation': 2}
- C8 (n=312): representatives [␠renewed, ␠Begins, ␠restarting, ␠Ends, ␠Expand, ␠boosted, Checked, Finished, ␠Qualified, _Show]; target-extreme [完结, ␠Granted, -extension, /List, 过度, Outlined]; classes {'alphabetic': 264, 'mixed': 48}

Strongest intercommunity connections:

- C0 to C2: 1808 token edges; mean cosine 0.130093
- C0 to C3: 1264 token edges; mean cosine 0.134075
- C1 to C3: 1228 token edges; mean cosine 0.134947
- C0 to C4: 1219 token edges; mean cosine 0.136668
- C1 to C2: 1118 token edges; mean cosine 0.124779
- C0 to C1: 1095 token edges; mean cosine 0.130377
- C2 to C4: 1090 token edges; mean cosine 0.134454
- C0 to C7: 987 token edges; mean cosine 0.131890
- C1 to C4: 887 token edges; mean cosine 0.133548
- C2 to C3: 749 token edges; mean cosine 0.130168
- C1 to C6: 679 token edges; mean cosine 0.138422
- C4 to C7: 660 token edges; mean cosine 0.135135
- C0 to C8: 586 token edges; mean cosine 0.130001
- C1 to C5: 568 token edges; mean cosine 0.134195
- C2 to C7: 551 token edges; mean cosine 0.132660

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 6830
- Directed 10-NN edges: 68300
- Undirected edges: 47952
- Communities: 10
- Modularity: 0.519422

All communities:

- C0 (n=1532): representatives [떘, ␠silicone, ␠flakes, ␠disgusting, sensor, ␠cabin, 摁, ␠drinkers, oodoo, ␠resin]; target-extreme [ropsych, parameters, 侍, save, overwrite, ␠hang]; classes {'alphabetic': 1467, 'mixed': 61, 'punctuation': 4}
- C1 (n=1308): representatives [pushViewController, ﰰ, 턔, ␠spriteBatch, .visitMethodInsn, [SerializeField, תכנית, 😼, ␠SelectListItem, .dateTimePicker]; target-extreme [صيان, 큠, myśl, .drawImage, ⌯, ሴ]; classes {'alphabetic': 1044, 'mixed': 177, 'punctuation': 87}
- C2 (n=1016): representatives [se, ain, pe, ik, ka, ki, ap, um, ok, ys]; target-extreme [zon, kas, rk, man, ␠yn, yan]; classes {'alphabetic': 981, 'mixed': 35}
- C3 (n=861): representatives [(ds, (query, \tlbl, cs, ␠toolkit, q, 克, html, sn, ␠dataset]; target-extreme [码, season, ␠gps, sn, =config, ,params]; classes {'alphabetic': 545, 'mixed': 314, 'numeric': 1, 'punctuation': 1}
- C4 (n=766): representatives [だと思います, ␠ngồi, 赤ちゃん, นะคะ, 唷, とっても, であれば, になると, 거든요, ␠think]; target-extreme [实在, ですよね, ␠eğlen, ␠për, печат, てくる]; classes {'alphabetic': 759, 'mixed': 5, 'punctuation': 2}
- C5 (n=747): representatives [ito, ient, ira, ait, ati, ␠hizo, ica, ificaciones, ␠isi, дается]; target-extreme [ących, ucus, محاكم, etas, _transaksi, سعيد]; classes {'alphabetic': 728, 'mixed': 17, 'punctuation': 2}
- C6 (n=325): representatives [');\r\n\r\n, ");\r\n\r\n, ')\r\n\r\n, ");\r\n, ")\r\n\r\n, ?\n\n\n, ');\r\n, ";\r\n, "\r\n\r\n\r\n, .\n\n\n]; target-extreme [")\r\n\r\n, ␠␠␠␠␠␠\r\n, ');\r\n, .\r\n\r\n, six, ')\n\n]; classes {'alphabetic': 10, 'mixed': 6, 'punctuation': 268, 'whitespace': 41}
- C7 (n=138): representatives [␠kitchen, ␠garden, 服务中心, ␠huis, ␠chapel, controls, ␠Size, 城市管理, 园, 门店]; target-extreme [服务中心, 租房, ␠ctl, ␠vortex, 购物中心, 精准扶贫]; classes {'alphabetic': 134, 'mixed': 4}
- C8 (n=93): representatives [␠Delhi, ␠Cincinnati, ␠Syracuse, ␠Stuttgart, ␠دمشق, ␠Singapore, ␠Jamaica, ␠Jakarta, ประเทศไทย, ␠Bronx]; target-extreme [xford, ␠Cincinnati, .cz, ␠Alban, ประเทศไทย, 襄阳]; classes {'alphabetic': 86, 'mixed': 7}
- C9 (n=44): representatives [Ẋ, Γ, د, δ, ç, ص, ␠ü, Χ, ḣ, ṫ]; target-extreme [Χ, Ṫ, kü, Ẋ, ص, δ]; classes {'alphabetic': 41, 'punctuation': 3}

Strongest intercommunity connections:

- C2 to C5: 1607 token edges; mean cosine 0.140136
- C0 to C1: 1560 token edges; mean cosine 0.125668
- C0 to C2: 1244 token edges; mean cosine 0.134037
- C2 to C3: 1200 token edges; mean cosine 0.138393
- C1 to C4: 1194 token edges; mean cosine 0.131167
- C0 to C4: 1131 token edges; mean cosine 0.130727
- C0 to C3: 984 token edges; mean cosine 0.126586
- C0 to C5: 956 token edges; mean cosine 0.128682
- C1 to C3: 876 token edges; mean cosine 0.125447
- C4 to C5: 760 token edges; mean cosine 0.136067
- C1 to C5: 565 token edges; mean cosine 0.124870
- C1 to C2: 479 token edges; mean cosine 0.125494
- C2 to C4: 428 token edges; mean cosine 0.135419
- C3 to C5: 396 token edges; mean cosine 0.124593
- C0 to C7: 348 token edges; mean cosine 0.130680

#### negative_tail

- Nodes: 8134
- Directed 10-NN edges: 81340
- Undirected edges: 57423
- Communities: 10
- Modularity: 0.492626

All communities:

- C0 (n=1819): representatives [␠trucks, ␠LAW, ␠Clubs, ␠undisclosed, ␠manuscripts, ␠automobiles, ␠RECE, ␠births, ␠Traff, _Settings]; target-extreme [␠Joint, ␠contenders, ␠CROSS, ␠alumni, ␠Lever, 接力]; classes {'alphabetic': 1418, 'mixed': 401}
- C1 (n=1578): representatives [𬭶, ␠OnCollision, 明ら, �, ␠GUIStyle, ␠WPARAM, 嚆, 퓭, ␠마지, 펶]; target-extreme [={(), VERTISEMENT, ␠повер, ␠współpr, ␠Latter, .BorderFactory]; classes {'alphabetic': 1065, 'mixed': 326, 'punctuation': 187}
- C2 (n=1226): representatives [␠במיוחד, 两条, ␠أيضا, ␠également, 公共文化, 必须要, 举办的, ␠sogar, 前列, 就不会]; target-extreme [没有必要, ␠уровне, 一举, 祖国, 完结, 重心]; classes {'alphabetic': 1206, 'mixed': 14, 'punctuation': 6}
- C3 (n=1205): representatives [𝄕, ␠Crawford, ␠Dome, ␠CONT, ␠cere, .COMP, ␠Ав, ␠Ле, _Off, ␠Miche]; target-extreme [␠Buzz, ␠EFF, .prof, ␠Bella, ␠Emerson, ␠BUFF]; classes {'alphabetic': 923, 'mixed': 279, 'punctuation': 3}
- C4 (n=714): representatives [𝐚, ์, а, 𝑎, 𝖗, ever, нный, 𝒊, ｒ, 𝐑]; target-extreme [␠of, _of, �, ﾞ, ␠거, ａ]; classes {'alphabetic': 573, 'mixed': 18, 'numeric': 4, 'punctuation': 119}
- C5 (n=487): representatives [)}, }}}, }), ))], ))==, }}, }),, )}), "=>$, })",]; target-extreme [=}, ␠&), ␠=&, ␠%=, ++]=, :-------------</]; classes {'alphabetic': 39, 'mixed': 34, 'numeric': 1, 'punctuation': 404, 'special': 1, 'whitespace': 8}
- C6 (n=456): representatives [␠أمري, ␠tennis, ␠Boxing, ␠FIFA, ␠golf, ␠Golf, ␠league, ␠world, ␠fastball, ␠Zambia]; target-extreme [Army, ␠golf, ␠الأمير, ␠Farm, 旅游业, ␠feder]; classes {'alphabetic': 428, 'mixed': 28}
- C7 (n=290): representatives [␠areas, ␠line, ␠SPEED, .line, ␠user, ␠residents, ␠direction, ␠leaders, ␠class, (public]; target-extreme [_Height, /name, _basic, ␠SPEED, .Asset, ␠áreas]; classes {'alphabetic': 165, 'mixed': 124, 'punctuation': 1}
- C8 (n=241): representatives [第一位, \tfirst, ␠primeiro, 的第一, first, ␠DIRECT, [first, _Last, 第七届, ␠sixth]; target-extreme [第七届, ␠Monday, ␠Ninth, 第一位, ␠joint, /List]; classes {'alphabetic': 170, 'mixed': 71}
- C9 (n=118): representatives [␠renewed, ␠boosted, ␠concluded, ␠aument, _Show, urred, ␠Reve, ␠discussed, ␠testing, ␠fueled]; target-extreme [␠bolster, ␠sout, named, ␠Shows, ␠Hear, _Show]; classes {'alphabetic': 102, 'mixed': 16}

Strongest intercommunity connections:

- C0 to C3: 2388 token edges; mean cosine 0.132392
- C0 to C1: 1806 token edges; mean cosine 0.129408
- C0 to C2: 1407 token edges; mean cosine 0.134286
- C1 to C2: 1318 token edges; mean cosine 0.132710
- C1 to C3: 1221 token edges; mean cosine 0.128565
- C0 to C6: 1205 token edges; mean cosine 0.137242
- C1 to C4: 989 token edges; mean cosine 0.136482
- C3 to C4: 733 token edges; mean cosine 0.130817
- C0 to C7: 727 token edges; mean cosine 0.131826
- C2 to C4: 682 token edges; mean cosine 0.135657
- C3 to C6: 655 token edges; mean cosine 0.130634
- C2 to C3: 587 token edges; mean cosine 0.130176
- C1 to C5: 568 token edges; mean cosine 0.139776
- C0 to C4: 541 token edges; mean cosine 0.127623
- C1 to C6: 529 token edges; mean cosine 0.131089

## State 26 — block_25_output

Paired positive_head: membership Jaccard 0.819388; edge Jaccard 0.629528; shared tokens 7041.
Paired negative_tail: membership Jaccard 0.831736; edge Jaccard 0.655040; shared tokens 7464.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 7585
- Directed 10-NN edges: 75850
- Undirected edges: 53570
- Communities: 10
- Modularity: 0.537012

All communities:

- C0 (n=1378): representatives [␠flakes, ␠disgusting, ␠kitchen, ␠silicone, ␠cabin, ␠cardboard, ␠narciss, ␠veggies, ␠outsourcing, ␠synagogue]; target-extreme [ropsych, ␠distracting, Having, ␠cousin, ␠flakes, ␠scarf]; classes {'alphabetic': 1338, 'mixed': 39, 'punctuation': 1}
- C1 (n=1254): representatives [pushViewController, 떘, 씯, ␠productService, ␠spriteBatch, [SerializeField, igrationBuilder, ManyToOne, UIImageView, .dateTimePicker]; target-extreme [parameters, dsn, ,params, .drawImage, \tmat, .assertNot]; classes {'alphabetic': 796, 'mixed': 447, 'punctuation': 11}
- C2 (n=1209): representatives [ay, ap, pe, ik, ki, ok, ka, son, ␠kilometres, ad]; target-extreme [kas, zon, season, ␠sd, yan, .zone]; classes {'alphabetic': 1098, 'mixed': 111}
- C3 (n=1206): representatives [だと思います, 赤ちゃん, ␠ngồi, っております, はずです, นะคะ, とっても, になると, 거든요, かもしれません]; target-extreme [码, ですよね, 实在, محاكم, 嘲笑, ␠Produkt]; classes {'alphabetic': 1196, 'mixed': 8, 'punctuation': 2}
- C4 (n=1140): representatives [턔, ᵤ, ﰰ, תכנית, .ColumnStyle, 🐌, 唷, 圙, 薅, 😼]; target-extreme [صيان, myśl, ⌯, ᥴ, 碎, 🏙]; classes {'alphabetic': 989, 'mixed': 12, 'punctuation': 139}
- C5 (n=652): representatives [ían, ient, iento, ificaciones, ira, ␠descripcion, ait, ías, iendo, ␠meiden]; target-extreme [ucus, _transaksi, atient, ących, ventario, ␠sailor]; classes {'alphabetic': 641, 'mixed': 10, 'punctuation': 1}
- C6 (n=353): representatives [');\r\n\r\n, ");\r\n\r\n, ");\r\n, ')\r\n\r\n, >";\r\n, ")\r\n\r\n, ..."\n\n, }">\n, ")\r\n, ␠');\r\n]; target-extreme [")\r\n\r\n, ');\r\n, ␠?>">\n, ␠␠␠␠␠␠\r\n, .');\r\n, .")\r\n]; classes {'alphabetic': 4, 'mixed': 11, 'punctuation': 307, 'whitespace': 31}
- C7 (n=291): representatives [␠Portsmouth, ␠Southampton, ␠Cincinnati, ␠Syracuse, ␠Stuttgart, ประเทศไทย, ␠brown, ␠Slut, ␠Barcelona, ␠Jamaica]; target-extreme [ichael, entin, 主帅, Orange, almö, Carlos]; classes {'alphabetic': 284, 'mixed': 7}
- C8 (n=80): representatives [␠graveyard, ␠кафе, ␠Costco, 服务中心, ␠Küche, 保健品, カフェ, 微信群, 控制系统, 门店]; target-extreme [购物中心, 高等院校, 写字楼, 租房, 事业部, 服务中心]; classes {'alphabetic': 77, 'mixed': 3}
- C9 (n=22): representatives [␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠\t\t, \t␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; target-extreme [————————————————, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, ␠\t\t, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠␠, \t␠␠␠␠␠␠␠, ␠␠␠␠␠␠␠␠␠␠␠␠␠␠]; classes {'punctuation': 3, 'whitespace': 19}

Strongest intercommunity connections:

- C3 to C4: 1459 token edges; mean cosine 0.132728
- C0 to C1: 1443 token edges; mean cosine 0.127831
- C0 to C3: 1378 token edges; mean cosine 0.134507
- C1 to C2: 1342 token edges; mean cosine 0.131608
- C1 to C4: 1265 token edges; mean cosine 0.134329
- C2 to C5: 1151 token edges; mean cosine 0.138509
- C0 to C2: 1092 token edges; mean cosine 0.133734
- C0 to C4: 866 token edges; mean cosine 0.131696
- C1 to C3: 850 token edges; mean cosine 0.129509
- C3 to C5: 803 token edges; mean cosine 0.137127
- C0 to C5: 674 token edges; mean cosine 0.129282
- C2 to C4: 596 token edges; mean cosine 0.129158
- C2 to C3: 540 token edges; mean cosine 0.134198
- C1 to C5: 405 token edges; mean cosine 0.124844
- C0 to C7: 396 token edges; mean cosine 0.132652

#### negative_tail

- Nodes: 8318
- Directed 10-NN edges: 83180
- Undirected edges: 58302
- Communities: 12
- Modularity: 0.493056

All communities:

- C0 (n=2005): representatives [␠LAW, ␠trucks, ␠Clubs, ␠RECE, ␠Directed, _Settings, ␠Equipment, ␠undisclosed, _done, ␠Traff]; target-extreme [␠Joint, ␠Buzz, /authentication, Army, ␠contenders, ␠Relay]; classes {'alphabetic': 1552, 'mixed': 453}
- C1 (n=1353): representatives [␠OnCollision, 明ら, �, �, ␠vazge, 嚆, 퓭, ␠получа, 펶, ␠обесп]; target-extreme [�, ␠�, っ�, ␠повер, ␠alcanç, .Zoom]; classes {'alphabetic': 933, 'mixed': 190, 'punctuation': 230}
- C2 (n=1089): representatives [␠Crawford, 𝄕, ob, ␠hypoth, انيا, téri, ␠Ле, ␠Ав, ␠polit, ␠البريط]; target-extreme [␠Prel, ␠Bella, ␠Coron, ␠Trem, ␠الأمير, ␠Bere]; classes {'alphabetic': 1019, 'mixed': 68, 'punctuation': 2}
- C3 (n=1008): representatives [␠areas, area, 第一位, ␠world, ␠line, 真的很, 第一家, 的第一, 事故, 思路]; target-extreme [重心, 四级, 没有必要, ␠площад, 劲, 第七届]; classes {'alphabetic': 971, 'mixed': 37}
- C4 (n=813): representatives [ала, ␠במיוחד, ␠일이, 🖏, ์, 𝑎, ␠of, а, ␠centro, ａ]; target-extreme [␠of, _of, ７, ␠уровне, ﾞ, ␠Và]; classes {'alphabetic': 731, 'mixed': 20, 'numeric': 6, 'punctuation': 56}
- C5 (n=679): representatives [␠immedi, _Pro, .COMP, _Off, ␠Adv, ␠Ret, ␠RET, ␠PROF, BUFF, .Comm]; target-extreme [␠EFF, ␠Ret, ␠BUFF, Comm, _PULL, ␠STR]; classes {'alphabetic': 322, 'mixed': 357}
- C6 (n=499): representatives [)}, )), }), ))], }},, }}}, }}, ))), ))==, )})]; target-extreme [=}, ␠=&, ={(), ␠%=, ␠&), )}]; classes {'alphabetic': 28, 'mixed': 55, 'punctuation': 409, 'special': 1, 'whitespace': 6}
- C7 (n=442): representatives [␠current, ␠NEVER, ␠SPEED, _TOP, ␠stricter, ␠BEST, ␠last, first, (current, \tfirst]; target-extreme [_basic, ␠Tops, ␠SPEED, ALSE, _Height, ␠Latter]; classes {'alphabetic': 266, 'mixed': 175, 'punctuation': 1}
- C8 (n=272): representatives [␠warfare, ␠trade, ␠gotten, ␠obtained, ␠Trade, ␠Award, $list, ␠наз, ␠discussed, ␠commenced]; target-extreme [␠거, 买卖, ␠Trade, ␠Granted, getter, Revenue]; classes {'alphabetic': 237, 'mixed': 35}
- C9 (n=86): representatives [␠البر, ␠الط, ␠alf, ␠مو, ␠�, ␠الج, ␠הפר, ␠프, ␠الف, ␠الق]; target-extreme [␠המד, ␠세, ␠الز, ␠الطل, ␠הט, ␠الج]; classes {'alphabetic': 83, 'punctuation': 3}
- C10 (n=38): representatives [␠Rust, ␠androidx, ␠Flutter, ␠Unity, javax, ␠javax, ␠Angular, ␠Redux, .minecraft, ␠kotlin]; target-extreme [/android, (android, avax, ␠redux, android, (Route]; classes {'alphabetic': 27, 'mixed': 11}
- C11 (n=34): representatives [␠DIRECT, ␠film, ␠ciné, ␠filmm, ␠Direct, 电影, _direct, -direct, direct, DIRECT]; target-extreme [␠DIRECT, 电影, ␠filmm, ícul, 直播, ␠diret]; classes {'alphabetic': 31, 'mixed': 3}

Strongest intercommunity connections:

- C0 to C2: 2111 token edges; mean cosine 0.132746
- C0 to C3: 1675 token edges; mean cosine 0.134093
- C0 to C1: 1460 token edges; mean cosine 0.127688
- C0 to C5: 1407 token edges; mean cosine 0.127608
- C1 to C4: 999 token edges; mean cosine 0.135156
- C2 to C5: 994 token edges; mean cosine 0.134321
- C0 to C7: 989 token edges; mean cosine 0.134411
- C1 to C3: 875 token edges; mean cosine 0.132393
- C3 to C4: 852 token edges; mean cosine 0.136257
- C1 to C2: 849 token edges; mean cosine 0.129439
- C0 to C8: 763 token edges; mean cosine 0.135598
- C2 to C4: 739 token edges; mean cosine 0.131573
- C0 to C4: 737 token edges; mean cosine 0.129901
- C1 to C5: 533 token edges; mean cosine 0.125255
- C3 to C7: 460 token edges; mean cosine 0.139801

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 8049
- Directed 10-NN edges: 80490
- Undirected edges: 56503
- Communities: 9
- Modularity: 0.531696

All communities:

- C0 (n=1620): representatives [씯, 턔, ᵤ, ﰰ, תכנית, 믈, 🐌, ␠ngồi, 唷, 赤ちゃん]; target-extreme [صيان, محاكم, myśl, ␠misogyn, 큠, ⌯]; classes {'alphabetic': 1464, 'mixed': 17, 'numeric': 1, 'punctuation': 138}
- C1 (n=1585): representatives [ki, pe, ik, ka, ys, ient, ey, ek, man, han]; target-extreme [kas, zon, ucus, season, ␠sd, yan]; classes {'alphabetic': 1523, 'mixed': 61, 'punctuation': 1}
- C2 (n=1393): representatives [pushViewController, 떘, [SerializeField, igrationBuilder, .dateTimePicker, SharedPointer, UIImageView, sensor, GtkWidget, ␠kilometres]; target-extreme [码, parameters, .zone, ,params, .drawImage, dsn]; classes {'alphabetic': 901, 'mixed': 485, 'punctuation': 7}
- C3 (n=1392): representatives [␠flakes, ␠disgusting, ␠sensors, ␠drinkers, ␠classics, ␠shards, ␠ask, ␠identical, ␠outsourcing, 口味]; target-extreme [ropsych, Having, 嘲笑, atient, ␠asymmetric, ␠flakes]; classes {'alphabetic': 1349, 'mixed': 42, 'punctuation': 1}
- C4 (n=721): representatives [␠Portsmouth, ␠Cincinnati, ␠kitchen, ␠Southampton, ␠cardboard, ␠cabin, ␠silicone, ␠synagogue, ␠yogurt, ␠Barcelona]; target-extreme [ichael, 主帅, heim, Orange, ␠cousin, 高等院校]; classes {'alphabetic': 704, 'mixed': 17}
- C5 (n=615): representatives [だと思います, っております, とっても, นะคะ, はずです, אנשים, 거든요, になると, それでも, しております]; target-extreme [实在, ですよね, 看你, ようです, てくる, ␠realidad]; classes {'alphabetic': 610, 'mixed': 5}
- C6 (n=384): representatives [');\r\n\r\n, ");\r\n\r\n, ')\r\n\r\n, ");\r\n, >";\r\n, ")\r\n, ..."\n\n, ');\r\n, ␠');\r\n, ␠";\n]; target-extreme [")\r\n\r\n, ␠␠␠␠␠␠\r\n, ␠?>">\n, .');\r\n, ');\r\n, .")\r\n]; classes {'alphabetic': 4, 'mixed': 14, 'punctuation': 324, 'whitespace': 42}
- C7 (n=238): representatives [iendo, iento, ías, ␠mensajes, ␠descripcion, ificaciones, ␠hizo, quivo, ucursal, ␠codigo]; target-extreme [_transaksi, ventario, persona, rito, feito, ائق]; classes {'alphabetic': 230, 'mixed': 7, 'punctuation': 1}
- C8 (n=101): representatives [,k, 𝑌, ␠K, _y, .getS, _s, [s, *x, _K, \tY]; target-extreme [=z, ␠ك, 𝐤, six, Χ, *k]; classes {'alphabetic': 47, 'mixed': 53, 'punctuation': 1}

Strongest intercommunity connections:

- C0 to C2: 1615 token edges; mean cosine 0.131928
- C0 to C3: 1537 token edges; mean cosine 0.133175
- C1 to C2: 1474 token edges; mean cosine 0.132532
- C2 to C3: 1389 token edges; mean cosine 0.128698
- C1 to C3: 1148 token edges; mean cosine 0.133574
- C0 to C1: 1141 token edges; mean cosine 0.130797
- C0 to C4: 1140 token edges; mean cosine 0.135148
- C3 to C4: 1119 token edges; mean cosine 0.133681
- C0 to C5: 1104 token edges; mean cosine 0.138247
- C1 to C4: 859 token edges; mean cosine 0.133796
- C3 to C5: 739 token edges; mean cosine 0.135416
- C2 to C4: 728 token edges; mean cosine 0.129183
- C1 to C5: 566 token edges; mean cosine 0.136630
- C1 to C7: 497 token edges; mean cosine 0.143899
- C2 to C5: 323 token edges; mean cosine 0.129511

#### negative_tail

- Nodes: 8120
- Directed 10-NN edges: 81200
- Undirected edges: 56902
- Communities: 11
- Modularity: 0.497644

All communities:

- C0 (n=1536): representatives [␠OnCollision, _Settings, ␠WPARAM, .closePath, ␠buttonWithType, .LinearLayoutManager, DidAppear, SuppressLint, ␠UIStoryboardSegue, ␠JSName]; target-extreme [={(), .dequeueReusableCell, .Zoom, PointSize, _Height, _plane]; classes {'alphabetic': 532, 'mixed': 1000, 'punctuation': 4}
- C1 (n=1344): representatives [␠LAW, ␠trucks, ␠Clubs, ␠undisclosed, ␠Equipment, ␠Directed, ␠cuffs, ␠surgical, ␠berth, ␠THR]; target-extreme [␠Buzz, ␠Joint, /authentication, Army, ␠Relay, ␠contenders]; classes {'alphabetic': 1294, 'mixed': 50}
- C2 (n=1303): representatives [␠vazge, 明ら, ␠thỏa, ␠получа, 嚆, ␠RECE, ␠обесп, ␠immedi, ␠�, ␠느]; target-extreme [␠거, ␠Coron, っ�, ␠�, ␠площад, �]; classes {'alphabetic': 1203, 'mixed': 32, 'punctuation': 68}
- C3 (n=967): representatives [␠Crawford, 𝄕, انيا, -world, ␠Cosby, ord, ␠world, ␠DIRECT, ␠Ret, ␠PROF]; target-extreme [␠Prel, ␠EFF, ␠Bella, ␠Gale, ␠Bere, ␠Ret]; classes {'alphabetic': 851, 'mixed': 115, 'punctuation': 1}
- C4 (n=664): representatives [␠current, ␠line, ␠areas, ␠last, ␠final, ␠direction, ␠concluded, ␠retrieve, ␠renewed, 當時]; target-extreme [完结, rored, getter, ␠closure, Methods, ␠Granted]; classes {'alphabetic': 616, 'mixed': 48}
- C5 (n=613): representatives [第一位, ␠NEVER, 真的很, ␠power, 两条, 举办的, ␠две, \tfirst, 更快, first]; target-extreme [重心, 四级, 没有必要, _basic, ␠Light, 外国]; classes {'alphabetic': 570, 'mixed': 43}
- C6 (n=522): representatives [์, 𝑎, нный, а, ａ, ␠of, 𝒊, �, �, е]; target-extreme [␠of, _of, ﾞ, ７, ALSE, 劲]; classes {'alphabetic': 434, 'mixed': 13, 'numeric': 6, 'punctuation': 69}
- C7 (n=494): representatives [)}, }}}, )), }), )}}, }}, }},, ))], ))==, ")))]; target-extreme [=}, ␠=&, :-------------</, ␠&), )}, ␠%=]; classes {'alphabetic': 23, 'mixed': 47, 'punctuation': 418, 'special': 1, 'whitespace': 5}
- C8 (n=424): representatives [퓭, �, �, 펶, CppGuid, 넠, 🖏, ✬, 🉑, 𦰡]; target-extreme [䢼, ଽ, 〴, 𝕷, BootTest, �]; classes {'alphabetic': 266, 'mixed': 8, 'punctuation': 149, 'whitespace': 1}
- C9 (n=225): representatives [␠במיוחד, ала, area, ␠centro, ␠verbally, ␠أيضا, ␠הייתה, ␠стала, ␠rapidement, ␠были]; target-extreme [␠уровне, ␠effectively, reas, ␠rapidement, ␠aussi, ␠помощи]; classes {'alphabetic': 225}
- C10 (n=28): representatives [_TOP, IDD, midd, ␠middle, ␠Top, .top, (top, ␠TOP, ␠Middle, トップ]; target-extreme [_Top, IDDLE, .top, midd, Middle, bottom]; classes {'alphabetic': 21, 'mixed': 7}

Strongest intercommunity connections:

- C0 to C1: 1810 token edges; mean cosine 0.128582
- C1 to C2: 1537 token edges; mean cosine 0.133313
- C1 to C3: 1425 token edges; mean cosine 0.132519
- C2 to C3: 1395 token edges; mean cosine 0.133795
- C0 to C2: 1382 token edges; mean cosine 0.128897
- C0 to C3: 1195 token edges; mean cosine 0.129298
- C1 to C4: 1128 token edges; mean cosine 0.135395
- C0 to C4: 765 token edges; mean cosine 0.129615
- C1 to C5: 743 token edges; mean cosine 0.135997
- C2 to C8: 671 token edges; mean cosine 0.132144
- C2 to C6: 634 token edges; mean cosine 0.137107
- C2 to C5: 623 token edges; mean cosine 0.133447
- C4 to C5: 614 token edges; mean cosine 0.136418
- C2 to C4: 591 token edges; mean cosine 0.130400
- C0 to C5: 524 token edges; mean cosine 0.129124

## State 27 — block_26_output

Paired positive_head: membership Jaccard 0.820971; edge Jaccard 0.631542; shared tokens 7814.
Paired negative_tail: membership Jaccard 0.822352; edge Jaccard 0.636664; shared tokens 7888.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 8703
- Directed 10-NN edges: 87030
- Undirected edges: 61254
- Communities: 8
- Modularity: 0.548671

All communities:

- C0 (n=1988): representatives [떘, ␠disgusting, ␠psychiatric, sensor, ␠flakes, ␠sensors, ␠kilometres, atisation, ␠kitchen, ␠electrodes]; target-extreme [parameters, ropsych, ␠paint, ountains, Servers, ␠hang]; classes {'alphabetic': 1870, 'mixed': 117, 'punctuation': 1}
- C1 (n=1798): representatives [pushViewController, ␠wyśw, 턔, [SerializeField, 뿍, ␠ngồi, igrationBuilder, UIImageView, 馧, 궕]; target-extreme [耔, صيان, myśl, ␠misdemean, 吮, ὓ]; classes {'alphabetic': 1491, 'mixed': 156, 'punctuation': 151}
- C2 (n=1762): representatives [ito, ían, ik, za, ay, pe, ak, se, ley, son]; target-extreme [zon, kas, sit, ucus, yan, ci]; classes {'alphabetic': 1720, 'mixed': 39, 'numeric': 1, 'punctuation': 2}
- C3 (n=866): representatives [だと思います, はずです, นะคะ, 赤ちゃん, ␠think, とっても, 거든요, 这样一来, いろんな, と思って]; target-extreme [实在, ␠سن, 看你, ですよね, ␠según, казывает]; classes {'alphabetic': 840, 'mixed': 16, 'punctuation': 10}
- C4 (n=849): representatives [к, 克, (fs, map, 𝑌, id, PM, sd, config, xt]; target-extreme [=config, Map, rk, NM, ,params, sn]; classes {'alphabetic': 582, 'mixed': 259, 'punctuation': 8}
- C5 (n=675): representatives [");\r\n, ');\r\n\r\n, ')\r\n\r\n, ));\n\n, ")\r\n, >";\r\n, "))\r\n, ");\r\n\r\n, ).\n\n\n\n, ));\r\n]; target-extreme [.")\r\n, ")\r\n\r\n, ');\r\n, .")\n, ␠?>">\n, ␠␠␠␠␠␠\r\n]; classes {'alphabetic': 2, 'mixed': 10, 'punctuation': 570, 'special': 1, 'whitespace': 92}
- C6 (n=565): representatives [ificaciones, ␠synagogue, stitución, 服务中心, acimiento, ␠Costco, ␠graveyard, ␠descripcion, ␠غزة, ucursal]; target-extreme [码, ␠cousin, season, ออกแบบ, 主帅, مساعدة]; classes {'alphabetic': 551, 'mixed': 14}
- C7 (n=200): representatives [␠Portsmouth, ␠Cincinnati, ␠Syracuse, ประเทศไทย, ␠Stuttgart, ␠brown, ␠squash, ␠Asheville, Green, ␠Charlottesville]; target-extreme [ichael, Orange, xford, Carlos, rvine, ␠Katherine]; classes {'alphabetic': 193, 'mixed': 7}

Strongest intercommunity connections:

- C0 to C2: 2073 token edges; mean cosine 0.132222
- C0 to C1: 2010 token edges; mean cosine 0.128829
- C2 to C4: 1417 token edges; mean cosine 0.143383
- C0 to C3: 1238 token edges; mean cosine 0.134653
- C1 to C3: 1207 token edges; mean cosine 0.135929
- C1 to C2: 1178 token edges; mean cosine 0.129247
- C0 to C6: 1170 token edges; mean cosine 0.133080
- C2 to C3: 966 token edges; mean cosine 0.142445
- C1 to C4: 951 token edges; mean cosine 0.131935
- C1 to C6: 912 token edges; mean cosine 0.130558
- C0 to C4: 805 token edges; mean cosine 0.129351
- C2 to C6: 680 token edges; mean cosine 0.135482
- C3 to C6: 603 token edges; mean cosine 0.137116
- C2 to C7: 401 token edges; mean cosine 0.137797
- C0 to C7: 354 token edges; mean cosine 0.130806

#### negative_tail

- Nodes: 8456
- Directed 10-NN edges: 84560
- Undirected edges: 59520
- Communities: 11
- Modularity: 0.472903

All communities:

- C0 (n=1485): representatives [_done, _Settings, ␠Equipment, ␠Clubs, ␠Directed, ␠peripheral, ␠berth, ␠surgical, ␠renovation, ␠abnormalities]; target-extreme [.Collapsed, ␠Relay, ␠RECORD, /authentication, .Qual, Completed]; classes {'alphabetic': 1000, 'mixed': 485}
- C1 (n=1476): representatives [明ら, ␠RECE, ␠undisclosed, ␠�, ␠получа, ␠обесп, ␠immedi, ␠yönt, ␠thỏa, 落ち着]; target-extreme [␠거, เทร, Benef, ␠refin, ␠Prel, ␠feder]; classes {'alphabetic': 1415, 'mixed': 56, 'punctuation': 4, 'whitespace': 1}
- C2 (n=1106): representatives [␠LAW, ␠trucks, ␠Crawford, ␠Dome, 𝄕, ␠maneuver, ␠Hamilton, ␠tennis, ␠weddings, ␠golf]; target-extreme [␠Joint, ␠Nets, ␠Bere, Army, ␠Buzz, ␠Foot]; classes {'alphabetic': 1054, 'mixed': 51, 'punctuation': 1}
- C3 (n=1068): representatives [嚆, ␠OnCollision, selectorMethod, ␠vazge, �, ␠마지, ␠להתמוד, 퓭, �, .setBackgroundResource]; target-extreme [.GetEnumerator, <AudioSource, ␠MaterialPageRoute, DidAppear, ␠lief, 폭]; classes {'alphabetic': 655, 'mixed': 252, 'punctuation': 161}
- C4 (n=904): representatives [␠CONT, .COMP, _MOV, _Pro, ␠RET, _RO, .CON, _TRA, ␠FIFA, _Dep]; target-extreme [␠EFF, ␠MOD, ␠Prest, .contrib, ␠Coron, .Writer]; classes {'alphabetic': 480, 'mixed': 424}
- C5 (n=802): representatives [␠במיוחד, ␠двух, 再度, ␠auditory, ала, ␠בהם, ␠NEVER, ␠أيضا, 真的很, ␠مباشرة]; target-extreme [没有必要, ７, ␠уровне, 四级, 最强, ␠أيضا]; classes {'alphabetic': 762, 'mixed': 36, 'numeric': 3, 'punctuation': 1}
- C6 (n=581): representatives [攻势, ␠areas, area, ␠arena, ␠motorists, 力度, ␠Area, Participants, ␠residents, ␠contenders]; target-extreme [␠contenders, 重心, ␠spouses, 劲, ␠arena, ␠NATIONAL]; classes {'alphabetic': 555, 'mixed': 26}
- C7 (n=448): representatives [}}}, )}, 】,【, "=>$, )const, $get, ))==, }}, ),$, ))/(]; target-extreme [=torch, =}, ={(), ␠=&, ␠``(, ␠&)]; classes {'alphabetic': 26, 'mixed': 101, 'punctuation': 317, 'special': 1, 'whitespace': 3}
- C8 (n=365): representatives [𝑎, а, �, 了, 𝐑, �, у, �, �, ␠of]; target-extreme [_of, ␠of, �, 缇, �, ом]; classes {'alphabetic': 247, 'mixed': 16, 'punctuation': 102}
- C9 (n=147): representatives [␠BEST, ␠fists, [first, .Dispose, -first, first, 更快, (first, ␠BIG, \tfirst]; target-extreme [␠melhores, ␠fists, _FIRST, ␠fist, :first, .Next]; classes {'alphabetic': 75, 'mixed': 72}
- C10 (n=74): representatives [<Movie, _motion, ␠Movie, <Event, (strings, <Account, 影视, <Audio, 电影, <F]; target-extreme [<Mesh, .movie, ␠Television, <B, <Float, /Card]; classes {'alphabetic': 23, 'mixed': 51}

Strongest intercommunity connections:

- C1 to C2: 1620 token edges; mean cosine 0.134879
- C0 to C2: 1547 token edges; mean cosine 0.131874
- C0 to C1: 1545 token edges; mean cosine 0.133957
- C1 to C3: 1527 token edges; mean cosine 0.134714
- C0 to C4: 1473 token edges; mean cosine 0.127874
- C1 to C4: 1375 token edges; mean cosine 0.135588
- C0 to C6: 1051 token edges; mean cosine 0.133306
- C2 to C4: 1050 token edges; mean cosine 0.134228
- C1 to C5: 1018 token edges; mean cosine 0.137853
- C1 to C6: 930 token edges; mean cosine 0.134218
- C0 to C3: 885 token edges; mean cosine 0.126553
- C0 to C5: 835 token edges; mean cosine 0.131595
- C2 to C6: 735 token edges; mean cosine 0.134964
- C5 to C6: 554 token edges; mean cosine 0.133407
- C2 to C3: 549 token edges; mean cosine 0.128949

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 8629
- Directed 10-NN edges: 86290
- Undirected edges: 60645
- Communities: 9
- Modularity: 0.550602

All communities:

- C0 (n=1590): representatives [ito, ik, pe, ay, za, ca, ley, ak, ki, ka]; target-extreme [zon, sit, ucus, kas, yan, ichael]; classes {'alphabetic': 1563, 'mixed': 27}
- C1 (n=1568): representatives [pushViewController, 떘, UIImageView, sensor, ␠fontSize, SharedPointer, ␠CascadeType, ␠spyOn, ␠synagogue, INFRINGEMENT]; target-extreme [parameters, ibrary, ,params, Servers, =config, Platforms]; classes {'alphabetic': 1158, 'mixed': 406, 'punctuation': 4}
- C2 (n=1347): representatives [␠sensors, ␠disgusting, ␠kitchen, ␠flakes, ␠eating, ␠blogging, ␠classics, atisation, ␠organisation, ␠drinkers]; target-extreme [␠paint, ␠supervise, ␠insect, arking, ␠transforming, ␠bargain]; classes {'alphabetic': 1310, 'mixed': 36, 'punctuation': 1}
- C3 (n=1249): representatives [턔, 뿍, ␠ngồi, 馧, ␠practise, 궕, ␠vivastreet, 唷, 赤ちゃん, ␠kutje]; target-extreme [myśl, صيان, 耔, ␠misdemean, ὓ, 吮]; classes {'alphabetic': 1108, 'mixed': 5, 'punctuation': 136}
- C4 (n=810): representatives [だと思います, ␠think, ␠때문이다, とっても, はずです, นะคะ, 거든요, と思って, 这样一来, ␠Çok]; target-extreme [码, 实在, 看你, ␠일을, ですよね, ␠según]; classes {'alphabetic': 792, 'mixed': 15, 'punctuation': 3}
- C5 (n=769): representatives [iento, ␠psychiatric, ificaciones, 合资公司, stitución, iendo, acimiento, سعيد, ␠Snapchat, 服务中心]; target-extreme [ropsych, ountains, ␠cousin, ออกแบบ, محاكم, ␠executive]; classes {'alphabetic': 756, 'mixed': 13}
- C6 (n=659): representatives [");\r\n, ');\r\n\r\n, ));\n\n, ')\r\n\r\n, ));\r\n, >";\r\n, "))\r\n, "))\n, ');\r\n, ");\r\n\r\n]; target-extreme [.")\r\n, ")\r\n\r\n, ');\r\n, .")\n, ␠?>">\n, ␠␠␠␠␠␠\r\n]; classes {'alphabetic': 2, 'mixed': 11, 'punctuation': 565, 'special': 1, 'whitespace': 80}
- C7 (n=470): representatives [к, xt, sd, PD, \tY, ␠cp, GS, ␠sd, \tX, CS]; target-extreme [␠سن, NM, xm, fm, ␠sd, ␠xm]; classes {'alphabetic': 361, 'mixed': 105, 'numeric': 1, 'punctuation': 3}
- C8 (n=167): representatives [␠Portsmouth, ␠Cincinnati, ␠Syracuse, ␠Stuttgart, ␠outsourcing, ␠brown, openhagen, ␠Asheville, ประเทศไทย, ␠Jamaica]; target-extreme [Orange, xford, ␠Monsanto, ␠outsourcing, rvine, ␠Katherine]; classes {'alphabetic': 165, 'mixed': 2}

Strongest intercommunity connections:

- C1 to C2: 1663 token edges; mean cosine 0.129484
- C1 to C3: 1345 token edges; mean cosine 0.129591
- C0 to C2: 1317 token edges; mean cosine 0.136655
- C2 to C5: 1211 token edges; mean cosine 0.134705
- C0 to C1: 1183 token edges; mean cosine 0.127861
- C2 to C3: 1041 token edges; mean cosine 0.132210
- C3 to C4: 1008 token edges; mean cosine 0.136409
- C2 to C4: 973 token edges; mean cosine 0.137029
- C3 to C5: 930 token edges; mean cosine 0.131816
- C0 to C7: 925 token edges; mean cosine 0.146670
- C0 to C3: 906 token edges; mean cosine 0.130812
- C0 to C5: 891 token edges; mean cosine 0.135562
- C1 to C5: 870 token edges; mean cosine 0.126416
- C0 to C4: 682 token edges; mean cosine 0.140598
- C4 to C5: 633 token edges; mean cosine 0.135227

#### negative_tail

- Nodes: 9024
- Directed 10-NN edges: 90240
- Undirected edges: 63346
- Communities: 10
- Modularity: 0.474580

All communities:

- C0 (n=1875): representatives [明ら, 嚆, ␠undisclosed, ␠vazge, selectorMethod, ␠OnCollision, 퓭, �, ␠обесп, ␠ReferentialAction]; target-extreme [␠거, เทร, .GetEnumerator, <AudioSource, ประโย, ␠площад]; classes {'alphabetic': 1368, 'mixed': 307, 'punctuation': 200}
- C1 (n=1801): representatives [␠Cameroon, ␠LAW, ␠Crawford, 𝄕, ␠Traff, ␠Dome, ␠cuffs, ␠berth, ␠Reception, ␠weddings]; target-extreme [␠Joint, ␠Buzz, ␠Nets, Army, ␠Bere, ␠Prel]; classes {'alphabetic': 1717, 'mixed': 83, 'punctuation': 1}
- C2 (n=1400): representatives [_done, ␠areas, _gap, area, Selected, ␠abnormalities, ␠assistance, ␠taped, ␠Area, -round]; target-extreme [Completed, ␠RECORD, .Qual, /authentication, _snd, ␠suspected]; classes {'alphabetic': 978, 'mixed': 422}
- C3 (n=1277): representatives [攻势, ␠במיוחד, 再度, ала, ␠בהם, ␠NEVER, ␠BEST, 接力, ␠مباشرة, 不合适]; target-extreme [␠melhores, 没有必要, ␠feder, 重心, ␠уровне, 四级]; classes {'alphabetic': 1206, 'mixed': 71}
- C4 (n=726): representatives [␠RECE, ␠CONT, _Pro, ␠promising, _MOV, .COMP, _Dep, ␠Restr, _RO, ␠Ret]; target-extreme [Benef, ␠refin, ␠EFF, ␠MOD, ␠OVER, 'aff]; classes {'alphabetic': 421, 'mixed': 305}
- C5 (n=522): representatives [␠двух, 𝑎, ord, ａ, �, ␠Боль, 𝐑, �, а, у]; target-extreme [_of, ␠of, ７, �, ом, 폭]; classes {'alphabetic': 396, 'mixed': 34, 'numeric': 4, 'punctuation': 88}
- C6 (n=445): representatives [)}, ))==, "=>$, }}}, )const, 】,【, }}, )},, ),$, }),]; target-extreme [=}, ={(), ␠``(, ␠=&, :-------------</, ␠&)]; classes {'alphabetic': 23, 'mixed': 81, 'punctuation': 336, 'special': 1, 'whitespace': 4}
- C7 (n=444): representatives [␠trucks, ␠Equipment, ␠Directed, ␠Clubs, メンバー, _Settings, ␠surgical, ␠peripheral, ␠auditory, ␠automobiles]; target-extreme [␠spouses, ␠arena, ␠cattle, 农家, -team, ␠đệ]; classes {'alphabetic': 400, 'mixed': 44}
- C8 (n=411): representatives [$get, ␠SPEED, <Event, (strings, [first, $time, 的新, (Local, .High, (current]; target-extreme [=torch, /disc, (Op, .Writer, (Packet, /name]; classes {'alphabetic': 112, 'mixed': 299}
- C9 (n=123): representatives [前列, 第一家, 的第一, ␠Rust, 第一位, ␠Ult, ␠sixth, ␠seventh, 的第一个, .First]; target-extreme [␠fist, _FIRST, 第七届, ␠Ninth, 第一部, :first]; classes {'alphabetic': 95, 'mixed': 28}

Strongest intercommunity connections:

- C1 to C2: 2007 token edges; mean cosine 0.132239
- C0 to C1: 1857 token edges; mean cosine 0.133856
- C0 to C3: 1689 token edges; mean cosine 0.135508
- C2 to C3: 1549 token edges; mean cosine 0.133602
- C1 to C4: 1456 token edges; mean cosine 0.137800
- C0 to C2: 1403 token edges; mean cosine 0.128992
- C1 to C3: 1172 token edges; mean cosine 0.132747
- C2 to C4: 1145 token edges; mean cosine 0.129224
- C1 to C7: 1044 token edges; mean cosine 0.137337
- C2 to C7: 868 token edges; mean cosine 0.131360
- C0 to C5: 859 token edges; mean cosine 0.138052
- C0 to C4: 792 token edges; mean cosine 0.133223
- C2 to C8: 689 token edges; mean cosine 0.127624
- C1 to C5: 612 token edges; mean cosine 0.133845
- C3 to C5: 565 token edges; mean cosine 0.137187

## State 28 — final_norm_after_block_27

Paired positive_head: membership Jaccard 0.775602; edge Jaccard 0.560134; shared tokens 7566.
Paired negative_tail: membership Jaccard 0.773731; edge Jaccard 0.558323; shared tokens 7499.

### baseline

Prompt: `What structure forms from electro pink, curvature density, Tokyo nightlife?`

#### positive_head

- Nodes: 8785
- Directed 10-NN edges: 87850
- Undirected edges: 61142
- Communities: 11
- Modularity: 0.495051

All communities:

- C0 (n=1675): representatives [pushViewController, ארוחת, ␠productService, 住房公积, 컥, 흣, ␠@{@", ᵤ, 뿍, :@"%@",]; target-extreme [文章来源, /apimachinery, 浍, ␠GetHashCode, _PLUGIN, הלכה]; classes {'alphabetic': 1072, 'mixed': 574, 'punctuation': 29}
- C1 (n=1287): representatives [هة, ␠psychological, ␠экономическ, ␠opportunities, היסטוריה, политическ, ␠économique, حتياج, ␠insecurity, ␠philosophical]; target-extreme [␠passions, ␠geography, Phys, context, ût, ␠downloading]; classes {'alphabetic': 1212, 'mixed': 74, 'punctuation': 1}
- C2 (n=1240): representatives [クリニック, 奢侈品, 房企, 걀, ␠vodka, ␠granite, 的精神, ␠decor, 옷, 服务]; target-extreme [证券, 祖, 社会, 统计数据, 广场, ␠liqu]; classes {'alphabetic': 1209, 'mixed': 14, 'punctuation': 17}
- C3 (n=1127): representatives [␠jakieś, 唷, ␠오히려, ␠굉장히, たくさん, אנשים, やっぱ, มากมาย, そもそも, ␠המשפחה]; target-extreme [简称, 是由, ␠yıl, ␠każdym, 将在, 仅供参考]; classes {'alphabetic': 1113, 'mixed': 9, 'punctuation': 5}
- C4 (n=941): representatives [(CC, ␠text, ␠sc, ␠image, \tchar, ␠char, (param, ␠name, ␠XML, ␠object]; target-extreme [gcc, .Configuration, .XML, _FL, ym, _Get]; classes {'alphabetic': 565, 'mixed': 375, 'punctuation': 1}
- C5 (n=847): representatives [죳, ﭩ, 😘, ␠miệ, ☧, ס, ⇾, ическ, дается, wünsche]; target-extreme [뫼, 얏, ǘ, Ù, 〼, 🦌]; classes {'alphabetic': 639, 'mixed': 7, 'numeric': 1, 'punctuation': 200}
- C6 (n=670): representatives [Hugh, ␠하나님의, ks, har, ham, ␠ха, ␠Sec, ␠Kr, ␠Gr, ␠Sag]; target-extreme [شؤون, hum, ␠schl, ␠pó, ␠gén, íg]; classes {'alphabetic': 628, 'mixed': 41, 'punctuation': 1}
- C7 (n=456): representatives [))));\n, ?", !", ())));\n, 。（, ")\r\n\r\n, ."));\n, ');\r\n, ␠&\n, ."\n\n\n]; target-extreme [<?>>, ␠}}"><, ┅, =$("#, &_, ';\n\n\n\n]; classes {'alphabetic': 13, 'mixed': 79, 'punctuation': 345, 'whitespace': 19}
- C8 (n=327): representatives [خلق, ␠transform, ␠Create, ␠compilers, ␠classify, 推崇, ␠form, ␠disappear, 构建, 组建]; target-extreme [␠transforming, LOAD, تحضير, 盼望, Assembler, ␠Construct]; classes {'alphabetic': 305, 'mixed': 22}
- C9 (n=187): representatives [␠الحكومة, ␠السياسية, مفهوم, ␠ترامب, פעילויות, ␠деятельность, ␠Antarctica, ␠Bolshevik, 在上海, فلسطين]; target-extreme [Paris, ␠الاسلام, ␠власти, ␠barcelona, ␠Corbyn, منتدى]; classes {'alphabetic': 185, 'mixed': 2}
- C10 (n=28): representatives [系統, 시스템, 控制系统, _SYS, 控制, ␠систем, ␠sys, ␠système, 信息系统, SYS]; target-extreme [(SYS, 市场化, 管理体系, 信息系统, 高标准, _SYS]; classes {'alphabetic': 22, 'mixed': 6}

Strongest intercommunity connections:

- C1 to C2: 1764 token edges; mean cosine 0.134531
- C0 to C4: 1515 token edges; mean cosine 0.127258
- C0 to C1: 1494 token edges; mean cosine 0.128173
- C0 to C5: 1387 token edges; mean cosine 0.136256
- C0 to C2: 1335 token edges; mean cosine 0.130570
- C2 to C3: 1006 token edges; mean cosine 0.133802
- C0 to C3: 986 token edges; mean cosine 0.135326
- C1 to C3: 920 token edges; mean cosine 0.133620
- C1 to C4: 826 token edges; mean cosine 0.127048
- C1 to C6: 808 token edges; mean cosine 0.131013
- C4 to C6: 806 token edges; mean cosine 0.128443
- C3 to C5: 787 token edges; mean cosine 0.138867
- C2 to C6: 693 token edges; mean cosine 0.128462
- C1 to C8: 563 token edges; mean cosine 0.132267
- C5 to C6: 559 token edges; mean cosine 0.133196

#### negative_tail

- Nodes: 8809
- Directed 10-NN edges: 88090
- Undirected edges: 62113
- Communities: 13
- Modularity: 0.516579

All communities:

- C0 (n=2107): representatives [␠trucks, ␠Clubs, ␠doubling, -shot, Money, ␠tuning, ␠knives, ␠officers, ␠Officers, riding]; target-extreme [␠Ribbon, ␠pony, ␠riders, Retention, ␠Powers, _warnings]; classes {'alphabetic': 1749, 'mixed': 358}
- C1 (n=1655): representatives [␠zarówn, 辁, �, OptionsResolver, ␠undisclosed, ␠느, ␠patië, ␠RTBU, ᶅ, ␠overposting]; target-extreme [DidAppear, ␠buz, 鲠, 잴, 蟊, ␠glBegin]; classes {'alphabetic': 1352, 'mixed': 177, 'punctuation': 126}
- C2 (n=1190): representatives [el, era, ler, ra, ner, est, em, ter, ine, تها]; target-extreme [ardy, ewe, وا, jualan, ook, ten]; classes {'alphabetic': 1164, 'mixed': 15, 'punctuation': 11}
- C3 (n=872): representatives [␠unnecessary, ␠surely, ␠goof, 最好不要, ␠clear, ␠במיוחד, ␠BEST, ␠בהם, ␠should, ␠better]; target-extreme [均有, eneral, ␠Knot, Ready, ␠Nearly, .before]; classes {'alphabetic': 818, 'mixed': 52, 'punctuation': 2}
- C4 (n=800): representatives [␠EVEN, ␠DNC, ␠ENC, ␠CONT, ␠monot, ␠bi, ␠AF, NA, ␠overs, ␠JC]; target-extreme [常务, (reply, ␠Cran, ␠eyed, ␠Lanc, nex]; classes {'alphabetic': 644, 'mixed': 156}
- C5 (n=770): representatives [␠report, ␠reported, ␠penned, ␠release, ␠study, ␠softened, ␠openings, ␠noted, 檢查, Selected]; target-extreme [พบ, ␠indicates, OTAL, ␠tuned, ␠CARE, ␠STATE]; classes {'alphabetic': 690, 'mixed': 79, 'punctuation': 1}
- C6 (n=503): representatives [␠Phillips, ␠Vance, ␠Madrid, ␠Serbian, ␠Hamilton, ␠Brennan, ␠Macedonia, ␠WHITE, ␠neon, טלוו]; target-extreme [␠Kristen, ␠Crest, peng, ␠Bailey, ␠Platinum, ␠Elizabeth]; classes {'alphabetic': 486, 'mixed': 15, 'punctuation': 2}
- C7 (n=345): representatives ["f, ');");\n, ")\n, "));\n, ")))\n, !!,, )],, *, "], );\n]; target-extreme [******\n, ␠"::, ]+\, ]", _eof, "Some]; classes {'alphabetic': 16, 'mixed': 69, 'punctuation': 254, 'whitespace': 6}
- C8 (n=241): representatives [瑞, 边, 龙, 明, 华, 船, 达, 雷, 马, 迪]; target-extreme [边, 毅, 명, 범, 邑, 寧]; classes {'alphabetic': 226, 'mixed': 7, 'punctuation': 8}
- C9 (n=158): representatives [nine, -five, ␠Seven, ␠ноября, ␠HALF, ␠daily, five, -One, ␠Birthday, Five]; target-extreme [␠Tonight, -eight, 晚, ␠zeroes, ␠Latter, ␠Plenty]; classes {'alphabetic': 145, 'mixed': 12, 'numeric': 1}
- C10 (n=129): representatives [𝒊, น, ␠д, ด, eta, α, ␠F, ว, т, ա]; target-extreme [เจ, ␠epsilon, N, ᕑ, Assertion, ւ]; classes {'alphabetic': 114, 'mixed': 8, 'numeric': 2, 'punctuation': 5}
- C11 (n=30): representatives [-entry, \tentry, ␠cases, ␠entries, Entries, ␠instance, _entries, entry, ␠entered, entered]; target-extreme [␠cases, -entry, Entries, ␠entries, ␠ENTRY, ␠instance]; classes {'alphabetic': 23, 'mixed': 7}
- C12 (n=9): representatives [␠vídeo, ␠vídeos, ideos, ␠vidéo, ␠видео, ␠vidéos, _pedido, ␠vidé, ␠videot]; target-extreme [␠videot, ␠видео, ␠vidé, ␠vidéo, ␠vídeo, ␠vidéos]; classes {'alphabetic': 8, 'mixed': 1}

Strongest intercommunity connections:

- C0 to C1: 1768 token edges; mean cosine 0.130834
- C0 to C5: 1711 token edges; mean cosine 0.139475
- C0 to C2: 1405 token edges; mean cosine 0.136544
- C0 to C4: 1248 token edges; mean cosine 0.132216
- C1 to C3: 1120 token edges; mean cosine 0.133337
- C0 to C3: 1047 token edges; mean cosine 0.135284
- C0 to C6: 919 token edges; mean cosine 0.136186
- C2 to C4: 881 token edges; mean cosine 0.140652
- C1 to C4: 804 token edges; mean cosine 0.129211
- C3 to C5: 774 token edges; mean cosine 0.138164
- C1 to C2: 724 token edges; mean cosine 0.131552
- C1 to C5: 681 token edges; mean cosine 0.131012
- C2 to C3: 658 token edges; mean cosine 0.141031
- C2 to C5: 521 token edges; mean cosine 0.134697
- C2 to C6: 487 token edges; mean cosine 0.143471

### variation

Prompt: `What structure forms from electro pink, Tokyo nightlife, curvature density?`

#### positive_head

- Nodes: 8536
- Directed 10-NN edges: 85360
- Undirected edges: 59628
- Communities: 9
- Modularity: 0.498675

All communities:

- C0 (n=1645): representatives [␠psychological, هة, ␠psychiatric, クリニック, ␠opportunities, ␠économique, ␠comparing, ␠insecurity, 奢侈品, ␠vegetation]; target-extreme [␠geography, ␠passions, Phys, ␠liqu, تحضير, 统计数据]; classes {'alphabetic': 1495, 'mixed': 150}
- C1 (n=1521): representatives [씯, ארוחת, 住房公积, 컥, ␠@{@", 흣, 죳, ␠wyśw, 뿍, ᵤ]; target-extreme [뫼, شؤون, 얏, ǘ, 祖, ␠schl]; classes {'alphabetic': 1264, 'mixed': 25, 'punctuation': 232}
- C2 (n=1378): representatives [pushViewController, :@"%@",, \Seeder, SharedPointer, .DataGridViewColumnHeadersHeightSizeMode, GtkWidget, ␠authDomain, DataSetChanged, .fillStyle, toMatchSnapshot]; target-extreme [文章来源, .Configuration, _Get, <?>>, /apimachinery, _OBJECT]; classes {'alphabetic': 636, 'mixed': 729, 'punctuation': 13}
- C3 (n=1211): representatives [やっぱり, אנשים, ␠jakieś, そもそも, ␠오히려, มากมาย, ␠Çok, を変え, ␠그것을, まさに]; target-extreme [简称, 是由, 两句, ␠yıl, ␠każdym, ␠لل]; classes {'alphabetic': 1198, 'mixed': 9, 'punctuation': 4}
- C4 (n=957): representatives [␠하나님의, Hugh, ␠SEG, ␠Sag, ס, ическ, ␠그리스, iedo, ólogo, ks]; target-extreme [hum, íg, Ỷ, ym, Paris, ␠pó]; classes {'alphabetic': 876, 'mixed': 78, 'numeric': 1, 'punctuation': 2}
- C5 (n=600): representatives [␠экономическ, политическ, 房企, היסטוריה, ␠الحكومية, 选股, ␠челов, ␠الحكومة, ␠political, 化妆]; target-extreme [证券, 社会, 感情, 广场, 税务局, 穷]; classes {'alphabetic': 592, 'mixed': 8}
- C6 (n=519): representatives [␠text, ␠PostgreSQL, ␠sc, ␠Sec, ␠XML, ␠MySql, Text, ␠cp, ,v, ␠SQL]; target-extreme [gcc, .XML, ␠math, _h, xm, ␠jq]; classes {'alphabetic': 377, 'mixed': 140, 'punctuation': 2}
- C7 (n=357): representatives [))));\n, ?", ─, ...");\n\n, ');\r\n, $("#, .");\r\n, !", ())));\n, …”]; target-extreme [&_, ┅, =$("#, ␠}}"><, 。www, $("#]; classes {'alphabetic': 6, 'mixed': 40, 'punctuation': 296, 'whitespace': 15}
- C8 (n=348): representatives [個人資訊, ␠transform, ␠image, _information, ␠Create, ␠place, ␠word, ␠expression, 推崇, ␠transforming]; target-extreme [改革, LOAD, ␠transforming, ␠Comb, 管理办法, ␠Name]; classes {'alphabetic': 327, 'mixed': 21}

Strongest intercommunity connections:

- C0 to C2: 1628 token edges; mean cosine 0.125365
- C1 to C2: 1570 token edges; mean cosine 0.133138
- C1 to C3: 1500 token edges; mean cosine 0.137239
- C0 to C1: 1466 token edges; mean cosine 0.133137
- C0 to C4: 1325 token edges; mean cosine 0.129267
- C1 to C4: 1315 token edges; mean cosine 0.132183
- C0 to C5: 1301 token edges; mean cosine 0.136277
- C0 to C3: 1052 token edges; mean cosine 0.133226
- C3 to C4: 850 token edges; mean cosine 0.136012
- C2 to C6: 823 token edges; mean cosine 0.131335
- C0 to C8: 776 token edges; mean cosine 0.133081
- C1 to C5: 743 token edges; mean cosine 0.135743
- C3 to C5: 709 token edges; mean cosine 0.138666
- C4 to C6: 688 token edges; mean cosine 0.130718
- C2 to C4: 638 token edges; mean cosine 0.125842

#### negative_tail

- Nodes: 8382
- Directed 10-NN edges: 83820
- Undirected edges: 58950
- Communities: 11
- Modularity: 0.516217

All communities:

- C0 (n=1425): representatives [辁, ␠RTBU, ␠undisclosed, ᶅ, ␠느, 룁, ␠activeClassName, ␠overposting, ␠zobow, 梽]; target-extreme [DidAppear, ␠граф, 蟊, 鲠, ␠buz, ␠ConnectionState]; classes {'alphabetic': 1151, 'mixed': 174, 'punctuation': 100}
- C1 (n=1341): representatives [␠report, ␠doubling, ␠reported, ␠penned, ␠trailed, riding, -shot, coded, ␠clear, ␠study]; target-extreme [พบ, ␠indicates, Retention, ␠tuned, ␠entrepreneurship, ␠noted]; classes {'alphabetic': 1193, 'mixed': 148}
- C2 (n=1216): representatives [el, era, ler, ner, ra, em, est, ter, ac, ant]; target-extreme [ardy, وا, ewe, jualan, ook, ten]; classes {'alphabetic': 1194, 'mixed': 14, 'numeric': 1, 'punctuation': 7}
- C3 (n=1063): representatives [␠Vance, ␠Phillips, ␠Brennan, ␠Hamilton, ␠rulers, ␠Madrid, ␠Nelson, ␠republic, ␠Serbian, ␠Macedonia]; target-extreme [␠Kristen, ␠pony, ␠Leak, ␠Crest, peng, 常务]; classes {'alphabetic': 1022, 'mixed': 41}
- C4 (n=1003): representatives [␠trucks, ␠Clubs, ␠knives, ␠Officers, ␠Boards, ␠residents, ␠Activities, ␠team, ␠officers, ␠nipples]; target-extreme [␠Ribbon, ␠riders, ␠soldiers, Members, ␠Probe, _warnings]; classes {'alphabetic': 883, 'mixed': 120}
- C5 (n=678): representatives [␠unnecessary, ␠surely, ␠should, ␠BEST, 近些年, ␠After, ␠costly, ␠EVERY, ␠Highly, ␠current]; target-extreme [均有, OTAL, ␠Knot, OULD, ␠Nearly, ␠knots]; classes {'alphabetic': 627, 'mixed': 49, 'punctuation': 2}
- C6 (n=452): representatives [␠EE, ␠ENC, ␠endpoint, ␠CONT, AW, (endpoint, ␠AF, W, ␠cl, ␠д]; target-extreme [เจ, _ENDPOINT, (reply, IPC, ␠STATE, .dc]; classes {'alphabetic': 296, 'mixed': 156}
- C7 (n=389): representatives [!!,, "));\n, ")))\n, ),, ⩽, '], )],, "f, );\n, ")\n]; target-extreme []", >n, ******\n, ␠"::, ]+\, "C]; classes {'alphabetic': 48, 'mixed': 44, 'numeric': 1, 'punctuation': 288, 'whitespace': 8}
- C8 (n=378): representatives [瑞, 龙, 明, 边, 船, 点, ␠cattle, 华, 板, 达]; target-extreme [边, ␠cattle, 毅, 명, ␠vòng, 辫]; classes {'alphabetic': 350, 'mixed': 3, 'punctuation': 25}
- C9 (n=288): representatives [-round, ␠WHITE, ␠BLUE, -loop, ␠neon, ␠Bronze, ␠enamel, Length, Nodes, sweet]; target-extreme [␠Powers, ␠epsilon, Tweet, ␠mạnh, ␠Platinum, _tweets]; classes {'alphabetic': 191, 'mixed': 97}
- C10 (n=149): representatives [-wide, ␠Seven, -five, nine, Five, five, -One, ␠ноября, ␠lengthy, ␠November]; target-extreme [-positive, ␠CARE, 相关部门, ␠Tonight, 晚, -eight]; classes {'alphabetic': 124, 'mixed': 24, 'numeric': 1}

Strongest intercommunity connections:

- C1 to C4: 1630 token edges; mean cosine 0.135402
- C3 to C4: 1288 token edges; mean cosine 0.136661
- C0 to C1: 1110 token edges; mean cosine 0.130062
- C2 to C3: 1030 token edges; mean cosine 0.141786
- C1 to C5: 948 token edges; mean cosine 0.140608
- C1 to C2: 874 token edges; mean cosine 0.136526
- C1 to C3: 870 token edges; mean cosine 0.135573
- C0 to C3: 844 token edges; mean cosine 0.131394
- C0 to C4: 821 token edges; mean cosine 0.128675
- C2 to C4: 760 token edges; mean cosine 0.136707
- C0 to C5: 736 token edges; mean cosine 0.133472
- C0 to C2: 640 token edges; mean cosine 0.129286
- C2 to C5: 586 token edges; mean cosine 0.141128
- C2 to C6: 578 token edges; mean cosine 0.146530
- C0 to C8: 534 token edges; mean cosine 0.130770
