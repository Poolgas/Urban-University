immutable_var_ = (23, 'Fruit', 'Meat')
print('immutable_var: ' + str(immutable_var_))
# immutable_var_[1] = 547  # - immytable_var_ не возможно изменить т.к. это Кортеж (коллекция) которая не может быть изенена.
mutable_list = ['Wood', 'Stone', 'Glass', 2.645]
mutable_list.extend(['Grass', 'Cobblestone'])
mutable_list.remove('Wood')
print('mutable_list: ' + str(mutable_list))
