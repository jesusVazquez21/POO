import hashlib
import datetime
# from conexionBD import cursor, conexion  # Asumimos que tienes este archivo

# -------------------------------------------------------------------
# 📦 CLASE PRODUCTOS
# -------------------------------------------------------------------
class Productos:
    def __init__(self, id_producto: int, nombre: str, cantidad: int, unidad: str, precio: float, descripcion: str):
        self._id_producto = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._unidad = unidad
        self._precio = precio
        self._descripcion = descripcion

    # --- Métodos Set y Get (Properties) ---

    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self._cantidad = cantidad

    @property
    def unidad(self):
        return self._unidad

    @unidad.setter
    def unidad(self, unidad):
        self._unidad = unidad

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    # --- Métodos de la Clase ---

    def actualizarStock(self, nueva_cantidad: int):
        self.cantidad = nueva_cantidad
        print(f"Stock de '{self.nombre}' actualizado a {self.cantidad} {self.unidad}.")
        
        try:
            cursor.execute(
                "UPDATE productos SET cantidad = %s WHERE id = %s",
                (self.cantidad, self.id_producto)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar stock en BD: {e}")
        return False
    
    def __str__(self):
        # Un método útil para imprimir el objeto
        return f"Producto(ID: {self.id_producto}, Nombre: {self.nombre}, Stock: {self.cantidad} {self.unidad})"


# -------------------------------------------------------------------
# 👤 CLASE USUARIOS
# -------------------------------------------------------------------
class Usuarios:
    """
    [cite_start]Representa a un usuario del sistema[cite: 254].
    Combina el estilo 'Coches' (para los datos) y 'Usuario' (para los métodos estáticos).
    """
    def __init__(self, id_usuario: int, nombre: str, apellidos: str, correo: str, password_hash: str):
        # Atributos de un usuario que ya existe
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._apellidos = apellidos
        self._correo = correo
        self._password_hash = password_hash # Guardamos el hash, no la contraseña

    # --- Métodos Set y Get (Properties) ---

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        self._id_usuario = id_usuario

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self._apellidos = apellidos

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, correo):
        self._correo = correo

    # --- Métodos Estáticos (como tu ejemplo 'Usuario') ---

    @staticmethod
    def _hash_password(contrasena: str) -> str:
        [cite_start]"""Helper para encriptar la contraseña [cite: 255]"""
        return hashlib.sha256(contrasena.encode()).hexdigest()

    @staticmethod
    def registrarUsuario(nombre: str, apellidos: str, email: str, contrasena: str):
        """
        [cite_start]Registra un nuevo usuario en la base de datos[cite: 256].
        Este método es estático porque no necesitas "ser un usuario" para registrarte.
        """
        print(f"Registrando a {nombre} {apellidos}...")
        
        # --- Lógica de Base de Datos (basada en tu ejemplo) ---
        # try:
        #     contrasena_hash = Usuarios._hash_password(contrasena)
        #     fecha = datetime.datetime.now()
        #     cursor.execute(
        #         "INSERT INTO usuarios VALUES (NULL, %s, %s, %s, %s, %s)",
        #         (nombre, apellidos, email, contrasena_hash, fecha)
        #     )
        #     conexion.commit()
        #     print("Registro exitoso.")
        #     # Opcional: retornar el nuevo objeto Usuario
        #     # new_id = cursor.lastrowid
        #     # return Usuarios(new_id, nombre, apellidos, email, contrasena_hash)
        #     return True
        # except Exception as e:
        #     print(f"Error al registrar usuario: {e}")
        #     return False
        # -------------------------------------------
        pass

    @staticmethod
    def iniciarSesion(email: str, contrasena: str):
        """
        [cite_start]Valida un usuario y, si es exitoso, retorna el objeto Usuario[cite: 256].
        Este método es estático porque se usa *antes* de tener un objeto de usuario.
        """
        print(f"Iniciando sesión para {email}...")

        # --- Lógica de Base de Datos (basada en tu ejemplo) ---
        # try:
        #     contrasena_hash = Usuarios._hash_password(contrasena)
        #     cursor.execute(
        #         "SELECT * FROM usuarios WHERE email=%s AND password=%s",
        #         (email, contrasena_hash)
        #     )
        #     user_data = cursor.fetchone() # (id, nombre, apellidos, email, pass_hash, fecha)
            
        #     if user_data:
        #         print(f"¡Bienvenido, {user_data[1]}!")
        #         # Creamos y retornamos la *instancia* del usuario logueado
        #         return Usuarios(
        #             id_usuario=user_data[0],
        #             nombre=user_data[1],
        #             apellidos=user_data[2],
        #             correo=user_data[3],
        #             password_hash=user_data[4]
        #         )
        #     else:
        #         print("Credenciales incorrectas.")
        #         return None
        # except Exception as e:
        #     print(f"Error al iniciar sesión: {e}")
        #     return None
        # -------------------------------------------
        
        # Simulación de inicio de sesión exitoso
        if email == "juan@gmail.com":
            [cite_start]# [cite: 260]
            return Usuarios(1, "Juan", "García", "juan@gmail.com", "hash_simulado_123")
        else:
            return None


    # --- Métodos de Instancia ---

    def registrarProducto(self, producto: Productos):
        """
        [cite_start]Un usuario (instancia 'self') registra un producto[cite: 256].
        Este método NO es estático, porque requiere que un usuario *esté logueado*.
        """
        print(f"El usuario '{self.nombre}' está registrando el producto '{producto.nombre}'...")
        # --- Lógica de Base de Datos ---
        # cursor.execute(
        #     "INSERT INTO productos (nombre, cantidad, ...) VALUES (%s, %s, ...)",
        #     (producto.nombre, producto.cantidad, ...)
        # )
        # conexion.commit()
        # --------------------------------
        pass
        
    def __str__(self):
        return f"Usuario(ID: {self.id_usuario}, Nombre: {self.nombre} {self.apellidos}, Email: {self.correo})"

# -------------------------------------------------------------------
# 🚚 CLASE PROVEEDORES
# -------------------------------------------------------------------
class Proveedores:
    """
    [cite_start]Representa a un proveedor de insumos[cite: 257].
    """
    def __init__(self, id_proveedor: str, nombre: str, contacto: str, telefono: int, direccion: str):
        self._id_proveedor = id_proveedor
        self._nombre = nombre
        self._contacto = contacto
        self._telefono = telefono
        self._direccion = direccion

    # --- Métodos Set y Get (Properties) ---

    @property
    def id_proveedor(self):
        return self._id_proveedor

    @id_proveedor.setter
    def id_proveedor(self, id_proveedor):
        self._id_proveedor = id_proveedor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def contacto(self):
        return self._contacto

    @contacto.setter
    def contacto(self, contacto):
        self._contacto = contacto

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono

    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, direccion):
        self._direccion = direccion

    # --- Métodos de la Clase ---

    @staticmethod
    def registrarProveedor(id_proveedor: str, nombre: str, contacto: str, telefono: int, direccion: str):
        """
        [cite_start]Registra un nuevo proveedor en la BD[cite: 258].
        Es estático porque no necesitas un proveedor para registrar uno nuevo.
        """
        print(f"Registrando al proveedor '{nombre}'...")
        # --- Lógica de Base de Datos ---
        # try:
        #     cursor.execute(
        #         "INSERT INTO proveedores VALUES (%s, %s, %s, %s, %s)",
        #         (id_proveedor, nombre, contacto, telefono, direccion)
        #     )
        #     conexion.commit()
        #     print("Proveedor registrado.")
        #     return Proveedores(id_proveedor, nombre, contacto, telefono, direccion)
        # except Exception as e:
        #     print(f"Error al registrar proveedor: {e}")
        #     return None
        # -------------------------------------------
        pass

    def registrarProducto(self, producto: Productos):
        """
        [cite_start]El proveedor (instancia 'self') registra un producto que él surte[cite: 258].
        """
        print(f"El proveedor '{self.nombre}' está registrando el producto '{producto.nombre}'...")
        # --- Lógica de Base de Datos ---
        # Se insertaría el producto y se asociaría con 'self.id_proveedor'
        # cursor.execute(
        #     "INSERT INTO productos (nombre, ..., id_proveedor) VALUES (%s, ..., %s)",
        #     (producto.nombre, ..., self.id_proveedor)
        # )
        # conexion.commit()
        # --------------------------------
        pass
        
    def __str__(self):
        return f"Proveedor(ID: {self.id_proveedor}, Nombre: {self.nombre}, Contacto: {self.contacto})"