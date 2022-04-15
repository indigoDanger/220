"""
Name: <Indigo Dockery>
<SalesForce>.py

Problem: <This program utilizes an object with a list and a list of objects.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""
# from sales_person import SalesPerson


class SalesForce:

    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        file = open(file_name, 'r')
        inside = file.readlines()
        self.sales_people.append(inside)

    def quota_report(self, quota):
        outer_list = []
        for person in self.sales_people:
            inner_list = []
            inner_list.append(person.get_id())
            inner_list.append(person.get_name())
            inner_list.append(person.total_sales())
            inner_list.append(person.quota_met(quota))
            outer_list.append(inner_list)
        return outer_list

    def top_seller(self):
        for person in self.sales_people:
            return person

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if person.get_id() == employee_id:
                return person
        return None

    def get_sale_frequencies(self):
        for person in self.sales_people:
            sales_key = person.get_sales
            quantity_value = 1
            value_list = []
            for other_people in self.sales_people:
                if sales_key == other_people.get_sales:
                    quantity_value += 1
                    value_list.append(quantity_value)
            sales_key.get(quantity_value)
            value_list.append(quantity_value)
            return value_list
