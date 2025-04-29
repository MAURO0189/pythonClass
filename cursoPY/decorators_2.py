def check_accses(func):
    def wrapper(employee):
        if employee.get('role') == 'admin':
            return func(employee)
        else:
            print('ACCESO DENEGADO. Solo los administradores pueden acceder.')
    return wrapper
        
@check_accses
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')

admin = {'name': 'Carlos','role': 'admin'}
employee = {'name': 'Ana','role': 'employee'}

#delete_employee(admin)
delete_employee(employee)