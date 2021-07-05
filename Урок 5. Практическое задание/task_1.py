from collections import namedtuple


def average_profit():
    list_name = 'my_list'
    company_profit = {}
    all_total = 0
    firm_list = namedtuple(list_name, 'name first_quarter second_quarter third_quarter fourth_quarter')

    try:
        for i in range(int(input('Enter firm number for checking: '))):
            company = firm_list(
                name=input('Enter company name: '),
                first_quarter=int(input('Enter first period profit: ')),
                second_quarter=int(input('Enter second period profit: ')),
                third_quarter=int(input('Enter third period profit: ')),
                fourth_quarter=int(input('Enter fourth period profit: '))
            )

            company_profit[company.name] = (
                                                   company.first_quarter + company.second_quarter
                                                   + company.third_quarter + company.fourth_quarter
                                           ) / 4
    except ValueError:
        print('Wrong data! Try one more time from first company')
        return average_profit()

    for value in company_profit.values():
        all_total += value / len(company_profit)

    print(company_profit)

    for company_name, value in company_profit.items():
        if value > all_total:
            print(f'Firm {company_name} has profit above average')
        elif value < all_total:
            print(f'Firm {company_name} has profit below average')
        elif value == all_total:
            print(f'Firm {company_name} has profit like average')


average_profit()
