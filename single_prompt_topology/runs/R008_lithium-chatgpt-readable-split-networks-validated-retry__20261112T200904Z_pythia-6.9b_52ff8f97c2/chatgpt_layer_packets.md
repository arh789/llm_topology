# R008 ChatGPT layer packets

These packets summarize all 66 split community networks. The JSON and CSV artifacts contain the complete compact and token-level evidence.

Interpretation boundary: positive_head means high target-relative cosine alignment and negative_tail means geometric anti-alignment. Community partitions are not established topics. Negative membership does not by itself establish suppression, contradiction or exclusion.

## State 0: input_embedding

### positive_head

- Nodes: 1871
- Directed 10-NN edges: 18710
- Undirected edges: 13172
- Mean 10-NN cosine: 0.151103
- Communities: 12
- Modularity: 0.589040

Largest communities:

- C0 (n=361): representatives [␠antidepress, ␠glutathione, ␠schizophrenia, ␠hepatocellular, ␠glucose, aphylococcus, ␠tuberculosis, ␠doxorubicin]; target-extreme [␠bipolar, ␠metformin, ␠glutathione, ␠antidepress, ␠schizophrenia]; token classes {'continuation_or_standalone': 114, 'punctuation_or_symbol': 1, 'word_initial': 246}
- C1 (n=262): representatives [␠Iran, ␠Li, Li, ␠Liu, ␠Kuwait, ␠Malaysia, ␠Roberto, ␠Massachusetts]; target-extreme [␠Li, Li, ␠Lith, ␠lith, ␠li]; token classes {'continuation_or_standalone': 57, 'punctuation_or_symbol': 1, 'target_lexical_variant': 7, 'word_initial': 197}
- C2 (n=230): representatives [␠hospitalization, ␠Temperature, ␠thermally, ␠temperature, ␠cooling, temperature, ␠inorganic, ␠groundwater]; target-extreme [␠recharge, ␠Liquid, hydration, liquid, ␠molten]; token classes {'continuation_or_standalone': 25, 'word_initial': 205}
- C3 (n=206): representatives [␠electrochemical, ␠piezoelectric, ␠electromagnetic, ␠magnetization, ␠superconduct, ␠electrically, ␠conductivity, ␠capacitance]; target-extreme [␠electrolyte, ␠batteries, ␠battery, ␠Battery, ␠electroly]; token classes {'continuation_or_standalone': 38, 'word_initial': 168}
- C4 (n=182): representatives [␠cryptocurrencies, ␠telecommunications, ␠Samsung, ␠Bluetooth, ␠laptops, Apple, ␠cryptocurrency, ␠Apple]; target-extreme [␠LTE, ␠Tesla, ␠Wi, ␠solar, ␠Nissan]; token classes {'continuation_or_standalone': 44, 'word_initial': 138}
- C5 (n=142): representatives [778, 740, 732, 735, 528, ␠535, 532, 538]; target-extreme [636, 528, 368, ␠384, ␠540]; token classes {'continuation_or_standalone': 80, 'word_initial': 62}
- C6 (n=139): representatives [␠Zn, ␠Ti, Mg, ␠Cu, ␠Cd, ␠millig, ␠Mi, ␠Hg]; target-extreme [␠Mg, ␠Cd, Mg, Rb, ␠tau]; token classes {'continuation_or_standalone': 30, 'punctuation_or_symbol': 1, 'target_lexical_variant': 2, 'word_initial': 106}
- C7 (n=127): representatives [␠phosphorus, ␠chlor, ␠ethanol, ␠methyl, ␠hydrogen, ␠hydrochlor, ␠phosphate, ␠fluor]; target-extreme [␠helium, ␠hydrox, ␠alkali, ␠hydrogen, ␠carbon]; token classes {'continuation_or_standalone': 38, 'word_initial': 89}

Strongest intercommunity connections:

- C2 to C3: 306 token edges; mean cosine 0.112243
- C0 to C2: 230 token edges; mean cosine 0.102687
- C3 to C4: 181 token edges; mean cosine 0.102113
- C0 to C1: 163 token edges; mean cosine 0.089926
- C2 to C4: 150 token edges; mean cosine 0.107198
- C0 to C4: 146 token edges; mean cosine 0.099554
- C0 to C3: 140 token edges; mean cosine 0.100426
- C0 to C7: 139 token edges; mean cosine 0.120800
- C1 to C6: 131 token edges; mean cosine 0.094352
- C1 to C4: 130 token edges; mean cosine 0.092359

### negative_tail

- Nodes: 1316
- Directed 10-NN edges: 13160
- Undirected edges: 8663
- Mean 10-NN cosine: 0.104853
- Communities: 10
- Modularity: 0.468613

Largest communities:

- C0 (n=307): representatives [Sp, pl, ␠Ted, ␠Fred, ␠cott, Ron, Rick, Sav]; target-extreme [␠Gent, Ø, Dev, PASS, ␠Wesley]; token classes {'continuation_or_standalone': 163, 'punctuation_or_symbol': 12, 'whitespace': 1, 'word_initial': 131}
- C1 (n=222): representatives [Session, writer, Reader, Dialog, reader, ␠writer, ographer, Context]; target-extreme [Menu, ␠conn, Wrapper, Args, ducer]; token classes {'continuation_or_standalone': 170, 'punctuation_or_symbol': 3, 'word_initial': 49}
- C2 (n=172): representatives [␠ignorant, ␠serm, ␠inqu, ␠fascinating, ␠intric, akespeare, ␠comprehend, ␠acquainted]; target-extreme [␠fart, ␠savage, ␠inqu, ␠circus, ␠acquainted]; token classes {'continuation_or_standalone': 28, 'whitespace': 1, 'word_initial': 143}
- C3 (n=138): representatives [ifying, ␠negotiated, ␠depicting, ␠surrendered, ␠altered, cerning, ␠depicted, ␠finishing]; target-extreme [␠altered, reve, ␠contest, Moreover, ␠specified]; token classes {'continuation_or_standalone': 51, 'word_initial': 87}
- C4 (n=116): representatives [ce, achers, pe, der, ars, ters, lers, ␠gentleman]; target-extreme [asant, eer, deed, pts, idd]; token classes {'continuation_or_standalone': 101, 'whitespace': 1, 'word_initial': 14}
- C5 (n=115): representatives [␠birds, ␠horses, ␠Dog, birds, Dog, ␠horse, ␠Veter, ␠ducks]; target-extreme [␠Archer, ␠cozy, ␠horses, deck, ␠bred]; token classes {'continuation_or_standalone': 40, 'word_initial': 75}
- C6 (n=77): representatives [ent, ␠␠, ], ␠an, “, our, )}_{\, }}}_{\]; target-extreme [––––, ------------, ��, ]{\, }}-\]; token classes {'continuation_or_standalone': 8, 'punctuation_or_symbol': 58, 'whitespace': 3, 'word_initial': 8}
- C7 (n=74): representatives [␠Officers, ␠Capt, ␠Sgt, ␠Sergeant, ␠detective, ␠Patrol, ␠cops, pector]; target-extreme [Capt, ␠Sgt, geons, ␠Capt, geant]; token classes {'continuation_or_standalone': 27, 'word_initial': 47}

Strongest intercommunity connections:

- C0 to C1: 332 token edges; mean cosine 0.082265
- C2 to C3: 227 token edges; mean cosine 0.085802
- C0 to C2: 212 token edges; mean cosine 0.077524
- C0 to C4: 205 token edges; mean cosine 0.079298
- C0 to C5: 166 token edges; mean cosine 0.082448
- C1 to C2: 164 token edges; mean cosine 0.083509
- C1 to C3: 146 token edges; mean cosine 0.079487
- C0 to C7: 136 token edges; mean cosine 0.080326
- C2 to C5: 135 token edges; mean cosine 0.085109
- C2 to C4: 109 token edges; mean cosine 0.081800

### Secondary cross-side relations from R005

- rules (positive_head) to Rules (negative_tail): cosine 0.324598, combined-neighbour rank 1
- Rules (negative_tail) to rules (positive_head): cosine 0.324598, combined-neighbour rank 1
- 097 (negative_tail) to 088 (positive_head): cosine 0.256032, combined-neighbour rank 3
- 088 (positive_head) to 097 (negative_tail): cosine 0.256032, combined-neighbour rank 1
- 088 (positive_head) to 099 (negative_tail): cosine 0.255224, combined-neighbour rank 2
- 099 (negative_tail) to 088 (positive_head): cosine 0.255224, combined-neighbour rank 3
- ␠171 (positive_head) to ␠191 (negative_tail): cosine 0.245486, combined-neighbour rank 2
- ␠191 (negative_tail) to ␠171 (positive_head): cosine 0.245486, combined-neighbour rank 1
- 098 (negative_tail) to 088 (positive_head): cosine 0.229413, combined-neighbour rank 3
- 088 (positive_head) to 098 (negative_tail): cosine 0.229413, combined-neighbour rank 3

## State 1: block_00_output

### positive_head

- Nodes: 3125
- Directed 10-NN edges: 31250
- Undirected edges: 21396
- Mean 10-NN cosine: 0.119799
- Communities: 12
- Modularity: 0.538869

Largest communities:

- C0 (n=402): representatives [), i, ␠was, ␠is, en, ␠have, ␠all, ␠more]; target-extreme [), seeking, ␠IS, eting, ␠Round]; token classes {'continuation_or_standalone': 218, 'punctuation_or_symbol': 5, 'whitespace': 3, 'word_initial': 176}
- C1 (n=380): representatives [␠electronically, ␠mysql, ␠MySQL, ␠formatted, ␠renormalization, ␠sqlite, ␠SQL, ␠Database]; target-extreme [Form, ␠Hash, ␠electronically, ␠surfaces, Absolute]; token classes {'continuation_or_standalone': 205, 'word_initial': 175}
- C2 (n=370): representatives [Anna, ␠Katherine, ไ, ␠Sandy, ␠Michelle, ös, ␠Barnes, ␠Curtis]; target-extreme [idis, �, ellen, ös, entre]; token classes {'continuation_or_standalone': 214, 'punctuation_or_symbol': 27, 'whitespace': 2, 'word_initial': 127}
- C3 (n=280): representatives [}}}), })}, ])), }}}, )))), }}, })), ))).]; target-extreme [␠PARTICULAR, ␠==, )))), >), ␠KIND]; token classes {'continuation_or_standalone': 44, 'punctuation_or_symbol': 205, 'whitespace': 7, 'word_initial': 24}
- C4 (n=279): representatives [␠maintaining, ␠reviewing, ␠positioning, ␠highlighted, ␠ignoring, ␠establishes, ␠recognizing, documented]; target-extreme [␠accessing, ␠solved, Modified, serve, ␠remembers]; token classes {'continuation_or_standalone': 74, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 203}
- C5 (n=272): representatives [␠IGF, SS, PC, ␠CP, ␠IP, ␠gap, ␠CS, Bo]; target-extreme [CSI, ␠FIN, ␠BCG, ␠NAS, Spin]; token classes {'continuation_or_standalone': 135, 'target_lexical_variant': 1, 'whitespace': 4, 'word_initial': 132}
- C6 (n=252): representatives [␠Nigerian, ␠Indonesian, ␠Pakistani, ␠psychological, ␠psychosocial, ␠politically, ␠administrative, ␠Chinese]; target-extreme [␠administrative, ␠Civil, ␠Appellate, African, ␠Indonesian]; token classes {'continuation_or_standalone': 78, 'whitespace': 3, 'word_initial': 171}
- C7 (n=251): representatives [␠extraordinarily, interesting, ␠satisfactory, ␠unsatisfactory, ␠interesting, Eventually, ␠professionally, probably]; target-extreme [␠refreshing, ␠mycket, ␠permanent, ␠cheaper, ␠miser]; token classes {'continuation_or_standalone': 87, 'word_initial': 164}

Strongest intercommunity connections:

- C0 to C4: 446 token edges; mean cosine 0.099051
- C0 to C2: 340 token edges; mean cosine 0.085055
- C1 to C4: 300 token edges; mean cosine 0.095511
- C4 to C7: 277 token edges; mean cosine 0.098731
- C2 to C5: 261 token edges; mean cosine 0.083846
- C0 to C7: 253 token edges; mean cosine 0.110234
- C1 to C5: 244 token edges; mean cosine 0.088915
- C0 to C1: 240 token edges; mean cosine 0.097473
- C0 to C5: 232 token edges; mean cosine 0.087860
- C2 to C6: 229 token edges; mean cosine 0.089220

### negative_tail

- Nodes: 2793
- Directed 10-NN edges: 27930
- Undirected edges: 18955
- Mean 10-NN cosine: 0.116566
- Communities: 13
- Modularity: 0.505917

Largest communities:

- C0 (n=401): representatives [␠Gab, ␠Murphy, ␠Hab, ␠Qu, ␠Fel, ␠Thompson, ␠Ab, ␠Ke]; target-extreme [stead, ␠Max, ␠Romania, ␠percent, ␠Ab]; token classes {'continuation_or_standalone': 134, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 264}
- C1 (n=358): representatives [␠pathophysiology, ␠zebrafish, ␠unconstitutional, ␠epidemiology, ␠methodologies, ␠technologies, ␠phenotypes, ␠thermoplastic]; target-extreme [demonstr, tox, ␠biomarkers, opath, ␠alk]; token classes {'continuation_or_standalone': 119, 'target_lexical_variant': 1, 'word_initial': 238}
- C2 (n=272): representatives [␠enthus, ␠comp, ␠imposs, ␠ingred, ␠unequiv, ␠clums, ␠incomp, ␠Com]; target-extreme [␠comp, ␠trop, Ver, ␠env, ␠parad]; token classes {'continuation_or_standalone': 87, 'punctuation_or_symbol': 15, 'target_lexical_variant': 2, 'whitespace': 5, 'word_initial': 163}
- C3 (n=268): representatives [␠transformed, ␠transformation, ␠Inhibition, ␠transformations, inguishable, ancement, ␠increase, ␠enhancement]; target-extreme [␠bolster, orphism, ␠Beginning, ␠begin, ␠neb]; token classes {'continuation_or_standalone': 70, 'whitespace': 2, 'word_initial': 196}
- C4 (n=268): representatives [determination, ␠interpretation, ␠prohibited, ␠instructed, ␠explanations, ␠recommendations, ␠prohibition, ␠expectations]; target-extreme [␠visions, ␠Laws, ␠humor, ␠beliefs, ␠authority]; token classes {'continuation_or_standalone': 72, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 193}
- C5 (n=257): representatives [␠hallway, ␠staircase, ␠jacket, ␠technician, boats, ␠guns, ␠stairs, ␠floors]; target-extreme [␠colors, ␠clad, ␠contractor, ␠shots, ␠barrel]; token classes {'continuation_or_standalone': 51, 'whitespace': 1, 'word_initial': 205}
- C6 (n=236): representatives [␠Archbishop, ␠monsters, ␠producer, ␠demons, Professor, ␠Rabbi, ␠Governor, ␠demon]; target-extreme [␠Chair, ␠Rabbi, ␠composer, ␠musical, ␠Creator]; token classes {'continuation_or_standalone': 46, 'word_initial': 190}
- C7 (n=229): representatives [o, ␠if, ␠$, ized, B, man, ian, ␠level]; target-extreme [␠$, ␠whether, ’, RA, ORD]; token classes {'continuation_or_standalone': 158, 'punctuation_or_symbol': 5, 'whitespace': 2, 'word_initial': 64}

Strongest intercommunity connections:

- C0 to C2: 419 token edges; mean cosine 0.084509
- C3 to C4: 347 token edges; mean cosine 0.100179
- C1 to C3: 330 token edges; mean cosine 0.100069
- C0 to C6: 277 token edges; mean cosine 0.095216
- C1 to C4: 252 token edges; mean cosine 0.101055
- C1 to C5: 240 token edges; mean cosine 0.093350
- C1 to C2: 237 token edges; mean cosine 0.086767
- C5 to C6: 235 token edges; mean cosine 0.098053
- C4 to C8: 231 token edges; mean cosine 0.099970
- C0 to C1: 231 token edges; mean cosine 0.085348

### Secondary cross-side relations from R005

- ␠Egypt (negative_tail) to ␠Egyptian (positive_head): cosine 0.503496, combined-neighbour rank 1
- ␠Egyptian (positive_head) to ␠Egypt (negative_tail): cosine 0.503496, combined-neighbour rank 1
- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ␠argues (negative_tail) to ␠contends (positive_head): cosine 0.422392, combined-neighbour rank 2
- ␠contends (positive_head) to ␠argues (negative_tail): cosine 0.422392, combined-neighbour rank 1
- vironments (positive_head) to ␠environments (negative_tail): cosine 0.414715, combined-neighbour rank 1
- ␠environments (negative_tail) to vironments (positive_head): cosine 0.414715, combined-neighbour rank 1
- ␠shining (positive_head) to ␠shine (negative_tail): cosine 0.390668, combined-neighbour rank 1
- ␠shine (negative_tail) to ␠shining (positive_head): cosine 0.390668, combined-neighbour rank 1

## State 2: block_01_output

### positive_head

- Nodes: 3063
- Directed 10-NN edges: 30630
- Undirected edges: 20957
- Mean 10-NN cosine: 0.120455
- Communities: 14
- Modularity: 0.545877

Largest communities:

- C0 (n=390): representatives [interesting, ␠development, ␠activates, ␠enjoyable, ␠initiating, ␠established, ␠satisfactory, ␠travelling]; target-extreme [␠refreshing, ␠solved, ␠permanent, Modified, Absolute]; token classes {'continuation_or_standalone': 102, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 286}
- C1 (n=383): representatives [␠angiotensin, ␠conformational, ␠psychological, ediatric, ␠adolescents, ␠glucocortic, ␠hypothal, ␠pituitary]; target-extreme [␠BCG, lion, ortex, ␠FIN, oric]; token classes {'continuation_or_standalone': 155, 'word_initial': 228}
- C2 (n=382): representatives [), ␠is, en, ␠was, ␠have, ␠more, ␠work, et]; target-extreme [), seeking, ␠remembers, tar, eting]; token classes {'continuation_or_standalone': 199, 'punctuation_or_symbol': 5, 'target_lexical_variant': 2, 'whitespace': 4, 'word_initial': 172}
- C3 (n=379): representatives [␠mysql, ␠DB, ␠MySQL, ␠CS, ␠SQL, ␠Database, ␠TS, ␠sqlite]; target-extreme [␠NAS, ␠CSS, SQL, CS, ␠ACP]; token classes {'continuation_or_standalone': 187, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 189}
- C4 (n=280): representatives [␠Nigerian, ␠Indonesian, California, ␠Ethiop, ␠Sacramento, ifornia, ␠Chinese, ␠Canadian]; target-extreme [African, ␠Indonesian, ayan, ␠Thai, ncia]; token classes {'continuation_or_standalone': 138, 'whitespace': 1, 'word_initial': 141}
- C5 (n=254): representatives [}}}), ])), )))), ")), *),, )));, ]));, }}}]; target-extreme [␠PARTICULAR, )))), ␠==, 00000000000000000000000000000000, ?.]; token classes {'continuation_or_standalone': 33, 'punctuation_or_symbol': 186, 'whitespace': 12, 'word_initial': 23}
- C6 (n=208): representatives [␠psychosocial, ␠politically, ␠political, Political, ␠bureaucracy, ␠administrative, ␠athletes, ␠democratic]; target-extreme [␠administrative, ercise, ␠Civil, ␠resort, ␠Appellate]; token classes {'continuation_or_standalone': 73, 'word_initial': 135}
- C7 (n=206): representatives [␠electronically, ␠Subsequently, Eventually, ␠professionally, ␠emotional, Therefore, ␠emotionally, ␠subsequent]; target-extreme [␠Active, ␠intermittent, ␠electronically, Further, ␠ideally]; token classes {'continuation_or_standalone': 82, 'word_initial': 124}

Strongest intercommunity connections:

- C0 to C2: 424 token edges; mean cosine 0.103788
- C1 to C3: 351 token edges; mean cosine 0.091114
- C0 to C7: 336 token edges; mean cosine 0.105770
- C0 to C1: 297 token edges; mean cosine 0.093769
- C2 to C3: 254 token edges; mean cosine 0.088761
- C0 to C6: 251 token edges; mean cosine 0.102818
- C3 to C4: 243 token edges; mean cosine 0.087472
- C1 to C4: 236 token edges; mean cosine 0.087323
- C1 to C6: 223 token edges; mean cosine 0.093145
- C2 to C7: 221 token edges; mean cosine 0.104663

### negative_tail

- Nodes: 2816
- Directed 10-NN edges: 28160
- Undirected edges: 19176
- Mean 10-NN cosine: 0.115306
- Communities: 13
- Modularity: 0.512463

Largest communities:

- C0 (n=426): representatives [␠Gab, ␠Luke, ␠Nick, ␠Hicks, ␠Jeff, ␠Murphy, ␠Lucas, Jeff]; target-extreme [␠Max, ␠Rabbi, stead, ␠Romania, ␠alk]; token classes {'continuation_or_standalone': 145, 'whitespace': 1, 'word_initial': 280}
- C1 (n=379): representatives [determination, ␠prohibiting, ␠interpretation, ␠prohibited, ␠visualization, inguishable, ␠transformation, ␠unconstitutional]; target-extreme [␠Beginning, demonstr, ␠Laws, ␠visions, ␠approved]; token classes {'continuation_or_standalone': 103, 'whitespace': 3, 'word_initial': 273}
- C2 (n=292): representatives [o, ␠if, ia, ␠$, ␠␠␠, ized, man, ED]; target-extreme [␠colors, ␠$, gate, ORD, ␠unit]; token classes {'continuation_or_standalone': 184, 'punctuation_or_symbol': 6, 'whitespace': 5, 'word_initial': 97}
- C3 (n=275): representatives [␠murdered, ␠massacre, ␠murders, ␠thief, ␠murder, ␠killings, ␠killing, ␠tragedy]; target-extreme [␠trop, ␠trump, ␠audible, ␠news, ␠thief]; token classes {'continuation_or_standalone': 54, 'whitespace': 1, 'word_initial': 220}
- C4 (n=232): representatives [␠hallway, ␠staircase, ␠guns, ␠sidewalk, ␠Transportation, ␠jacket, ␠gown, ␠rifles]; target-extreme [␠wireless, ␠shots, ␠snow, ␠clad, afers]; token classes {'continuation_or_standalone': 28, 'whitespace': 1, 'word_initial': 203}
- C5 (n=218): representatives [␠producer, ␠physician, ␠goddess, ␠technician, ␠Archbishop, ␠Duchess, ␠technicians, ␠monsters]; target-extreme [␠Chair, ␠Devil, ␠contractor, ␠Batman, ␠Productions]; token classes {'continuation_or_standalone': 41, 'whitespace': 1, 'word_initial': 176}
- C6 (n=179): representatives [␠inhibition, ␠Experiments, ␠Inhibition, omorphisms, ␠enhancement, ␠stabilization, ␠initialization, ␠detectors]; target-extreme [orphism, ␠bolster, reducible, ␠neb, bounded]; token classes {'continuation_or_standalone': 68, 'whitespace': 1, 'word_initial': 110}
- C7 (n=169): representatives [␠imposs, ␠abrog, ␠incomp, ␠abol, ␠insign, ␠incred, ␠ingred, ␠incapable]; target-extreme [␠comp, drv, ␠dilig, ␠uint, ␠abol]; token classes {'continuation_or_standalone': 39, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 127}

Strongest intercommunity connections:

- C1 to C3: 463 token edges; mean cosine 0.100959
- C1 to C2: 331 token edges; mean cosine 0.098441
- C1 to C6: 275 token edges; mean cosine 0.095949
- C0 to C5: 268 token edges; mean cosine 0.095458
- C0 to C2: 256 token edges; mean cosine 0.082850
- C0 to C8: 250 token edges; mean cosine 0.083216
- C0 to C7: 207 token edges; mean cosine 0.088167
- C1 to C7: 202 token edges; mean cosine 0.093692
- C3 to C5: 194 token edges; mean cosine 0.098393
- C0 to C4: 190 token edges; mean cosine 0.088942

### Secondary cross-side relations from R005

- ␠Egypt (negative_tail) to ␠Egyptian (positive_head): cosine 0.503496, combined-neighbour rank 1
- ␠Egyptian (positive_head) to ␠Egypt (negative_tail): cosine 0.503496, combined-neighbour rank 1
- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ␠argues (negative_tail) to ␠contends (positive_head): cosine 0.422392, combined-neighbour rank 2
- ␠contends (positive_head) to ␠argues (negative_tail): cosine 0.422392, combined-neighbour rank 1
- vironments (positive_head) to ␠environments (negative_tail): cosine 0.414715, combined-neighbour rank 1
- ␠environments (negative_tail) to vironments (positive_head): cosine 0.414715, combined-neighbour rank 1
- ␠eru (positive_head) to ␠eruption (negative_tail): cosine 0.402027, combined-neighbour rank 1
- ␠eruption (negative_tail) to ␠eru (positive_head): cosine 0.402027, combined-neighbour rank 1

## State 3: block_02_output

### positive_head

- Nodes: 3167
- Directed 10-NN edges: 31670
- Undirected edges: 21640
- Mean 10-NN cosine: 0.121890
- Communities: 11
- Modularity: 0.549390

Largest communities:

- C0 (n=510): representatives [), en, ␠of, ate, ␠is, ␠was, ␠have, ␠more]; target-extreme [), ppen, ␠LOS, idis, eting]; token classes {'continuation_or_standalone': 313, 'punctuation_or_symbol': 10, 'target_lexical_variant': 4, 'whitespace': 3, 'word_initial': 180}
- C1 (n=480): representatives [␠immunosuppressive, ␠angiotensin, ␠conformational, ediatric, ␠IGF, ␠glucocortic, ␠testicular, ␠Phosph]; target-extreme [Spin, ensch, �, oric, ␠fo]; token classes {'continuation_or_standalone': 186, 'punctuation_or_symbol': 27, 'whitespace': 1, 'word_initial': 266}
- C2 (n=399): representatives [␠accessing, ␠giving, ␠forgotten, ␠travelling, ␠formatted, ␠ascertained, ␠retrieving, ␠response]; target-extreme [seeking, counter, ␠solved, ␠remembers, recognized]; token classes {'continuation_or_standalone': 114, 'whitespace': 1, 'word_initial': 284}
- C3 (n=319): representatives [␠psychosocial, ␠extraordinarily, ␠electronically, Eventually, ␠emotional, ␠Subsequently, ␠qualitatively, Therefore]; target-extreme [␠refreshing, ␠Active, ␠mycket, ␠electronically, ␠permanent]; token classes {'continuation_or_standalone': 115, 'whitespace': 1, 'word_initial': 203}
- C4 (n=318): representatives [␠Indonesian, ␠Nigerian, ␠Finnish, Financial, ␠Charleston, Political, ␠Australian, ␠administrative]; target-extreme [␠administrative, ayan, ␠Civil, ␠Indonesian, ␠FIN]; token classes {'continuation_or_standalone': 131, 'word_initial': 187}
- C5 (n=278): representatives [PC, ␠TS, ␠txt, SC, Tra, Bo, ␠DB, ␠MM]; target-extreme [␠NAS, CS, PC, ␠ds, BM]; token classes {'continuation_or_standalone': 143, 'target_lexical_variant': 2, 'whitespace': 3, 'word_initial': 130}
- C6 (n=267): representatives [␠sites, ␠mysql, ␠forms, ␠transactions, ␠SQL, CONNE, Group, SQL]; target-extreme [Form, ␠PARTICULAR, ␠Role, ␠formul, ␠CSS]; token classes {'continuation_or_standalone': 125, 'word_initial': 142}
- C7 (n=225): representatives [}}), ])), ")), )));, )))), ]));, )))., '))]; target-extreme [)))), ␠===, 00000000000000000000000000000000, ?., ␠==]; token classes {'continuation_or_standalone': 19, 'punctuation_or_symbol': 182, 'whitespace': 16, 'word_initial': 8}

Strongest intercommunity connections:

- C0 to C2: 453 token edges; mean cosine 0.110019
- C2 to C3: 441 token edges; mean cosine 0.094617
- C0 to C1: 410 token edges; mean cosine 0.084916
- C1 to C3: 388 token edges; mean cosine 0.094973
- C1 to C2: 362 token edges; mean cosine 0.096716
- C1 to C4: 344 token edges; mean cosine 0.086830
- C0 to C5: 335 token edges; mean cosine 0.090101
- C1 to C5: 305 token edges; mean cosine 0.094290
- C0 to C6: 302 token edges; mean cosine 0.091843
- C2 to C6: 288 token edges; mean cosine 0.096551

### negative_tail

- Nodes: 2809
- Directed 10-NN edges: 28090
- Undirected edges: 19121
- Mean 10-NN cosine: 0.116237
- Communities: 15
- Modularity: 0.517040

Largest communities:

- C0 (n=355): representatives [␠theolog, ␠Nick, ␠Alex, ␠Jeff, ␠Alan, ␠Dest, Josh, ␠Dav]; target-extreme [␠Rabbi, ␠Max, ␠alk, stead, ␠Turk]; token classes {'continuation_or_standalone': 113, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 239}
- C1 (n=335): representatives [␠unconstitutional, ␠discour, ␠unacceptable, ␠indistinguishable, ␠catast, ␠tragedy, ␠disproportion, demonstr]; target-extreme [␠comp, ␠dilig, ␠audible, ␠trop, ␠conclusive]; token classes {'continuation_or_standalone': 66, 'punctuation_or_symbol': 3, 'target_lexical_variant': 3, 'word_initial': 263}
- C2 (n=322): representatives [determination, ␠visualization, ␠epidemiology, ␠interpretation, ␠descriptions, ␠phenotypes, ␠stabilization, ␠technologies]; target-extreme [␠slated, ␠visions, ␠displacement, onder, ␠compliment]; token classes {'continuation_or_standalone': 72, 'whitespace': 2, 'word_initial': 248}
- C3 (n=259): representatives [␠technician, ␠Archbishop, ␠professor, ␠Chairman, ␠goddess, ␠Congressman, ␠officer, ␠warriors]; target-extreme [␠Chair, ␠Devil, ␠contractor, ␠news, akers]; token classes {'continuation_or_standalone': 53, 'word_initial': 206}
- C4 (n=256): representatives [␠hallway, ␠staircase, ␠guns, ␠smartphones, ␠sidewalk, ␠outfits, ␠Transportation, ␠sculptures]; target-extreme [␠colors, ␠trump, ␠wireless, ␠shots, afers]; token classes {'continuation_or_standalone': 52, 'whitespace': 1, 'word_initial': 203}
- C5 (n=233): representatives [ia, ␠$, ized, ␠␠␠, als, ␠how, ␠take, ED]; target-extreme [␠$, ␠que, ’, ␠unit, ORD]; token classes {'continuation_or_standalone': 144, 'punctuation_or_symbol': 7, 'whitespace': 7, 'word_initial': 75}
- C6 (n=182): representatives [␠echocardiography, ␠pathophysiology, ␠anesthesia, ␠pathogens, ␠medications, ␠therapies, ␠skull, oscopy]; target-extreme [␠biomarkers, unks, ␠allele, terminus, neck]; token classes {'continuation_or_standalone': 61, 'target_lexical_variant': 1, 'word_initial': 120}
- C7 (n=152): representatives [公, �, ␠vé, amente, �, emente, ␠د, ␠vý]; target-extreme [␠raz, ␠î, ić, ␠modo, ␠sig]; token classes {'continuation_or_standalone': 77, 'punctuation_or_symbol': 15, 'word_initial': 60}

Strongest intercommunity connections:

- C1 to C2: 377 token edges; mean cosine 0.101831
- C0 to C1: 267 token edges; mean cosine 0.086246
- C3 to C4: 263 token edges; mean cosine 0.101792
- C1 to C8: 249 token edges; mean cosine 0.098791
- C0 to C3: 243 token edges; mean cosine 0.099718
- C2 to C4: 220 token edges; mean cosine 0.094664
- C0 to C7: 211 token edges; mean cosine 0.080042
- C2 to C5: 201 token edges; mean cosine 0.096146
- C2 to C6: 186 token edges; mean cosine 0.102396
- C2 to C8: 185 token edges; mean cosine 0.098680

### Secondary cross-side relations from R005

- ␠Egypt (negative_tail) to ␠Egyptian (positive_head): cosine 0.503496, combined-neighbour rank 1
- ␠Egyptian (positive_head) to ␠Egypt (negative_tail): cosine 0.503496, combined-neighbour rank 1
- ␠traveled (negative_tail) to ␠travelled (positive_head): cosine 0.485664, combined-neighbour rank 1
- ␠travelled (positive_head) to ␠traveled (negative_tail): cosine 0.485664, combined-neighbour rank 1
- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ␠argues (negative_tail) to ␠contends (positive_head): cosine 0.422392, combined-neighbour rank 2
- ␠contends (positive_head) to ␠argues (negative_tail): cosine 0.422392, combined-neighbour rank 1
- ␠affirm (negative_tail) to ␠affirmed (positive_head): cosine 0.396894, combined-neighbour rank 1
- ␠affirmed (positive_head) to ␠affirm (negative_tail): cosine 0.396894, combined-neighbour rank 1

## State 4: block_03_output

### positive_head

- Nodes: 3054
- Directed 10-NN edges: 30540
- Undirected edges: 20730
- Mean 10-NN cosine: 0.119301
- Communities: 12
- Modularity: 0.537150

Largest communities:

- C0 (n=404): representatives [␠initiating, ␠participating, ␠retrieving, ␠extracted, ␠travelling, ␠recognizing, ␠formatted, ␠determining]; target-extreme [Form, seeking, ␠solved, ␠formul, ␠Forms]; token classes {'continuation_or_standalone': 129, 'whitespace': 1, 'word_initial': 274}
- C1 (n=373): representatives [), ␠of, ate, en, ␠was, ␠is, ␠have, et]; target-extreme [), ppen, eting, tar, �]; token classes {'continuation_or_standalone': 263, 'punctuation_or_symbol': 8, 'target_lexical_variant': 2, 'whitespace': 7, 'word_initial': 93}
- C2 (n=372): representatives [␠immunosuppressive, ␠glucocortic, ␠Phosph, ␠infertility, ␠rice, ␠evolutionary, ediatric, ␠communities]; target-extreme [␠rice, carbon, ␠polys, lion, idis]; token classes {'continuation_or_standalone': 146, 'word_initial': 226}
- C3 (n=330): representatives [Bo, ไ, ␠Ext, �, ␠De, ␠Rel, La, akespe]; target-extreme [␠Gest, ␠fo, �, ensch, �]; token classes {'continuation_or_standalone': 122, 'punctuation_or_symbol': 27, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 178}
- C4 (n=264): representatives [␠Nigerian, ␠Charlotte, ␠Indonesian, ␠Orlando, ␠Sandy, ␠Sacramento, ␠Charleston, ␠Egyptian]; target-extreme [bara, entre, lando, ␠Thai, ayan]; token classes {'continuation_or_standalone': 116, 'word_initial': 148}
- C5 (n=262): representatives [␠CA, PC, ␠Database, ␠mysql, ␠SW, ␠IP, ␠MySQL, ␠txt]; target-extreme [␠NAS, ␠ACP, CS, ␠ds, ␠LOS]; token classes {'continuation_or_standalone': 142, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 117}
- C6 (n=248): representatives [␠conformational, ␠renormalization, ␠electronically, ␠molecule, rientation, olecules, Server, ␠cyclin]; target-extreme [counter, ␠Active, Spin, ␠Hash, ␠surfaces]; token classes {'continuation_or_standalone': 102, 'word_initial': 146}
- C7 (n=247): representatives [")), )))), .”)., )))., .")., !), ?), )));]; target-extreme [00000000000000000000000000000000, ␠===, )))), ␠KIND, ?.]; token classes {'continuation_or_standalone': 46, 'punctuation_or_symbol': 165, 'whitespace': 12, 'word_initial': 24}

Strongest intercommunity connections:

- C0 to C1: 399 token edges; mean cosine 0.096907
- C0 to C6: 356 token edges; mean cosine 0.092241
- C1 to C3: 347 token edges; mean cosine 0.090793
- C2 to C6: 336 token edges; mean cosine 0.093661
- C2 to C3: 324 token edges; mean cosine 0.089430
- C3 to C5: 283 token edges; mean cosine 0.085588
- C0 to C8: 274 token edges; mean cosine 0.095099
- C0 to C2: 253 token edges; mean cosine 0.090850
- C2 to C5: 222 token edges; mean cosine 0.090592
- C3 to C4: 214 token edges; mean cosine 0.087091

### negative_tail

- Nodes: 3100
- Directed 10-NN edges: 31000
- Undirected edges: 21228
- Mean 10-NN cosine: 0.119504
- Communities: 13
- Modularity: 0.523384

Largest communities:

- C0 (n=551): representatives [␠Thompson, ␠Liz, ␠comp, ␠Luke, ␠illum, ␠Sullivan, ␠clums, ␠Col]; target-extreme [␠Max, ␠comp, ␠Turk, ект, ␠dilig]; token classes {'continuation_or_standalone': 172, 'punctuation_or_symbol': 11, 'target_lexical_variant': 4, 'whitespace': 2, 'word_initial': 362}
- C1 (n=380): representatives [Characteristics, ␠Characteristics, ␠analysis, ␠descriptions, ␠estimates, ␠pathophysiology, ␠recommendations, ␠messages]; target-extreme [␠biomarkers, ␠covariance, ␠visions, ␠news, icial]; token classes {'continuation_or_standalone': 100, 'whitespace': 3, 'word_initial': 277}
- C2 (n=346): representatives [␠unconstitutional, ␠Archbishop, ␠goddess, ␠Congressman, ␠Chairman, ␠sculptures, ␠leaders, ␠professor]; target-extreme [␠Rabbi, ␠Chair, ␠Laws, ␠officials, stead]; token classes {'continuation_or_standalone': 93, 'word_initial': 253}
- C3 (n=288): representatives [␠not, ␠if, ia, ␠or, ␠$, B, ␠␠␠, ized]; target-extreme [␠que, omes, means, ’, zero]; token classes {'continuation_or_standalone': 176, 'punctuation_or_symbol': 11, 'whitespace': 5, 'word_initial': 96}
- C4 (n=261): representatives [␠uncomfortable, ␠unacceptable, ␠terrifying, ␠annoying, ␠indistinguishable, ␠horrific, ␠brilli, ␠uniforms]; target-extreme [␠colors, ␠conclusive, ␠audible, ␠applause, ␠sturdy]; token classes {'continuation_or_standalone': 43, 'word_initial': 218}
- C5 (n=233): representatives [␠pulled, ␠decrease, ␠alteration, ␠dropped, ␠constructing, ␠prohibited, ␠determined, ␠dropping]; target-extreme [␠slated, ␠Beginning, ␠begin, ␠bolster, ␠trump]; token classes {'continuation_or_standalone': 54, 'whitespace': 2, 'word_initial': 177}
- C6 (n=226): representatives [␠hospitalization, ␠echocardiography, ␠catast, ology, ␠warriors, ␠angiography, ␠pathogens, ␠anesthesia]; target-extreme [␠Devil, ␠epidermis, remia, NRAS, ␠aer]; token classes {'continuation_or_standalone': 63, 'whitespace': 1, 'word_initial': 162}
- C7 (n=214): representatives [␠hallway, ␠stairs, ␠staircase, ␠stair, ␠guns, ␠piezoelectric, ␠cliffs, ␠trucks]; target-extreme [␠shots, ␠wireless, afers, ␠staircase, ␠nozzle]; token classes {'continuation_or_standalone': 32, 'whitespace': 2, 'word_initial': 180}

Strongest intercommunity connections:

- C0 to C2: 414 token edges; mean cosine 0.090881
- C1 to C5: 318 token edges; mean cosine 0.109862
- C1 to C4: 286 token edges; mean cosine 0.102386
- C1 to C2: 281 token edges; mean cosine 0.103795
- C1 to C3: 271 token edges; mean cosine 0.099271
- C0 to C6: 269 token edges; mean cosine 0.088738
- C0 to C4: 266 token edges; mean cosine 0.095032
- C0 to C9: 251 token edges; mean cosine 0.083334
- C2 to C7: 238 token edges; mean cosine 0.102900
- C3 to C5: 235 token edges; mean cosine 0.094499

### Secondary cross-side relations from R005

- ␠market (positive_head) to ␠markets (negative_tail): cosine 0.462327, combined-neighbour rank 1
- ␠markets (negative_tail) to ␠market (positive_head): cosine 0.462327, combined-neighbour rank 1
- AW (positive_head) to ␠AW (negative_tail): cosine 0.402867, combined-neighbour rank 1
- ␠AW (negative_tail) to AW (positive_head): cosine 0.402867, combined-neighbour rank 1
- ␠mathemat (negative_tail) to ␠Mathemat (positive_head): cosine 0.398725, combined-neighbour rank 1
- ␠Mathemat (positive_head) to ␠mathemat (negative_tail): cosine 0.398725, combined-neighbour rank 1
- ␠drag (negative_tail) to drag (positive_head): cosine 0.396710, combined-neighbour rank 3
- drag (positive_head) to ␠drag (negative_tail): cosine 0.396710, combined-neighbour rank 1
- ␠shining (positive_head) to ␠shine (negative_tail): cosine 0.390668, combined-neighbour rank 1
- ␠shine (negative_tail) to ␠shining (positive_head): cosine 0.390668, combined-neighbour rank 1

## State 5: block_04_output

### positive_head

- Nodes: 2886
- Directed 10-NN edges: 28860
- Undirected edges: 19706
- Mean 10-NN cosine: 0.118557
- Communities: 13
- Modularity: 0.521452

Largest communities:

- C0 (n=348): representatives [), ate, ␠is, en, ␠of, A, ␠was, ␠have]; target-extreme [), �, Reading, tar, ANT]; token classes {'continuation_or_standalone': 195, 'punctuation_or_symbol': 9, 'target_lexical_variant': 2, 'whitespace': 4, 'word_initial': 138}
- C1 (n=335): representatives [PC, SC, Bo, ␠CA, HA, CONNE, SS, ␠CP]; target-extreme [␠NAS, ␠ds, CS, イン, PC]; token classes {'continuation_or_standalone': 177, 'punctuation_or_symbol': 3, 'target_lexical_variant': 3, 'whitespace': 2, 'word_initial': 150}
- C2 (n=330): representatives [Acknowledgements, ␠response, ␠electronically, ␠sites, ␠mysql, ␠accessing, rientation, Connection]; target-extreme [␠Views, ␠KIND, ␠Role, Role, Press]; token classes {'continuation_or_standalone': 163, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 165}
- C3 (n=309): representatives [Financial, ␠initiating, ␠travelling, ␠formatted, ␠Financial, ␠specializes, ␠giving, ␠extracted]; target-extreme [Form, seeking, ␠solved, ␠franchise, ␠Forms]; token classes {'continuation_or_standalone': 86, 'whitespace': 1, 'word_initial': 222}
- C4 (n=296): representatives [␠immunosuppressive, ␠conformational, ␠glucocortic, ␠Phosph, ␠inflammatory, ␠pituitary, ␠renormalization, ␠metabolic]; target-extreme [Spin, ␠mitotic, ␠surfaces, ␠renormalization, ␠cycle]; token classes {'continuation_or_standalone': 89, 'whitespace': 1, 'word_initial': 206}
- C5 (n=284): representatives [␠Indonesian, ␠Nigerian, ␠Sacramento, ␠Charleston, California, Chicago, ␠Chinese, ␠Canadian]; target-extreme [␠resort, ppen, ös, bara, idis]; token classes {'continuation_or_standalone': 146, 'word_initial': 138}
- C6 (n=271): representatives [␠psychological, ␠psychosocial, ␠emotional, Political, ␠emotionally, ␠political, habilitation, ␠administrative]; target-extreme [counter, ␠Active, ␠Civil, ␠administrative, ␠Brothers]; token classes {'continuation_or_standalone': 90, 'whitespace': 1, 'word_initial': 180}
- C7 (n=181): representatives [])), }}), ")), )))), )))., .”)., ]));, )));]; target-extreme [)))), ␠===, 00000000000000000000000000000000, ␠*,, srep]; token classes {'continuation_or_standalone': 20, 'punctuation_or_symbol': 145, 'whitespace': 13, 'word_initial': 3}

Strongest intercommunity connections:

- C2 to C3: 399 token edges; mean cosine 0.097837
- C0 to C3: 372 token edges; mean cosine 0.100926
- C0 to C1: 321 token edges; mean cosine 0.085854
- C3 to C6: 315 token edges; mean cosine 0.096682
- C4 to C6: 306 token edges; mean cosine 0.095825
- C2 to C4: 256 token edges; mean cosine 0.089869
- C1 to C4: 246 token edges; mean cosine 0.092610
- C2 to C6: 245 token edges; mean cosine 0.091265
- C0 to C2: 241 token edges; mean cosine 0.093669
- C1 to C2: 237 token edges; mean cosine 0.090011

### negative_tail

- Nodes: 3218
- Directed 10-NN edges: 32180
- Undirected edges: 22018
- Mean 10-NN cosine: 0.120098
- Communities: 14
- Modularity: 0.536848

Largest communities:

- C0 (n=477): representatives [␠Hayes, ␠Liz, ␠Dav, ␠Thompson, ␠Murphy, Dav, ␠Roberts, ␠Hal]; target-extreme [␠Max, ␠Turk, ␠Claud, ␠Kepler, Wat]; token classes {'continuation_or_standalone': 176, 'punctuation_or_symbol': 6, 'whitespace': 1, 'word_initial': 294}
- C1 (n=475): representatives [Characteristics, ␠Characteristics, ␠analysis, ␠explanations, ␠descriptions, ␠interpretation, ␠constructions, ␠estimates]; target-extreme [␠colors, ␠slated, plugins, yses, ␠composed]; token classes {'continuation_or_standalone': 139, 'whitespace': 3, 'word_initial': 333}
- C2 (n=447): representatives [␠uncomfortable, ␠unconstitutional, ␠disappointment, ␠destroys, ␠pulled, ␠tragedy, ␠massacre, ␠annoying]; target-extreme [␠dilig, ␠conclusive, ␠sturdy, ␠displacement, stead]; token classes {'continuation_or_standalone': 90, 'whitespace': 4, 'word_initial': 353}
- C3 (n=317): representatives [␠staircase, ␠hallway, ␠stairs, ␠boats, ␠guns, ␠palace, ␠Palace, ␠balcon]; target-extreme [␠shots, ␠wireless, afers, ␠tir, ␠reactors]; token classes {'continuation_or_standalone': 65, 'whitespace': 3, 'word_initial': 249}
- C4 (n=299): representatives [␠if, ␠not, ia, ie, ized, ␠$, ␠or, ␠␠␠]; target-extreme [␠que, ␠$, UU, means, blk]; token classes {'continuation_or_standalone': 200, 'punctuation_or_symbol': 12, 'whitespace': 6, 'word_initial': 81}
- C5 (n=294): representatives [␠Archbishop, ␠goddess, ␠theolog, ␠Congressman, ␠pastor, ␠technicians, ␠Chairman, ␠murders]; target-extreme [␠Rabbi, ␠Devil, ␠speakers, ␠IJ, ␠Chair]; token classes {'continuation_or_standalone': 74, 'whitespace': 1, 'word_initial': 219}
- C6 (n=200): representatives [␠echocardiography, ␠pathophysiology, ␠abdomen, ␠angiography, ␠skull, ␠anesthesia, ␠cerebellum, oscopy]; target-extreme [remia, ␠biomarkers, unks, ␠pyro, NRAS]; token classes {'continuation_or_standalone': 70, 'word_initial': 130}
- C7 (n=186): representatives [␠catast, ␠discour, demonstr, ␠comp, ␠unsatisf, ␠prodig, ␠incomp, ␠abol]; target-extreme [␠comp, ект, demonstr, ␠begin, ␠uncon]; token classes {'continuation_or_standalone': 35, 'punctuation_or_symbol': 9, 'target_lexical_variant': 4, 'word_initial': 138}

Strongest intercommunity connections:

- C1 to C2: 700 token edges; mean cosine 0.100336
- C1 to C4: 342 token edges; mean cosine 0.104219
- C0 to C5: 321 token edges; mean cosine 0.091569
- C2 to C7: 313 token edges; mean cosine 0.101515
- C1 to C5: 311 token edges; mean cosine 0.100117
- C3 to C5: 299 token edges; mean cosine 0.104816
- C1 to C3: 287 token edges; mean cosine 0.093088
- C0 to C7: 286 token edges; mean cosine 0.086891
- C2 to C3: 279 token edges; mean cosine 0.091964
- C2 to C4: 268 token edges; mean cosine 0.095689

### Secondary cross-side relations from R005

- ␠various (positive_head) to Various (negative_tail): cosine 0.448009, combined-neighbour rank 1
- Various (negative_tail) to ␠various (positive_head): cosine 0.448009, combined-neighbour rank 1
- ␠video (negative_tail) to ␠Video (positive_head): cosine 0.421697, combined-neighbour rank 1
- ␠Video (positive_head) to ␠video (negative_tail): cosine 0.421697, combined-neighbour rank 1
- AW (positive_head) to ␠AW (negative_tail): cosine 0.402867, combined-neighbour rank 1
- ␠AW (negative_tail) to AW (positive_head): cosine 0.402867, combined-neighbour rank 1
- ␠mathemat (negative_tail) to ␠Mathemat (positive_head): cosine 0.398725, combined-neighbour rank 1
- ␠Mathemat (positive_head) to ␠mathemat (negative_tail): cosine 0.398725, combined-neighbour rank 1
- ␠drag (negative_tail) to drag (positive_head): cosine 0.396710, combined-neighbour rank 1
- drag (positive_head) to ␠drag (negative_tail): cosine 0.396710, combined-neighbour rank 1

## State 6: block_05_output

### positive_head

- Nodes: 2951
- Directed 10-NN edges: 29510
- Undirected edges: 20086
- Mean 10-NN cosine: 0.117935
- Communities: 13
- Modularity: 0.525968

Largest communities:

- C0 (n=409): representatives [␠mysql, ␠DB, rientation, ␠formatted, ␠transactions, ␠Database, ␠activities, ␠MySQL]; target-extreme [Form, ␠formul, ␠KIND, ␠Forms, ␠Role]; token classes {'continuation_or_standalone': 200, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 207}
- C1 (n=347): representatives [�, ␠immedi, �, ␠Rel, Bo, �, ␠neo, แ]; target-extreme [ensch, �, ␠FIN, camp, ␠Gest]; token classes {'continuation_or_standalone': 135, 'punctuation_or_symbol': 31, 'word_initial': 181}
- C2 (n=346): representatives [), ␠of, en, ␠is, ␠was, ␠have, ␠all, ␠A]; target-extreme [), ␠ds, anden, �, ANT]; token classes {'continuation_or_standalone': 228, 'punctuation_or_symbol': 7, 'target_lexical_variant': 3, 'whitespace': 5, 'word_initial': 103}
- C3 (n=306): representatives [␠travelling, ␠initiating, ␠accessing, Working, ␠Having, having, ␠giving, ␠extracted]; target-extreme [seeking, counter, ␠remembers, ␠solved, ␠resolving]; token classes {'continuation_or_standalone': 80, 'word_initial': 226}
- C4 (n=306): representatives [␠immunosuppressive, ␠neurodegenerative, ␠conformational, ␠glucocortic, ␠electronically, ␠renormalization, ␠inflammatory, ␠metabolic]; target-extreme [Spin, ␠renormalization, carbon, ocortic, ␠surfaces]; token classes {'continuation_or_standalone': 117, 'word_initial': 189}
- C5 (n=278): representatives [␠psychosocial, ␠psychological, ␠political, Political, ␠communities, ␠emotional, ␠parliamentary, ␠financial]; target-extreme [␠administrative, ␠Civil, ␠franchise, ␠employment, Financial]; token classes {'continuation_or_standalone': 70, 'whitespace': 2, 'word_initial': 206}
- C6 (n=237): representatives [␠Indonesian, ␠Nigerian, Chicago, ␠Atlanta, ␠Sacramento, ␠Laura, ␠Orlando, California]; target-extreme [␠resort, bara, iane, ayan, entre]; token classes {'continuation_or_standalone': 106, 'whitespace': 1, 'word_initial': 130}
- C7 (n=230): representatives [␠Subsequently, Eventually, ␠Alternatively, ␠subsequent, ␠Eventually, Anyway, ␠Anyway, Acknowledgements]; target-extreme [␠refreshing, ␠Active, ␠OK, ␠active, ␠reinst]; token classes {'continuation_or_standalone': 91, 'target_lexical_variant': 1, 'word_initial': 138}

Strongest intercommunity connections:

- C0 to C5: 352 token edges; mean cosine 0.090870
- C0 to C4: 345 token edges; mean cosine 0.090084
- C1 to C2: 344 token edges; mean cosine 0.086280
- C0 to C3: 340 token edges; mean cosine 0.101671
- C1 to C4: 300 token edges; mean cosine 0.086863
- C3 to C7: 282 token edges; mean cosine 0.096060
- C3 to C5: 273 token edges; mean cosine 0.098217
- C2 to C3: 268 token edges; mean cosine 0.100959
- C4 to C5: 255 token edges; mean cosine 0.097830
- C0 to C1: 247 token edges; mean cosine 0.084580

### negative_tail

- Nodes: 3152
- Directed 10-NN edges: 31520
- Undirected edges: 21574
- Mean 10-NN cosine: 0.119959
- Communities: 13
- Modularity: 0.537083

Largest communities:

- C0 (n=472): representatives [␠Hayes, ␠Liz, ␠Thompson, ␠Murphy, ␠Hicks, ␠Shapiro, ␠Luke, anyahu]; target-extreme [␠Max, ␠Turk, ␠alk, VV, ␠Claud]; token classes {'continuation_or_standalone': 189, 'punctuation_or_symbol': 5, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 276}
- C1 (n=464): representatives [␠disappointment, ␠destroys, ␠unconstitutional, ␠unacceptable, ␠destroyed, ␠magnificent, ␠tragedy, ␠terrifying]; target-extreme [␠slated, ␠conclusive, ␠authority, prises, ␠composed]; token classes {'continuation_or_standalone': 92, 'target_lexical_variant': 2, 'whitespace': 4, 'word_initial': 366}
- C2 (n=446): representatives [Characteristics, ␠assessments, ␠echocardiography, ␠Characteristics, ␠pathophysiology, ␠analysis, ␠decrease, ␠interpretation]; target-extreme [␠colors, ␠displacement, remia, yses, ␠Features]; token classes {'continuation_or_standalone': 141, 'word_initial': 305}
- C3 (n=332): representatives [␠if, ␠not, ia, ie, ␠or, B, el, ized]; target-extreme [␠begin, ␠que, point, ues, unks]; token classes {'continuation_or_standalone': 210, 'punctuation_or_symbol': 11, 'whitespace': 7, 'word_initial': 104}
- C4 (n=311): representatives [␠brilli, ␠catast, ␠comp, ␠unmist, ␠discontin, ␠unsatisf, ␠arrog, ␠imposs]; target-extreme [␠comp, ␠dilig, ект, ␠IJ, ␠abol]; token classes {'continuation_or_standalone': 77, 'punctuation_or_symbol': 14, 'whitespace': 1, 'word_initial': 219}
- C5 (n=291): representatives [␠Archbishop, ␠goddess, ␠priest, ␠priests, ␠technicians, ␠theolog, ␠Constitution, ␠Palace]; target-extreme [␠Devil, ␠Chair, ␠Rabbi, ␠speakers, ␠shouted]; token classes {'continuation_or_standalone': 53, 'whitespace': 2, 'word_initial': 236}
- C6 (n=228): representatives [␠staircase, ␠hallway, boats, ␠cliffs, ␠guns, ␠stair, ␠murders, ␠kill]; target-extreme [␠shots, afers, ␠barrel, ␠rue, ␠nozzle]; token classes {'continuation_or_standalone': 41, 'whitespace': 2, 'word_initial': 185}
- C7 (n=138): representatives [␠abdomen, ␠cerebellum, ␠skull, ␠uniforms, ␠epidermis, ␠robe, ␠erythrocytes, ␠gluc]; target-extreme [␠unit, ␠clad, ␠amel, ␠pyro, ␠lith]; token classes {'continuation_or_standalone': 37, 'target_lexical_variant': 1, 'word_initial': 100}

Strongest intercommunity connections:

- C1 to C2: 631 token edges; mean cosine 0.101725
- C0 to C4: 410 token edges; mean cosine 0.081595
- C1 to C4: 382 token edges; mean cosine 0.104095
- C2 to C3: 363 token edges; mean cosine 0.097812
- C1 to C3: 361 token edges; mean cosine 0.096189
- C0 to C5: 332 token edges; mean cosine 0.100831
- C1 to C5: 314 token edges; mean cosine 0.106410
- C2 to C5: 279 token edges; mean cosine 0.100872
- C1 to C6: 274 token edges; mean cosine 0.096592
- C0 to C3: 236 token edges; mean cosine 0.087268

### Secondary cross-side relations from R005

- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ␠captain (negative_tail) to Captain (positive_head): cosine 0.423141, combined-neighbour rank 1
- Captain (positive_head) to ␠captain (negative_tail): cosine 0.423141, combined-neighbour rank 1
- 14 (positive_head) to ␠14 (negative_tail): cosine 0.421743, combined-neighbour rank 1
- ␠14 (negative_tail) to 14 (positive_head): cosine 0.421743, combined-neighbour rank 1
- ␠mathemat (negative_tail) to ␠Mathemat (positive_head): cosine 0.398725, combined-neighbour rank 1
- ␠Mathemat (positive_head) to ␠mathemat (negative_tail): cosine 0.398725, combined-neighbour rank 1
- ␠shining (positive_head) to ␠shine (negative_tail): cosine 0.390668, combined-neighbour rank 1
- ␠shine (negative_tail) to ␠shining (positive_head): cosine 0.390668, combined-neighbour rank 1

## State 7: block_06_output

### positive_head

- Nodes: 2934
- Directed 10-NN edges: 29340
- Undirected edges: 20091
- Mean 10-NN cosine: 0.119657
- Communities: 12
- Modularity: 0.527096

Largest communities:

- C0 (n=454): representatives [␠immunosuppressive, ␠neurodegenerative, ␠psychological, ␠psychosocial, ␠Psychological, ␠conformational, ␠inflammatory, ␠glucocortic]; target-extreme [␠renormalization, ␠mitotic, Press, ocortic, ␠gang]; token classes {'continuation_or_standalone': 140, 'whitespace': 1, 'word_initial': 313}
- C1 (n=374): representatives [␠travelling, Working, ␠getting, ␠accessing, having, ␠initiating, ␠participating, ␠originating]; target-extreme [seeking, ␠formul, ␠solved, ␠Forms, ␠Views]; token classes {'continuation_or_standalone': 111, 'whitespace': 1, 'word_initial': 262}
- C2 (n=367): representatives [␠of, ), en, ␠have, ␠is, ␠was, ␠all, ␠A]; target-extreme [), urs, �, anden, Rel]; token classes {'continuation_or_standalone': 235, 'punctuation_or_symbol': 11, 'target_lexical_variant': 2, 'whitespace': 6, 'word_initial': 113}
- C3 (n=334): representatives [␠Database, Connection, ␠mysql, ␠response, ␠DB, ␠transactions, Day, ␠formatted]; target-extreme [␠Hash, ␠KIND, ␠Role, Entry, ␠seasonal]; token classes {'continuation_or_standalone': 179, 'word_initial': 155}
- C4 (n=244): representatives [Financial, ␠political, ␠cultural, ␠administrative, ␠Financial, ␠reimbursement, Political, ␠culturally]; target-extreme [␠employment, ␠Civil, ␠administrative, ␠resort, ␠Brothers]; token classes {'continuation_or_standalone': 53, 'punctuation_or_symbol': 1, 'word_initial': 190}
- C5 (n=229): representatives [␠Pakistani, ␠Indonesian, ␠Cleveland, ␠Charlotte, ␠Mexican, ␠Atlanta, ␠Sacramento, ␠Laura]; target-extreme [ayan, iane, entre, etica, bara]; token classes {'continuation_or_standalone': 97, 'word_initial': 132}
- C6 (n=190): representatives [�, �, ไ, �, �, �, ␠delic, ␠immedi]; target-extreme [�, �, ensch, hon, ␠indul]; token classes {'continuation_or_standalone': 77, 'punctuation_or_symbol': 34, 'word_initial': 79}
- C7 (n=186): representatives [}}), )))), )}}, )))., ")), }}., ================, }]; target-extreme [)))), srep, ␠===, 00000000000000000000000000000000, spacing]; token classes {'continuation_or_standalone': 30, 'punctuation_or_symbol': 134, 'whitespace': 13, 'word_initial': 9}

Strongest intercommunity connections:

- C0 to C3: 433 token edges; mean cosine 0.094317
- C1 to C3: 413 token edges; mean cosine 0.090067
- C0 to C1: 377 token edges; mean cosine 0.097454
- C0 to C4: 322 token edges; mean cosine 0.096470
- C1 to C2: 312 token edges; mean cosine 0.100906
- C1 to C4: 280 token edges; mean cosine 0.096011
- C3 to C4: 245 token edges; mean cosine 0.091743
- C2 to C6: 244 token edges; mean cosine 0.083635
- C2 to C8: 228 token edges; mean cosine 0.094099
- C0 to C6: 221 token edges; mean cosine 0.084933

### negative_tail

- Nodes: 2990
- Directed 10-NN edges: 29900
- Undirected edges: 20392
- Mean 10-NN cosine: 0.118865
- Communities: 12
- Modularity: 0.527268

Largest communities:

- C0 (n=464): representatives [determination, Characteristics, ␠Characteristics, ␠analysis, ␠recommendations, ␠interpretation, ␠environments, ␠prohibited]; target-extreme [␠displacement, ␠begin, ␠composed, ␠slated, yses]; token classes {'continuation_or_standalone': 163, 'whitespace': 2, 'word_initial': 299}
- C1 (n=394): representatives [␠Thompson, ␠Murphy, ␠Liz, ␠Lucy, ␠Smith, Gib, ␠Hicks, ␠Nick]; target-extreme [␠Max, ␠Turk, ␠trop, ␠ecc, ␠Tanz]; token classes {'continuation_or_standalone': 130, 'punctuation_or_symbol': 6, 'whitespace': 1, 'word_initial': 257}
- C2 (n=388): representatives [o, ␠not, ia, ie, ized, el, ␠$, ␠␠␠]; target-extreme [point, ić, adows, ␠que, ␠WHAT]; token classes {'continuation_or_standalone': 230, 'punctuation_or_symbol': 21, 'whitespace': 5, 'word_initial': 132}
- C3 (n=348): representatives [␠echocardiography, ␠staircase, ␠angiography, ␠hallway, ␠abdomen, boats, ␠phenotypes, ␠uniforms]; target-extreme [␠alk, remia, ␠Lith, ␠nozzle, ␠shuffle]; token classes {'continuation_or_standalone': 94, 'punctuation_or_symbol': 1, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 250}
- C4 (n=348): representatives [␠disappointment, ␠unconstitutional, ␠unacceptable, ␠terrifying, ␠horrific, ␠dismay, ␠brilli, ␠inconsistency]; target-extreme [␠conclusive, prises, ект, ␠shouted, ␠robustness]; token classes {'continuation_or_standalone': 67, 'whitespace': 3, 'word_initial': 278}
- C5 (n=230): representatives [␠priest, ␠technicians, ␠Archbishop, ␠priests, ␠Constitution, ␠concerts, ␠theolog, ␠Transportation]; target-extreme [␠Chair, ancers, ␠speakers, ␠wireless, ␠composer]; token classes {'continuation_or_standalone': 52, 'word_initial': 178}
- C6 (n=175): representatives [␠unsatisf, ␠catast, ␠unmist, ␠comp, ␠env, ␠displ, ␠Disc, establ]; target-extreme [␠displ, ␠comp, DEC, ␠mét, ␠conspic]; token classes {'continuation_or_standalone': 50, 'punctuation_or_symbol': 5, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 117}
- C7 (n=155): representatives [␠destroys, ␠destroyed, ␠thief, ␠guns, ␠villain, ␠massacre, ␠creating, ␠pulled]; target-extreme [␠Devil, ␠shots, ␠Delete, ␠thief, ␠abol]; token classes {'continuation_or_standalone': 27, 'punctuation_or_symbol': 1, 'whitespace': 3, 'word_initial': 124}

Strongest intercommunity connections:

- C0 to C4: 577 token edges; mean cosine 0.100724
- C0 to C2: 422 token edges; mean cosine 0.103457
- C1 to C2: 311 token edges; mean cosine 0.083886
- C1 to C3: 293 token edges; mean cosine 0.088738
- C0 to C3: 286 token edges; mean cosine 0.094190
- C0 to C5: 263 token edges; mean cosine 0.094596
- C1 to C5: 260 token edges; mean cosine 0.097249
- C1 to C6: 242 token edges; mean cosine 0.083673
- C4 to C7: 234 token edges; mean cosine 0.099541
- C3 to C5: 231 token edges; mean cosine 0.093691

### Secondary cross-side relations from R005

- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ␠captain (negative_tail) to Captain (positive_head): cosine 0.423141, combined-neighbour rank 1
- Captain (positive_head) to ␠captain (negative_tail): cosine 0.423141, combined-neighbour rank 1
- ),$$ (negative_tail) to ].$$ (positive_head): cosine 0.408441, combined-neighbour rank 1
- ].$$ (positive_head) to ),$$ (negative_tail): cosine 0.408441, combined-neighbour rank 2
- ␠Australian (positive_head) to Australia (negative_tail): cosine 0.386323, combined-neighbour rank 1
- Australia (negative_tail) to ␠Australian (positive_head): cosine 0.386323, combined-neighbour rank 1
- ␠Sunday (positive_head) to ␠Sundays (negative_tail): cosine 0.384484, combined-neighbour rank 2
- ␠Sundays (negative_tail) to ␠Sunday (positive_head): cosine 0.384484, combined-neighbour rank 1

## State 8: block_07_output

### positive_head

- Nodes: 3214
- Directed 10-NN edges: 32140
- Undirected edges: 21925
- Mean 10-NN cosine: 0.120487
- Communities: 13
- Modularity: 0.530926

Largest communities:

- C0 (n=446): representatives [␠travelling, Working, ␠initiating, management, ␠unsatisfactory, ␠accessing, ␠formatted, ␠researching]; target-extreme [seeking, Reading, ␠solved, recognized, ␠resolving]; token classes {'continuation_or_standalone': 117, 'whitespace': 4, 'word_initial': 325}
- C1 (n=429): representatives [en, ␠is, ), ␠of, ␠have, ␠at, ␠A, ␠all]; target-extreme [), ␠NAS, urs, �, ␠ds]; token classes {'continuation_or_standalone': 265, 'punctuation_or_symbol': 14, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 146}
- C2 (n=377): representatives [␠immunosuppressive, ␠neurodegenerative, ␠psychosocial, ␠Psychological, ␠psychological, ␠immunodef, ␠angiotensin, ␠inflammatory]; target-extreme [␠mitotic, ocortic, ␠administrative, ␠psychosocial, ␠mediation]; token classes {'continuation_or_standalone': 92, 'whitespace': 1, 'word_initial': 284}
- C3 (n=364): representatives [␠Pakistani, ␠basketball, ␠Indonesian, ␠Atlanta, ␠Sacramento, ␠Charleston, ␠Nigerian, Political]; target-extreme [␠Civil, ␠resort, ␠Brothers, ␠Salvador, bara]; token classes {'continuation_or_standalone': 136, 'word_initial': 228}
- C4 (n=330): representatives [�, �, enen, Inter, �, �, Lif, Ju]; target-extreme [�, anden, Rel, ös, �]; token classes {'continuation_or_standalone': 144, 'punctuation_or_symbol': 35, 'word_initial': 151}
- C5 (n=305): representatives [␠DB, ␠Database, ␠mysql, ␠MySQL, Connection, Day, Processing, ␠SQL]; target-extreme [␠refreshing, camp, ␠Hash, Entry, ␠KIND]; token classes {'continuation_or_standalone': 189, 'word_initial': 116}
- C6 (n=237): representatives [␠conformational, ␠renormalization, ␠molecule, rientation, ␠forms, ␠dynamical, olecules, ␠hierarchical]; target-extreme [␠renormalization, ␠formul, srep, ␠Forms, ␠Views]; token classes {'continuation_or_standalone': 86, 'word_initial': 151}
- C7 (n=213): representatives [Financial, ␠activities, ␠Employment, Employ, ␠response, ␠development, Active, ␠organizing]; target-extreme [␠employment, ␠fellowship, aign, rese, ␠lending]; token classes {'continuation_or_standalone': 69, 'punctuation_or_symbol': 1, 'word_initial': 143}

Strongest intercommunity connections:

- C1 to C4: 458 token edges; mean cosine 0.085121
- C0 to C1: 349 token edges; mean cosine 0.104823
- C2 to C6: 332 token edges; mean cosine 0.098446
- C0 to C7: 313 token edges; mean cosine 0.103986
- C0 to C2: 311 token edges; mean cosine 0.094852
- C3 to C4: 295 token edges; mean cosine 0.085913
- C2 to C4: 282 token edges; mean cosine 0.092901
- C0 to C5: 276 token edges; mean cosine 0.096883
- C2 to C3: 251 token edges; mean cosine 0.095520
- C1 to C3: 248 token edges; mean cosine 0.086167

### negative_tail

- Nodes: 3211
- Directed 10-NN edges: 32110
- Undirected edges: 21917
- Mean 10-NN cosine: 0.121299
- Communities: 12
- Modularity: 0.541761

Largest communities:

- C0 (n=632): representatives [␠Nick, ␠catast, ␠Liz, ␠brilli, ␠Lucy, ␠disast, ␠unmist, ␠Sarah]; target-extreme [␠Max, ␠Turk, ␠ecc, ␠trop, ␠displ]; token classes {'continuation_or_standalone': 191, 'punctuation_or_symbol': 21, 'target_lexical_variant': 4, 'whitespace': 2, 'word_initial': 414}
- C1 (n=415): representatives [determination, ␠assessments, Characteristics, ␠analysis, ␠manifestations, ␠environments, ␠Characteristics, ␠phenotypes]; target-extreme [␠variability, ␠robustness, ␠exterior, ␠slated, measure]; token classes {'continuation_or_standalone': 136, 'whitespace': 3, 'word_initial': 276}
- C2 (n=412): representatives [␠Archbishop, ␠priest, ␠Cathedral, ␠concerts, ␠Constitution, ␠Palace, ␠palace, ␠Princess]; target-extreme [␠Chair, ␠Devil, ␠speakers, ␠thief, ␠officials]; token classes {'continuation_or_standalone': 95, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 315}
- C3 (n=382): representatives [(, ␠not, ␠if, 's, ia, ie, ized, el]; target-extreme [␠que, ␠begin, ␠WHAT, point, prises]; token classes {'continuation_or_standalone': 230, 'punctuation_or_symbol': 14, 'target_lexical_variant': 1, 'whitespace': 7, 'word_initial': 130}
- C4 (n=304): representatives [␠disappointment, ␠unconstitutional, ␠tragedy, ␠horrific, ␠unacceptable, ␠indistinguishable, ␠stunning, ␠precluded]; target-extreme [␠louder, ␠conclusive, ␠screamed, ␠gloom, ␠shouted]; token classes {'continuation_or_standalone': 56, 'whitespace': 1, 'word_initial': 247}
- C5 (n=266): representatives [␠destroys, ␠destroyed, ␠removed, ␠dropped, ␠murders, ␠creating, ␠eliminated, ␠murdered]; target-extreme [␠shots, ␠composed, ␠departure, ␠Delete, ␠displacement]; token classes {'continuation_or_standalone': 48, 'whitespace': 2, 'word_initial': 216}
- C6 (n=220): representatives [␠hallway, ␠staircase, ␠stairs, ␠guns, ␠mountains, ␠trucks, ␠corridor, ␠gown]; target-extreme [adows, ␠barrel, ␠nozzle, ␠shroud, ␠clad]; token classes {'continuation_or_standalone': 42, 'word_initial': 178}
- C7 (n=143): representatives [␠GCC, RR, compiler, ␠LED, vv, ZZ, ␠hw, zz]; target-extreme [drv, UU, VV, ␠png, sdk]; token classes {'continuation_or_standalone': 98, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 43}

Strongest intercommunity connections:

- C0 to C2: 518 token edges; mean cosine 0.090164
- C1 to C5: 420 token edges; mean cosine 0.110823
- C0 to C3: 405 token edges; mean cosine 0.084420
- C4 to C5: 360 token edges; mean cosine 0.100139
- C1 to C4: 324 token edges; mean cosine 0.101795
- C2 to C6: 317 token edges; mean cosine 0.101259
- C1 to C3: 314 token edges; mean cosine 0.093768
- C0 to C4: 311 token edges; mean cosine 0.098881
- C1 to C2: 301 token edges; mean cosine 0.096103
- C2 to C4: 235 token edges; mean cosine 0.097610

### Secondary cross-side relations from R005

- ␠dominate (positive_head) to ␠dominates (negative_tail): cosine 0.571433, combined-neighbour rank 1
- ␠dominates (negative_tail) to ␠dominate (positive_head): cosine 0.571433, combined-neighbour rank 1
- 214 (positive_head) to ␠214 (negative_tail): cosine 0.457515, combined-neighbour rank 1
- ␠214 (negative_tail) to 214 (positive_head): cosine 0.457515, combined-neighbour rank 1
- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ␠video (negative_tail) to ␠Video (positive_head): cosine 0.421697, combined-neighbour rank 1
- ␠Video (positive_head) to ␠video (negative_tail): cosine 0.421697, combined-neighbour rank 1
- ),$$ (negative_tail) to ].$$ (positive_head): cosine 0.408441, combined-neighbour rank 1
- ].$$ (positive_head) to ),$$ (negative_tail): cosine 0.408441, combined-neighbour rank 2

## State 9: block_08_output

### positive_head

- Nodes: 3059
- Directed 10-NN edges: 30590
- Undirected edges: 20756
- Mean 10-NN cosine: 0.119028
- Communities: 13
- Modularity: 0.519715

Largest communities:

- C0 (n=500): representatives [␠determinations, ␠administrative, acceptable, Financial, Political, ␠satisfactory, ␠resolving, ␠initiating]; target-extreme [␠employment, seeking, rese, ␠fellowship, counter]; token classes {'continuation_or_standalone': 107, 'word_initial': 393}
- C1 (n=449): representatives [␠interactions, ␠activities, ␠renormalization, createElement, ␠development, ␠transactions, ␠DB, ␠forms]; target-extreme [␠renormalization, ␠formul, Spin, ␠Forms, Entry]; token classes {'continuation_or_standalone': 228, 'whitespace': 3, 'word_initial': 218}
- C2 (n=421): representatives [), ␠of, ␠is, ␠have, ␠at, ␠A, am, ␠a]; target-extreme [urs, ), �, arming, ␠perfor]; token classes {'continuation_or_standalone': 254, 'punctuation_or_symbol': 10, 'target_lexical_variant': 3, 'whitespace': 3, 'word_initial': 151}
- C3 (n=398): representatives [␠immunosuppressive, ␠neurodegenerative, ␠psychosocial, ␠conformational, ␠investigative, ␠glucocortic, ␠psychological, ␠immunodef]; target-extreme [␠mitotic, inhib, ␠psychosocial, ␠rheumatoid, ocortic]; token classes {'continuation_or_standalone': 103, 'punctuation_or_symbol': 1, 'whitespace': 6, 'word_initial': 288}
- C4 (n=283): representatives [␠Atlanta, ␠Indonesian, ␠Charleston, ␠Springfield, ␠Nigerian, ␠Terry, enen, Anne]; target-extreme [␠NAS, iley, ␠Salvador, Greek, etica]; token classes {'continuation_or_standalone': 142, 'whitespace': 1, 'word_initial': 140}
- C5 (n=204): representatives [�, Inter, �, �, �, ␠Rel, ␠Costa, �]; target-extreme [�, �, �, Pf, ια]; token classes {'continuation_or_standalone': 89, 'punctuation_or_symbol': 38, 'word_initial': 77}
- C6 (n=195): representatives [}}), ")), )))), )))., }$), ]));, )}}, "}](#]; target-extreme [srep, )))), ␠*);, ␠Caption, ␠$$|]; token classes {'continuation_or_standalone': 30, 'punctuation_or_symbol': 146, 'whitespace': 14, 'word_initial': 5}
- C7 (n=157): representatives [␠travelling, ␠rice, ␠literary, ␠culinary, ␠theatre, ␠fibres, ␠theat, ␠cafe]; target-extreme [␠beet, games, ␠travelled, ␠resort, arette]; token classes {'continuation_or_standalone': 42, 'word_initial': 115}

Strongest intercommunity connections:

- C0 to C1: 575 token edges; mean cosine 0.092878
- C0 to C3: 492 token edges; mean cosine 0.099793
- C1 to C3: 443 token edges; mean cosine 0.094083
- C0 to C2: 393 token edges; mean cosine 0.096198
- C1 to C2: 357 token edges; mean cosine 0.091686
- C2 to C4: 311 token edges; mean cosine 0.088186
- C2 to C5: 292 token edges; mean cosine 0.084304
- C3 to C7: 208 token edges; mean cosine 0.098700
- C0 to C7: 205 token edges; mean cosine 0.089623
- C2 to C3: 203 token edges; mean cosine 0.082778

### negative_tail

- Nodes: 2942
- Directed 10-NN edges: 29420
- Undirected edges: 20035
- Mean 10-NN cosine: 0.119038
- Communities: 12
- Modularity: 0.539629

Largest communities:

- C0 (n=517): representatives [␠hallway, ␠Cathedral, ␠Constitution, ␠palace, ␠Palace, ␠murders, ␠uniforms, ␠disasters]; target-extreme [␠shots, ␠uniforms, ␠Turk, ␠barrel, ␠Chair]; token classes {'continuation_or_standalone': 101, 'whitespace': 2, 'word_initial': 414}
- C1 (n=464): representatives [␠catast, ␠anec, ␠disast, ␠comp, ␠brilli, ␠gluc, ␠Luc, ␠Dob]; target-extreme [␠ecc, ␠trop, ␠SL, ␠png, diag]; token classes {'continuation_or_standalone': 147, 'punctuation_or_symbol': 11, 'target_lexical_variant': 3, 'whitespace': 3, 'word_initial': 300}
- C2 (n=418): representatives [␠environments, Characteristics, ␠Characteristics, ␠technologies, ␠analysis, ␠characteristics, ␠recommendations, ␠Analyses]; target-extreme [␠Max, ␠Features, ␠quotient, ␠variability, ␠circumstance]; token classes {'continuation_or_standalone': 152, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 263}
- C3 (n=378): representatives [␠unconstitutional, ␠destroys, ␠requirement, ␠unreasonable, ␠exclude, ␠inconsistent, ␠precluded, ␠creates]; target-extreme [␠Delete, ␠composed, ␠shuffle, ␠conclusive, ␠begin]; token classes {'continuation_or_standalone': 104, 'whitespace': 2, 'word_initial': 272}
- C4 (n=285): representatives [␠not, 's, ia, ␠or, 0, ized, ␠$, up]; target-extreme [␠WHAT, measure, ’, ␠HOW, omes]; token classes {'continuation_or_standalone': 175, 'punctuation_or_symbol': 8, 'target_lexical_variant': 1, 'whitespace': 8, 'word_initial': 93}
- C5 (n=153): representatives [␠echocardiography, ␠angiography, ␠cerebellum, ␠phenotypes, ␠abdomen, oscopy, ␠epithelium, ␠pelvis]; target-extreme [␠exterior, ␠allele, ␠angiography, ␠erythrocytes, oscopy]; token classes {'continuation_or_standalone': 52, 'word_initial': 101}
- C6 (n=152): representatives [␠horrific, ␠incredible, ␠tragedy, ␠stunning, ␠disappointing, substantial, ␠screamed, ␠sadness]; target-extreme [␠louder, amental, ␠gloom, ␠harsh, ␠screamed]; token classes {'continuation_or_standalone': 25, 'word_initial': 127}
- C7 (n=144): representatives [␠Nick, ␠Hicks, ␠Smith, ␠Lucy, ␠Molly, ␠Luke, ␠Murphy, ␠Palmer]; target-extreme [␠Violet, ␠broadcasts, ␠Telegraph, ␠Kat, ␠Mirror]; token classes {'continuation_or_standalone': 45, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 97}

Strongest intercommunity connections:

- C2 to C3: 565 token edges; mean cosine 0.096816
- C0 to C2: 442 token edges; mean cosine 0.094249
- C0 to C1: 399 token edges; mean cosine 0.087826
- C0 to C3: 392 token edges; mean cosine 0.097978
- C3 to C4: 311 token edges; mean cosine 0.092872
- C1 to C3: 285 token edges; mean cosine 0.090880
- C1 to C2: 274 token edges; mean cosine 0.086614
- C2 to C4: 273 token edges; mean cosine 0.091044
- C0 to C4: 272 token edges; mean cosine 0.088410
- C0 to C7: 232 token edges; mean cosine 0.095704

### Secondary cross-side relations from R005

- ].$$ (positive_head) to ]$$ (negative_tail): cosine 0.425212, combined-neighbour rank 1
- ]$$ (negative_tail) to ].$$ (positive_head): cosine 0.425212, combined-neighbour rank 1
- ),$$ (negative_tail) to ].$$ (positive_head): cosine 0.408441, combined-neighbour rank 1
- ].$$ (positive_head) to ),$$ (negative_tail): cosine 0.408441, combined-neighbour rank 2
- ␠performance (negative_tail) to ␠performances (positive_head): cosine 0.401969, combined-neighbour rank 1
- ␠performances (positive_head) to ␠performance (negative_tail): cosine 0.401969, combined-neighbour rank 1
- ␠submitted (positive_head) to ␠submit (negative_tail): cosine 0.398350, combined-neighbour rank 1
- ␠submit (negative_tail) to ␠submitted (positive_head): cosine 0.398350, combined-neighbour rank 1
- ␠148 (negative_tail) to ␠149 (positive_head): cosine 0.390873, combined-neighbour rank 1
- ␠149 (positive_head) to ␠148 (negative_tail): cosine 0.390873, combined-neighbour rank 1

## State 10: block_09_output

### positive_head

- Nodes: 2963
- Directed 10-NN edges: 29630
- Undirected edges: 20119
- Mean 10-NN cosine: 0.118752
- Communities: 13
- Modularity: 0.516624

Largest communities:

- C0 (n=408): representatives [␠psychological, ␠psychosocial, ␠conversations, ␠Psychological, ␠transactions, ␠motivational, ␠determinations, ␠environmentally]; target-extreme [␠employment, camp, ␠talks, ␠fellowship, aign]; token classes {'continuation_or_standalone': 68, 'whitespace': 1, 'word_initial': 339}
- C1 (n=388): representatives [␠making, ␠investigations, Working, management, ␠resolving, ␠investigative, ␠initiating, ␠requesting]; target-extreme [Reading, rese, seeking, uploads, ␠threatened]; token classes {'continuation_or_standalone': 109, 'whitespace': 1, 'word_initial': 278}
- C2 (n=361): representatives [␠immunosuppressive, ␠immunodef, ␠biodegrad, ␠conformational, ␠glucocortic, ␠intracellular, ␠antipsych, ␠dexamethasone]; target-extreme [␠mitotic, ␠mediation, inhib, ␠perfor, ␠regeneration]; token classes {'continuation_or_standalone': 114, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 244}
- C3 (n=360): representatives [), ␠is, ␠at, ␠have, ␠A, am, ␠and, ␠a]; target-extreme [urs, лен, ), �, ␠q]; token classes {'continuation_or_standalone': 207, 'punctuation_or_symbol': 11, 'target_lexical_variant': 3, 'whitespace': 3, 'word_initial': 136}
- C4 (n=254): representatives [␠Charleston, ␠Stockholm, ␠Springfield, ␠Atlanta, ␠Mumbai, ␠Brooklyn, ␠Nigerian, ␠Berlin]; target-extreme [iley, ␠Salvador, Greek, Gary, etica]; token classes {'continuation_or_standalone': 128, 'word_initial': 126}
- C5 (n=242): representatives [␠telecommunications, Acknowledgements, ␠forms, ␠administrative, ␠mysql, ␠DB, ␠MySQL, createElement]; target-extreme [sizeof, spacing, ␠formul, Entry, ␠Views]; token classes {'continuation_or_standalone': 142, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 97}
- C6 (n=190): representatives [␠µm, ␠volunte, HA, Tri, ␠MH, Ju, YA, ␠NE]; target-extreme [␠sket, ␠BD, ␠NAS, ␠ds, 12345]; token classes {'continuation_or_standalone': 65, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 120}
- C7 (n=178): representatives [")), )))), )}}, )))., .”)., }$), \]., ”).]; target-extreme [srep, ␠Caption, )))), ␠*);, Modified]; token classes {'continuation_or_standalone': 32, 'punctuation_or_symbol': 134, 'whitespace': 10, 'word_initial': 2}

Strongest intercommunity connections:

- C0 to C1: 586 token edges; mean cosine 0.097886
- C0 to C2: 368 token edges; mean cosine 0.097806
- C1 to C3: 329 token edges; mean cosine 0.103304
- C1 to C2: 264 token edges; mean cosine 0.097780
- C3 to C4: 250 token edges; mean cosine 0.082549
- C0 to C5: 249 token edges; mean cosine 0.091887
- C3 to C6: 246 token edges; mean cosine 0.089141
- C1 to C5: 217 token edges; mean cosine 0.091309
- C3 to C8: 211 token edges; mean cosine 0.081567
- C0 to C3: 206 token edges; mean cosine 0.089073

### negative_tail

- Nodes: 3095
- Directed 10-NN edges: 30950
- Undirected edges: 21123
- Mean 10-NN cosine: 0.120506
- Communities: 14
- Modularity: 0.524378

Largest communities:

- C0 (n=492): representatives [Characteristics, ␠unconstitutional, ␠Characteristics, ␠horrific, ␠environments, ␠catast, ␠unreasonable, ␠characteristics]; target-extreme [␠circumstance, ␠harsh, ␠Features, ␠uniforms, diag]; token classes {'continuation_or_standalone': 132, 'whitespace': 5, 'word_initial': 355}
- C1 (n=363): representatives [␠Lucy, ullivan, ␠Ler, ␠gluc, ␠Luc, ␠Murphy, ␠Jon, ␠province]; target-extreme [␠Violet, ␠Turk, ␠Lucas, ␠Telegraph, ␠Max]; token classes {'continuation_or_standalone': 128, 'punctuation_or_symbol': 1, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 231}
- C2 (n=328): representatives [o, (, ␠not, 's, I, ␠or, ␠“, 0]; target-extreme [omes, ␠WHAT, ␠que, ORD, ancers]; token classes {'continuation_or_standalone': 193, 'punctuation_or_symbol': 24, 'target_lexical_variant': 2, 'whitespace': 6, 'word_initial': 103}
- C3 (n=317): representatives [␠Cathedral, ␠warriors, ␠hallway, ␠sidewalk, ␠priest, ␠disasters, ␠mountains, ␠Archbishop]; target-extreme [␠exterior, ␠Devil, ␠Territory, ␠creature, ␠roads]; token classes {'continuation_or_standalone': 64, 'whitespace': 3, 'word_initial': 250}
- C4 (n=261): representatives [␠prohibiting, ␠eliminating, ␠destroyed, ␠prohibit, ␠destroys, ␠includes, ␠exclude, ␠kill]; target-extreme [␠Delete, ␠composed, ␠shots, ␠destroyed, ␠pulled]; token classes {'continuation_or_standalone': 71, 'whitespace': 2, 'word_initial': 188}
- C5 (n=233): representatives [notification, ␠compiler, LG, ␠sg, ␠initialization, compiler, ␠dashboard, Sig]; target-extreme [␠SL, CI, signal, ␠glyph, UU]; token classes {'continuation_or_standalone': 138, 'whitespace': 1, 'word_initial': 94}
- C6 (n=222): representatives [␠discour, ␠comp, ␠Comp, ␠abol, ␠Cap, ␠disg, ␠cont, ␠vý]; target-extreme [␠crypt, ␠ş, ␠ecc, ␠Cons, crypt]; token classes {'continuation_or_standalone': 80, 'punctuation_or_symbol': 12, 'target_lexical_variant': 1, 'whitespace': 4, 'word_initial': 125}
- C7 (n=161): representatives [␠1884, 170, 70, ␠170, ␠1880, ␠1882, 140, 141]; target-extreme [751, ␠490, ␠1882, 142, ␠407]; token classes {'continuation_or_standalone': 85, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 74}

Strongest intercommunity connections:

- C0 to C4: 451 token edges; mean cosine 0.103493
- C1 to C3: 311 token edges; mean cosine 0.094752
- C1 to C6: 305 token edges; mean cosine 0.081848
- C0 to C3: 285 token edges; mean cosine 0.096996
- C0 to C2: 281 token edges; mean cosine 0.096878
- C0 to C9: 260 token edges; mean cosine 0.094321
- C2 to C4: 242 token edges; mean cosine 0.101832
- C0 to C6: 230 token edges; mean cosine 0.089294
- C0 to C5: 209 token edges; mean cosine 0.087065
- C3 to C8: 203 token edges; mean cosine 0.096060

### Secondary cross-side relations from R005

- ␠captain (negative_tail) to Captain (positive_head): cosine 0.423141, combined-neighbour rank 1
- Captain (positive_head) to ␠captain (negative_tail): cosine 0.423141, combined-neighbour rank 1
- ␠orders (positive_head) to ␠Orders (negative_tail): cosine 0.418735, combined-neighbour rank 1
- ␠Orders (negative_tail) to ␠orders (positive_head): cosine 0.418735, combined-neighbour rank 1
- ␠performance (negative_tail) to ␠performances (positive_head): cosine 0.401969, combined-neighbour rank 1
- ␠performances (positive_head) to ␠performance (negative_tail): cosine 0.401969, combined-neighbour rank 1
- ␠Sunday (positive_head) to ␠Sundays (negative_tail): cosine 0.384484, combined-neighbour rank 2
- ␠Sundays (negative_tail) to ␠Sunday (positive_head): cosine 0.384484, combined-neighbour rank 1
- ␠clo (negative_tail) to clo (positive_head): cosine 0.380487, combined-neighbour rank 1
- clo (positive_head) to ␠clo (negative_tail): cosine 0.380487, combined-neighbour rank 1

## State 11: block_10_output

### positive_head

- Nodes: 3161
- Directed 10-NN edges: 31610
- Undirected edges: 21368
- Mean 10-NN cosine: 0.119861
- Communities: 14
- Modularity: 0.516859

Largest communities:

- C0 (n=437): representatives [␠negotiating, ␠psychosocial, ␠investigations, ␠conversations, ␠psychological, ␠Psychological, ␠therapists, ␠determinations]; target-extreme [rese, ␠employment, ␠sket, ␠fellowship, ␠talks]; token classes {'continuation_or_standalone': 110, 'whitespace': 1, 'word_initial': 326}
- C1 (n=386): representatives [), ␠is, ␠at, ␠all, ␠A, am, ␠where, ␠and]; target-extreme [Reading, лен, urs, Got, ␠Working]; token classes {'continuation_or_standalone': 225, 'punctuation_or_symbol': 8, 'target_lexical_variant': 2, 'whitespace': 4, 'word_initial': 147}
- C2 (n=358): representatives [␠initiating, ␠observing, ␠emerging, ␠travelling, ␠resolving, ␠evaluating, ␠motivated, ␠experiencing]; target-extreme [␠keeping, ␠resolving, ␠stake, seeking, ␠threatened]; token classes {'continuation_or_standalone': 76, 'whitespace': 1, 'word_initial': 281}
- C3 (n=296): representatives [Ken, ␠Stockholm, Kar, ␠Palestinian, ␠Berlin, ␠Brooklyn, ␠Karen, ␠MAR]; target-extreme [iley, Greek, ␠Berlin, Gary, ␠Mumbai]; token classes {'continuation_or_standalone': 129, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 165}
- C4 (n=285): representatives [␠immunosuppressive, ␠dopaminergic, ␠antipsych, ␠biodegrad, ␠neurotrans, ␠transmembrane, ␠dexamethasone, ␠intracellular]; target-extreme [␠mitotic, ␠trans, amid, ␠recycled, ␠perfor]; token classes {'continuation_or_standalone': 95, 'whitespace': 1, 'word_initial': 189}
- C5 (n=269): representatives [␠interactions, ␠forms, ␠renormalization, ␠coupling, ␠actions, ␠regularization, ␠action, ␠interaction]; target-extreme [Spin, spacing, ␠renormalization, ␠Spin, ␠formul]; token classes {'continuation_or_standalone': 105, 'whitespace': 1, 'word_initial': 163}
- C6 (n=232): representatives [␠coffee, ␠rice, ␠grinned, ␠laughed, ␠washing, ␠malaria, ␠amusement, ␠fishermen]; target-extreme [␠beet, camp, ␠resorts, ␠washing, ␠grinned]; token classes {'continuation_or_standalone': 38, 'whitespace': 1, 'word_initial': 193}
- C7 (n=226): representatives [}}), ")), )))., )}}, )))), )));, ␠)), }$)]; target-extreme [srep, ␠*);, \]., )))), ],[@]; token classes {'continuation_or_standalone': 35, 'punctuation_or_symbol': 176, 'whitespace': 9, 'word_initial': 6}

Strongest intercommunity connections:

- C0 to C2: 539 token edges; mean cosine 0.101949
- C1 to C2: 399 token edges; mean cosine 0.098257
- C0 to C5: 329 token edges; mean cosine 0.093572
- C0 to C4: 307 token edges; mean cosine 0.100956
- C2 to C5: 286 token edges; mean cosine 0.096480
- C1 to C3: 279 token edges; mean cosine 0.086884
- C1 to C8: 249 token edges; mean cosine 0.081501
- C4 to C6: 248 token edges; mean cosine 0.098602
- C0 to C1: 243 token edges; mean cosine 0.092089
- C0 to C3: 240 token edges; mean cosine 0.089888

### negative_tail

- Nodes: 3060
- Directed 10-NN edges: 30600
- Undirected edges: 20856
- Mean 10-NN cosine: 0.120571
- Communities: 12
- Modularity: 0.530987

Largest communities:

- C0 (n=486): representatives [␠Lucy, ␠discour, ␠Molly, ullivan, ␠Blair, ␠Claud, LG, ␠Hicks]; target-extreme [␠crypt, ␠Violet, CI, ␠glyph, crypt]; token classes {'continuation_or_standalone': 193, 'punctuation_or_symbol': 2, 'target_lexical_variant': 4, 'whitespace': 2, 'word_initial': 285}
- C1 (n=405): representatives [Characteristics, ␠Characteristics, ␠characteristics, ␠environments, ␠distributions, ␠uniforms, ␠technologies, ␠uniformity]; target-extreme [␠uniforms, ␠exterior, ␠circumstance, ␠Features, ␠composed]; token classes {'continuation_or_standalone': 160, 'whitespace': 2, 'word_initial': 243}
- C2 (n=402): representatives [␠unconstitutional, ␠unreasonable, ␠circumstantial, ␠horrific, ␠catast, ␠discriminatory, ␠disasters, ␠whispers]; target-extreme [␠harsh, ␠louder, ␠catast, amental, ␠supreme]; token classes {'continuation_or_standalone': 105, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 294}
- C3 (n=317): representatives [o, ␠not, 's, 2, I, ␠or, ␠“, ized]; target-extreme [ED, agg, omes, <empty>, ␠percent]; token classes {'continuation_or_standalone': 207, 'punctuation_or_symbol': 34, 'target_lexical_variant': 2, 'whitespace': 6, 'word_initial': 68}
- C4 (n=288): representatives [␠warriors, ␠queen, ␠guards, ␠princess, ␠users, ␠priest, ␠Cathedral, ␠prince]; target-extreme [IDENT, ␠departure, lace, ␠throne, ␠speakers]; token classes {'continuation_or_standalone': 83, 'whitespace': 1, 'word_initial': 204}
- C5 (n=251): representatives [␠hallway, ␠trucks, ␠sidewalk, ␠automobiles, ␠roadway, ␠mountains, ␠dashboard, ␠roads]; target-extreme [␠barrel, ␠cylinder, ␠roads, ␠barrels, ␠Gates]; token classes {'continuation_or_standalone': 50, 'whitespace': 2, 'word_initial': 199}
- C6 (n=248): representatives [␠prohibiting, ␠eliminating, ␠destroys, ␠Delete, ␠includes, ␠destroyed, ␠prohibited, ␠prohibits]; target-extreme [␠Delete, ␠preceded, ␠Creator, ␠pulled, ␠destroyed]; token classes {'continuation_or_standalone': 68, 'whitespace': 5, 'word_initial': 175}
- C7 (n=181): representatives [␠cette, emente, ␠ст, ␠questa, ␠Qué, ␠ça, ␠sempre, ␠que]; target-extreme [␠ş, ␠que, тор, ␠apenas, že]; token classes {'continuation_or_standalone': 94, 'punctuation_or_symbol': 11, 'whitespace': 1, 'word_initial': 75}

Strongest intercommunity connections:

- C1 to C2: 432 token edges; mean cosine 0.098690
- C2 to C6: 379 token edges; mean cosine 0.101304
- C1 to C6: 320 token edges; mean cosine 0.095639
- C0 to C3: 307 token edges; mean cosine 0.089429
- C0 to C2: 300 token edges; mean cosine 0.088685
- C0 to C1: 296 token edges; mean cosine 0.086193
- C0 to C5: 294 token edges; mean cosine 0.089890
- C2 to C4: 279 token edges; mean cosine 0.095135
- C1 to C4: 279 token edges; mean cosine 0.094250
- C0 to C4: 265 token edges; mean cosine 0.088668

### Secondary cross-side relations from R005

- neum (negative_tail) to ␠pneum (positive_head): cosine 0.515575, combined-neighbour rank 1
- ␠pneum (positive_head) to neum (negative_tail): cosine 0.515575, combined-neighbour rank 1
- ␠whether (negative_tail) to ␠Whether (positive_head): cosine 0.488394, combined-neighbour rank 1
- ␠Whether (positive_head) to ␠whether (negative_tail): cosine 0.488394, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠orders (positive_head) to ␠Orders (negative_tail): cosine 0.418735, combined-neighbour rank 1
- ␠Orders (negative_tail) to ␠orders (positive_head): cosine 0.418735, combined-neighbour rank 1
- ␠1970 (negative_tail) to ␠1969 (positive_head): cosine 0.410926, combined-neighbour rank 1
- ␠1969 (positive_head) to ␠1970 (negative_tail): cosine 0.410926, combined-neighbour rank 1

## State 12: block_11_output

### positive_head

- Nodes: 3491
- Directed 10-NN edges: 34910
- Undirected edges: 23541
- Mean 10-NN cosine: 0.120197
- Communities: 11
- Modularity: 0.508393

Largest communities:

- C0 (n=560): representatives [Ken, ␠Ken, ␠Berlin, Gary, �, German, ␠Hamburg, �]; target-extreme [iley, лен, �, ␠Berlin, Greek]; token classes {'continuation_or_standalone': 236, 'punctuation_or_symbol': 38, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 283}
- C1 (n=515): representatives [␠initiating, ␠observing, ␠journeys, ␠adventures, ␠characterizing, ␠innovative, ␠travelling, ␠trembling]; target-extreme [␠travers, ␠stake, ␠informed, ␠resolving, ␠quoted]; token classes {'continuation_or_standalone': 89, 'whitespace': 2, 'word_initial': 424}
- C2 (n=475): representatives [␠psychosocial, ␠conversations, ␠negotiating, management, ␠Psychological, ␠psychological, ␠investigations, ␠interventions]; target-extreme [rese, Reading, ␠sket, ␠employment, camp]; token classes {'continuation_or_standalone': 131, 'whitespace': 2, 'word_initial': 342}
- C3 (n=450): representatives [), ␠is, ␠at, ␠A, am, ␠where, ␠and, ␠back]; target-extreme [␠keeping, Got, ours, ␠Working, met]; token classes {'continuation_or_standalone': 239, 'punctuation_or_symbol': 6, 'target_lexical_variant': 2, 'whitespace': 4, 'word_initial': 199}
- C4 (n=430): representatives [␠immunosuppressive, ␠breastfeeding, ␠dexamethasone, ␠doxorubicin, ␠antifungal, menopausal, ␠pneum, ␠malaria]; target-extreme [␠mitotic, ␠beet, ␠recycled, amid, arette]; token classes {'continuation_or_standalone': 137, 'whitespace': 1, 'word_initial': 292}
- C5 (n=265): representatives [␠interactions, ␠forms, ␠coupling, ␠size, ␠actions, ␠molecule, rangian, ␠renormalization]; target-extreme [Spin, spacing, ␠Spin, ␠renormalization, interacting]; token classes {'continuation_or_standalone': 105, 'whitespace': 2, 'word_initial': 158}
- C6 (n=254): representatives [}}), )}}, ")), ␠}), )))), }}=\, )))., }$)]; target-extreme [srep, ␠*);, \]., ==============, vii]; token classes {'continuation_or_standalone': 40, 'punctuation_or_symbol': 194, 'whitespace': 11, 'word_initial': 9}
- C7 (n=229): representatives [Acknowledgements, ␠telecommunications, ␠BytePtrFromString, Inflater, ␠photosensitive, findViewById, ␠findViewById, ␠scrolling]; target-extreme [sizeof, ␠Caption, uploads, getElementById, mathchoice]; token classes {'continuation_or_standalone': 137, 'punctuation_or_symbol': 2, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 87}

Strongest intercommunity connections:

- C1 to C2: 688 token edges; mean cosine 0.100674
- C1 to C3: 601 token edges; mean cosine 0.095380
- C0 to C4: 511 token edges; mean cosine 0.088615
- C2 to C4: 483 token edges; mean cosine 0.098784
- C0 to C3: 476 token edges; mean cosine 0.087065
- C0 to C2: 451 token edges; mean cosine 0.086141
- C1 to C4: 446 token edges; mean cosine 0.098090
- C1 to C5: 333 token edges; mean cosine 0.098325
- C2 to C3: 320 token edges; mean cosine 0.096904
- C2 to C5: 312 token edges; mean cosine 0.094910

### negative_tail

- Nodes: 2945
- Directed 10-NN edges: 29450
- Undirected edges: 20218
- Mean 10-NN cosine: 0.118334
- Communities: 13
- Modularity: 0.530009

Largest communities:

- C0 (n=495): representatives [␠Characteristics, Characteristics, ␠characteristics, ␠distributions, ␠environments, ␠hospitalization, ␠uniforms, ␠concepts]; target-extreme [␠exterior, ␠uniforms, ␠Features, ␠circumstance, ␠specificity]; token classes {'continuation_or_standalone': 206, 'punctuation_or_symbol': 1, 'whitespace': 6, 'word_initial': 282}
- C1 (n=407): representatives [␠Molly, ␠Emily, ␠Lah, ␠Gh, ␠Freder, ␠Lucas, ␠Claud, ␠Crom]; target-extreme [␠crypt, ␠Violet, crypt, ␠gluc, ocr]; token classes {'continuation_or_standalone': 182, 'punctuation_or_symbol': 7, 'target_lexical_variant': 3, 'word_initial': 215}
- C2 (n=351): representatives [o, ␠not, 2, 's, I, ␠or, up, B]; target-extreme [<empty>, ␠ş, ED, ␠preceded, ORD]; token classes {'continuation_or_standalone': 210, 'punctuation_or_symbol': 35, 'target_lexical_variant': 2, 'whitespace': 5, 'word_initial': 99}
- C3 (n=324): representatives [␠unconstitutional, ␠unreasonable, ␠catast, ␠horrific, ␠circumstantial, ␠disasters, ␠tragedy, ␠encouragement]; target-extreme [␠harsh, ␠louder, substantial, ␠bleak, ␠supreme]; token classes {'continuation_or_standalone': 64, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 257}
- C4 (n=244): representatives [␠Constitution, ␠citizens, ␠guards, ␠legislature, ␠palace, ␠emperor, ␠Cathedral, ␠queen]; target-extreme [IDENT, ␠throne, ␠Interior, ␠Constitution, ␠Mirror]; token classes {'continuation_or_standalone': 49, 'whitespace': 1, 'word_initial': 194}
- C5 (n=225): representatives [␠automobiles, ␠trucks, ␠sidewalk, ␠lake, ␠gravel, ␠driveway, ␠dashboard, ␠chassis]; target-extreme [␠barrel, ␠cylinder, ␠Territory, ␠barrels, ␠roofs]; token classes {'continuation_or_standalone': 31, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 192}
- C6 (n=219): representatives [␠prohibiting, ␠eliminating, ␠Delete, ␠Remove, ␠includes, ␠prohibited, ␠prohibits, ␠emphasizes]; target-extreme [␠chop, ␠pulled, ␠resembled, ␠Creator, ␠Delete]; token classes {'continuation_or_standalone': 69, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 148}
- C7 (n=171): representatives [␠echocardiography, ␠cardiovascular, ␠angiography, ␠torso, ␠thighs, oscopy, ␠physiology, ␠morphology]; target-extreme [oscopy, ␠physiology, ␠feces, ␠Ultra, azol]; token classes {'continuation_or_standalone': 62, 'word_initial': 109}

Strongest intercommunity connections:

- C0 to C6: 395 token edges; mean cosine 0.097452
- C0 to C3: 380 token edges; mean cosine 0.102984
- C1 to C2: 356 token edges; mean cosine 0.083913
- C0 to C4: 305 token edges; mean cosine 0.099402
- C3 to C6: 295 token edges; mean cosine 0.099010
- C0 to C5: 267 token edges; mean cosine 0.090794
- C0 to C1: 260 token edges; mean cosine 0.079970
- C1 to C3: 253 token edges; mean cosine 0.085922
- C0 to C2: 240 token edges; mean cosine 0.085453
- C1 to C4: 237 token edges; mean cosine 0.090637

### Secondary cross-side relations from R005

- ␠dish (positive_head) to ␠dishes (negative_tail): cosine 0.524536, combined-neighbour rank 1
- ␠dishes (negative_tail) to ␠dish (positive_head): cosine 0.524536, combined-neighbour rank 1
- neum (negative_tail) to ␠pneum (positive_head): cosine 0.515575, combined-neighbour rank 1
- ␠pneum (positive_head) to neum (negative_tail): cosine 0.515575, combined-neighbour rank 1
- ␠Liter (negative_tail) to Liter (positive_head): cosine 0.502862, combined-neighbour rank 1
- Liter (positive_head) to ␠Liter (negative_tail): cosine 0.502862, combined-neighbour rank 1
- ␠session (negative_tail) to ␠sessions (positive_head): cosine 0.499858, combined-neighbour rank 1
- ␠sessions (positive_head) to ␠session (negative_tail): cosine 0.499858, combined-neighbour rank 1
- ␠whether (negative_tail) to ␠Whether (positive_head): cosine 0.488394, combined-neighbour rank 1
- ␠Whether (positive_head) to ␠whether (negative_tail): cosine 0.488394, combined-neighbour rank 1

## State 13: block_12_output

### positive_head

- Nodes: 3099
- Directed 10-NN edges: 30990
- Undirected edges: 20790
- Mean 10-NN cosine: 0.119276
- Communities: 12
- Modularity: 0.521255

Largest communities:

- C0 (n=629): representatives [␠Am, Ken, ␠Ken, ␠Coca, �, ␠Karen, ␠Mitchell, Gary]; target-extreme [iley, rese, ␠prem, �, sal]; token classes {'continuation_or_standalone': 232, 'punctuation_or_symbol': 38, 'target_lexical_variant': 3, 'whitespace': 4, 'word_initial': 352}
- C1 (n=503): representatives [Food, ␠dexamethasone, ␠breastfeeding, ␠telecommunications, ␠motivational, ␠dopaminergic, ␠pneum, ␠neurotrans]; target-extreme [␠stake, ␠informed, ␠customary, ␠airborne, ivated]; token classes {'continuation_or_standalone': 150, 'whitespace': 1, 'word_initial': 352}
- C2 (n=382): representatives [as, ␠at, ␠A, ␠where, am, ide, ␠making, ␠back]; target-extreme [ours, ␠keeping, ␠Working, Got, met]; token classes {'continuation_or_standalone': 223, 'punctuation_or_symbol': 4, 'target_lexical_variant': 2, 'whitespace': 3, 'word_initial': 150}
- C3 (n=316): representatives [}}=\, )}}, ␠BytePtrFromString, )))), }}), Acknowledgements, }$), $.[]{]; target-extreme [sizeof, ␠(), Thanks, mathchoice, srep]; token classes {'continuation_or_standalone': 78, 'punctuation_or_symbol': 185, 'whitespace': 11, 'word_initial': 42}
- C4 (n=297): representatives [management, ␠conversations, ␠investigations, ␠experience, ␠interviews, ␠adventures, ␠negotiating, ␠businesses]; target-extreme [␠travers, Reading, Posted, ␠Caption, ␠quoted]; token classes {'continuation_or_standalone': 99, 'word_initial': 198}
- C5 (n=233): representatives [␠interactions, interacting, ␠superconducting, ␠size, ␠development, ␠coupling, ␠values, change]; target-extreme [spacing, ␠renormalization, Spin, interacting, ␠Spin]; token classes {'continuation_or_standalone': 82, 'whitespace': 1, 'word_initial': 150}
- C6 (n=219): representatives [␠characterizing, ␠initiating, ␠remembering, ␠exploring, ␠observing, ␠entering, ␠hypothesized, ␠inserting]; target-extreme [␠sket, ␠recycled, ␠fluores, ␠resolving, ␠owed]; token classes {'continuation_or_standalone': 23, 'word_initial': 196}
- C7 (n=182): representatives [␠MH, ␠MAR, ␠DB, ␠mysql, ␠µm, Browser, ␠facebook, Entry]; target-extreme [RAW, 12345, ␠BA, Entry, Amazon]; token classes {'continuation_or_standalone': 93, 'word_initial': 89}

Strongest intercommunity connections:

- C0 to C1: 542 token edges; mean cosine 0.088158
- C1 to C4: 430 token edges; mean cosine 0.102993
- C0 to C2: 408 token edges; mean cosine 0.090090
- C1 to C6: 370 token edges; mean cosine 0.100543
- C1 to C5: 315 token edges; mean cosine 0.091736
- C2 to C6: 295 token edges; mean cosine 0.099212
- C1 to C2: 295 token edges; mean cosine 0.088107
- C0 to C7: 277 token edges; mean cosine 0.087788
- C4 to C6: 250 token edges; mean cosine 0.103702
- C1 to C8: 244 token edges; mean cosine 0.101507

### negative_tail

- Nodes: 3205
- Directed 10-NN edges: 32050
- Undirected edges: 21806
- Mean 10-NN cosine: 0.118995
- Communities: 13
- Modularity: 0.524856

Largest communities:

- C0 (n=512): representatives [␠Characteristics, Characteristics, ␠prohibiting, ␠unconstitutional, ␠circumstantial, ␠encouragement, ␠downregulation, ␠Delete]; target-extreme [␠specificity, ␠Features, ␠Creator, ␠circumstance, ␠preceded]; token classes {'continuation_or_standalone': 169, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 341}
- C1 (n=436): representatives [␠Claud, Jess, ␠Dav, ␠Emily, TG, ␠Muh, ␠Molly, GH]; target-extreme [␠Violet, ␠crypt, CI, crypt, ␠ş]; token classes {'continuation_or_standalone': 200, 'punctuation_or_symbol': 19, 'target_lexical_variant': 4, 'whitespace': 2, 'word_initial': 211}
- C2 (n=425): representatives [e, 's, I, ␠not, ␠or, ized, B, ␠“]; target-extreme [<empty>, agg, ORD, тор, ้]; token classes {'continuation_or_standalone': 269, 'punctuation_or_symbol': 37, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 115}
- C3 (n=372): representatives [␠emperor, ␠Constitution, ␠palace, ␠guards, ␠cathedral, ␠church, ␠Cathedral, mother]; target-extreme [IDENT, ocr, ␠Universe, ␠Constitution, ␠throne]; token classes {'continuation_or_standalone': 81, 'whitespace': 1, 'word_initial': 290}
- C4 (n=336): representatives [␠circumferential, ␠chassis, ␠trucks, ␠automobiles, ␠administrator, ␠sidewalk, ␠driveway, ␠mountains]; target-extreme [␠cylinder, ␠barrel, rors, olith, ␠curb]; token classes {'continuation_or_standalone': 85, 'whitespace': 1, 'word_initial': 250}
- C5 (n=264): representatives [␠uniforms, ␠distributions, ␠uniformity, ␠technologies, ␠concepts, distribution, ␠database, ␠algorithms]; target-extreme [␠uniforms, ␠exterior, diag, ␠variance, ␠concepts]; token classes {'continuation_or_standalone': 100, 'whitespace': 1, 'word_initial': 163}
- C6 (n=250): representatives [␠disasters, ␠catast, ␠horrific, ␠disastrous, ␠catastrophe, ␠tragedy, ␠catastrophic, ␠incredible]; target-extreme [␠harsh, ␠chop, ␠supreme, ␠catast, ␠louder]; token classes {'continuation_or_standalone': 52, 'whitespace': 2, 'word_initial': 196}
- C7 (n=192): representatives [␠immunofluorescence, ␠echocardiography, ␠cardiovascular, ␠atherosclerotic, ␠malignancies, ␠diseases, ␠electrophoresis, ␠dysfunction]; target-extreme [␠glyph, ␠gluc, ␠physiology, ␠feces, oscopy]; token classes {'continuation_or_standalone': 71, 'word_initial': 121}

Strongest intercommunity connections:

- C1 to C2: 510 token edges; mean cosine 0.088630
- C0 to C5: 471 token edges; mean cosine 0.099844
- C0 to C3: 405 token edges; mean cosine 0.100632
- C0 to C6: 381 token edges; mean cosine 0.102907
- C3 to C4: 337 token edges; mean cosine 0.095662
- C0 to C4: 280 token edges; mean cosine 0.091740
- C4 to C5: 272 token edges; mean cosine 0.091006
- C1 to C4: 262 token edges; mean cosine 0.089832
- C0 to C2: 259 token edges; mean cosine 0.090923
- C1 to C6: 258 token edges; mean cosine 0.084680

### Secondary cross-side relations from R005

- neum (negative_tail) to ␠pneum (positive_head): cosine 0.515575, combined-neighbour rank 1
- ␠pneum (positive_head) to neum (negative_tail): cosine 0.515575, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠road (positive_head) to ␠roads (negative_tail): cosine 0.440244, combined-neighbour rank 1
- ␠roads (negative_tail) to ␠road (positive_head): cosine 0.440244, combined-neighbour rank 1
- ␠orders (positive_head) to ␠Orders (negative_tail): cosine 0.418735, combined-neighbour rank 1
- ␠Orders (negative_tail) to ␠orders (positive_head): cosine 0.418735, combined-neighbour rank 1
- ␠anesthesia (negative_tail) to ␠anesthetized (positive_head): cosine 0.412530, combined-neighbour rank 1
- ␠anesthetized (positive_head) to ␠anesthesia (negative_tail): cosine 0.412530, combined-neighbour rank 1

## State 14: block_13_output

### positive_head

- Nodes: 2652
- Directed 10-NN edges: 26520
- Undirected edges: 17716
- Mean 10-NN cosine: 0.115320
- Communities: 13
- Modularity: 0.507873

Largest communities:

- C0 (n=411): representatives [␠remem, ␠negot, Se, Ama, ␠reappe, �, Emer, Barn]; target-extreme [␠travers, Bab, ␠sket, を, ■]; token classes {'continuation_or_standalone': 125, 'punctuation_or_symbol': 37, 'special': 1, 'target_lexical_variant': 2, 'whitespace': 3, 'word_initial': 243}
- C1 (n=328): representatives [␠resolving, ␠characterizing, ␠exploring, ␠remembering, ␠initiating, ␠observing, ␠computed, ␠development]; target-extreme [␠informed, ␠stake, ␠customary, ␠animated, ␠viable]; token classes {'continuation_or_standalone': 49, 'word_initial': 279}
- C2 (n=321): representatives [as, ation, ␠at, ating, ␠back, ␠making, ␠right, ␠found]; target-extreme [ours, ausing, ivated, tmp, met]; token classes {'continuation_or_standalone': 200, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 115}
- C3 (n=287): representatives [␠breastfeeding, ␠dexamethasone, ␠dopaminergic, ␠ventilation, ␠stainless, menopausal, ␠analges, ␠fres]; target-extreme [␠trans, Fresh, ␠fluores, ␠airborne, ␠recycled]; token classes {'continuation_or_standalone': 72, 'whitespace': 2, 'word_initial': 213}
- C4 (n=263): representatives [␠Am, ␠Manchester, ␠Karen, Maria, Gary, Anne, ␠Hamburg, Am]; target-extreme [sal, ␠Berlin, ␠Krish, rese, iley]; token classes {'continuation_or_standalone': 128, 'target_lexical_variant': 1, 'word_initial': 134}
- C5 (n=259): representatives [␠conversations, ␠negotiating, management, ␠discussions, ␠negotiation, ␠psychosocial, ␠interventions, ␠psychiat]; target-extreme [␠militant, pages, ␠resorts, ␠interventions, ␠psychosocial]; token classes {'continuation_or_standalone': 70, 'word_initial': 189}
- C6 (n=250): representatives [}$;, }}=\, $.[]{, }$), )}}, \}.$$, \]., $;]; target-extreme [␠(), sizeof, mathchoice, javase, spacing]; token classes {'continuation_or_standalone': 65, 'punctuation_or_symbol': 158, 'whitespace': 8, 'word_initial': 19}
- C7 (n=152): representatives [␠facebook, ␠size, Entry, Radius, Length, ␠PB, ␠PRES, ␠NE]; target-extreme [RAW, ␠upgrade, ␠peng, 12345, ␠BA]; token classes {'continuation_or_standalone': 79, 'whitespace': 1, 'word_initial': 72}

Strongest intercommunity connections:

- C0 to C4: 448 token edges; mean cosine 0.085956
- C1 to C2: 431 token edges; mean cosine 0.099248
- C1 to C5: 335 token edges; mean cosine 0.104147
- C0 to C3: 313 token edges; mean cosine 0.085567
- C3 to C5: 283 token edges; mean cosine 0.092102
- C1 to C3: 281 token edges; mean cosine 0.094299
- C0 to C1: 274 token edges; mean cosine 0.082704
- C0 to C5: 205 token edges; mean cosine 0.089693
- C3 to C4: 202 token edges; mean cosine 0.084002
- C2 to C4: 193 token edges; mean cosine 0.093292

### negative_tail

- Nodes: 2933
- Directed 10-NN edges: 29330
- Undirected edges: 19930
- Mean 10-NN cosine: 0.116435
- Communities: 13
- Modularity: 0.513892

Largest communities:

- C0 (n=579): representatives [␠Characteristics, Characteristics, ␠unconstitutional, ␠characteristics, ␠downregulation, ␠recommendations, ␠encouragement, availability]; target-extreme [crypt, ␠specificity, ␠Characteristics, ␠Constitution, ␠Interior]; token classes {'continuation_or_standalone': 199, 'whitespace': 4, 'word_initial': 376}
- C1 (n=484): representatives [␠disastrous, ␠circumstantial, ␠catast, ␠discriminatory, ␠unbelievable, ␠prohibiting, ␠incredible, ␠catastrophe]; target-extreme [␠harsh, ␠chop, ␠Creator, ␠heavily, ␠Mirror]; token classes {'continuation_or_standalone': 117, 'whitespace': 1, 'word_initial': 366}
- C2 (n=421): representatives [␠Caroline, Jess, ␠Gh, ␠Claud, Gh, ␠Tob, ␠Emily, ␠cytok]; target-extreme [␠Violet, ␠crypt, olith, ottom, ocr]; token classes {'continuation_or_standalone': 173, 'punctuation_or_symbol': 12, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 234}
- C3 (n=386): representatives [e, ␠not, I, ', H, ␠or, ized, ␠than]; target-extreme [<empty>, agg, IDENT, ้, ␠ş]; token classes {'continuation_or_standalone': 256, 'punctuation_or_symbol': 25, 'target_lexical_variant': 5, 'whitespace': 1, 'word_initial': 99}
- C4 (n=237): representatives [␠cardiovascular, ␠atherosclerotic, ␠circumferential, aphylococcus, ofluorescence, ␠trauma, clerosis, ␠interleukin]; target-extreme [␠Universe, ␠cylinder, ␠exterior, ␠Ia, ␠physiology]; token classes {'continuation_or_standalone': 67, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 168}
- C5 (n=209): representatives [␠theology, ␠emperor, mother, ␠grandmother, ␠palace, ␠cathedral, ␠church, ␠Empire]; target-extreme [␠Uncle, ␠throne, ␠Beast, orce, ␠aunt]; token classes {'continuation_or_standalone': 37, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 170}
- C6 (n=162): representatives [␠uniforms, ␠trucks, ␠automobiles, ␠roadway, ␠cliffs, ␠woods, ␠sidewalk, ␠driveway]; target-extreme [␠uniforms, ␠curb, ␠barrel, ␠quilt, ␠cloth]; token classes {'continuation_or_standalone': 31, 'whitespace': 1, 'word_initial': 130}
- C7 (n=134): representatives [␠chassis, ␠hardware, TG, ␠appliances, ␠Rails, ACC, ␠furniture, ␠TG]; target-extreme [CI, ␠SSH, lg, ␠SL, ␠LCD]; token classes {'continuation_or_standalone': 65, 'punctuation_or_symbol': 1, 'word_initial': 68}

Strongest intercommunity connections:

- C0 to C1: 883 token edges; mean cosine 0.102020
- C2 to C3: 442 token edges; mean cosine 0.084835
- C0 to C4: 334 token edges; mean cosine 0.099919
- C1 to C3: 317 token edges; mean cosine 0.090074
- C0 to C3: 291 token edges; mean cosine 0.092965
- C1 to C2: 284 token edges; mean cosine 0.082365
- C0 to C5: 263 token edges; mean cosine 0.095077
- C2 to C4: 259 token edges; mean cosine 0.092973
- C1 to C5: 239 token edges; mean cosine 0.095522
- C0 to C2: 237 token edges; mean cosine 0.087272

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- neum (negative_tail) to ␠pneum (positive_head): cosine 0.515575, combined-neighbour rank 1
- ␠pneum (positive_head) to neum (negative_tail): cosine 0.515575, combined-neighbour rank 1
- hydroxy (positive_head) to ␠hydroxy (negative_tail): cosine 0.459724, combined-neighbour rank 1
- ␠hydroxy (negative_tail) to hydroxy (positive_head): cosine 0.459724, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠road (positive_head) to ␠roads (negative_tail): cosine 0.440244, combined-neighbour rank 1
- ␠roads (negative_tail) to ␠road (positive_head): cosine 0.440244, combined-neighbour rank 1

## State 15: block_14_output

### positive_head

- Nodes: 2469
- Directed 10-NN edges: 24690
- Undirected edges: 16523
- Mean 10-NN cosine: 0.116003
- Communities: 9
- Modularity: 0.507417

Largest communities:

- C0 (n=387): representatives [as, ation, ␠at, le, ␠back, ␠making, ide, ␠right]; target-extreme [ours, ausing, pages, ␠Back, ␠Good]; token classes {'continuation_or_standalone': 219, 'punctuation_or_symbol': 3, 'target_lexical_variant': 1, 'whitespace': 4, 'word_initial': 160}
- C1 (n=331): representatives [␠Am, ␠Bav, Portug, ␠Berlin, ␠Ak, ␠Manchester, ␠Mitchell, ␠Karen]; target-extreme [␠Berlin, ␠propri, Pen, ␠Krish, iy]; token classes {'continuation_or_standalone': 144, 'punctuation_or_symbol': 1, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 183}
- C2 (n=324): representatives [}$;, \}.$$, $;, $.\, }$., $.[]{, }}=\, }_{(]; target-extreme [␠(), を, sizeof, ■, vii]; token classes {'continuation_or_standalone': 103, 'punctuation_or_symbol': 187, 'whitespace': 7, 'word_initial': 27}
- C3 (n=317): representatives [␠remem, ␠exempl, Compan, ␠exem, ␠ejemplo, ␠fres, ␠reappe, dil]; target-extreme [Bab, sal, ␠sket, ␠trans, ␠prem]; token classes {'continuation_or_standalone': 105, 'punctuation_or_symbol': 10, 'special': 1, 'whitespace': 3, 'word_initial': 198}
- C4 (n=300): representatives [␠exploring, ␠characterizing, ␠evolving, ␠remembering, ␠motivations, ␠discuss, ␠developments, ␠retrieved]; target-extreme [␠quoted, ␠informed, ␠stake, ␠vice, Thanks]; token classes {'continuation_or_standalone': 47, 'punctuation_or_symbol': 2, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 249}
- C5 (n=295): representatives [␠dexamethasone, ␠breastfeeding, ␠pulmonary, ␠constrained, monary, ␠ventilation, ␠psychiat, ␠happier]; target-extreme [␠recycled, ␠airborne, ␠peng, ␠sal, ␠µm]; token classes {'continuation_or_standalone': 76, 'whitespace': 1, 'word_initial': 218}
- C6 (n=243): representatives [␠conversations, ␠interactions, ␠resolving, ␠discussions, ␠adventures, ␠negotiating, management, ␠computed]; target-extreme [␠travers, ␠interactions, Bibliography, interacting, director]; token classes {'continuation_or_standalone': 63, 'whitespace': 2, 'word_initial': 178}
- C7 (n=144): representatives [Food, ␠MAR, business, ␠workshops, ␠shoppers, ␠hospital, ␠healthcare, ␠shopping]; target-extreme [Posted, ␠Caption, tmp, ␠animated, ␠resorts]; token classes {'continuation_or_standalone': 45, 'whitespace': 1, 'word_initial': 98}

Strongest intercommunity connections:

- C1 to C3: 483 token edges; mean cosine 0.083241
- C0 to C4: 422 token edges; mean cosine 0.097609
- C4 to C6: 407 token edges; mean cosine 0.099219
- C3 to C5: 341 token edges; mean cosine 0.086295
- C0 to C6: 339 token edges; mean cosine 0.089842
- C0 to C5: 288 token edges; mean cosine 0.090908
- C4 to C5: 280 token edges; mean cosine 0.091805
- C1 to C5: 257 token edges; mean cosine 0.083352
- C0 to C1: 244 token edges; mean cosine 0.086307
- C3 to C4: 234 token edges; mean cosine 0.088616

### negative_tail

- Nodes: 2689
- Directed 10-NN edges: 26890
- Undirected edges: 18273
- Mean 10-NN cosine: 0.112817
- Communities: 13
- Modularity: 0.512347

Largest communities:

- C0 (n=430): representatives [Characteristics, ␠Characteristics, ␠downregulation, ␠recommendations, ␠encouragement, ␠distributions, ␠administrator, representation]; target-extreme [␠variance, ␠specificity, ␠exterior, ␠Characteristics, codec]; token classes {'continuation_or_standalone': 152, 'whitespace': 1, 'word_initial': 277}
- C1 (n=376): representatives [I, ␠or, ized, ED, ␠they, ian, ␠say, ra]; target-extreme [<empty>, agg, ้, uz, ties]; token classes {'continuation_or_standalone': 269, 'punctuation_or_symbol': 20, 'target_lexical_variant': 2, 'word_initial': 85}
- C2 (n=342): representatives [␠Caroline, ␠Gh, Jess, ␠Tob, ␠fluor, ␠Claude, ␠Tah, ␠Cer]; target-extreme [␠Violet, olith, ocr, ocy, ␠Celt]; token classes {'continuation_or_standalone': 126, 'punctuation_or_symbol': 16, 'target_lexical_variant': 4, 'whitespace': 2, 'word_initial': 194}
- C3 (n=304): representatives [␠circumstantial, ␠unconstitutional, ␠discriminatory, ␠unbelievable, ␠disastrous, ␠prohibiting, ␠incredible, ␠catastrophe]; target-extreme [␠harsh, ␠heavily, ␠supreme, substantial, ␠intense]; token classes {'continuation_or_standalone': 69, 'whitespace': 2, 'word_initial': 233}
- C4 (n=261): representatives [␠emperor, ␠Constitution, ␠palace, ␠queen, ␠cathedral, ␠church, ␠Empire, ␠Sultan]; target-extreme [␠Uncle, ␠Universe, ␠Constitution, IDENT, ␠Beast]; token classes {'continuation_or_standalone': 50, 'whitespace': 1, 'word_initial': 210}
- C5 (n=217): representatives [␠atherosclerotic, ␠cardiovascular, ␠epidemiological, ␠macrophage, ␠gluc, ␠dysfunction, ␠interleukin, aphylococcus]; target-extreme [␠gluc, ␠monocyte, ␠physiology, ␠feces, ␠dimer]; token classes {'continuation_or_standalone': 75, 'word_initial': 142}
- C6 (n=187): representatives [TG, ␠TG, GGT, ACC, UU, CE, Gs, ␠RF]; target-extreme [␠crypt, crypt, CI, ␠SSH, ␠glyph]; token classes {'continuation_or_standalone': 105, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 79}
- C7 (n=163): representatives [␠circumferential, ␠uniforms, ␠trucks, ␠chassis, ␠bulbs, ␠automobiles, ␠vegetables, ␠sidewalk]; target-extreme [ottom, ␠uniforms, ␠Interior, ␠curb, ␠barrel]; token classes {'continuation_or_standalone': 31, 'whitespace': 2, 'word_initial': 130}

Strongest intercommunity connections:

- C0 to C3: 447 token edges; mean cosine 0.101781
- C1 to C2: 353 token edges; mean cosine 0.081819
- C0 to C4: 306 token edges; mean cosine 0.096005
- C0 to C8: 270 token edges; mean cosine 0.100211
- C0 to C1: 251 token edges; mean cosine 0.085297
- C2 to C6: 244 token edges; mean cosine 0.085886
- C3 to C4: 243 token edges; mean cosine 0.099188
- C0 to C5: 228 token edges; mean cosine 0.095593
- C2 to C5: 224 token edges; mean cosine 0.084320
- C0 to C7: 214 token edges; mean cosine 0.096843

### Secondary cross-side relations from R005

- mot (negative_tail) to Mot (positive_head): cosine 0.511479, combined-neighbour rank 1
- Mot (positive_head) to mot (negative_tail): cosine 0.511479, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠road (positive_head) to ␠roads (negative_tail): cosine 0.440244, combined-neighbour rank 1
- ␠roads (negative_tail) to ␠road (positive_head): cosine 0.440244, combined-neighbour rank 1
- ␠orders (positive_head) to ␠Orders (negative_tail): cosine 0.418735, combined-neighbour rank 1
- ␠Orders (negative_tail) to ␠orders (positive_head): cosine 0.418735, combined-neighbour rank 1
- ␠anest (positive_head) to ␠anesthesia (negative_tail): cosine 0.400689, combined-neighbour rank 1
- ␠anesthesia (negative_tail) to ␠anest (positive_head): cosine 0.400689, combined-neighbour rank 1

## State 16: block_15_output

### positive_head

- Nodes: 2550
- Directed 10-NN edges: 25500
- Undirected edges: 17095
- Mean 10-NN cosine: 0.115894
- Communities: 11
- Modularity: 0.508229

Largest communities:

- C0 (n=544): representatives [␠Am, ␠Manchester, ␠remem, ␠Jay, ␠Mitchell, ␠MAR, Kar, ␠Karen]; target-extreme [sal, Bab, を, ␠beaut, ␠Berlin]; token classes {'continuation_or_standalone': 218, 'punctuation_or_symbol': 18, 'target_lexical_variant': 1, 'whitespace': 6, 'word_initial': 301}
- C1 (n=419): representatives [␠transformations, ␠interactions, ␠exploring, ␠anticipated, ␠development, ␠Measurements, ␠resolving, ␠characterizing]; target-extreme [␠travers, ␠quoted, Observ, ␠informed, ␠interactions]; token classes {'continuation_or_standalone': 99, 'whitespace': 4, 'word_initial': 316}
- C2 (n=294): representatives [Food, ␠breastfeeding, ␠happiness, ␠adventures, ␠negotiating, ␠discomfort, ␠interviews, ␠conversations]; target-extreme [␠motivations, ␠Wrest, business, ␠vice, ␠militant]; token classes {'continuation_or_standalone': 54, 'word_initial': 240}
- C3 (n=264): representatives [as, ation, ␠at, ating, ine, le, ␠into, ␠back]; target-extreme [ours, ausing, ␠Good, met, ␠Back]; token classes {'continuation_or_standalone': 164, 'punctuation_or_symbol': 2, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 96}
- C4 (n=243): representatives [␠dexamethasone, ␠pulmonary, ␠fibers, ␠analgesic, ␠imaging, monary, ␠pneum, ␠designing]; target-extreme [␠trans, ␠Caption, ␠peng, ␠airborne, ␠\n␠␠␠␠␠]; token classes {'continuation_or_standalone': 67, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 169}
- C5 (n=192): representatives [\}.$$, }$;, $.\, $.[]{, $;, }_{(, \]., >(]; target-extreme [␠(), ■, ␠@@, ](, �]; token classes {'continuation_or_standalone': 19, 'punctuation_or_symbol': 161, 'whitespace': 3, 'word_initial': 9}
- C6 (n=177): representatives [management, Notification, ␠platforms, Length, PhysRev, pntd, spacing, Resolver]; target-extreme [sizeof, javase, mathchoice, ое, pages]; token classes {'continuation_or_standalone': 121, 'punctuation_or_symbol': 5, 'whitespace': 1, 'word_initial': 50}
- C7 (n=121): representatives [Next, ␠Got, Got, With, ␠adopting, More, Clearly, ␠Now]; target-extreme [Posted, Thanks, tmp, Got, ␠extra]; token classes {'continuation_or_standalone': 66, 'target_lexical_variant': 1, 'word_initial': 54}

Strongest intercommunity connections:

- C1 to C2: 557 token edges; mean cosine 0.096843
- C1 to C3: 469 token edges; mean cosine 0.094826
- C0 to C4: 432 token edges; mean cosine 0.082477
- C0 to C3: 277 token edges; mean cosine 0.090025
- C0 to C2: 274 token edges; mean cosine 0.088367
- C1 to C4: 255 token edges; mean cosine 0.097112
- C2 to C4: 248 token edges; mean cosine 0.090911
- C0 to C8: 232 token edges; mean cosine 0.086458
- C0 to C1: 215 token edges; mean cosine 0.083133
- C0 to C6: 215 token edges; mean cosine 0.080901

### negative_tail

- Nodes: 2643
- Directed 10-NN edges: 26430
- Undirected edges: 17924
- Mean 10-NN cosine: 0.111815
- Communities: 12
- Modularity: 0.495328

Largest communities:

- C0 (n=522): representatives [␠Characteristics, Characteristics, ␠circumstantial, ␠downregulation, ␠unconstitutional, ␠Configuration, ␠recommendations, ␠discriminatory]; target-extreme [␠specificity, ␠characteristics, ␠Characteristics, ␠enactment, ␠disadvantages]; token classes {'continuation_or_standalone': 138, 'whitespace': 1, 'word_initial': 383}
- C1 (n=408): representatives [I, ␠or, ized, ␠they, ED, ra, ␠WHAT, THIS]; target-extreme [<empty>, CI, agg, ␠cette, gy]; token classes {'continuation_or_standalone': 290, 'punctuation_or_symbol': 12, 'target_lexical_variant': 3, 'whitespace': 1, 'word_initial': 102}
- C2 (n=314): representatives [␠Claire, ␠Gh, ␠Caroline, ␠Theod, ␠Betty, ␠Connie, ␠Sarah, ␠catast]; target-extreme [␠Violet, ␠Ia, phan, ␠Maur, enger]; token classes {'continuation_or_standalone': 109, 'punctuation_or_symbol': 20, 'word_initial': 185}
- C3 (n=253): representatives [␠cardiovascular, ␠atherosclerotic, ␠jurisdictional, ␠macrophage, ␠erythrocytes, ␠epidemiological, clerosis, aphylococcus]; target-extreme [olith, ␠monocyte, ␠gluc, ␠physiology, teral]; token classes {'continuation_or_standalone': 87, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 162}
- C4 (n=215): representatives [␠disproportionate, ␠unbelievable, asionally, ␠disastrous, ␠incredible, ␠catastrophic, Excellent, ␠Sometimes]; target-extreme [␠harsh, ␠chop, ␠heavily, ␠excessive, esque]; token classes {'continuation_or_standalone': 56, 'word_initial': 159}
- C5 (n=201): representatives [␠circumferential, ␠trucks, ␠chassis, ␠gravel, ␠automobiles, ␠roadway, ␠vegetables, ␠Rails]; target-extreme [ottom, ␠curb, rors, ␠dishes, ␠ignition]; token classes {'continuation_or_standalone': 38, 'word_initial': 163}
- C6 (n=160): representatives [representation, distribution, ␠uniforms, ␠uniformity, ␠perpendicular, ␠distributions, ogeneity, ␠contradictory]; target-extreme [␠uniforms, ␠exterior, ␠affirmative, ␠variance, ␠algebra]; token classes {'continuation_or_standalone': 68, 'whitespace': 1, 'word_initial': 91}
- C7 (n=159): representatives [␠Constitution, ␠Alabama, ␠Philadelphia, ␠Louisiana, Florida, ␠Americans, ␠Florida, ␠individuals]; target-extreme [ocr, individual, inois, ␠Universe, ␠Illinois]; token classes {'continuation_or_standalone': 47, 'word_initial': 112}

Strongest intercommunity connections:

- C0 to C6: 421 token edges; mean cosine 0.094967
- C0 to C4: 415 token edges; mean cosine 0.100646
- C0 to C1: 399 token edges; mean cosine 0.087861
- C1 to C2: 373 token edges; mean cosine 0.080320
- C0 to C5: 270 token edges; mean cosine 0.091371
- C0 to C3: 265 token edges; mean cosine 0.094146
- C2 to C3: 224 token edges; mean cosine 0.083323
- C1 to C4: 220 token edges; mean cosine 0.089017
- C0 to C7: 214 token edges; mean cosine 0.098704
- C1 to C9: 185 token edges; mean cosine 0.083994

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- mot (negative_tail) to Mot (positive_head): cosine 0.511479, combined-neighbour rank 1
- Mot (positive_head) to mot (negative_tail): cosine 0.511479, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠orders (positive_head) to ␠Orders (negative_tail): cosine 0.418735, combined-neighbour rank 1
- ␠Orders (negative_tail) to ␠orders (positive_head): cosine 0.418735, combined-neighbour rank 1
- ␠anest (positive_head) to ␠anesthesia (negative_tail): cosine 0.400689, combined-neighbour rank 1
- ␠anesthesia (negative_tail) to ␠anest (positive_head): cosine 0.400689, combined-neighbour rank 1

## State 17: block_16_output

### positive_head

- Nodes: 2733
- Directed 10-NN edges: 27330
- Undirected edges: 18544
- Mean 10-NN cosine: 0.119174
- Communities: 13
- Modularity: 0.512731

Largest communities:

- C0 (n=350): representatives [␠anticipated, ␠Measurements, ␠anticipation, ␠development, ␠evolving, ␠recorded, ␠happiness, ␠observed]; target-extreme [␠quoted, ␠motivations, Observ, ␠informed, ␠stake]; token classes {'continuation_or_standalone': 54, 'special': 1, 'whitespace': 3, 'word_initial': 292}
- C1 (n=315): representatives [␠exploring, ␠inev, ␠discuss, ␠unve, ␠resolving, ␠unavoid, Emer, ␠explores]; target-extreme [␠travers, sal, ␠propri, ␠beaut, ␠trans]; token classes {'continuation_or_standalone': 79, 'punctuation_or_symbol': 4, 'whitespace': 3, 'word_initial': 229}
- C2 (n=287): representatives [␠transformations, ␠determinations, ␠interactions, ␠characterizing, ␠values, ␠coupling, ␠partnerships, izations]; target-extreme [sizeof, ␠interactions, ␠animated, pages, Manager]; token classes {'continuation_or_standalone': 147, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 138}
- C3 (n=280): representatives [as, ␠at, ation, ating, le, ine, ␠more, it]; target-extreme [ours, ausing, ilation, ␠unse, amid]; token classes {'continuation_or_standalone': 187, 'punctuation_or_symbol': 2, 'target_lexical_variant': 5, 'whitespace': 2, 'word_initial': 84}
- C4 (n=280): representatives [}$;, $.\, ␠.$$, \}.$$, $.[]{, \]., $;, }$.]; target-extreme [Posted, ␠(), ␠@@, �, ■]; token classes {'continuation_or_standalone': 60, 'punctuation_or_symbol': 180, 'target_lexical_variant': 1, 'whitespace': 5, 'word_initial': 34}
- C5 (n=248): representatives [␠entrepreneurs, Food, ␠breastfeeding, ␠conversations, ␠businesses, ␠adventures, ␠negotiating, ␠filmmakers]; target-extreme [business, ␠students, director, Bibliography, ␠resorts]; token classes {'continuation_or_standalone': 60, 'word_initial': 188}
- C6 (n=224): representatives [␠Manchester, ␠Matt, ␠Bristol, ␠Kashmir, ␠Hamburg, itzerland, ␠Stockholm, ␠Pak]; target-extreme [Bab, ␠Berlin, Pen, iy, ␠Krish]; token classes {'continuation_or_standalone': 94, 'word_initial': 130}
- C7 (n=218): representatives [␠dexamethasone, ␠psychiat, ␠imaging, ␠analgesic, monary, ␠pulmonary, ␠pneum, ␠ventilation]; target-extreme [␠recycled, ␠airborne, ␠fluores, ␠µm, ␠sensing]; token classes {'continuation_or_standalone': 57, 'punctuation_or_symbol': 1, 'whitespace': 3, 'word_initial': 157}

Strongest intercommunity connections:

- C0 to C2: 361 token edges; mean cosine 0.097420
- C0 to C3: 321 token edges; mean cosine 0.104211
- C0 to C1: 312 token edges; mean cosine 0.093267
- C0 to C5: 299 token edges; mean cosine 0.096493
- C2 to C5: 266 token edges; mean cosine 0.094770
- C0 to C8: 257 token edges; mean cosine 0.096827
- C1 to C7: 252 token edges; mean cosine 0.090700
- C1 to C6: 249 token edges; mean cosine 0.083888
- C2 to C3: 212 token edges; mean cosine 0.094838
- C5 to C7: 208 token edges; mean cosine 0.098695

### negative_tail

- Nodes: 2938
- Directed 10-NN edges: 29380
- Undirected edges: 19909
- Mean 10-NN cosine: 0.113182
- Communities: 10
- Modularity: 0.516139

Largest communities:

- C0 (n=522): representatives [␠circumstantial, ␠disproportionate, ␠unconstitutional, ␠recommendations, ␠encouragement, ␠downregulation, ␠discriminatory, asionally]; target-extreme [␠harsh, ␠uniforms, ␠exterior, ␠heavily, ␠affirmative]; token classes {'continuation_or_standalone': 153, 'whitespace': 1, 'word_initial': 368}
- C1 (n=475): representatives [␠Caroline, ␠Gh, ␠Laura, ␠Connie, ␠Sarah, ␠Tob, ␠Claire, ␠Tah]; target-extreme [␠Violet, ␠crypt, ocr, agg, ␠Chi]; token classes {'continuation_or_standalone': 187, 'punctuation_or_symbol': 20, 'target_lexical_variant': 2, 'whitespace': 3, 'word_initial': 263}
- C2 (n=380): representatives [␠Characteristics, Characteristics, ␠Configuration, ␠administrators, representation, mother, ␠administrator, ␠regulations]; target-extreme [crypt, ␠Uncle, individual, ␠characteristics, ␠specificity]; token classes {'continuation_or_standalone': 140, 'whitespace': 2, 'word_initial': 238}
- C3 (n=346): representatives [I, ␠or, ED, ra, ␠different, ␠WHAT, THIS, 28]; target-extreme [<empty>, ␠cette, ␠Une, ла, ␠ITS]; token classes {'continuation_or_standalone': 232, 'punctuation_or_symbol': 12, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 100}
- C4 (n=342): representatives [␠cardiovascular, ␠atherosclerotic, ␠cytokines, ␠cytokine, ␠macrophage, clerosis, ␠monocyte, IGF]; target-extreme [ottom, olith, ␠monocyte, ␠gluc, ␠Universe]; token classes {'continuation_or_standalone': 126, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 214}
- C5 (n=290): representatives [␠palace, ␠emperor, ␠Alabama, ␠king, ␠Constitution, ␠empire, ␠dragon, ␠terrace]; target-extreme [␠Beast, inois, ␠Ia, ␠conspiracy, ␠Interior]; token classes {'continuation_or_standalone': 71, 'word_initial': 219}
- C6 (n=274): representatives [␠automobiles, ␠trucks, ␠circumferential, ␠vegetables, ␠gravel, ␠pavement, ␠extremities, ␠furniture]; target-extreme [␠chop, ␠curb, ␠cassette, rors, ␠barrel]; token classes {'continuation_or_standalone': 52, 'whitespace': 2, 'word_initial': 220}
- C7 (n=129): representatives [␠TC, TG, GGT, ␠Rails, ␠USSR, ACC, ␠TG, ␠SSH]; target-extreme [CI, ␠SSH, ␠USSR, ␠LCD, ␠CPU]; token classes {'continuation_or_standalone': 69, 'target_lexical_variant': 1, 'word_initial': 59}

Strongest intercommunity connections:

- C0 to C2: 784 token edges; mean cosine 0.098842
- C1 to C3: 431 token edges; mean cosine 0.082265
- C0 to C3: 353 token edges; mean cosine 0.087846
- C0 to C6: 342 token edges; mean cosine 0.093116
- C0 to C4: 310 token edges; mean cosine 0.093854
- C1 to C4: 309 token edges; mean cosine 0.085396
- C1 to C5: 305 token edges; mean cosine 0.091815
- C2 to C4: 288 token edges; mean cosine 0.092236
- C2 to C5: 270 token edges; mean cosine 0.096172
- C0 to C1: 264 token edges; mean cosine 0.090504

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- mot (negative_tail) to Mot (positive_head): cosine 0.511479, combined-neighbour rank 1
- Mot (positive_head) to mot (negative_tail): cosine 0.511479, combined-neighbour rank 1
- ␠1978 (negative_tail) to ␠1977 (positive_head): cosine 0.463036, combined-neighbour rank 1
- ␠1977 (positive_head) to ␠1978 (negative_tail): cosine 0.463036, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠anest (positive_head) to ␠anesthesia (negative_tail): cosine 0.400689, combined-neighbour rank 1
- ␠anesthesia (negative_tail) to ␠anest (positive_head): cosine 0.400689, combined-neighbour rank 1

## State 18: block_17_output

### positive_head

- Nodes: 3015
- Directed 10-NN edges: 30150
- Undirected edges: 20455
- Mean 10-NN cosine: 0.119811
- Communities: 12
- Modularity: 0.518355

Largest communities:

- C0 (n=526): representatives [␠Manchester, Scott, ␠Hamburg, ␠Am, ␠Mitchell, ␠Karen, ␠Matt, ␠Josh]; target-extreme [Bab, sal, ␠Berlin, ␠beaut, ␠trans]; token classes {'continuation_or_standalone': 233, 'punctuation_or_symbol': 16, 'target_lexical_variant': 2, 'whitespace': 3, 'word_initial': 272}
- C1 (n=421): representatives [Food, ␠breastfeeding, ␠Hospit, ␠pneum, ␠psychiat, Fresh, ␠shoppers, ␠hospital]; target-extreme [␠peng, ␠recycled, ␠refres, ␠mars, ␠µm]; token classes {'continuation_or_standalone': 94, 'punctuation_or_symbol': 1, 'whitespace': 3, 'word_initial': 323}
- C2 (n=392): representatives [␠exploring, ␠entrepreneurs, ␠anticipated, ␠negotiating, ␠explores, ␠motivations, ␠yields, ␠motivation]; target-extreme [␠motivations, ␠stake, ␠informed, ␠debated, ␠dominant]; token classes {'continuation_or_standalone': 63, 'whitespace': 2, 'word_initial': 327}
- C3 (n=318): representatives [as, ␠at, ation, ating, ␠more, le, it, ine]; target-extreme [met, ␠Good, ausing, ours, done]; token classes {'continuation_or_standalone': 207, 'punctuation_or_symbol': 2, 'target_lexical_variant': 3, 'whitespace': 3, 'word_initial': 103}
- C4 (n=298): representatives [␠transformations, ␠determinations, ␠interactions, ␠Measurements, ␠characterizing, ␠Measurement, ␠size, ␠evolving]; target-extreme [␠interactions, ␠estim, Observ, ␠Measurements, pages]; token classes {'continuation_or_standalone': 116, 'whitespace': 3, 'word_initial': 179}
- C5 (n=292): representatives [}$;, $.[]{, $;, \}.$$, ␠.$$, $.\, \]., .[]{]; target-extreme [␠(), ␠@@, �, を, ое]; token classes {'continuation_or_standalone': 63, 'punctuation_or_symbol': 203, 'whitespace': 5, 'word_initial': 21}
- C6 (n=178): representatives [␠conversations, ␠filmmakers, ␠filmmaker, ␠Learning, ␠interviews, ␠photography, ␠interventions, Play]; target-extreme [Posted, ␠quoted, ␠Caption, ␠students, Thanks]; token classes {'continuation_or_standalone': 52, 'target_lexical_variant': 1, 'word_initial': 125}
- C7 (n=145): representatives [Notification, ␠browsers, ␠Firefox, Resolver, ␠animation, ␠travers, ␠Query, ␠NE]; target-extreme [␠travers, sizeof, Manager, ␠animated, EXPORT]; token classes {'continuation_or_standalone': 85, 'word_initial': 60}

Strongest intercommunity connections:

- C0 to C1: 501 token edges; mean cosine 0.089665
- C2 to C4: 468 token edges; mean cosine 0.098437
- C1 to C2: 417 token edges; mean cosine 0.092670
- C2 to C3: 361 token edges; mean cosine 0.098814
- C0 to C3: 333 token edges; mean cosine 0.094688
- C1 to C4: 295 token edges; mean cosine 0.093127
- C3 to C4: 281 token edges; mean cosine 0.098193
- C2 to C6: 270 token edges; mean cosine 0.099206
- C1 to C3: 260 token edges; mean cosine 0.089985
- C0 to C10: 238 token edges; mean cosine 0.083840

### negative_tail

- Nodes: 3291
- Directed 10-NN edges: 32910
- Undirected edges: 22357
- Mean 10-NN cosine: 0.116276
- Communities: 12
- Modularity: 0.530863

Largest communities:

- C0 (n=512): representatives [␠Characteristics, Characteristics, ␠administrators, ␠superintendent, ␠characteristics, ␠Configuration, ␠administrator, Configuration]; target-extreme [␠characteristics, ␠Characteristics, ␠variance, ␠exterior, ␠Interior]; token classes {'continuation_or_standalone': 166, 'whitespace': 3, 'word_initial': 343}
- C1 (n=424): representatives [␠Laura, ␠Emily, ␠Sarah, ␠Caroline, ␠Catherine, ␠Tah, ␠Connie, ␠Claire]; target-extreme [␠Violet, ␠Chi, heter, tetra, ␠Comp]; token classes {'continuation_or_standalone': 160, 'punctuation_or_symbol': 23, 'whitespace': 4, 'word_initial': 237}
- C2 (n=366): representatives [␠WHAT, ␠Gh, RA, TG, GH, ␠TC, ␠TG, GGT]; target-extreme [<empty>, crypt, ␠crypt, CI, agg]; token classes {'continuation_or_standalone': 216, 'target_lexical_variant': 2, 'whitespace': 4, 'word_initial': 144}
- C3 (n=349): representatives [␠circumstantial, ␠unconstitutional, ␠discriminatory, ␠circumstances, ␠incredible, ALLY, ␠jurisdictional, asionally]; target-extreme [␠affirmative, ␠harsh, gy, ␠heavily, ␠disadvantages]; token classes {'continuation_or_standalone': 86, 'whitespace': 1, 'word_initial': 262}
- C4 (n=335): representatives [␠cardiovascular, ␠cytokine, ␠atherosclerotic, ␠epidemiological, ␠cytokines, ␠macrophage, ␠archaeological, ␠interleukin]; target-extreme [ottom, olith, ␠monocyte, ␠cassette, ␠gluc]; token classes {'continuation_or_standalone': 136, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 196}
- C5 (n=326): representatives [␠downregulation, ␠prohibiting, ␠encourages, ␠resembled, ␠encouragement, ␠discour, received, ␠activate]; target-extreme [␠chop, rors, ␠enactment, ␠submit, clus]; token classes {'continuation_or_standalone': 93, 'punctuation_or_symbol': 1, 'word_initial': 232}
- C6 (n=269): representatives [␠grandmother, ␠Constitution, ␠palace, ␠emperor, mother, ␠church, ␠dragon, ␠Sultan]; target-extreme [␠Uncle, individual, ocr, ␠Ia, ␠Universe]; token classes {'continuation_or_standalone': 59, 'word_initial': 210}
- C7 (n=241): representatives [e, I, ', ␠or, ED, ␠said, ra, ␠different]; target-extreme [␠cette, ␠Une, ла, ocy, uple]; token classes {'continuation_or_standalone': 161, 'punctuation_or_symbol': 11, 'word_initial': 69}

Strongest intercommunity connections:

- C0 to C5: 557 token edges; mean cosine 0.102273
- C0 to C3: 481 token edges; mean cosine 0.102036
- C1 to C2: 403 token edges; mean cosine 0.090039
- C3 to C5: 394 token edges; mean cosine 0.098359
- C0 to C6: 337 token edges; mean cosine 0.101940
- C0 to C4: 334 token edges; mean cosine 0.094002
- C0 to C2: 280 token edges; mean cosine 0.087736
- C1 to C7: 280 token edges; mean cosine 0.082625
- C0 to C8: 265 token edges; mean cosine 0.097369
- C3 to C6: 244 token edges; mean cosine 0.101171

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- neum (negative_tail) to ␠pneum (positive_head): cosine 0.515575, combined-neighbour rank 1
- ␠pneum (positive_head) to neum (negative_tail): cosine 0.515575, combined-neighbour rank 1
- ␠1978 (negative_tail) to ␠1977 (positive_head): cosine 0.463036, combined-neighbour rank 1
- ␠1977 (positive_head) to ␠1978 (negative_tail): cosine 0.463036, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1

## State 19: block_18_output

### positive_head

- Nodes: 2967
- Directed 10-NN edges: 29670
- Undirected edges: 20076
- Mean 10-NN cosine: 0.120292
- Communities: 13
- Modularity: 0.510400

Largest communities:

- C0 (n=474): representatives [Scott, ␠Manchester, ␠Karen, ␠Matt, ␠Mitchell, ␠terrorists, ␠Hamburg, Emer]; target-extreme [Bab, sal, ␠Berlin, iy, RAW]; token classes {'continuation_or_standalone': 199, 'punctuation_or_symbol': 5, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 267}
- C1 (n=364): representatives [as, ␠at, ation, ating, ␠more, le, ine, it]; target-extreme [ое, ␠dominant, ו, ausing, ilation]; token classes {'continuation_or_standalone': 238, 'punctuation_or_symbol': 3, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 119}
- C2 (n=339): representatives [}$;, )$;, $;, $.[]{, ␠.$$, }},\, $.\, }=-\]; target-extreme [␠(), ␠@@, �, を, ■]; token classes {'continuation_or_standalone': 87, 'punctuation_or_symbol': 201, 'special': 1, 'whitespace': 10, 'word_initial': 40}
- C3 (n=311): representatives [␠exploring, ␠characterizing, ␠anticipated, ␠evolves, ␠discuss, ␠adventures, ␠explores, ␠development]; target-extreme [␠travers, ␠quoted, ␠stake, ␠debated, ␠recall]; token classes {'continuation_or_standalone': 51, 'whitespace': 1, 'word_initial': 259}
- C4 (n=281): representatives [␠transformations, ␠Measurements, ␠interactions, ␠sessions, ␠Measurement, ␠conversations, ␠quantification, ␠computations]; target-extreme [␠interactions, ␠motivations, Observ, ␠tension, tmp]; token classes {'continuation_or_standalone': 82, 'whitespace': 2, 'word_initial': 197}
- C5 (n=278): representatives [␠breastfeeding, ␠Hospit, ␠dexamethasone, ␠psychiat, ospit, ␠periodontal, ␠hospital, Medical]; target-extreme [␠trans, ␠µm, ␠tornado, ␠recycled, ␠fluores]; token classes {'continuation_or_standalone': 74, 'punctuation_or_symbol': 3, 'word_initial': 201}
- C6 (n=254): representatives [␠entrepreneurs, ␠filmmakers, Notification, ␠photography, ␠filmmaker, business, ␠Netflix, ␠pamph]; target-extreme [Posted, sizeof, ␠peng, Manager, ␠animated]; token classes {'continuation_or_standalone': 123, 'punctuation_or_symbol': 1, 'word_initial': 130}
- C7 (n=180): representatives [␠inev, ␠unavoid, ␠controvers, ␠regeneration, ␠unve, ␠maneu, ␠Philosoph, ␠reappe]; target-extreme [␠propri, ␠estim, ␠sket, ␠Wrest, ␠\n␠␠␠␠␠]; token classes {'continuation_or_standalone': 36, 'whitespace': 3, 'word_initial': 141}

Strongest intercommunity connections:

- C3 to C4: 410 token edges; mean cosine 0.104745
- C1 to C3: 373 token edges; mean cosine 0.103616
- C0 to C1: 356 token edges; mean cosine 0.092626
- C0 to C5: 318 token edges; mean cosine 0.086316
- C0 to C7: 281 token edges; mean cosine 0.085076
- C4 to C6: 279 token edges; mean cosine 0.094003
- C1 to C4: 261 token edges; mean cosine 0.095470
- C0 to C2: 201 token edges; mean cosine 0.080466
- C3 to C8: 199 token edges; mean cosine 0.099510
- C3 to C6: 199 token edges; mean cosine 0.099179

### negative_tail

- Nodes: 2669
- Directed 10-NN edges: 26690
- Undirected edges: 18087
- Mean 10-NN cosine: 0.111897
- Communities: 11
- Modularity: 0.520447

Largest communities:

- C0 (n=403): representatives [␠circumstantial, ␠unconstitutional, ␠circumstances, ␠encouragement, ␠Constitution, ␠discriminatory, asionally, ␠prohibiting]; target-extreme [␠affirmative, ␠enactment, ␠heavily, ␠disadvantages, ␠uncommon]; token classes {'continuation_or_standalone': 108, 'whitespace': 1, 'word_initial': 294}
- C1 (n=362): representatives [␠Characteristics, Characteristics, ␠recommendations, ␠downregulation, ␠Configuration, Configuration, ␠administrators, ␠characteristics]; target-extreme [␠characteristics, ␠Classic, ␠Characteristics, ␠variance, ␠physiology]; token classes {'continuation_or_standalone': 148, 'whitespace': 1, 'word_initial': 213}
- C2 (n=345): representatives [␠Laura, ␠Caroline, ␠Sarah, ␠Gh, ␠Catherine, ␠Claire, ␠Emily, ␠Connie]; target-extreme [␠Violet, heter, ␠crypt, agg, ␠Maur]; token classes {'continuation_or_standalone': 136, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 206}
- C3 (n=284): representatives [I, ␠or, ED, ra, ET, THIS, ␠different, 25]; target-extreme [<empty>, ␠cette, ␠Chi, gy, ␠ITS]; token classes {'continuation_or_standalone': 196, 'punctuation_or_symbol': 7, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 78}
- C4 (n=280): representatives [nsylvania, ␠palace, ␠cathedral, ␠Alabama, ␠grandmother, ␠emperor, ␠warriors, ␠archaeological]; target-extreme [␠Uncle, individual, ocr, ␠Ia, inois]; token classes {'continuation_or_standalone': 62, 'word_initial': 218}
- C5 (n=212): representatives [␠incredible, ␠disastrous, ␠unbelievable, ␠stupid, ␠brutal, ␠screamed, ␠frightening, ␠incompetent]; target-extreme [␠chop, esque, ␠harsh, ␠Beast, ␠supreme]; token classes {'continuation_or_standalone': 41, 'word_initial': 171}
- C6 (n=195): representatives [␠cardiovascular, ␠cytokine, ␠atherosclerotic, ␠interleukin, clerosis, ␠epidemiological, ␠erythrocytes, ␠supernatant]; target-extreme [olith, ␠monocyte, ␠gluc, teral, PLC]; token classes {'continuation_or_standalone': 83, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 110}
- C7 (n=194): representatives [␠trucks, ␠chassis, ␠cylinder, ␠automobiles, ␠roads, ␠vegetables, ␠gravel, ␠uniforms]; target-extreme [ottom, ␠curb, ␠exterior, ␠uniforms, ␠dishes]; token classes {'continuation_or_standalone': 39, 'word_initial': 155}

Strongest intercommunity connections:

- C0 to C1: 635 token edges; mean cosine 0.103591
- C0 to C5: 389 token edges; mean cosine 0.097931
- C2 to C3: 283 token edges; mean cosine 0.084170
- C1 to C4: 266 token edges; mean cosine 0.095982
- C2 to C4: 262 token edges; mean cosine 0.097289
- C2 to C8: 232 token edges; mean cosine 0.090871
- C0 to C3: 208 token edges; mean cosine 0.090600
- C1 to C7: 204 token edges; mean cosine 0.093824
- C1 to C6: 202 token edges; mean cosine 0.092858
- C0 to C4: 197 token edges; mean cosine 0.097444

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1
- ␠ek (positive_head) to ␠Ek (negative_tail): cosine 0.394657, combined-neighbour rank 1
- ␠Ek (negative_tail) to ␠ek (positive_head): cosine 0.394657, combined-neighbour rank 1

## State 20: block_19_output

### positive_head

- Nodes: 2727
- Directed 10-NN edges: 27270
- Undirected edges: 18470
- Mean 10-NN cosine: 0.119084
- Communities: 12
- Modularity: 0.509438

Largest communities:

- C0 (n=369): representatives [␠terrorists, ␠Manchester, Scott, ␠Matt, Peter, ␠Mitchell, ␠Kashmir, ␠Karen]; target-extreme [Bab, ␠Berlin, sal, ␠peng, Pen]; token classes {'continuation_or_standalone': 137, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'word_initial': 227}
- C1 (n=356): representatives [as, ation, ␠at, le, ine, ␠more, l, it]; target-extreme [tmp, ו, ausing, ␠vault, ilation]; token classes {'continuation_or_standalone': 234, 'punctuation_or_symbol': 3, 'target_lexical_variant': 1, 'word_initial': 118}
- C2 (n=285): representatives [␠filmmakers, ␠filmmaker, ␠Bitmap, ␠photography, ␠Netflix, Notification, ␠filming, ␠Animation]; target-extreme [Posted, sizeof, ␠Caption, Manager, ␠animated]; token classes {'continuation_or_standalone': 151, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 132}
- C3 (n=275): representatives [␠exploring, ␠entrepreneurs, ␠motivations, ␠motivation, ␠happiness, ␠anticipated, ␠explores, ␠discuss]; target-extreme [␠travers, ␠motivations, ␠stake, ␠dominant, ␠recall]; token classes {'continuation_or_standalone': 43, 'special': 1, 'whitespace': 1, 'word_initial': 230}
- C4 (n=263): representatives [␠breastfeeding, ␠psychiat, ␠Hospit, ␠Sleep, ␠dexamethasone, ␠biomed, Medical, ␠tumorigenesis]; target-extreme [␠beaut, ␠trans, ␠recycled, ␠tornado, ␠vice]; token classes {'continuation_or_standalone': 66, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 195}
- C5 (n=245): representatives [}).$$, }$;, ␠.$$, $.[]{, $;, $.\, .[]{, }$.]; target-extreme [␠(), ␠@@, �, を, ■]; token classes {'continuation_or_standalone': 45, 'punctuation_or_symbol': 181, 'whitespace': 5, 'word_initial': 14}
- C6 (n=221): representatives [␠inev, ␠Emer, ␠fres, Emer, ␠unve, ␠unavoid, ␠reappe, ␠Fres]; target-extreme [␠estim, RAW, ␠sket, ␠refres, ␠snar]; token classes {'continuation_or_standalone': 51, 'punctuation_or_symbol': 5, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 161}
- C7 (n=186): representatives [␠interactions, ␠Measurements, ␠characterizing, ␠Measurement, ␠evolves, ␠quantification, ␠recorded, ␠imaging]; target-extreme [␠interactions, ␠tension, Observ, ␠Measurements, ␠interaction]; token classes {'continuation_or_standalone': 39, 'whitespace': 3, 'word_initial': 144}

Strongest intercommunity connections:

- C0 to C4: 310 token edges; mean cosine 0.085491
- C0 to C1: 291 token edges; mean cosine 0.088285
- C0 to C6: 290 token edges; mean cosine 0.080412
- C1 to C3: 289 token edges; mean cosine 0.092128
- C3 to C7: 265 token edges; mean cosine 0.098033
- C1 to C2: 261 token edges; mean cosine 0.087242
- C4 to C6: 240 token edges; mean cosine 0.089676
- C3 to C6: 226 token edges; mean cosine 0.093422
- C1 to C7: 216 token edges; mean cosine 0.102496
- C4 to C7: 214 token edges; mean cosine 0.092169

### negative_tail

- Nodes: 2948
- Directed 10-NN edges: 29480
- Undirected edges: 19925
- Mean 10-NN cosine: 0.113391
- Communities: 11
- Modularity: 0.530266

Largest communities:

- C0 (n=577): representatives [␠Characteristics, ␠circumstantial, Characteristics, ␠downregulation, ␠recommendations, ␠unconstitutional, ␠encouragement, ␠Constitution]; target-extreme [crypt, individual, ␠affirmative, ␠Classic, ␠characteristics]; token classes {'continuation_or_standalone': 213, 'whitespace': 1, 'word_initial': 363}
- C1 (n=438): representatives [␠Gh, GH, ␠Rub, ␠Kh, ␠Rog, ␠Tob, ␠discour, ␠Tah]; target-extreme [␠crypt, heter, agg, gy, PROT]; token classes {'continuation_or_standalone': 180, 'punctuation_or_symbol': 29, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 227}
- C2 (n=398): representatives [I, ', ␠or, ED, ra, RA, ␠10, ␠WHAT]; target-extreme [<empty>, ␠cette, ␠Chi, CI, ␠ITS]; token classes {'continuation_or_standalone': 283, 'punctuation_or_symbol': 16, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 97}
- C3 (n=342): representatives [␠emperor, ␠trucks, ␠palace, ␠automobiles, ␠warriors, ␠chapel, ␠cathedral, ␠chassis]; target-extreme [ocr, ␠cassette, ␠Uncle, ␠curb, ␠USSR]; token classes {'continuation_or_standalone': 63, 'whitespace': 1, 'word_initial': 278}
- C4 (n=300): representatives [␠cardiovascular, ␠macrophage, ␠cytokines, ␠cytokine, ␠interleukin, ␠atherosclerotic, ␠circumferential, ␠epidemiological]; target-extreme [ottom, olith, ␠monocyte, teral, ␠gluc]; token classes {'continuation_or_standalone': 107, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 190}
- C5 (n=295): representatives [␠incredible, asionally, ␠stupid, ␠occasionally, ␠disastrous, ␠unbelievable, ␠brutal, ␠frightening]; target-extreme [␠chop, ␠uncommon, ␠therefrom, esque, ␠harsh]; token classes {'continuation_or_standalone': 73, 'word_initial': 222}
- C6 (n=243): representatives [nsylvania, ␠Sarah, ␠Laura, ␠Caroline, ␠Emily, Florida, ␠Alabama, ␠Florida]; target-extreme [␠Violet, inois, ␠Ia, abama, ␠Africans]; token classes {'continuation_or_standalone': 85, 'whitespace': 1, 'word_initial': 157}
- C7 (n=171): representatives [␠encourages, ␠prohibiting, ␠removing, ␠resembled, ␠Delete, ␠prohibited, ␠activates, ␠verifying]; target-extreme [rors, vee, ␠submit, ␠practicing, ␠preceded]; token classes {'continuation_or_standalone': 37, 'whitespace': 1, 'word_initial': 133}

Strongest intercommunity connections:

- C1 to C2: 499 token edges; mean cosine 0.085435
- C0 to C5: 470 token edges; mean cosine 0.099766
- C0 to C3: 455 token edges; mean cosine 0.095252
- C0 to C7: 435 token edges; mean cosine 0.103054
- C0 to C4: 407 token edges; mean cosine 0.094274
- C0 to C2: 316 token edges; mean cosine 0.087450
- C3 to C4: 302 token edges; mean cosine 0.094253
- C3 to C6: 296 token edges; mean cosine 0.099769
- C0 to C1: 276 token edges; mean cosine 0.091471
- C1 to C6: 274 token edges; mean cosine 0.087862

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1
- \]) (positive_head) to \])]{} (negative_tail): cosine 0.397660, combined-neighbour rank 1
- \])]{} (negative_tail) to \]) (positive_head): cosine 0.397660, combined-neighbour rank 1

## State 21: block_20_output

### positive_head

- Nodes: 2706
- Directed 10-NN edges: 27060
- Undirected edges: 18443
- Mean 10-NN cosine: 0.118216
- Communities: 12
- Modularity: 0.507473

Largest communities:

- C0 (n=435): representatives [␠Steve, Scott, ␠Matt, Peter, ␠Karen, ␠Josh, ␠Manchester, ␠Mitchell]; target-extreme [Bab, sal, ␠Berlin, ␠Kumar, ␠Krish]; token classes {'continuation_or_standalone': 174, 'punctuation_or_symbol': 10, 'target_lexical_variant': 2, 'whitespace': 6, 'word_initial': 243}
- C1 (n=345): representatives [as, ation, ␠at, le, ␠more, ine, l, it]; target-extreme [ilation, ␠Good, ausing, ␠viable, Got]; token classes {'continuation_or_standalone': 222, 'punctuation_or_symbol': 3, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 118}
- C2 (n=340): representatives [␠exploring, ␠Measurements, ␠characterizing, ␠quantification, ␠motivations, ␠Measurement, ␠anticipated, ␠recorded]; target-extreme [␠travers, ␠stake, ␠motivations, ␠dominant, ␠debated]; token classes {'continuation_or_standalone': 65, 'special': 1, 'word_initial': 274}
- C3 (n=298): representatives [␠interactions, ␠inev, ␠evolves, ␠unavoid, ␠unve, ␠evolving, ␠reappe, Rele]; target-extreme [␠recycled, ␠tension, ␠estim, ␠interactions, ␠sket]; token classes {'continuation_or_standalone': 67, 'punctuation_or_symbol': 3, 'whitespace': 4, 'word_initial': 224}
- C4 (n=276): representatives [␠breastfeeding, ␠dopaminergic, ␠psychiat, ␠Hospit, Medical, ␠immunostaining, ␠Biomed, ␠dexamethasone]; target-extreme [␠propri, ␠peng, ␠trans, ␠beaut, ␠tornado]; token classes {'continuation_or_standalone': 71, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 202}
- C5 (n=247): representatives [Food, ␠sessions, ␠entrepreneurs, ␠filmmakers, ␠interventions, ␠conversations, ␠shops, ␠negotiating]; target-extreme [␠quoted, ␠animated, director, ␠Wrest, ␠students]; token classes {'continuation_or_standalone': 53, 'word_initial': 194}
- C6 (n=246): representatives [}).$$, }$;, $.\, ␠.$$, $.[]{, $;, .[]{, .$$]; target-extreme [␠(), ␠@@, �, triangle, を]; token classes {'continuation_or_standalone': 56, 'punctuation_or_symbol': 169, 'whitespace': 5, 'word_initial': 16}
- C7 (n=172): representatives [␠photography, ␠facebook, Photo, ␠Netflix, Notification, ␠widths, Address, Position]; target-extreme [Posted, sizeof, ␠Caption, Manager, ajax]; token classes {'continuation_or_standalone': 112, 'word_initial': 60}

Strongest intercommunity connections:

- C1 to C2: 446 token edges; mean cosine 0.100122
- C2 to C3: 408 token edges; mean cosine 0.097198
- C0 to C1: 368 token edges; mean cosine 0.086142
- C2 to C5: 358 token edges; mean cosine 0.096675
- C0 to C4: 334 token edges; mean cosine 0.084260
- C0 to C3: 313 token edges; mean cosine 0.084842
- C3 to C4: 298 token edges; mean cosine 0.090457
- C1 to C3: 252 token edges; mean cosine 0.089470
- C4 to C5: 233 token edges; mean cosine 0.093534
- C3 to C5: 223 token edges; mean cosine 0.094168

### negative_tail

- Nodes: 3155
- Directed 10-NN edges: 31550
- Undirected edges: 21294
- Mean 10-NN cosine: 0.114645
- Communities: 11
- Modularity: 0.523512

Largest communities:

- C0 (n=580): representatives [␠Characteristics, Characteristics, ␠recommendations, ␠administrators, Configuration, ␠characteristics, ␠unconstitutional, ␠Configuration]; target-extreme [crypt, individual, ␠characteristics, ␠Classic, ␠uniforms]; token classes {'continuation_or_standalone': 211, 'whitespace': 2, 'word_initial': 367}
- C1 (n=407): representatives [I, ', ␠or, B, ED, ra, ␠said, ao]; target-extreme [␠Chi, ␠cette, ла, ␠Une, vee]; token classes {'continuation_or_standalone': 217, 'punctuation_or_symbol': 98, 'whitespace': 6, 'word_initial': 86}
- C2 (n=396): representatives [GH, Cl, RA, ␠Bra, ␠Gh, ␠Tob, Hu, ␠Tah]; target-extreme [<empty>, ocr, CI, ␠chop, ␠crypt]; token classes {'continuation_or_standalone': 196, 'punctuation_or_symbol': 1, 'target_lexical_variant': 3, 'whitespace': 1, 'word_initial': 195}
- C3 (n=303): representatives [␠downregulation, ␠removing, ␠encourages, ␠prohibiting, ␠resembled, ␠Delete, ␠creates, ␠prohibited]; target-extreme [␠therefrom, ␠enactment, ␠discour, ␠choked, ␠multiplied]; token classes {'continuation_or_standalone': 70, 'whitespace': 1, 'word_initial': 232}
- C4 (n=277): representatives [␠unreasonable, asionally, ␠disastrous, ␠incredible, ALLY, ␠occasionally, ␠stupid, ␠spectacular]; target-extreme [␠affirmative, ␠uncommon, esque, ␠excessive, ␠harsh]; token classes {'continuation_or_standalone': 79, 'whitespace': 1, 'word_initial': 197}
- C5 (n=271): representatives [␠trucks, ␠automobiles, ␠roads, ␠circumferential, ␠vegetables, ␠cylinder, ␠gravel, ␠pavement]; target-extreme [␠cassette, ␠curb, ␠rails, ␠Universe, ␠dishes]; token classes {'continuation_or_standalone': 61, 'whitespace': 1, 'word_initial': 209}
- C6 (n=246): representatives [nsylvania, ␠Laura, ␠Alabama, ␠Sarah, ␠Caroline, Florida, ␠Louisiana, ␠Florida]; target-extreme [inois, ␠Violet, ␠Ia, ␠Guardian, abama]; token classes {'continuation_or_standalone': 94, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 149}
- C7 (n=234): representatives [␠emperor, ␠bureaucracy, ␠palace, ␠chapel, ␠grandmother, ␠church, ␠Americans, mother]; target-extreme [ottom, ␠Uncle, ␠USSR, ␠conspiracy, orce]; token classes {'continuation_or_standalone': 43, 'word_initial': 191}

Strongest intercommunity connections:

- C0 to C3: 576 token edges; mean cosine 0.102639
- C1 to C2: 486 token edges; mean cosine 0.082458
- C0 to C4: 419 token edges; mean cosine 0.102141
- C0 to C5: 357 token edges; mean cosine 0.092837
- C0 to C7: 330 token edges; mean cosine 0.100807
- C3 to C4: 304 token edges; mean cosine 0.097984
- C0 to C8: 267 token edges; mean cosine 0.091873
- C2 to C6: 244 token edges; mean cosine 0.091254
- C0 to C2: 231 token edges; mean cosine 0.087555
- C6 to C7: 227 token edges; mean cosine 0.096216

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- ␠1978 (negative_tail) to ␠1977 (positive_head): cosine 0.463036, combined-neighbour rank 1
- ␠1977 (positive_head) to ␠1978 (negative_tail): cosine 0.463036, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1

## State 22: block_21_output

### positive_head

- Nodes: 2787
- Directed 10-NN edges: 27870
- Undirected edges: 18948
- Mean 10-NN cosine: 0.119253
- Communities: 11
- Modularity: 0.512516

Largest communities:

- C0 (n=507): representatives [␠exploring, ␠Measurements, ␠characterizing, ␠sessions, ␠interactions, ␠quantification, ␠navigating, ␠Measurement]; target-extreme [␠travers, ␠quoted, ␠stake, ␠motivations, ␠tension]; token classes {'continuation_or_standalone': 108, 'whitespace': 1, 'word_initial': 398}
- C1 (n=413): representatives [␠inev, ␠fres, Emer, ␠snar, Rew, ␠negot, ␠Emer, ␠unve]; target-extreme [␠propri, �, ␠estim, ␠trans, ␠beaut]; token classes {'continuation_or_standalone': 107, 'punctuation_or_symbol': 21, 'special': 1, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 281}
- C2 (n=345): representatives [as, ation, ␠at, le, ␠more, ine, l, it]; target-extreme [tmp, ilation, ␠Sort, ausing, Got]; token classes {'continuation_or_standalone': 237, 'punctuation_or_symbol': 3, 'target_lexical_variant': 2, 'whitespace': 5, 'word_initial': 98}
- C3 (n=300): representatives [Food, ␠Researchers, ␠entrepreneurs, ␠filmmakers, ␠photography, ␠Travel, ␠adventures, ␠filmmaker]; target-extreme [Posted, ␠peng, ␠Caption, ␠students, ␠animated]; token classes {'continuation_or_standalone': 87, 'word_initial': 213}
- C4 (n=252): representatives [␠Karen, Scott, ␠Matt, ␠Manchester, Peter, ␠Mitchell, Jay, ␠Jake]; target-extreme [Bab, ␠Berlin, sal, ␠Kumar, ␠Krish]; token classes {'continuation_or_standalone': 110, 'whitespace': 1, 'word_initial': 141}
- C5 (n=219): representatives [}).$$, }$;, $.[]{, }}=, ␠.$$, $.\, $;, .[]{]; target-extreme [␠@@, ␠(), triangle, を, ␠µm]; token classes {'continuation_or_standalone': 35, 'punctuation_or_symbol': 166, 'whitespace': 6, 'word_initial': 12}
- C6 (n=209): representatives [␠size, ␠widths, ␠Firefox, Address, ␠browsers, javase, Length, dialog]; target-extreme [sizeof, Manager, javase, ajax, mathchoice]; token classes {'continuation_or_standalone': 128, 'punctuation_or_symbol': 2, 'word_initial': 79}
- C7 (n=184): representatives [␠breastfeeding, ␠happiness, Baby, ␠dopaminergic, ␠dexamethasone, ␠psychiat, Medical, ␠tumorigenesis]; target-extreme [␠tornado, ␠hospital, ␠Lung, ␠soybean, ␠healthcare]; token classes {'continuation_or_standalone': 50, 'word_initial': 134}

Strongest intercommunity connections:

- C0 to C3: 541 token edges; mean cosine 0.100642
- C0 to C2: 515 token edges; mean cosine 0.099909
- C0 to C1: 384 token edges; mean cosine 0.097832
- C1 to C4: 359 token edges; mean cosine 0.083973
- C0 to C7: 292 token edges; mean cosine 0.097056
- C1 to C2: 260 token edges; mean cosine 0.082937
- C0 to C6: 259 token edges; mean cosine 0.096918
- C1 to C7: 249 token edges; mean cosine 0.089176
- C3 to C7: 234 token edges; mean cosine 0.097353
- C1 to C3: 229 token edges; mean cosine 0.087449

### negative_tail

- Nodes: 3188
- Directed 10-NN edges: 31880
- Undirected edges: 21499
- Mean 10-NN cosine: 0.114919
- Communities: 12
- Modularity: 0.524236

Largest communities:

- C0 (n=594): representatives [␠removing, ␠encourages, ␠encouragement, ␠unconstitutional, ␠prohibiting, ␠unbelievable, ␠resembled, ␠jurisdictional]; target-extreme [␠affirmative, ␠therefrom, ␠excessive, ␠Beast, esque]; token classes {'continuation_or_standalone': 133, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 458}
- C1 (n=525): representatives [␠Characteristics, Characteristics, ␠recommendations, ␠administrators, ␠characteristics, ␠Specific, ␠Configuration, ␠beneficiaries]; target-extreme [individual, ␠characteristics, ␠Classic, ␠uniforms, ␠variance]; token classes {'continuation_or_standalone': 213, 'whitespace': 2, 'word_initial': 310}
- C2 (n=368): representatives [GH, ␠Gh, ␠Bra, ␠Gu, Hu, ␠Kh, ␠TC, ␠Tah]; target-extreme [crypt, ␠Chi, CI, ␠chop, ␠crypt]; token classes {'continuation_or_standalone': 171, 'target_lexical_variant': 3, 'word_initial': 194}
- C3 (n=299): representatives [␠trucks, ␠automobiles, ␠pavement, ␠roads, ␠furniture, ␠gravel, ␠chassis, ␠firearms]; target-extreme [ottom, ␠cassette, ␠curb, ␠rails, ␠dishes]; token classes {'continuation_or_standalone': 70, 'whitespace': 2, 'word_initial': 227}
- C4 (n=271): representatives [␠downregulation, ␠cardiovascular, ␠macrophage, ␠cytokines, ␠cytokine, ␠interleukin, aphylococcus, ␠circumferential]; target-extreme [olith, ␠monocyte, teral, ␠gluc, phan]; token classes {'continuation_or_standalone': 114, 'target_lexical_variant': 1, 'word_initial': 156}
- C5 (n=256): representatives [I, ', B, ␠or, ED, ra, ability, ␠WHAT]; target-extreme [<empty>, ␠ITS, ALE, FORE, ␠block]; token classes {'continuation_or_standalone': 185, 'punctuation_or_symbol': 12, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 57}
- C6 (n=225): representatives [nsylvania, ␠Sarah, ␠Laura, ␠Alabama, ␠Caroline, Florida, ␠Florida, ␠Louisiana]; target-extreme [inois, ␠Violet, ␠Ia, abama, ␠Illinois]; token classes {'continuation_or_standalone': 77, 'word_initial': 148}
- C7 (n=219): representatives [␠cette, ␠خ, ␠questa, ␠или, ␠ق, خ, enza, ␠della]; target-extreme [␠cette, ␠Une, �, ла, ␠или]; token classes {'continuation_or_standalone': 125, 'punctuation_or_symbol': 29, 'whitespace': 4, 'word_initial': 61}

Strongest intercommunity connections:

- C0 to C1: 880 token edges; mean cosine 0.099098
- C1 to C3: 345 token edges; mean cosine 0.091986
- C1 to C4: 310 token edges; mean cosine 0.092697
- C0 to C3: 302 token edges; mean cosine 0.091578
- C2 to C5: 291 token edges; mean cosine 0.091929
- C1 to C5: 278 token edges; mean cosine 0.090945
- C0 to C8: 269 token edges; mean cosine 0.101981
- C2 to C7: 262 token edges; mean cosine 0.080042
- C1 to C2: 250 token edges; mean cosine 0.083611
- C0 to C2: 242 token edges; mean cosine 0.086076

### Secondary cross-side relations from R005

- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- ␠1978 (negative_tail) to ␠1977 (positive_head): cosine 0.463036, combined-neighbour rank 1
- ␠1977 (positive_head) to ␠1978 (negative_tail): cosine 0.463036, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1

## State 23: block_22_output

### positive_head

- Nodes: 3261
- Directed 10-NN edges: 32610
- Undirected edges: 22113
- Mean 10-NN cosine: 0.122941
- Communities: 13
- Modularity: 0.507777

Largest communities:

- C0 (n=523): representatives [␠Steve, ␠Matt, ␠Manchester, ␠Mitchell, ␠Karen, Scott, ␠Hamburg, ␠Pakistan]; target-extreme [Bab, ␠Berlin, sal, ␠propri, ␠peng]; token classes {'continuation_or_standalone': 230, 'punctuation_or_symbol': 3, 'special': 1, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 285}
- C1 (n=326): representatives [␠exploring, ␠characterizing, ␠sessions, ␠negotiating, ␠yields, ␠evolves, ␠conversations, ␠develops]; target-extreme [␠quoted, ␠travers, ␠INTRODUCTION, ␠debated, ␠Sort]; token classes {'continuation_or_standalone': 69, 'whitespace': 2, 'word_initial': 255}
- C2 (n=305): representatives [␠Measurements, ␠interactions, ␠quantification, ␠interventions, ␠Measurement, ␠computations, ␠renormalization, Examples]; target-extreme [␠motivations, ␠tension, ␠interactions, ␠example, emplo]; token classes {'continuation_or_standalone': 108, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 194}
- C3 (n=295): representatives [}).$$, }}=, }$;, $.[]{, $;, ␠.$$, \]., $.\]; target-extreme [␠(), ␠@@, triangle, �, を]; token classes {'continuation_or_standalone': 61, 'punctuation_or_symbol': 198, 'whitespace': 6, 'word_initial': 30}
- C4 (n=283): representatives [as, ation, ating, ␠at, ␠more, it, le, ine]; target-extreme [ilation, �, ו, ivated, met]; token classes {'continuation_or_standalone': 196, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 80}
- C5 (n=269): representatives [␠navigating, ␠size, Notification, Position, manager, ␠Writing, ␠score, ␠platforms]; target-extreme [sizeof, Manager, tmp, ajax, pages]; token classes {'continuation_or_standalone': 151, 'word_initial': 118}
- C6 (n=249): representatives [Food, ␠adventures, ␠happiness, ␠shops, ␠discomfort, ␠shopping, ␠fishing, ␠workshops]; target-extreme [␠recycled, ␠snar, ␠Wrest, space, ␠smiled]; token classes {'continuation_or_standalone': 43, 'whitespace': 2, 'word_initial': 204}
- C7 (n=246): representatives [␠dopaminergic, ␠breastfeeding, ␠tumorigenesis, ␠biomedical, Baby, ␠dexamethasone, ␠analges, ␠biomed]; target-extreme [␠tornado, ␠trans, ␠µm, ␠hospital, ␠Lung]; token classes {'continuation_or_standalone': 75, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 168}

Strongest intercommunity connections:

- C1 to C2: 388 token edges; mean cosine 0.104477
- C0 to C4: 351 token edges; mean cosine 0.094705
- C0 to C9: 341 token edges; mean cosine 0.082830
- C1 to C5: 277 token edges; mean cosine 0.099240
- C2 to C5: 271 token edges; mean cosine 0.092185
- C1 to C4: 263 token edges; mean cosine 0.103876
- C0 to C7: 258 token edges; mean cosine 0.092781
- C1 to C6: 249 token edges; mean cosine 0.098431
- C1 to C8: 242 token edges; mean cosine 0.101789
- C0 to C6: 232 token edges; mean cosine 0.088499

### negative_tail

- Nodes: 3275
- Directed 10-NN edges: 32750
- Undirected edges: 22213
- Mean 10-NN cosine: 0.115729
- Communities: 11
- Modularity: 0.528927

Largest communities:

- C0 (n=551): representatives [␠Laura, ␠Sarah, ␠Emily, ␠Gh, ␠Molly, ␠Connie, ␠Tah, GH]; target-extreme [CI, ␠chop, ␠Ia, ␠Violet, ␠Maur]; token classes {'continuation_or_standalone': 221, 'punctuation_or_symbol': 2, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 324}
- C1 (n=476): representatives [␠encourages, ␠prohibiting, ␠removing, asionally, ␠unreasonable, ␠Comprehensive, ␠encouragement, ␠Specific]; target-extreme [␠affirmative, individual, ␠uncommon, ␠therefrom, ␠discour]; token classes {'continuation_or_standalone': 132, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 341}
- C2 (n=429): representatives [e, I, ', ␠or, B, ized, ␠say, ra]; target-extreme [<empty>, ␠Chi, ␠cette, ␠или, ␠ITS]; token classes {'continuation_or_standalone': 287, 'punctuation_or_symbol': 21, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 118}
- C3 (n=315): representatives [␠downregulation, ␠cardiovascular, ␠macrophage, ␠cytokine, ␠interleukin, aphylococcus, ␠cytokines, ␠atherosclerotic]; target-extreme [olith, ottom, ␠monocyte, teral, tetra]; token classes {'continuation_or_standalone': 135, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 178}
- C4 (n=315): representatives [␠Characteristics, Characteristics, ␠recommendations, ability, ␠characteristics, ␠Configuration, ␠regulations, ␠Constitution]; target-extreme [crypt, ␠characteristics, ␠uniforms, heter, ␠crypt]; token classes {'continuation_or_standalone': 149, 'whitespace': 1, 'word_initial': 165}
- C5 (n=304): representatives [␠automobiles, ␠trucks, ␠vegetables, ␠furniture, ␠roads, ␠pavement, ␠chassis, ␠walls]; target-extreme [␠cassette, ␠curb, ␠rails, ␠dishes, vee]; token classes {'continuation_or_standalone': 75, 'whitespace': 1, 'word_initial': 228}
- C6 (n=289): representatives [␠administrators, ␠beneficiaries, ␠palace, ␠king, ␠warriors, ␠emperor, ␠chapel, ␠liberals]; target-extreme [ocr, ␠Classic, ␠USSR, ␠conspiracy, ␠Executive]; token classes {'continuation_or_standalone': 58, 'whitespace': 1, 'word_initial': 230}
- C7 (n=222): representatives [␠disastrous, ␠revolutionary, ␠spectacular, ␠incredible, ␠detrimental, ␠frightening, ␠unbelievable, ␠alarming]; target-extreme [esque, ␠Beast, ␠harsh, ␠insult, ␠supreme]; token classes {'continuation_or_standalone': 43, 'punctuation_or_symbol': 1, 'word_initial': 178}

Strongest intercommunity connections:

- C0 to C2: 543 token edges; mean cosine 0.090131
- C1 to C4: 512 token edges; mean cosine 0.102656
- C1 to C7: 407 token edges; mean cosine 0.102444
- C1 to C2: 335 token edges; mean cosine 0.096354
- C0 to C3: 286 token edges; mean cosine 0.088488
- C1 to C6: 276 token edges; mean cosine 0.099066
- C0 to C5: 273 token edges; mean cosine 0.092975
- C0 to C6: 272 token edges; mean cosine 0.092014
- C4 to C6: 267 token edges; mean cosine 0.096039
- C3 to C5: 258 token edges; mean cosine 0.091528

### Secondary cross-side relations from R005

- aiser (positive_head) to ␠Kaiser (negative_tail): cosine 0.564930, combined-neighbour rank 1
- ␠Kaiser (negative_tail) to aiser (positive_head): cosine 0.564930, combined-neighbour rank 1
- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- ␠1978 (negative_tail) to ␠1977 (positive_head): cosine 0.463036, combined-neighbour rank 1
- ␠1977 (positive_head) to ␠1978 (negative_tail): cosine 0.463036, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1

## State 24: block_23_output

### positive_head

- Nodes: 2883
- Directed 10-NN edges: 28830
- Undirected edges: 19561
- Mean 10-NN cosine: 0.119620
- Communities: 12
- Modularity: 0.502559

Largest communities:

- C0 (n=388): representatives [␠exploring, ␠characterizing, ␠anticipated, ␠predicting, ␠adventures, ␠resolving, ␠evolves, ␠happiness]; target-extreme [␠stake, ␠quoted, ␠travers, ␠motivations, ␠tension]; token classes {'continuation_or_standalone': 67, 'whitespace': 1, 'word_initial': 320}
- C1 (n=350): representatives [␠inev, ␠ik, ␠unve, ␠Interpret, ␠happ, ␠routes, ␠maneu, ␠FB]; target-extreme [␠propri, ое, ␠trans, ün, äm]; token classes {'continuation_or_standalone': 115, 'punctuation_or_symbol': 15, 'special': 1, 'whitespace': 2, 'word_initial': 217}
- C2 (n=329): representatives [as, ation, ␠at, le, ␠more, ine, l, am]; target-extreme [ilation, �, ␠Sort, ו, building]; token classes {'continuation_or_standalone': 231, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 90}
- C3 (n=274): representatives [␠Animation, ␠filmmaker, Training, ␠filmmakers, Play, ␠browsers, Notification, ␠videot]; target-extreme [Posted, sizeof, ␠estim, ␠INTRODUCTION, ␠Caption]; token classes {'continuation_or_standalone': 153, 'word_initial': 121}
- C4 (n=243): representatives [␠Karen, ␠Matt, ␠Mitchell, ␠Manchester, ␠Gary, ␠Josh, Scott, becca]; target-extreme [Bab, ␠Berlin, ␠Kumar, ␠Krish, iy]; token classes {'continuation_or_standalone': 92, 'target_lexical_variant': 2, 'word_initial': 149}
- C5 (n=240): representatives [$.[]{, }}=, }$;, $;, ␠.$$, }}=\, $.\, \].]; target-extreme [␠@@, ␠(), triangle, を, ■]; token classes {'continuation_or_standalone': 49, 'punctuation_or_symbol': 176, 'whitespace': 6, 'word_initial': 9}
- C6 (n=230): representatives [␠dopaminergic, ␠dexamethasone, ␠gravitational, Fresh, ␠tumorigenesis, ␠clinically, ␠regener, ␠fres]; target-extreme [sal, ␠recycled, ␠tornado, ␠refres, ␠µm]; token classes {'continuation_or_standalone': 67, 'punctuation_or_symbol': 1, 'whitespace': 3, 'word_initial': 159}
- C7 (n=220): representatives [␠Measurements, ␠size, ␠quantification, ␠Measurement, ␠interactions, results, ␠exempl, ␠computations]; target-extreme [emplo, ␠interactions, ␠example, ␠Measurements, ␠sket]; token classes {'continuation_or_standalone': 81, 'whitespace': 2, 'word_initial': 137}

Strongest intercommunity connections:

- C0 to C7: 390 token edges; mean cosine 0.104251
- C0 to C2: 370 token edges; mean cosine 0.096633
- C1 to C4: 331 token edges; mean cosine 0.082821
- C1 to C2: 291 token edges; mean cosine 0.080609
- C0 to C3: 260 token edges; mean cosine 0.094911
- C0 to C8: 257 token edges; mean cosine 0.101595
- C1 to C6: 241 token edges; mean cosine 0.085113
- C3 to C7: 234 token edges; mean cosine 0.097814
- C3 to C8: 222 token edges; mean cosine 0.094216
- C0 to C1: 220 token edges; mean cosine 0.088077

### negative_tail

- Nodes: 2620
- Directed 10-NN edges: 26200
- Undirected edges: 17663
- Mean 10-NN cosine: 0.111130
- Communities: 12
- Modularity: 0.514272

Largest communities:

- C0 (n=460): representatives [␠Gh, ␠TC, ␠discour, ␠gluc, ␠Gu, ␠Kh, CE, GH]; target-extreme [CI, ␠Chi, �, ␠chop, ␠discour]; token classes {'continuation_or_standalone': 217, 'punctuation_or_symbol': 27, 'target_lexical_variant': 3, 'whitespace': 6, 'word_initial': 207}
- C1 (n=378): representatives [Characteristics, ␠Characteristics, ␠recommendations, ␠Constitution, ␠administrators, ␠characteristics, ␠regulations, ␠administrator]; target-extreme [␠affirmative, ␠Classic, ␠characteristics, individual, ocr]; token classes {'continuation_or_standalone': 106, 'whitespace': 1, 'word_initial': 271}
- C2 (n=267): representatives [␠disastrous, asionally, ALLY, particularly, ␠unbelievable, ␠circumferential, ␠occasionally, ␠incredible]; target-extreme [␠uncommon, esque, ␠Beast, ␠complimentary, ␠excessive]; token classes {'continuation_or_standalone': 71, 'punctuation_or_symbol': 1, 'word_initial': 195}
- C3 (n=260): representatives [␠downregulation, ␠encourages, ␠encouragement, ␠prohibiting, ␠resembled, ␠activates, ␠participated, ␠prohibited]; target-extreme [crypt, ␠therefrom, vee, arant, ␠submit]; token classes {'continuation_or_standalone': 76, 'word_initial': 184}
- C4 (n=253): representatives [␠cardiovascular, ␠macrophage, ␠cytokine, ␠interleukin, aphylococcus, ␠erythrocytes, ␠atherosclerotic, clerosis]; target-extreme [olith, ␠monocyte, teral, ␠dishes, ␠vegetables]; token classes {'continuation_or_standalone': 103, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'word_initial': 148}
- C5 (n=199): representatives [nsylvania, ␠Laura, ␠Florida, Florida, ␠Louisiana, ␠Canada, ␠Alabama, ␠Sarah]; target-extreme [inois, ␠Ia, tetra, ␠Violet, Canada]; token classes {'continuation_or_standalone': 80, 'word_initial': 119}
- C6 (n=196): representatives [␠trucks, ␠automobiles, ␠roads, ␠pavement, ␠Mountains, ␠Rails, ␠terrace, ␠cylinder]; target-extreme [ottom, ␠curb, ␠cassette, ␠uniforms, ␠rails]; token classes {'continuation_or_standalone': 47, 'whitespace': 1, 'word_initial': 148}
- C7 (n=144): representatives [I, ', ␠or, ED, ra, ␠said, ␠M, RA]; target-extreme [<empty>, �, ␠_____, ston, �]; token classes {'continuation_or_standalone': 61, 'punctuation_or_symbol': 59, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 20}

Strongest intercommunity connections:

- C1 to C3: 371 token edges; mean cosine 0.098952
- C1 to C2: 369 token edges; mean cosine 0.097678
- C2 to C3: 324 token edges; mean cosine 0.093585
- C0 to C5: 292 token edges; mean cosine 0.086137
- C1 to C4: 278 token edges; mean cosine 0.090204
- C0 to C4: 275 token edges; mean cosine 0.084811
- C0 to C1: 209 token edges; mean cosine 0.081375
- C0 to C7: 205 token edges; mean cosine 0.086781
- C1 to C6: 202 token edges; mean cosine 0.091837
- C1 to C8: 194 token edges; mean cosine 0.095096

### Secondary cross-side relations from R005

- aiser (positive_head) to ␠Kaiser (negative_tail): cosine 0.564930, combined-neighbour rank 1
- ␠Kaiser (negative_tail) to aiser (positive_head): cosine 0.564930, combined-neighbour rank 1
- ␠Greek (negative_tail) to Greek (positive_head): cosine 0.531889, combined-neighbour rank 1
- Greek (positive_head) to ␠Greek (negative_tail): cosine 0.531889, combined-neighbour rank 1
- ␠1978 (negative_tail) to ␠1977 (positive_head): cosine 0.463036, combined-neighbour rank 1
- ␠1977 (positive_head) to ␠1978 (negative_tail): cosine 0.463036, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1

## State 25: block_24_output

### positive_head

- Nodes: 2713
- Directed 10-NN edges: 27130
- Undirected edges: 18413
- Mean 10-NN cosine: 0.118009
- Communities: 11
- Modularity: 0.498732

Largest communities:

- C0 (n=324): representatives [as, ation, ␠at, ␠more, le, ine, l, ␠into]; target-extreme [ilation, tmp, space, ␠\n␠␠␠␠␠, anie]; token classes {'continuation_or_standalone': 208, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'whitespace': 4, 'word_initial': 107}
- C1 (n=312): representatives [␠exploring, ␠resolving, ␠development, ␠anticipated, ␠evolves, ␠snar, ␠happiness, ␠builds]; target-extreme [␠travers, ␠recycled, ␠debated, ␠snar, ␠recall]; token classes {'continuation_or_standalone': 52, 'whitespace': 1, 'word_initial': 259}
- C2 (n=309): representatives [␠Karen, ␠Matt, ␠Mitchell, ␠Gary, ␠Josh, ␠Nam, ␠terrorists, ␠Bennett]; target-extreme [␠Berlin, ␠peng, ␠Kumar, ␠Krish, iy]; token classes {'continuation_or_standalone': 125, 'punctuation_or_symbol': 2, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 180}
- C3 (n=298): representatives [␠recorded, ␠filmmakers, ␠Writing, ␠filmmaker, PhysRev, ␠browsers, Notification, eLife]; target-extreme [Posted, ␠Caption, sizeof, ␠trans, Manager]; token classes {'continuation_or_standalone': 166, 'punctuation_or_symbol': 2, 'target_lexical_variant': 1, 'word_initial': 129}
- C4 (n=296): representatives [␠entrepreneurs, ␠negotiating, ␠sessions, ␠interventions, ␠adventures, ␠Hospit, business, ␠justification]; target-extreme [␠stake, ␠motivations, ␠hospital, ␠students, ␠tension]; token classes {'continuation_or_standalone': 60, 'word_initial': 236}
- C5 (n=291): representatives [␠inev, Fresh, ␠Interpret, ␠fres, ␠reappe, ␠regener, ␠Craw, ␠gener]; target-extreme [␠propri, sal, ␠refres, RAW, ␠estim]; token classes {'continuation_or_standalone': 93, 'punctuation_or_symbol': 12, 'whitespace': 3, 'word_initial': 183}
- C6 (n=245): representatives [␠Measurements, ␠characterizing, ␠quantification, ␠Measurement, Examples, ␠understanding, ␠exempl, ␠quantified]; target-extreme [␠quoted, triangle, ␠INTRODUCTION, emplo, ␠Measurements]; token classes {'continuation_or_standalone': 90, 'whitespace': 2, 'word_initial': 153}
- C7 (n=204): representatives [␠breastfeeding, Food, Baby, ␠dexamethasone, ␠dopaminergic, ␠periodontal, ␠Baby, ␠Ebola]; target-extreme [Bab, ␠tornado, ␠soybean, ␠salivary, ␠mitotic]; token classes {'continuation_or_standalone': 64, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 137}

Strongest intercommunity connections:

- C1 to C4: 439 token edges; mean cosine 0.098112
- C0 to C1: 323 token edges; mean cosine 0.098080
- C2 to C5: 317 token edges; mean cosine 0.081206
- C3 to C4: 282 token edges; mean cosine 0.092049
- C3 to C6: 272 token edges; mean cosine 0.092818
- C1 to C6: 266 token edges; mean cosine 0.100409
- C0 to C2: 251 token edges; mean cosine 0.086078
- C0 to C3: 244 token edges; mean cosine 0.088863
- C4 to C6: 242 token edges; mean cosine 0.099963
- C2 to C7: 241 token edges; mean cosine 0.087293

### negative_tail

- Nodes: 2699
- Directed 10-NN edges: 26990
- Undirected edges: 18162
- Mean 10-NN cosine: 0.111042
- Communities: 10
- Modularity: 0.520672

Largest communities:

- C0 (n=488): representatives [␠Gh, ␠TC, RA, ␠Tah, ␠Rh, GH, ␠Kh, ␠Lah]; target-extreme [<empty>, �, CI, crypt, ocr]; token classes {'continuation_or_standalone': 243, 'punctuation_or_symbol': 25, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 216}
- C1 (n=391): representatives [Characteristics, ␠Characteristics, ␠recommendations, ␠administrators, ␠jurisdictional, ␠characteristics, ␠Constitution, ␠beneficiaries]; target-extreme [ottom, ␠characteristics, ␠uniforms, ␠Classic, tetra]; token classes {'continuation_or_standalone': 131, 'whitespace': 2, 'word_initial': 258}
- C2 (n=361): representatives [␠Laura, ␠Florida, ␠warriors, ␠emperor, Florida, ␠church, ␠Canada, ␠Alabama]; target-extreme [inois, orce, ␠USSR, ␠Violet, Canada]; token classes {'continuation_or_standalone': 113, 'target_lexical_variant': 1, 'word_initial': 247}
- C3 (n=290): representatives [␠disastrous, ␠discour, ␠incredible, ␠discriminatory, ␠unbelievable, ␠brutal, ␠frightening, ␠inconsistent]; target-extreme [␠affirmative, ␠discour, esque, ␠Beast, ␠enh]; token classes {'continuation_or_standalone': 70, 'word_initial': 220}
- C4 (n=266): representatives [␠trucks, ␠automobiles, ␠Mountains, ␠roads, ␠terrace, ␠pavement, ␠cylinder, ␠Rails]; target-extreme [␠cassette, ␠dishes, ␠Ia, ␠curb, ␠rails]; token classes {'continuation_or_standalone': 59, 'whitespace': 2, 'word_initial': 205}
- C5 (n=258): representatives [␠downregulation, ␠encouragement, ␠Specific, asionally, ␠resembled, ␠prohibiting, ␠occasionally, ALLY]; target-extreme [individual, icated, ␠therefrom, arant, ␠uncommon]; token classes {'continuation_or_standalone': 85, 'word_initial': 173}
- C6 (n=215): representatives [␠cardiovascular, ␠macrophage, ␠cytokine, aphylococcus, ␠circumferential, ␠interleukin, ␠erythrocytes, ␠atherosclerotic]; target-extreme [olith, ␠monocyte, teral, ␠Diamond, clerosis]; token classes {'continuation_or_standalone': 90, 'target_lexical_variant': 1, 'word_initial': 124}
- C7 (n=173): representatives [', ␠or, ED, ␠said, ␠10, ␠M, 25, ra]; target-extreme [�, displaystyle, �, ␠_____, �]; token classes {'continuation_or_standalone': 62, 'punctuation_or_symbol': 75, 'target_lexical_variant': 1, 'whitespace': 5, 'word_initial': 30}

Strongest intercommunity connections:

- C1 to C5: 436 token edges; mean cosine 0.100867
- C0 to C2: 393 token edges; mean cosine 0.087433
- C3 to C5: 346 token edges; mean cosine 0.100028
- C1 to C2: 318 token edges; mean cosine 0.091907
- C0 to C8: 287 token edges; mean cosine 0.079048
- C1 to C3: 284 token edges; mean cosine 0.095582
- C1 to C4: 277 token edges; mean cosine 0.089133
- C0 to C4: 267 token edges; mean cosine 0.086545
- C0 to C1: 267 token edges; mean cosine 0.082957
- C2 to C4: 266 token edges; mean cosine 0.091276

### Secondary cross-side relations from R005

- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- \]) (positive_head) to \])]{} (negative_tail): cosine 0.397660, combined-neighbour rank 1
- \])]{} (negative_tail) to \]) (positive_head): cosine 0.397660, combined-neighbour rank 1
- Notification (positive_head) to notification (negative_tail): cosine 0.393724, combined-neighbour rank 1
- notification (negative_tail) to Notification (positive_head): cosine 0.393724, combined-neighbour rank 1
- ␠stairs (negative_tail) to ␠stair (positive_head): cosine 0.385155, combined-neighbour rank 1
- ␠stair (positive_head) to ␠stairs (negative_tail): cosine 0.385155, combined-neighbour rank 1
- ␠printed (negative_tail) to ␠printing (positive_head): cosine 0.371179, combined-neighbour rank 1
- ␠printing (positive_head) to ␠printed (negative_tail): cosine 0.371179, combined-neighbour rank 1

## State 26: block_25_output

### positive_head

- Nodes: 3005
- Directed 10-NN edges: 30050
- Undirected edges: 20430
- Mean 10-NN cosine: 0.120205
- Communities: 12
- Modularity: 0.508238

Largest communities:

- C0 (n=388): representatives [␠entrepreneurs, ␠Researchers, ␠adventures, ␠businesses, ␠negotiating, ␠conversations, ␠entrepreneur, ␠Hospit]; target-extreme [␠stake, ␠motivations, ␠hospital, ␠students, ␠beaut]; token classes {'continuation_or_standalone': 82, 'word_initial': 306}
- C1 (n=353): representatives [Food, ␠breastfeeding, ␠dopaminergic, ␠dexamethasone, Fresh, ␠analges, ␠psychosocial, ␠fluorescent]; target-extreme [␠refres, ␠recycled, RAW, ␠tornado, ␠µm]; token classes {'continuation_or_standalone': 90, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 260}
- C2 (n=337): representatives [as, ␠at, 3, ␠more, le, ine, ␠into, l]; target-extreme [triangle, ilation, leq, ines, ␠Sort]; token classes {'continuation_or_standalone': 210, 'punctuation_or_symbol': 3, 'target_lexical_variant': 4, 'whitespace': 2, 'word_initial': 118}
- C3 (n=324): representatives [␠Brian, ␠Steve, ␠Karen, ␠Matt, Baby, ␠terrorists, ␠Krish, ␠Rick]; target-extreme [Bab, ␠Berlin, ␠peng, sal, ␠Kumar]; token classes {'continuation_or_standalone': 128, 'punctuation_or_symbol': 2, 'word_initial': 194}
- C4 (n=306): representatives [␠inev, ␠discrep, Bre, ␠maneu, ␠disproportion, Rew, Jan, Feb]; target-extreme [␠propri, ␠trans, ое, ное, äm]; token classes {'continuation_or_standalone': 105, 'punctuation_or_symbol': 13, 'special': 1, 'whitespace': 4, 'word_initial': 183}
- C5 (n=273): representatives [␠size, ␠navigating, ␠Bitmap, Notification, Address, ␠Size, ␠browsers, ␠FB]; target-extreme [sizeof, Manager, tmp, space, ␠anchors]; token classes {'continuation_or_standalone': 151, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 120}
- C6 (n=254): representatives [␠characterizing, ␠quantification, ␠Measurements, ␠Measurement, ␠recorded, ␠exempl, ␠characterize, results]; target-extreme [␠tension, ␠Measurements, emplo, ␠example, ␠interactions]; token classes {'continuation_or_standalone': 76, 'whitespace': 1, 'word_initial': 177}
- C7 (n=246): representatives [}$;, }}=\, $.[]{, $.\, $;, \]., ␠.$$, }$.]; target-extreme [␠@@, ␠(), ■, ](, を]; token classes {'continuation_or_standalone': 45, 'punctuation_or_symbol': 182, 'whitespace': 6, 'word_initial': 13}

Strongest intercommunity connections:

- C0 to C1: 384 token edges; mean cosine 0.096366
- C0 to C6: 352 token edges; mean cosine 0.098552
- C3 to C4: 348 token edges; mean cosine 0.081741
- C1 to C3: 300 token edges; mean cosine 0.092497
- C0 to C8: 280 token edges; mean cosine 0.097849
- C1 to C4: 264 token edges; mean cosine 0.085037
- C2 to C5: 249 token edges; mean cosine 0.095270
- C2 to C8: 248 token edges; mean cosine 0.103592
- C1 to C6: 247 token edges; mean cosine 0.094653
- C1 to C2: 243 token edges; mean cosine 0.092614

### negative_tail

- Nodes: 3313
- Directed 10-NN edges: 33130
- Undirected edges: 22370
- Mean 10-NN cosine: 0.114820
- Communities: 12
- Modularity: 0.528336

Largest communities:

- C0 (n=639): representatives [␠discour, ␠Gh, ␠Rh, ␠Tah, ␠Rub, GH, ␠Kh, Hu]; target-extreme [<empty>, �, ␠Chi, crypt, tetra]; token classes {'continuation_or_standalone': 318, 'punctuation_or_symbol': 42, 'target_lexical_variant': 3, 'whitespace': 3, 'word_initial': 273}
- C1 (n=518): representatives [␠Characteristics, Characteristics, ␠downregulation, ␠recommendations, ␠administrators, ␠administrative, ␠characteristics, ␠Constitution]; target-extreme [␠affirmative, ␠characteristics, ␠uniforms, ␠Classic, ␠variance]; token classes {'continuation_or_standalone': 176, 'whitespace': 2, 'word_initial': 340}
- C2 (n=337): representatives [␠encourages, ␠resembled, ␠prohibiting, ␠removed, ␠activates, ␠prohibited, ␠created, ␠creates]; target-extreme [␠chop, ␠therefrom, icated, ␠submit, arant]; token classes {'continuation_or_standalone': 80, 'word_initial': 257}
- C3 (n=264): representatives [e, I, ized, ', ␠or, ED, ra, ␠said]; target-extreme [␠cette, ␠или, ла, ␠Une, ка]; token classes {'continuation_or_standalone': 169, 'punctuation_or_symbol': 4, 'target_lexical_variant': 1, 'word_initial': 90}
- C4 (n=262): representatives [␠emperor, ␠Sultan, ␠palace, ␠king, ␠warriors, ␠believers, ␠cathedral, ␠USSR]; target-extreme [␠USSR, orce, ␠Beast, ␠Uncle, ocrat]; token classes {'continuation_or_standalone': 65, 'word_initial': 197}
- C5 (n=257): representatives [␠trucks, ␠automobiles, ␠Rails, ␠cylinder, ␠furniture, ␠pavement, ␠decorative, ␠chassis]; target-extreme [ottom, ␠cassette, ␠dishes, ␠curb, ␠rails]; token classes {'continuation_or_standalone': 55, 'whitespace': 1, 'word_initial': 201}
- C6 (n=252): representatives [␠Florida, ␠Laura, Florida, ␠Alabama, ␠Sarah, ␠Louisiana, ␠Northwestern, ␠Minnesota]; target-extreme [␠Ia, ␠Violet, inois, ␠Interior, leans]; token classes {'continuation_or_standalone': 86, 'whitespace': 1, 'word_initial': 165}
- C7 (n=215): representatives [␠cardiovascular, ␠macrophage, ␠cytokine, ␠atherosclerotic, ␠cytokines, aphylococcus, ␠endothelium, ␠throm]; target-extreme [olith, ␠monocyte, teral, clerosis, ␠gluc]; token classes {'continuation_or_standalone': 82, 'target_lexical_variant': 1, 'word_initial': 132}

Strongest intercommunity connections:

- C1 to C2: 551 token edges; mean cosine 0.105226
- C0 to C3: 408 token edges; mean cosine 0.084732
- C0 to C6: 403 token edges; mean cosine 0.088654
- C1 to C4: 341 token edges; mean cosine 0.092787
- C0 to C1: 308 token edges; mean cosine 0.089649
- C0 to C7: 305 token edges; mean cosine 0.089056
- C1 to C5: 301 token edges; mean cosine 0.095170
- C1 to C7: 286 token edges; mean cosine 0.097606
- C1 to C8: 272 token edges; mean cosine 0.097649
- C4 to C6: 264 token edges; mean cosine 0.101536

### Secondary cross-side relations from R005

- aiser (positive_head) to ␠Kaiser (negative_tail): cosine 0.564930, combined-neighbour rank 1
- ␠Kaiser (negative_tail) to aiser (positive_head): cosine 0.564930, combined-neighbour rank 1
- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1
- ␠anesthesia (negative_tail) to ␠anesthetized (positive_head): cosine 0.412530, combined-neighbour rank 1
- ␠anesthetized (positive_head) to ␠anesthesia (negative_tail): cosine 0.412530, combined-neighbour rank 1

## State 27: block_26_output

### positive_head

- Nodes: 2894
- Directed 10-NN edges: 28940
- Undirected edges: 19618
- Mean 10-NN cosine: 0.119642
- Communities: 10
- Modularity: 0.508275

Largest communities:

- C0 (n=515): representatives [␠characterizing, ␠Measurements, ␠quantification, ␠testing, ␠recorded, ␠acquiring, ␠Measurement, ␠anticipated]; target-extreme [␠stake, ␠motivations, ␠trans, ␠estim, ␠funding]; token classes {'continuation_or_standalone': 118, 'whitespace': 5, 'word_initial': 392}
- C1 (n=432): representatives [␠Steve, ␠Matt, ␠terrorists, ␠Karen, ␠Gary, ␠Krish, ␠Nam, ␠Pakistan]; target-extreme [Bab, ␠Berlin, ␠Kumar, ␠peng, ␠Krish]; token classes {'continuation_or_standalone': 174, 'punctuation_or_symbol': 11, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 243}
- C2 (n=330): representatives [␠filmmakers, Notification, ␠filmmaker, ␠Photograph, Photo, ␠browsers, PhysRev, Reading]; target-extreme [Posted, ␠quoted, sizeof, ␠Caption, Manager]; token classes {'continuation_or_standalone': 197, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 130}
- C3 (n=321): representatives [as, ␠at, 3, ␠more, le, ine, am, ␠into]; target-extreme [triangle, ilation, ines, ␠at, leq]; token classes {'continuation_or_standalone': 213, 'punctuation_or_symbol': 7, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 98}
- C4 (n=303): representatives [␠breastfeeding, Food, Baby, ␠dopaminergic, ␠dexamethasone, ␠doxorubicin, ␠Baby, ␠Sleep]; target-extreme [sal, ␠recycled, ␠mitotic, ␠tornado, ␠µm]; token classes {'continuation_or_standalone': 67, 'punctuation_or_symbol': 1, 'special': 1, 'word_initial': 234}
- C5 (n=230): representatives [␠entrepreneurs, ␠entrepreneur, ␠businesses, ␠interventions, ␠Hospit, business, Medical, ␠shops]; target-extreme [␠hospital, ␠students, ␠travers, space, ␠Tours]; token classes {'continuation_or_standalone': 73, 'word_initial': 157}
- C6 (n=223): representatives [␠misunderstanding, ␠inev, ␠conversations, ␠unve, ␠negotiating, ␠reappe, ␠interviewing, ␠discussions]; target-extreme [␠propri, ␠beaut, ␠interviews, ␠Rew, ␠interviewing]; token classes {'continuation_or_standalone': 48, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 172}
- C7 (n=208): representatives [$.\, $;, }$;, \]., ␠.$$, $.[]{, }}=\, }$)]; target-extreme [␠@@, ␠(), ■, ](, を]; token classes {'continuation_or_standalone': 26, 'punctuation_or_symbol': 169, 'whitespace': 5, 'word_initial': 8}

Strongest intercommunity connections:

- C0 to C3: 478 token edges; mean cosine 0.099166
- C0 to C2: 453 token edges; mean cosine 0.097154
- C0 to C4: 444 token edges; mean cosine 0.095736
- C1 to C3: 367 token edges; mean cosine 0.088363
- C0 to C5: 363 token edges; mean cosine 0.095645
- C1 to C4: 354 token edges; mean cosine 0.086535
- C0 to C6: 346 token edges; mean cosine 0.094447
- C1 to C6: 295 token edges; mean cosine 0.083903
- C0 to C8: 280 token edges; mean cosine 0.095221
- C2 to C3: 258 token edges; mean cosine 0.095445

### negative_tail

- Nodes: 3120
- Directed 10-NN edges: 31200
- Undirected edges: 20972
- Mean 10-NN cosine: 0.113247
- Communities: 12
- Modularity: 0.516710

Largest communities:

- C0 (n=423): representatives [␠Sarah, ␠Laura, ␠Martha, ␠Connie, ␠Tah, ␠Gh, ␠Emily, ␠Ruth]; target-extreme [␠Chi, tetra, ␠Violet, clus, ␠Maur]; token classes {'continuation_or_standalone': 157, 'punctuation_or_symbol': 1, 'target_lexical_variant': 3, 'whitespace': 1, 'word_initial': 261}
- C1 (n=417): representatives [␠encourages, ␠discour, ␠prohibiting, ␠resembled, ␠created, ␠extremities, ␠creates, ␠activates]; target-extreme [␠chop, crypt, ␠discour, ␠submit, ␠multiplied]; token classes {'continuation_or_standalone': 102, 'whitespace': 1, 'word_initial': 314}
- C2 (n=364): representatives [Characteristics, ␠Characteristics, ␠downregulation, ␠recommendations, ␠administrators, ␠discriminatory, ␠Comprehensive, ␠regulations]; target-extreme [␠affirmative, ␠characteristics, ␠variance, ␠Classic, ␠Characteristics]; token classes {'continuation_or_standalone': 111, 'word_initial': 253}
- C3 (n=350): representatives [␠trucks, ␠automobiles, ␠agriculture, ␠furniture, ␠Mountains, ␠pavement, ␠chassis, ␠cylinder]; target-extreme [olith, ottom, ␠dishes, ␠uniforms, ␠cassette]; token classes {'continuation_or_standalone': 98, 'whitespace': 1, 'word_initial': 251}
- C4 (n=325): representatives [I, ␠or, ED, ␠M, ra, ars, ao, ␠или]; target-extreme [�, ␠cette, ␠или, heter, ла]; token classes {'continuation_or_standalone': 208, 'punctuation_or_symbol': 39, 'target_lexical_variant': 1, 'whitespace': 2, 'word_initial': 75}
- C5 (n=270): representatives [␠cardiovascular, ␠atherosclerotic, ␠circumferential, ␠macrophage, ␠cytokine, ␠malignancies, aphylococcus, ␠lipids]; target-extreme [␠monocyte, teral, clerosis, ␠thrombosis, ␠physiology]; token classes {'continuation_or_standalone': 118, 'word_initial': 152}
- C6 (n=233): representatives [␠emperor, ␠palace, ␠warriors, ␠USSR, ␠decorative, ␠church, ␠cathedral, ␠Africans]; target-extreme [orce, ␠USSR, ␠Beast, ␠conspiracy, ␠Uncle]; token classes {'continuation_or_standalone': 46, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 184}
- C7 (n=230): representatives [asionally, ␠spectacular, ␠incredibly, ␠incredible, ␠stupid, ␠Sometimes, ␠occasionally, ␠unreasonable]; target-extreme [␠therefrom, individual, esque, ␠uncommon, ␠complimentary]; token classes {'continuation_or_standalone': 69, 'whitespace': 2, 'word_initial': 159}

Strongest intercommunity connections:

- C1 to C2: 538 token edges; mean cosine 0.099452
- C0 to C4: 421 token edges; mean cosine 0.084312
- C1 to C7: 375 token edges; mean cosine 0.098172
- C1 to C3: 338 token edges; mean cosine 0.088606
- C2 to C5: 334 token edges; mean cosine 0.094828
- C2 to C3: 319 token edges; mean cosine 0.090796
- C0 to C3: 281 token edges; mean cosine 0.089281
- C0 to C8: 277 token edges; mean cosine 0.091499
- C2 to C6: 250 token edges; mean cosine 0.094899
- C3 to C5: 248 token edges; mean cosine 0.091108

### Secondary cross-side relations from R005

- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1
- Notification (positive_head) to notification (negative_tail): cosine 0.393724, combined-neighbour rank 1
- notification (negative_tail) to Notification (positive_head): cosine 0.393724, combined-neighbour rank 1
- ␠stairs (negative_tail) to ␠stair (positive_head): cosine 0.385155, combined-neighbour rank 1
- ␠stair (positive_head) to ␠stairs (negative_tail): cosine 0.385155, combined-neighbour rank 1

## State 28: block_27_output

### positive_head

- Nodes: 2792
- Directed 10-NN edges: 27920
- Undirected edges: 18999
- Mean 10-NN cosine: 0.118587
- Communities: 11
- Modularity: 0.516356

Largest communities:

- C0 (n=471): representatives [␠misunderstanding, ␠characterizing, ␠quantification, ␠Measurements, ␠testing, ␠characterize, ␠justification, ␠recorded]; target-extreme [␠stake, triangle, ␠motivations, ␠debated, ␠tension]; token classes {'continuation_or_standalone': 105, 'word_initial': 366}
- C1 (n=464): representatives [␠Matt, ␠Steve, ␠Brian, ␠terrorists, ␠Karen, Scott, Peter, ␠Bennett]; target-extreme [Bab, ␠Berlin, ␠Kumar, ␠propri, ␠Krish]; token classes {'continuation_or_standalone': 178, 'punctuation_or_symbol': 11, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 272}
- C2 (n=325): representatives [as, ation, ␠at, 3, ␠more, le, ine, ␠into]; target-extreme [ilation, ines, leq, ␠at, ו]; token classes {'continuation_or_standalone': 208, 'punctuation_or_symbol': 3, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 110}
- C3 (n=292): representatives [␠entrepreneurs, ␠conversations, ␠interventions, ␠entrepreneur, ␠negotiating, ␠businesses, ␠adventures, ␠filmmaker]; target-extreme [Posted, ␠quoted, ␠hospital, ␠students, ␠Caption]; token classes {'continuation_or_standalone': 91, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 198}
- C4 (n=288): representatives [␠breastfeeding, Baby, ␠neonates, ␠dexamethasone, Medical, ␠Baby, ␠analges, Fresh]; target-extreme [␠recycled, ␠refres, RAW, ␠salivary, ␠mitotic]; token classes {'continuation_or_standalone': 83, 'punctuation_or_symbol': 1, 'whitespace': 3, 'word_initial': 201}
- C5 (n=263): representatives [␠navigating, ␠size, Notification, ␠Search, ␠browsers, ␠widths, ␠Bitmap, ␠imaging]; target-extreme [sizeof, ␠travers, pages, ␠markup, tmp]; token classes {'continuation_or_standalone': 143, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 118}
- C6 (n=226): representatives [$;, $.[]{, }$;, $.\, \]., ␠.$$, }}=\, PhysRev]; target-extreme [␠@@, ␠(), ■, ](, _{\]; token classes {'continuation_or_standalone': 47, 'punctuation_or_symbol': 157, 'whitespace': 9, 'word_initial': 13}
- C7 (n=136): representatives [Food, ␠Sleep, ␠Draw, ␠snar, ␠discomfort, ␠camping, ␠kissing, ␠fishermen]; target-extreme [space, ␠patience, ␠smiled, ␠sket, ␠Tours]; token classes {'continuation_or_standalone': 22, 'word_initial': 114}

Strongest intercommunity connections:

- C0 to C3: 468 token edges; mean cosine 0.099984
- C0 to C2: 445 token edges; mean cosine 0.103870
- C1 to C4: 363 token edges; mean cosine 0.084878
- C0 to C4: 355 token edges; mean cosine 0.094931
- C0 to C5: 335 token edges; mean cosine 0.093118
- C1 to C2: 332 token edges; mean cosine 0.092835
- C3 to C5: 252 token edges; mean cosine 0.091449
- C1 to C3: 231 token edges; mean cosine 0.087292
- C2 to C5: 216 token edges; mean cosine 0.090504
- C0 to C7: 209 token edges; mean cosine 0.099309

### negative_tail

- Nodes: 2730
- Directed 10-NN edges: 27300
- Undirected edges: 18289
- Mean 10-NN cosine: 0.110793
- Communities: 10
- Modularity: 0.522560

Largest communities:

- C0 (n=475): representatives [Characteristics, ␠downregulation, ␠Characteristics, ␠recommendations, ␠characteristics, ␠regulations, ␠upregulation, ␠administrators]; target-extreme [␠characteristics, ottom, ␠affirmative, ␠Characteristics, ␠Classic]; token classes {'continuation_or_standalone': 141, 'word_initial': 334}
- C1 (n=429): representatives [asionally, ␠incredible, ␠prohibiting, ␠Sometimes, ␠spectacular, ␠disastrous, ␠resembled, ␠incred]; target-extreme [␠therefrom, esque, ␠submit, clus, ␠tho]; token classes {'continuation_or_standalone': 117, 'whitespace': 2, 'word_initial': 310}
- C2 (n=417): representatives [␠or, ED, ␠10, ars, ao, RA, ERS, ities]; target-extreme [␠Chi, ␠или, <empty>, ␠cette, ␠chop]; token classes {'continuation_or_standalone': 298, 'punctuation_or_symbol': 7, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 108}
- C3 (n=344): representatives [␠Tah, ␠Rh, ␠Gh, ␠Maur, ␠discour, ␠Gu, ␠rh, ␠Kh]; target-extreme [�, tetra, crypt, ␠Maur, ␠enh]; token classes {'continuation_or_standalone': 120, 'punctuation_or_symbol': 20, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 201}
- C4 (n=259): representatives [␠trucks, ␠automobiles, ␠cylinder, ␠Mountains, ␠pavement, ␠walls, ␠roads, ␠agriculture]; target-extreme [␠dishes, ␠uniforms, ␠curb, ␠cassette, rors]; token classes {'continuation_or_standalone': 57, 'whitespace': 3, 'word_initial': 199}
- C5 (n=216): representatives [␠cardiovascular, ␠macrophage, ␠malignancies, ␠atherosclerotic, ␠cytokine, ␠extremities, clerosis, ␠lymphocytes]; target-extreme [olith, ␠monocyte, clerosis, teral, ␠oxides]; token classes {'continuation_or_standalone': 82, 'punctuation_or_symbol': 1, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 131}
- C6 (n=206): representatives [␠emperor, ␠warriors, ␠goddess, ␠cathedral, ␠dragon, ␠church, ␠believers, ␠rituals]; target-extreme [␠Beast, ␠rituals, orce, ␠USSR, ␠conspiracy]; token classes {'continuation_or_standalone': 45, 'word_initial': 161}
- C7 (n=180): representatives [␠Alabama, ␠Sarah, ␠Laura, ␠Martha, Florida, ␠Florida, ␠Emily, ␠Mexico]; target-extreme [␠Ia, Canada, ␠Violet, inois, leans]; token classes {'continuation_or_standalone': 61, 'word_initial': 119}

Strongest intercommunity connections:

- C0 to C1: 674 token edges; mean cosine 0.099024
- C2 to C3: 539 token edges; mean cosine 0.087152
- C0 to C4: 380 token edges; mean cosine 0.089961
- C1 to C2: 312 token edges; mean cosine 0.089781
- C0 to C2: 286 token edges; mean cosine 0.089520
- C0 to C5: 279 token edges; mean cosine 0.095288
- C0 to C6: 256 token edges; mean cosine 0.092441
- C3 to C5: 225 token edges; mean cosine 0.086060
- C6 to C7: 207 token edges; mean cosine 0.098826
- C4 to C6: 205 token edges; mean cosine 0.095249

### Secondary cross-side relations from R005

- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1
- Notification (positive_head) to notification (negative_tail): cosine 0.393724, combined-neighbour rank 1
- notification (negative_tail) to Notification (positive_head): cosine 0.393724, combined-neighbour rank 1
- ␠stairs (negative_tail) to ␠stair (positive_head): cosine 0.385155, combined-neighbour rank 1
- ␠stair (positive_head) to ␠stairs (negative_tail): cosine 0.385155, combined-neighbour rank 1

## State 29: block_28_output

### positive_head

- Nodes: 3105
- Directed 10-NN edges: 31050
- Undirected edges: 21163
- Mean 10-NN cosine: 0.122108
- Communities: 9
- Modularity: 0.513464

Largest communities:

- C0 (n=486): representatives [␠quantification, ␠conversations, ␠characterizing, ␠Measurements, ␠Measurement, ␠testing, ␠recorded, ␠evolves]; target-extreme [␠quoted, ␠motivations, ␠tension, ␠Measurements, ␠debated]; token classes {'continuation_or_standalone': 105, 'punctuation_or_symbol': 2, 'word_initial': 379}
- C1 (n=464): representatives [␠Brian, ␠Steve, ␠Karen, ␠Matt, ␠Jay, Peter, ␠Mumbai, Scott]; target-extreme [Bab, ␠Kumar, ␠Krish, ␠Berlin, ␠peng]; token classes {'continuation_or_standalone': 180, 'punctuation_or_symbol': 3, 'target_lexical_variant': 1, 'whitespace': 3, 'word_initial': 277}
- C2 (n=428): representatives [␠misunderstanding, ␠inev, ␠unpredict, ␠immunostaining, ␠analges, ␠antidepress, ␠dopaminergic, ␠renormalization]; target-extreme [␠propri, ␠trans, ␠salivary, ␠mitotic, ␠tornado]; token classes {'continuation_or_standalone': 108, 'punctuation_or_symbol': 2, 'special': 1, 'whitespace': 5, 'word_initial': 312}
- C3 (n=426): representatives [␠entrepreneurs, Food, business, ␠businesses, ␠interventions, ␠filmmakers, ␠entrepreneur, ␠constructions]; target-extreme [Posted, ␠hospital, ␠recycled, ␠Caption, ␠students]; token classes {'continuation_or_standalone': 116, 'punctuation_or_symbol': 1, 'word_initial': 309}
- C4 (n=392): representatives [as, ation, ␠at, 3, ␠more, ating, le, ␠all]; target-extreme [␠at, leq, ilation, ines, Got]; token classes {'continuation_or_standalone': 238, 'punctuation_or_symbol': 3, 'target_lexical_variant': 2, 'whitespace': 3, 'word_initial': 146}
- C5 (n=258): representatives [␠breastfeeding, Baby, ␠Baby, ␠suitably, ␠less, ␠baby, ␠surprisingly, Fresh]; target-extreme [␠stake, ␠refres, RAW, ␠informed, boy]; token classes {'continuation_or_standalone': 83, 'target_lexical_variant': 1, 'word_initial': 174}
- C6 (n=257): representatives [}$;, $.[]{, $;, }}=\, ␠.$$, $.\, \]., }=]; target-extreme [␠@@, triangle, ](, ␠](, ■]; token classes {'continuation_or_standalone': 56, 'punctuation_or_symbol': 177, 'whitespace': 5, 'word_initial': 19}
- C7 (n=246): representatives [Length, ␠Bitmap, Notification, manager, ␠browsers, ␠resolving, buffer, Position]; target-extreme [sizeof, Manager, tmp, ␠markup, DATA]; token classes {'continuation_or_standalone': 153, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 90}

Strongest intercommunity connections:

- C0 to C3: 696 token edges; mean cosine 0.098206
- C0 to C2: 610 token edges; mean cosine 0.099304
- C0 to C4: 530 token edges; mean cosine 0.098597
- C1 to C2: 462 token edges; mean cosine 0.086178
- C2 to C3: 426 token edges; mean cosine 0.092426
- C1 to C4: 343 token edges; mean cosine 0.088540
- C1 to C3: 327 token edges; mean cosine 0.087550
- C0 to C5: 317 token edges; mean cosine 0.098932
- C0 to C7: 310 token edges; mean cosine 0.093944
- C4 to C5: 304 token edges; mean cosine 0.105115

### negative_tail

- Nodes: 2918
- Directed 10-NN edges: 29180
- Undirected edges: 19577
- Mean 10-NN cosine: 0.111232
- Communities: 12
- Modularity: 0.518074

Largest communities:

- C0 (n=545): representatives [␠Sarah, ␠Gu, ␠Tah, ␠Gh, ␠Emily, ␠Michelle, ao, ␠Martha]; target-extreme [�, ␠Chi, ␠chop, clus, ␠Violet]; token classes {'continuation_or_standalone': 228, 'punctuation_or_symbol': 18, 'target_lexical_variant': 3, 'whitespace': 2, 'word_initial': 294}
- C1 (n=535): representatives [Characteristics, ␠downregulation, ␠Characteristics, ␠recommendations, ifferences, ␠consequences, ␠regulations, ␠upregulation]; target-extreme [␠characteristics, ␠affirmative, crypt, ␠uniforms, BLOCK]; token classes {'continuation_or_standalone': 188, 'whitespace': 4, 'word_initial': 343}
- C2 (n=484): representatives [ALLY, ␠ridiculous, ␠disastrous, ␠incredible, ␠discour, ␠prohibiting, ␠Sometimes, ␠incredibly]; target-extreme [esque, gy, ␠submit, ␠discour, ␠therefrom]; token classes {'continuation_or_standalone': 129, 'punctuation_or_symbol': 1, 'word_initial': 354}
- C3 (n=297): representatives [␠automobiles, ars, ␠trucks, ␠cylinder, ␠Mountains, ␠vegetables, ␠agriculture, ␠vegetation]; target-extreme [ottom, ␠dishes, rors, ␠rails, ␠curb]; token classes {'continuation_or_standalone': 81, 'whitespace': 2, 'word_initial': 214}
- C4 (n=224): representatives [␠cardiovascular, ␠atherosclerotic, ␠macrophage, ␠malignancies, ␠cytokine, ␠gluc, ␠antioxidants, ␠circumferential]; target-extreme [olith, tetra, ␠monocyte, clerosis, teral]; token classes {'continuation_or_standalone': 94, 'target_lexical_variant': 2, 'word_initial': 128}
- C5 (n=223): representatives [␠dragon, ␠emperor, ␠palace, ␠empire, ␠church, ␠kingdom, ␠warriors, ␠cathedral]; target-extreme [␠Beast, ␠rituals, orce, ␠Interior, ␠USSR]; token classes {'continuation_or_standalone': 50, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 171}
- C6 (n=220): representatives [␠cette, ␠или, ␠خ, ␠NEVER, ␠questa, ␠ق, ana, ␠doesnt]; target-extreme [␠или, ␠cette, ла, ␠Une, ␠tho]; token classes {'continuation_or_standalone': 125, 'punctuation_or_symbol': 12, 'whitespace': 1, 'word_initial': 82}
- C7 (n=109): representatives [␠or, }}}_, ]}, ]),, \])]{}, )}+, ␠M, '])]; target-extreme [displaystyle, ␠_____, ␠%), *(*, ␠{$]; token classes {'continuation_or_standalone': 12, 'punctuation_or_symbol': 89, 'whitespace': 5, 'word_initial': 3}

Strongest intercommunity connections:

- C1 to C2: 803 token edges; mean cosine 0.099966
- C1 to C3: 422 token edges; mean cosine 0.091027
- C0 to C6: 364 token edges; mean cosine 0.079637
- C0 to C2: 328 token edges; mean cosine 0.088389
- C0 to C1: 307 token edges; mean cosine 0.083331
- C0 to C4: 305 token edges; mean cosine 0.086856
- C1 to C5: 300 token edges; mean cosine 0.091900
- C0 to C3: 293 token edges; mean cosine 0.094043
- C2 to C3: 284 token edges; mean cosine 0.091299
- C1 to C4: 266 token edges; mean cosine 0.093122

### Secondary cross-side relations from R005

- chr (positive_head) to ␠chr (negative_tail): cosine 0.456221, combined-neighbour rank 1
- ␠chr (negative_tail) to chr (positive_head): cosine 0.456221, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- ␠raised (negative_tail) to ␠raising (positive_head): cosine 0.413591, combined-neighbour rank 1
- ␠raising (positive_head) to ␠raised (negative_tail): cosine 0.413591, combined-neighbour rank 1
- \]) (positive_head) to \])]{} (negative_tail): cosine 0.397660, combined-neighbour rank 1
- \])]{} (negative_tail) to \]) (positive_head): cosine 0.397660, combined-neighbour rank 1
- Notification (positive_head) to notification (negative_tail): cosine 0.393724, combined-neighbour rank 1
- notification (negative_tail) to Notification (positive_head): cosine 0.393724, combined-neighbour rank 1

## State 30: block_29_output

### positive_head

- Nodes: 2887
- Directed 10-NN edges: 28870
- Undirected edges: 19723
- Mean 10-NN cosine: 0.120762
- Communities: 11
- Modularity: 0.518586

Largest communities:

- C0 (n=475): representatives [␠Steve, ␠Matt, Scott, Peter, ␠Karen, ␠Mik, ␠unw, ␠Pakistan]; target-extreme [␠Krish, sal, ␠Kumar, ␠Berlin, ␠peng]; token classes {'continuation_or_standalone': 195, 'punctuation_or_symbol': 9, 'whitespace': 2, 'word_initial': 269}
- C1 (n=377): representatives [␠characterizing, ␠conversations, ␠introducing, ␠acquiring, ␠development, ␠discussion, ␠characterizes, ␠justification]; target-extreme [␠quoted, ␠motivations, ␠travers, ␠debated, ␠informed]; token classes {'continuation_or_standalone': 59, 'whitespace': 2, 'word_initial': 316}
- C2 (n=346): representatives [as, ␠(, ation, ␠at, 3, ␠more, ating, le]; target-extreme [triangle, ␠propri, ␠at, DATA, ו]; token classes {'continuation_or_standalone': 198, 'punctuation_or_symbol': 5, 'target_lexical_variant': 2, 'whitespace': 1, 'word_initial': 140}
- C3 (n=342): representatives [␠entrepreneurs, ␠businesses, ␠filmmakers, ␠recorded, business, ␠entrepreneur, ␠organisations, student]; target-extreme [␠stake, ␠hospital, ␠students, pages, ␠Business]; token classes {'continuation_or_standalone': 95, 'word_initial': 247}
- C4 (n=318): representatives [␠breastfeeding, Food, ␠immunostaining, Baby, ␠phenomenological, ␠dopaminergic, ␠kissing, ␠renormalization]; target-extreme [Bab, ␠refres, ␠tension, ␠µm, RAW]; token classes {'continuation_or_standalone': 86, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 230}
- C5 (n=248): representatives [␠Measurements, ␠Measurement, ␠quantification, ␠constructions, ␠transformation, ␠regularization, detection, results]; target-extreme [␠recycled, tmp, Manager, ␠Measurements, ␠measured]; token classes {'continuation_or_standalone': 128, 'word_initial': 120}
- C6 (n=234): representatives [}$;, $;, ␠.$$, }}=\, $.\, $.[]{, \]., }=]; target-extreme [␠@@, sizeof, ](, ■, _{\]; token classes {'continuation_or_standalone': 57, 'punctuation_or_symbol': 158, 'whitespace': 5, 'word_initial': 14}
- C7 (n=145): representatives [␠Photograph, ␠Firefox, Photo, ␠browsers, ␠Bitmap, Bio, ␠Biomed, ␠DB]; target-extreme [Posted, ␠Caption, ␠Photo, ajax, ␠markup]; token classes {'continuation_or_standalone': 59, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 84}

Strongest intercommunity connections:

- C1 to C2: 437 token edges; mean cosine 0.106211
- C1 to C3: 432 token edges; mean cosine 0.097163
- C1 to C5: 378 token edges; mean cosine 0.105067
- C0 to C2: 341 token edges; mean cosine 0.090803
- C3 to C4: 339 token edges; mean cosine 0.094104
- C0 to C4: 326 token edges; mean cosine 0.086892
- C1 to C4: 302 token edges; mean cosine 0.096306
- C2 to C5: 297 token edges; mean cosine 0.098276
- C0 to C3: 273 token edges; mean cosine 0.089296
- C3 to C5: 255 token edges; mean cosine 0.095562

### negative_tail

- Nodes: 2741
- Directed 10-NN edges: 27410
- Undirected edges: 18331
- Mean 10-NN cosine: 0.109951
- Communities: 12
- Modularity: 0.515817

Largest communities:

- C0 (n=472): representatives [␠prohibiting, ␠ridiculous, asionally, ␠resembled, ␠disastrous, ␠ruins, ␠Sometimes, ␠detrimental]; target-extreme [esque, rors, ␠therefrom, ␠submit, clus]; token classes {'continuation_or_standalone': 118, 'word_initial': 354}
- C1 (n=469): representatives [␠Tah, ␠discour, ␠Gh, Hu, ␠Gu, ␠Rh, ␠M, Th]; target-extreme [olith, ␠Chi, tetra, <empty>, CI]; token classes {'continuation_or_standalone': 210, 'punctuation_or_symbol': 2, 'target_lexical_variant': 5, 'whitespace': 1, 'word_initial': 251}
- C2 (n=405): representatives [Characteristics, ␠Characteristics, ␠recommendations, ␠regulations, ␠encouragement, ␠Constitution, ␠Specific, representation]; target-extreme [␠characteristics, ␠affirmative, ␠Characteristics, heter, ␠variance]; token classes {'continuation_or_standalone': 122, 'whitespace': 1, 'word_initial': 282}
- C3 (n=287): representatives [␠circumferential, ␠trucks, ␠automobiles, ␠cylinder, ␠gravel, ars, ␠Mountains, ␠vegetation]; target-extreme [ottom, ␠dishes, ␠caramel, ␠uniforms, BLOCK]; token classes {'continuation_or_standalone': 78, 'target_lexical_variant': 1, 'whitespace': 1, 'word_initial': 207}
- C4 (n=222): representatives [␠Sarah, ␠Laura, ␠Alabama, ␠Louisiana, ␠Martha, ␠Michelle, ␠Canada, ␠Florida]; target-extreme [␠Ia, ␠Violet, inois, ␠Gates, leans]; token classes {'continuation_or_standalone': 94, 'word_initial': 128}
- C5 (n=216): representatives [␠dragon, ␠warriors, ␠emperor, ␠cathedral, ␠Colonial, ␠USSR, ␠Universe, ␠king]; target-extreme [␠Beast, ␠USSR, orce, ␠LHC, ␠Uncle]; token classes {'continuation_or_standalone': 49, 'punctuation_or_symbol': 2, 'word_initial': 165}
- C6 (n=193): representatives [␠or, ␠или, ␠cette, ␠ق, �, ␠tiene, ␠questa, ␠خ]; target-extreme [�, ␠или, ␠cette, ␠Une, ла]; token classes {'continuation_or_standalone': 99, 'punctuation_or_symbol': 30, 'word_initial': 64}
- C7 (n=160): representatives [␠malignancies, ␠atherosclerotic, ␠cardiovascular, ␠cytokine, ␠macrophage, clerosis, ␠gluc, ␠cortic]; target-extreme [␠monocyte, clerosis, teral, ␠physiology, ␠thrombosis]; token classes {'continuation_or_standalone': 70, 'whitespace': 1, 'word_initial': 89}

Strongest intercommunity connections:

- C0 to C2: 663 token edges; mean cosine 0.097486
- C1 to C6: 338 token edges; mean cosine 0.080011
- C1 to C4: 332 token edges; mean cosine 0.087861
- C1 to C3: 319 token edges; mean cosine 0.087133
- C0 to C3: 307 token edges; mean cosine 0.088344
- C2 to C3: 298 token edges; mean cosine 0.094741
- C2 to C5: 296 token edges; mean cosine 0.094775
- C0 to C1: 264 token edges; mean cosine 0.088636
- C4 to C5: 217 token edges; mean cosine 0.096798
- C1 to C7: 215 token edges; mean cosine 0.088200

### Secondary cross-side relations from R005

- chr (positive_head) to ␠chr (negative_tail): cosine 0.456221, combined-neighbour rank 1
- ␠chr (negative_tail) to chr (positive_head): cosine 0.456221, combined-neighbour rank 1
- ␠height (positive_head) to ␠Height (negative_tail): cosine 0.451646, combined-neighbour rank 1
- ␠Height (negative_tail) to ␠height (positive_head): cosine 0.451646, combined-neighbour rank 1
- Notification (positive_head) to notification (negative_tail): cosine 0.393724, combined-neighbour rank 1
- notification (negative_tail) to Notification (positive_head): cosine 0.393724, combined-neighbour rank 1
- ␠stairs (negative_tail) to ␠stair (positive_head): cosine 0.385155, combined-neighbour rank 1
- ␠stair (positive_head) to ␠stairs (negative_tail): cosine 0.385155, combined-neighbour rank 1
- ␠liter (negative_tail) to Liter (positive_head): cosine 0.359790, combined-neighbour rank 1
- Liter (positive_head) to ␠liter (negative_tail): cosine 0.359790, combined-neighbour rank 1

## State 31: block_30_output

### positive_head

- Nodes: 2536
- Directed 10-NN edges: 25360
- Undirected edges: 17242
- Mean 10-NN cosine: 0.118576
- Communities: 11
- Modularity: 0.508703

Largest communities:

- C0 (n=415): representatives [␠characterizing, ␠Measurement, ␠Measurements, ␠introducing, ␠quantification, ␠acquiring, ␠development, ␠discussion]; target-extreme [␠quoted, ␠recycled, ␠measured, ␠tension, ␠debated]; token classes {'continuation_or_standalone': 98, 'whitespace': 1, 'word_initial': 316}
- C1 (n=379): representatives [␠unw, ␠Mitchell, ␠Krish, Jay, ␠Bennett, ␠Mik, ␠Mumbai, ␠Pakistan]; target-extreme [Bab, sal, ␠Berlin, ␠Krish, ␠Kumar]; token classes {'continuation_or_standalone': 160, 'punctuation_or_symbol': 9, 'whitespace': 2, 'word_initial': 208}
- C2 (n=292): representatives [as, ation, 3, ␠at, ating, ␠more, ␠all, l]; target-extreme [triangle, ␠at, ilation, charge, д]; token classes {'continuation_or_standalone': 180, 'punctuation_or_symbol': 3, 'target_lexical_variant': 2, 'whitespace': 2, 'word_initial': 105}
- C3 (n=270): representatives [␠filmmakers, ␠Photograph, Play, Notification, ␠filmmaker, ␠Bitmap, space, Output]; target-extreme [Posted, sizeof, ␠Photo, ␠recorder, ␠Caption]; token classes {'continuation_or_standalone': 149, 'punctuation_or_symbol': 2, 'whitespace': 1, 'word_initial': 118}
- C4 (n=257): representatives [␠entrepreneurs, ␠breastfeeding, ␠organisations, ␠businesses, business, Reading, ␠shops, ␠entrepreneur]; target-extreme [␠hospital, ␠dating, ␠Business, ␠students, ␠Tours]; token classes {'continuation_or_standalone': 65, 'word_initial': 192}
- C5 (n=206): representatives [}$;, $.[]{, Acknowledgments, $;, }},\, $.\, \]., ).](]; target-extreme [␠@@, ■, ](, ␠](, _{\]; token classes {'continuation_or_standalone': 34, 'punctuation_or_symbol': 154, 'whitespace': 4, 'word_initial': 14}
- C6 (n=193): representatives [␠periodontal, ␠renormalization, ␠phenomenological, ␠pulmonary, monary, ␠dopaminergic, ␠centrifug, ␠psychosocial]; target-extreme [␠µm, ␠psychosocial, ␠salivary, ␠tornado, ␠mitotic]; token classes {'continuation_or_standalone': 59, 'punctuation_or_symbol': 2, 'whitespace': 2, 'word_initial': 130}
- C7 (n=188): representatives [␠Interpret, ␠unavoid, ␠snar, ␠unpredict, ␠kissing, ␠discrepancies, ␠challenge, ␠inev]; target-extreme [␠travers, ␠estim, ␠unpack, ␠attribut, ␠sprang]; token classes {'continuation_or_standalone': 45, 'punctuation_or_symbol': 1, 'special': 1, 'whitespace': 1, 'word_initial': 140}

Strongest intercommunity connections:

- C0 to C2: 435 token edges; mean cosine 0.102794
- C0 to C4: 378 token edges; mean cosine 0.096311
- C0 to C3: 358 token edges; mean cosine 0.088534
- C0 to C7: 318 token edges; mean cosine 0.095411
- C1 to C2: 317 token edges; mean cosine 0.087003
- C1 to C7: 261 token edges; mean cosine 0.080782
- C0 to C6: 256 token edges; mean cosine 0.097752
- C3 to C4: 232 token edges; mean cosine 0.090146
- C1 to C4: 232 token edges; mean cosine 0.087456
- C0 to C9: 208 token edges; mean cosine 0.094811

### negative_tail

- Nodes: 2780
- Directed 10-NN edges: 27800
- Undirected edges: 18625
- Mean 10-NN cosine: 0.110219
- Communities: 13
- Modularity: 0.517497

Largest communities:

- C0 (n=499): representatives [Characteristics, ␠Characteristics, ␠recommendations, ability, ␠characteristics, ␠heterogeneity, ␠beneficiaries, ␠consequences]; target-extreme [␠characteristics, ␠uniforms, ␠affirmative, ␠Interior, ␠physiology]; token classes {'continuation_or_standalone': 146, 'whitespace': 2, 'word_initial': 351}
- C1 (n=314): representatives [␠Tah, ␠M, Th, ␠Rh, ␠Gh, ET, RA, TG]; target-extreme [␠Chi, tetra, ottom, CI, <empty>]; token classes {'continuation_or_standalone': 171, 'target_lexical_variant': 5, 'whitespace': 1, 'word_initial': 137}
- C2 (n=290): representatives [␠emperor, ␠dragon, ␠cathedral, ␠warriors, ␠Empire, ␠palace, ␠dragons, ␠king]; target-extreme [olith, ␠Ia, ␠shores, ␠Beast, ␠Uncle]; token classes {'continuation_or_standalone': 64, 'whitespace': 1, 'word_initial': 225}
- C3 (n=255): representatives [␠prohibiting, ␠resembled, ␠disappeared, ␠discour, ␠encourages, ␠prohibits, ␠created, ␠attempting]; target-extreme [␠therefrom, ␠submit, ␠chop, ␠discour, ␠assist]; token classes {'continuation_or_standalone': 54, 'punctuation_or_symbol': 1, 'word_initial': 200}
- C4 (n=253): representatives [␠Sarah, ␠Martha, ␠Laura, ␠Emily, ␠Michelle, ␠Catherine, ars, ao]; target-extreme [␠Violet, ␠cro, ␠Emily, ␠Sierra, clus]; token classes {'continuation_or_standalone': 128, 'target_lexical_variant': 2, 'word_initial': 123}
- C5 (n=236): representatives [␠macrophage, ␠atherosclerotic, ␠cytokine, ␠cardiovascular, ␠diseases, acteria, clerosis, ␠endothelium]; target-extreme [␠monocyte, clerosis, ␠enh, ␠oxides, ␠thrombosis]; token classes {'continuation_or_standalone': 87, 'word_initial': 149}
- C6 (n=228): representatives [␠or, ␠ق, ␠Sty, �, خ, ␠eller, ␠или, ␠خ]; target-extreme [�, ␠или, ␠cette, ␠м, ␠Une]; token classes {'continuation_or_standalone': 112, 'punctuation_or_symbol': 35, 'word_initial': 81}
- C7 (n=228): representatives [␠walls, ␠cylinder, ␠trucks, ␠automobiles, ␠vegetables, ␠gravel, ␠agriculture, ␠extremities]; target-extreme [␠dishes, ␠caramel, ␠limbs, ␠Rails, ␠Gates]; token classes {'continuation_or_standalone': 48, 'whitespace': 1, 'word_initial': 179}

Strongest intercommunity connections:

- C0 to C3: 463 token edges; mean cosine 0.098827
- C0 to C2: 363 token edges; mean cosine 0.091673
- C1 to C4: 358 token edges; mean cosine 0.087456
- C0 to C7: 321 token edges; mean cosine 0.089631
- C0 to C5: 292 token edges; mean cosine 0.092662
- C1 to C6: 276 token edges; mean cosine 0.083100
- C0 to C8: 252 token edges; mean cosine 0.099113
- C2 to C7: 251 token edges; mean cosine 0.092638
- C2 to C4: 226 token edges; mean cosine 0.094359
- C1 to C5: 221 token edges; mean cosine 0.090487

### Secondary cross-side relations from R005

- ␠transmit (positive_head) to ␠transmitting (negative_tail): cosine 0.462025, combined-neighbour rank 1
- ␠transmitting (negative_tail) to ␠transmit (positive_head): cosine 0.462025, combined-neighbour rank 1
- Notification (positive_head) to notification (negative_tail): cosine 0.393724, combined-neighbour rank 1
- notification (negative_tail) to Notification (positive_head): cosine 0.393724, combined-neighbour rank 1
- ␠stairs (negative_tail) to ␠stair (positive_head): cosine 0.385155, combined-neighbour rank 1
- ␠stair (positive_head) to ␠stairs (negative_tail): cosine 0.385155, combined-neighbour rank 1
- ␠handling (negative_tail) to ␠handled (positive_head): cosine 0.378483, combined-neighbour rank 1
- ␠handled (positive_head) to ␠handling (negative_tail): cosine 0.378483, combined-neighbour rank 1
- ␠liter (negative_tail) to Liter (positive_head): cosine 0.359790, combined-neighbour rank 1
- Liter (positive_head) to ␠liter (negative_tail): cosine 0.359790, combined-neighbour rank 1

## State 32: final_norm_after_block_31

### positive_head

- Nodes: 2908
- Directed 10-NN edges: 29080
- Undirected edges: 20360
- Mean 10-NN cosine: 0.129558
- Communities: 11
- Modularity: 0.555754

Largest communities:

- C0 (n=473): representatives [s, er, :, ␠that, ), ␠(, 1, as]; target-extreme [␠at, ␠find, ␠*, er, ␠roll]; token classes {'continuation_or_standalone': 238, 'punctuation_or_symbol': 24, 'target_lexical_variant': 3, 'whitespace': 15, 'word_initial': 193}
- C1 (n=386): representatives [␠ferromagnetic, ␠microorganisms, ␠antidepress, ␠psychosocial, ␠decentralized, ␠dopaminergic, ␠renormalization, ioxidants]; target-extreme [magnetic, ␠CNT, Cold, ␠lett, ␠rgb]; token classes {'continuation_or_standalone': 122, 'whitespace': 1, 'word_initial': 263}
- C2 (n=366): representatives [␠data, ␠detecting, manager, ␠problem, Size, ␠test, ␠Measurement, ␠process]; target-extreme [Tests, ␠exiting, ␠DATA, imaging, DATA]; token classes {'continuation_or_standalone': 206, 'whitespace': 1, 'word_initial': 159}
- C3 (n=271): representatives [0033, 389, 0013, 442, 0032, 0024, 797, 793]; target-extreme [03, 3333, 532, 422, 517]; token classes {'continuation_or_standalone': 199, 'word_initial': 72}
- C4 (n=250): representatives [Acknowledgements, ␠reported, ␠acknowledges, ␠explained, ␠recorded, Acknowledgments, VERTISEMENT, ␠videot]; target-extreme [␠listed, Reading, ␠recorder, eLife, ␠recording]; token classes {'continuation_or_standalone': 75, 'punctuation_or_symbol': 1, 'whitespace': 1, 'word_initial': 173}
- C5 (n=243): representatives [}}}}, )}}, }}), .", )., }}}}$, }}(, }}-]; target-extreme [␠\*\**, }}\,, :@", ],[@, }$:]; token classes {'continuation_or_standalone': 10, 'punctuation_or_symbol': 220, 'whitespace': 5, 'word_initial': 8}
- C6 (n=242): representatives [ação, ␠Bangladesh, ␠Brazil, ações, Lind, izione, iones, ␠Pakistan]; target-extreme [chst, ␠Pakistan, heim, Kam, ivas]; token classes {'continuation_or_standalone': 134, 'punctuation_or_symbol': 13, 'word_initial': 95}
- C7 (n=230): representatives [ating, izing, ␠withdrawing, pping, ␠retrieved, ␠inserting, ␠transfer, ␠acquisition]; target-extreme [igration, ␠favour, ␠retrieved, ␠amusement, inking]; token classes {'continuation_or_standalone': 100, 'whitespace': 1, 'word_initial': 129}

Strongest intercommunity connections:

- C0 to C2: 384 token edges; mean cosine 0.096300
- C0 to C6: 341 token edges; mean cosine 0.084435
- C2 to C7: 319 token edges; mean cosine 0.091619
- C1 to C7: 319 token edges; mean cosine 0.090035
- C0 to C7: 310 token edges; mean cosine 0.100028
- C2 to C4: 304 token edges; mean cosine 0.092127
- C1 to C2: 296 token edges; mean cosine 0.088073
- C1 to C9: 268 token edges; mean cosine 0.090034
- C0 to C4: 248 token edges; mean cosine 0.094602
- C0 to C8: 241 token edges; mean cosine 0.090234

### negative_tail

- Nodes: 2942
- Directed 10-NN edges: 29420
- Undirected edges: 19963
- Mean 10-NN cosine: 0.113821
- Communities: 12
- Modularity: 0.496130

Largest communities:

- C0 (n=427): representatives [␠Characteristics, Characteristics, ␠recommendations, ␠characteristics, ␠brutality, ␠singularities, ␠differences, ␠alterations]; target-extreme [helper, ␠Meaning, ␠curriculum, ␠correlated, ␠DEFAULT]; token classes {'continuation_or_standalone': 122, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 302}
- C1 (n=405): representatives [␠Diana, ␠Maggie, ␠Emily, ␠Molly, ␠Carrie, Smith, ␠Diane, ␠Rober]; target-extreme [␠Emily, گ, ␠Peggy, ␠Springs, ␠th]; token classes {'continuation_or_standalone': 137, 'punctuation_or_symbol': 14, 'target_lexical_variant': 1, 'whitespace': 5, 'word_initial': 248}
- C2 (n=308): representatives [␠extraordinarily, ␠tragedy, ␠spectacular, ␠glorious, ␠brilli, ␠magnific, ␠ridiculous, ␠indul]; target-extreme [␠premiered, ␠extremities, particularly, ␠prodig, ␠extremes]; token classes {'continuation_or_standalone': 73, 'word_initial': 235}
- C3 (n=304): representatives [␠discour, ␠Exper, ␠Cro, ␠encour, ␠Comp, ␠incor, ␠Sp, TA]; target-extreme [CI, tetra, ␠discour, EH, ␠multif]; token classes {'continuation_or_standalone': 135, 'target_lexical_variant': 1, 'word_initial': 168}
- C4 (n=299): representatives [␠dropped, ␠screamed, ␠deteriorated, ␠increased, ␠altering, ␠Increased, ␠destroying, ␠detrimental]; target-extreme [␠compelled, urbs, drop, ␠engages, ␠composed]; token classes {'continuation_or_standalone': 60, 'whitespace': 3, 'word_initial': 236}
- C5 (n=268): representatives [␠abnormalities, ␠proinflammatory, ␠pathophysiology, ␠inflammation, ␠hypersensitivity, ␠pathology, ␠physiology, ␠responsiveness]; target-extreme [␠preclinical, ␠metabol, ␠pathology, clerosis, ␠edema]; token classes {'continuation_or_standalone': 94, 'punctuation_or_symbol': 1, 'whitespace': 2, 'word_initial': 171}
- C6 (n=224): representatives [␠emperor, ␠King, ␠palace, ␠righteousness, ␠Emperor, ␠Princess, ␠warriors, ␠Sultan]; target-extreme [␠Duke, ␠Lion, ␠medals, ␠repent, ␠characters]; token classes {'continuation_or_standalone': 30, 'punctuation_or_symbol': 1, 'word_initial': 193}
- C7 (n=205): representatives [␠walls, ␠automobiles, ␠robes, ␠buildings, ␠clothing, ␠mountains, ␠Lemon, ␠vegetables]; target-extreme [␠Interior, ␠caramel, ␠bolts, ␠cliffs, ␠Heart]; token classes {'continuation_or_standalone': 32, 'whitespace': 2, 'word_initial': 171}

Strongest intercommunity connections:

- C1 to C3: 485 token edges; mean cosine 0.084272
- C0 to C4: 404 token edges; mean cosine 0.103185
- C2 to C4: 354 token edges; mean cosine 0.096164
- C0 to C2: 351 token edges; mean cosine 0.100101
- C0 to C5: 292 token edges; mean cosine 0.101247
- C1 to C6: 254 token edges; mean cosine 0.096167
- C3 to C5: 223 token edges; mean cosine 0.087834
- C2 to C6: 222 token edges; mean cosine 0.101371
- C2 to C3: 222 token edges; mean cosine 0.089372
- C0 to C3: 217 token edges; mean cosine 0.085331

### Secondary cross-side relations from R005

- ␠Expect (positive_head) to Expect (negative_tail): cosine 0.521179, combined-neighbour rank 1
- Expect (negative_tail) to ␠Expect (positive_head): cosine 0.521179, combined-neighbour rank 1
- 175 (positive_head) to ␠175 (negative_tail): cosine 0.471962, combined-neighbour rank 1
- ␠175 (negative_tail) to 175 (positive_head): cosine 0.471962, combined-neighbour rank 1
- ␠anticancer (positive_head) to ␠antitumor (negative_tail): cosine 0.447597, combined-neighbour rank 1
- ␠antitumor (negative_tail) to ␠anticancer (positive_head): cosine 0.447597, combined-neighbour rank 1
- According (positive_head) to according (negative_tail): cosine 0.416821, combined-neighbour rank 1
- according (negative_tail) to According (positive_head): cosine 0.416821, combined-neighbour rank 1
- ␠symbols (negative_tail) to ymbols (positive_head): cosine 0.415689, combined-neighbour rank 1
- ymbols (positive_head) to ␠symbols (negative_tail): cosine 0.415689, combined-neighbour rank 1

