# -*- coding: utf-8 -*-

import pickle as p

girl_friend_file = 'girl_friend.data'

girl_friends = ['大椒响', '小川阿佐美', '西翔野', '冲田杏梨', '星野明', '星野优', '吉泽明步', '苍井空']

with open(girl_friend_file, 'wb+') as f:
    p.dump(girl_friends, f)
    f.close()

del girl_friends  #删掉girl_friends

with open(girl_friend_file, 'rb+') as f:
    ls = p.load(f)
    print(ls)
