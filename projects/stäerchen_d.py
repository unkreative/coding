import random

rlist = []

# schloofen goen 11/12 vacanz
# schloofen goen 10/11 schoulzait

Complimenter = ['schéin', 'perfekt', 'cool', 'symphatesch', 'léif', 'sexyyy', ':)', 'schlau', 'begabt', 'süss',
                'supper', 'zum schmelzen', 'scharmant', 'en romantiker', "wichteg", "staark", "witzech", "cute",
                "en schatz:)", "den cutesten mensch den ech kennen:)"]

du_complimenter = "schéinheet", "perfekten mensch", "symphatesch persoun", "Stäerchen", "léifsten persoun", "sexiest persoun", "schlau persoun", "begabten persoun", "beléiften persoun", "süssest persoun", "scharmantest persoun", "Romantiker", "Wichtegst persoun fier mech", "Staark persoun", "witzech persoun", "Cutie", "Schatz"

emojis = ["♡ ´･ᴗ･ `♡", "<3", "<3", "<3", "<3", "❤️", "❤️", "❤️", "💕", "♥️", "♥️", "💛", "💚", "💙", "❣️", "💞", "💓",
          "💖", "💗", "(♡˙︶˙♡)", "(*¯ ³¯*)♡", "(─‿‿─)♡❤", "♡(≧◡≦)", "(*^^*)♡♡", "(⇀ 3 ↼)"]

ln_Complimenter = len(Complimenter)
ln_Complimenter = ln_Complimenter - 1

ln_du_complimenter = len(du_complimenter)
ln_du_complimenter = ln_du_complimenter - 1

ln_emoji = len(emojis) - 1

a = [
    [0, 1, 2, 3],
    [1, 0, 2, 3],
    [1, 2, 0, 3],
    [1, 2, 3, 0],
    [0, 2, 1, 3],
    [2, 0, 1, 3],
    [0, 1, 3, 2],
    [3, 0, 1, 2],
    [0, 3, 1, 2],
    [0, 2, 3, 1]
]
len_a = len(a) - 1

gn_emoji = random.randint(0, ln_emoji)
gn_compl = random.randint(0, ln_du_complimenter)

rlist.append(gn_emoji)
rlist.append(gn_compl)

gn_emoji = emojis[gn_emoji]
gn_compl = du_complimenter[gn_compl]

Gudd_nuecht1 = f'gudd nuecht du {gn_compl}{gn_emoji}'
Gudd_nuecht2 = f'Nuechtii {gn_compl} {gn_emoji}'
Gudd_nuecht3 = f'Schloof gudd {gn_compl} {gn_emoji}'
Gudd_nuecht4 = f'gudd nuecht {gn_compl} {gn_emoji}'
# Gudd_nuecht5 = ''

module1_emoji = random.randint(0, ln_emoji)
module1_compl1 = random.randint(0, ln_du_complimenter)
module1_compl2 = random.randint(0, ln_du_complimenter)

rlist.append(module1_emoji)
rlist.append(module1_compl1)
rlist.append(module1_compl2)

module1_emoji = emojis[module1_emoji]
module1_compl1 = Complimenter[module1_compl1]
module1_compl2 = Complimenter[module1_compl2]

module1_1 = f'du bass aawer haut besonnesch {module1_compl1} an {module1_compl2} {module1_emoji}'
module1_2 = f'wooow du bass aawer {module1_compl1} {module1_emoji}'
module1_3 = f'uii {module1_compl1}, {module1_compl2} passt gudd zu dier {module1_emoji}'
# module1_4 = ''
# module1_5 = ''

module2_emoji = random.randint(0, ln_emoji)
module2_compl1 = random.randint(0, ln_du_complimenter)
module2_compl2 = random.randint(0, ln_du_complimenter)

rlist.append(module2_emoji)
rlist.append(module2_compl1)
rlist.append(module2_compl2)

module2_emoji = emojis[module2_emoji]
module2_compl1 = Complimenter[module2_compl1]
module2_compl2 = Complimenter[module2_compl2]

module2_1 = f'dreem schéin {module2_emoji}'
module2_2 = f'dreem gudd {module2_emoji}'
module2_3 = f'schloof gudd an {module2_emoji}'
module2_4 = f'dreem an schloof gudd {module2_emoji}'
# module2_5 = ''

module3_emoji = random.randint(0, ln_emoji)
module3_compl1 = random.randint(0, ln_du_complimenter)
module3_compl2 = random.randint(0, ln_du_complimenter)

rlist.append(module3_emoji)
rlist.append(module3_compl1)
rlist.append(module3_compl2)

module3_emoji = emojis[module3_emoji]
module3_compl1 = Complimenter[module3_compl1]
module3_compl2 = Complimenter[module3_compl2]

module3_1 = f'Boo {module3_emoji}'
module3_2 = f'Schéinheet'
module3_3 = f'Stäerchen {module3_emoji}'
module3_4 = f'Schatzi?:)'
module3_5 = f'Cutie'

module4_emoji = random.randint(0, ln_emoji)
module4_compl1 = random.randint(0, ln_du_complimenter)
module4_compl2 = random.randint(0, ln_du_complimenter)

rlist.append(module4_emoji)
rlist.append(module4_compl1)
rlist.append(module4_compl2)

module4_emoji = emojis[module4_emoji]
module4_compl1 = Complimenter[module4_compl1]
module4_compl2 = Complimenter[module4_compl2]

module4_1 = f'merci fier alles:) {module4_emoji}'
module4_2 = f'merci dass du bei mier bass {module4_emoji}'
module4_3 = f'cutie, merci fier alles'
module4_4 = f'merci dass du existeierss {module4_emoji}'

# module4_5 = ''

gn = [Gudd_nuecht1, Gudd_nuecht2, Gudd_nuecht3, Gudd_nuecht4]
gn_len = len(gn) + 1
gn_len_1 = gn_len - 2

mod1 = [module1_1, module1_2, module1_3]
mod1_len = len(mod1)
mod1_len_1 = mod1_len - 1

mod2 = [module2_1, module2_2, module2_3, module2_4]
mod2_len = len(mod2)
mod2_len_1 = mod2_len - 1

mod3 = [module3_1, module3_2, module3_3, module3_4, module3_5]
mod3_len = len(mod3)
mod3_len_1 = mod3_len - 1

mod4 = [module4_1, module4_2, module4_3, module4_4]
mod4_len = len(mod4)
mod4_len_1 = mod4_len - 1

mods = [mod1, mod2, mod3, mod4]
mods_len = len(mods)
mods_len_1 = mods_len - 1


def create_mod(final=""):
    rgn = random.randint(0, gn_len_1)
    rmods = random.randint(0, len_a)
    rmod1 = random.randint(0, mod1_len_1)
    rmod2 = random.randint(0, mod2_len_1)
    rmod3 = random.randint(0, mod3_len_1)
    rmod4 = random.randint(0, mod4_len_1)

    gn_res = gn[rgn]
    mods_res = a[rmods]
    mod1_res = mod1[rmod1]
    mod2_res = mod2[rmod2]
    mod3_res = mod3[rmod3]
    mod4_res = mod4[rmod4]
    mods1 = [mod1_res, mod2_res, mod3_res, mod4_res]
    final = []
    final.append(gn_res)
    for x in mods_res:
        res = mods1[x]
        final.append(res)
    return final


final = create_mod()

final.append("<3")

final = ', \n'.join(str(e) for e in final)

print(final)