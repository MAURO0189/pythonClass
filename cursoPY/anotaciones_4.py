from typing import Optional

def find_employee(employee_ids: list[int], employee_id: int) -> Optional[int]:
    """
    Busca un ID de empleado en una lista de IDs y devuelve el valor si existe.

    Parámetros:
    employee_ids (list[int]): Lista de IDs de empleados.

    Retorna:
    Optional[int]: El ID encontrado o None sino existe en la lista.
    """
    if employee_id in employee_ids:
        return employee_id
    return None