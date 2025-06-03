import json
import os

class DataStore:
    _instance = None
    _file_path = "data/employees.json"

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataStore, cls).__new__(cls)
            cls._instance.load()
        return cls._instance

    def load(self):
        if os.path.exists(self._file_path):
            with open(self._file_path, 'r') as f:
                self.employees = json.load(f)
        else:
            self.employees = []

    def save(self):
        os.makedirs(os.path.dirname(self._file_path), exist_ok=True)
        with open(self._file_path, 'w') as f:
            json.dump(self.employees, f, indent=4)

    def add_employee(self, employee):
        self.employees.append(employee.to_dict())
        self.save()

    def update_employee(self, index, updated_data):
        self.employees[index] = updated_data
        self.save()

    def get_all(self):
        return self.employees
