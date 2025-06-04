# Importación de módulos para la interfaz gráfica y controladores
import tkinter as tk
from tkinter import ttk, messagebox
from controller.employee_controller import EmployeeController
from i18n.english import English
from i18n.spanish import Spanish

class MainWindow:
    """
    Clase que representa la ventana principal del sistema de control COVID.
    Gestiona la interfaz gráfica, entrada de datos y acciones del usuario.
    """

    def __init__(self):
        # Controlador principal para interactuar con los empleados
        self.controller = EmployeeController()

        # Diccionario de idiomas disponibles
        self.languages = {
            "Español": Spanish(),
            "English": English()
        }

        self.selected_index = None  # Índice del empleado seleccionado para edición
        self.lang = self.languages["Español"]  # Idioma por defecto

        # Inicialización de la ventana principal
        self.root = tk.Tk()
        self.root.title("Control COVID")

        # Carga los elementos gráficos
        self.setup_ui()

    def setup_ui(self):
        """
        Configura todos los elementos visuales de la interfaz.
        """

        # Menú para seleccionar idioma
        tk.Label(self.root, text="Idioma / Language:").pack(pady=5)
        self.lang_box = ttk.Combobox(self.root, values=list(self.languages.keys()), state="readonly")
        self.lang_box.set("Español")
        self.lang_box.pack()
        self.lang_box.bind("<<ComboboxSelected>>", self.change_language)

        # Campos del formulario de registro de empleados
        self.entries = {}  # Guarda las entradas de texto
        self.fields = [    # Campos generales del empleado
            "name", "address", "locality", "contacts",
            "health_status", "comorbidities", "covid_positive", "severity"
        ]
        self.daily_fields = ["temperature", "contact_with_infected", "mood"]  # Datos diarios
        self.labels = {}  # Guarda las etiquetas de cada campo para cambiar el idioma

        # Creación dinámica de etiquetas y campos de entrada
        for field in self.fields + self.daily_fields:
            label = tk.Label(self.root, text=self.lang.get("fields")[field])
            label.pack()
            entry = tk.Entry(self.root)
            entry.pack()
            self.entries[field] = entry
            self.labels[field] = label

        # Botón para guardar (crear o actualizar)
        self.save_btn = tk.Button(self.root, text=self.lang.get("save"), command=self.save)
        self.save_btn.pack(pady=5)

        # Botón para mostrar todos los empleados registrados
        self.view_btn = tk.Button(self.root, text=self.lang.get("view"), command=self.show_all)
        self.view_btn.pack(pady=5)

    def change_language(self, event=None):
        """
        Cambia el idioma de la interfaz según lo seleccionado en el menú desplegable.
        """
        selected = self.lang_box.get()
        self.lang = self.languages[selected]

        # Actualiza las etiquetas de los campos y botones
        for field in self.fields + self.daily_fields:
            self.labels[field].config(text=self.lang.get("fields")[field])
        self.save_btn.config(text=self.lang.get("update") if self.selected_index is not None else self.lang.get("save"))
        self.view_btn.config(text=self.lang.get("view"))
        self.root.title(self.lang.get("title"))

    def clear_fields(self):
        """
        Limpia todos los campos del formulario y restablece el estado a nuevo registro.
        """
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.selected_index = None
        self.save_btn.config(text=self.lang.get("save"))

    def save(self):
        """
        Guarda un nuevo empleado o actualiza uno existente.
        Valida la temperatura antes de proceder.
        """
        data = {k: self.entries[k].get() for k in self.entries}

        # Validación de temperatura
        try:
            float(data["temperature"])
        except ValueError:
            messagebox.showerror("Error", "Temperatura no válida.")
            return

        # Guardado o actualización según el estado
        if self.selected_index is None:
            self.controller.add_employee(**data)
        else:
            self.controller.update_employee(self.selected_index, {
                **data,
                "history": [self.controller.list_employees()[self.selected_index]["history"][0]]
            })

        messagebox.showinfo("✔", self.lang.get("success"))
        self.clear_fields()

    def show_all(self):
        """
        Muestra una ventana con la lista de todos los empleados y sus datos diarios.
        Permite seleccionar uno para edición.
        """
        top = tk.Toplevel(self.root)
        top.title(self.lang.get("view"))

        # Campos a mostrar en la tabla
        extended_fields = self.fields + self.daily_fields + ["puede_asistir"]

        # Tabla con encabezados
        tree = ttk.Treeview(top, columns=extended_fields, show="headings", height=10)

        for field in extended_fields:
            if field == "puede_asistir":
                label = "¿Puede asistir?"
            else:
                label = self.lang.get("fields").get(field, field.replace("_", " ").capitalize())
            tree.heading(field, text=label)
            tree.column(field, width=120)

        tree.pack(pady=10)

        # Cargar datos desde el controlador
        for idx, emp in enumerate(self.controller.list_employees()):
            history = emp.get("history", [])
            if history:
                ultimo = history[-1]
                temp = ultimo.get("temperatura", "")
                contacto = ultimo.get("contacto_con_infectado", "")
                estado = ultimo.get("estado_animo", "")
                asistencia = "Sí" if ultimo.get("puede_asistir", False) else "No"
            else:
                temp = contacto = estado = asistencia = "?"

            # Insertar fila en la tabla
            values = [
                emp.get("name", ""),
                emp.get("address", ""),
                emp.get("locality", ""),
                emp.get("contacts", ""),
                emp.get("health_status", ""),
                emp.get("comorbidities", ""),
                emp.get("covid_positive", ""),
                emp.get("severity", ""),
                temp,
                contacto,
                estado,
                asistencia
            ]

            tree.insert("", "end", iid=idx, values=values)

        def on_edit():
            """
            Carga los datos del empleado seleccionado en el formulario para su edición.
            """
            selected = tree.focus()
            if selected:
                data = self.controller.list_employees()[int(selected)]
                for k in self.entries:
                    self.entries[k].delete(0, tk.END)
                    self.entries[k].insert(0, data.get(k, ""))
                self.selected_index = int(selected)
                self.save_btn.config(text=self.lang.get("update"))
                top.destroy()

        # Botón para editar el seleccionado
        tk.Button(top, text=self.lang.get("edit_selected"), command=on_edit).pack(pady=5)

    def run(self):
        """
        Inicia el bucle principal de la aplicación.
        """
        self.root.mainloop()

