name = 'песик'
immutable_var=tuple([1, 7 , 'шарик', False, name])
print(immutable_var)
# изменить содержимое кортежа нельзя по определению:
name='котик'
print(immutable_var) #несмотря на изменение значения переменной, внутри кортежа
# песик котиком не стал
mutable_list=list([2,8,'апельсин'])
print('До обеда было:',mutable_list)
mutable_list[2]='кожура от апельсина'
print('после обеда осталось:',mutable_list)