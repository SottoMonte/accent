'''
# User
(code:natural)
(name:string)
(surname:string)
(email:string)
(roles:array[enum])
(permissions:array[enum])
(active:boolean)
'''

from typing import NewType

user = NewType('user', (int,int,int))
