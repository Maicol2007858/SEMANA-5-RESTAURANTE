from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto("Pizza", 8.50, True)
producto2 = Producto("Hamburguesa", 6.75, True)

# Crear clientes
cliente1 = Cliente("Maicol Castillo", 18, True)
cliente2 = Cliente("Juan Perez", 25, False)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()