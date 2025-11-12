from aula11 import Employee, FulltimeEmployee

if __name__ == '__main__':
    obj_fulltime1 = FulltimeEmployee(first_name='John', last_name='Doe', base_salary=6000.0)
    print('- FultimeEmployee 1:', obj_fulltime1)
    print('Nome', obj_fulltime1.get_first_name())
    print('Nome completo:', obj_fulltime1.full_name())
    print('- Salário fixo:', obj_fulltime1.get_base_salary())
    print('- Salário total :', obj_fulltime1.compute_salary())
    print('qt:', Employee.get_count_employees())

    obj_fulltime2 = FulltimeEmployee(first_name='Mary', last_name='Smith', base_salary=6040.0)
    print('-FultimeEmployee 2:', obj_fulltime2)
    print('Nome', obj_fulltime2.get_first_name())
    print('Nome completo:', obj_fulltime2.full_name())
    print('-Salário fixo:', obj_fulltime2.get_base_salary())
    print('-Salário total :', obj_fulltime2.compute_salary())


