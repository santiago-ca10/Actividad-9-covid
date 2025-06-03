from model.employee import Employee
from model.data_store import DataStore

class EmployeeController:
    def __init__(self):
        self.store = DataStore()

    def add_employee(self, **kwargs):
        employee = Employee(**kwargs)
        self.store.add_employee(employee)

    def update_employee(self, index, updated_data):
        self.store.update_employee(index, updated_data)

    def list_employees(self):
        return self.store.get_all()
