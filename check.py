import excel

ids_to_be_check_if_exist_in_bigger_list = excel.get_all_the_rows_from_column('A')
print('loaded ids_to_be_check_if_exist_in_bigger_list')
ids_from_bigger_list = excel.get_all_the_rows_from_column_sheet2('A')
print('loaded ids_from_bigger_list ')

true_or_false_list = []

for i in range(1, len(ids_to_be_check_if_exist_in_bigger_list)):
    if ids_to_be_check_if_exist_in_bigger_list[i] in ids_from_bigger_list:
        true_or_false_list.append('TRUE')
        print(f'{ids_to_be_check_if_exist_in_bigger_list[i]} true')
    else:
        true_or_false_list.append('FALSE')
        print(f'{ids_to_be_check_if_exist_in_bigger_list[i]} false')

excel.write_html_to_excel(true_or_false_list, 'B')
