def liquidez_corriente(activo_corriente, pasivo_corriente):
    return activo_corriente / pasivo_corriente

def razon_rapida(activo_corriente, inventario, pasivo_corriente):
    return (activo_corriente - inventario) / pasivo_corriente

def rotacion_inventario(costo_venta, inventario_promedio):
    return costo_venta / inventario_promedio

def periodo_promedio_cobro(cuentas_por_cobrar, ventas_netas):
    return cuentas_por_cobrar / (ventas_netas / 365)

def periodo_promedio_pago(cuentas_por_pagar, costo_venta):
    return cuentas_por_pagar / (costo_venta / 365)

def rotacion_activos_totales(ventas_netas, activos_totales):
    return ventas_netas / activos_totales

def razon_endeudamiento(total_pasivos, activos_totales):
    return total_pasivos / activos_totales

def razon_cargos_interes_fijos(EBIT, gastos_interes):
    return EBIT / gastos_interes

def razon_cobertura_pagos_fijos(EBIT, pagos_fijos):
    return EBIT / pagos_fijos

def margen_utilidad_bruta(ventas_netas, costo_venta):
    return (ventas_netas - costo_venta) / ventas_netas

def margen_utilidad_operativa(EBIT, ventas_netas):
    return EBIT / ventas_netas

def margen_utilidad_neta(utilidad_neta, ventas_netas):
    return utilidad_neta / ventas_netas

def ganancias_por_accion(utilidad_neta, acciones_emitidas):
    return utilidad_neta / acciones_emitidas

def rendimiento_sobre_activos_totales(utilidad_neta, activos_totales):
    return utilidad_neta / activos_totales

def rendimiento_sobre_patrimonio(utilidad_neta, patrimonio):
    return utilidad_neta / patrimonio

def razon_precio_ganancias(precio_accion, ganancias_por_accion):
    return precio_accion / ganancias_por_accion

def razon_mercado_libro(precio_accion, valor_libro_accion):
    return precio_accion / valor_libro_accion

SEPARADOR = "//" * 30
# Función para seleccionar qué opción desea calcular el usuario
def seleccionar_opcion():
    print("¿Qué desea calcular?")
    print("1) Razón financiera")
    print("2) Técnica de evaluación de proyectos de inversión")
    opcion = input("Ingrese 1 o 2: ")
    if opcion == "1":
        mostrar_opciones_razon_financiera()
    elif opcion == "2":
        mostrar_opciones_tecnicas_inversion()
    else:
        print("Opción no válida.")

# Función para mostrar las opciones de razones financieras
def mostrar_opciones_razon_financiera():
    print("Ingresa el numero de la razón financiera que necesita:")
    print("//////////////////////////Opciones//////////////////////////")
    print("1. Liquidez circulante")
    print("2. Razón rápida")
    print("3. Rotación de inventario")
    print("4. Período promedio de cobro")
    print("5. Período promedio de pago")
    print("6. Rotación de activos totales")
    print("7. Razón de endeudamiento")
    print("8. Razón deuda-capital patrimonial")
    print("9. Razón de cargos de interés fijos")
    print("10. Razón de cobertura de pagos fijos")
    print("11. Margen de utilidad bruta")
    print("12. Margen de utilidad operativa")
    print("13. Margen de utilidad neta")
    print("14. Ganancias por acción")
    print("15. Rendimiento sobre los activos totales")
    print("16. Rendimiento sobre el patrimonio")
    print(SEPARADOR)
    opcion = input("¿Qué razón financiera necesita? ")
    ejecutar_opcion_razon_financiera(opcion)

# Función para ejecutar la opción seleccionada de razón financiera
def ejecutar_opcion_razon_financiera(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1:
            activo_corriente = float(input("Introduzca el valor del activo corriente: "))
            pasivo_corriente = float(input("Introduzca el valor del pasivo corriente: "))
            resultado = liquidez_corriente(activo_corriente, pasivo_corriente)
            print("El resultado de la razón financiera de liquidez corriente es:", resultado)
            print(SEPARADOR)
        elif opcion == 2:
            activo_corriente = float(input("Introduzca el valor del activo corriente: "))
            inventario = float(input("Introduzca el valor del inventario: "))
            pasivo_corriente = float(input("Introduzca el valor del pasivo corriente: "))
            resultado = razon_rapida(activo_corriente, inventario, pasivo_corriente)
            print("El resultado de la razón financiera de razón rápida es:", resultado)
            print(SEPARADOR)
        elif opcion == 3:
            costo_venta = float(input("Introduzca el costo de venta: "))
            inventario_promedio = float(input("Introduzca el valor del inventario promedio: "))
            resultado = rotacion_inventario(costo_venta, inventario_promedio)
            print("El resultado de la razón financiera de rotación de inventario es:", resultado)
            print(SEPARADOR)
        elif opcion == 4:
            cuentas_por_cobrar = float(input("Introduzca el valor de las cuentas por cobrar: "))
            ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
            resultado = periodo_promedio_cobro(cuentas_por_cobrar, ventas_netas)
            print("El resultado del período promedio de cobro es:", resultado)
            print(SEPARADOR)
        elif opcion == 5:
            cuentas_por_pagar = float(input("Introduzca el valor de las cuentas por pagar: "))
            compras = float(input("Introduzca el valor de las compras: "))
            resultado = periodo_promedio_pago(cuentas_por_pagar, compras)
            print("El resultado del período promedio de pago es:", resultado)
            print(SEPARADOR)
        elif opcion == 6:
            ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
            activos_totales = float(input("Introduzca el valor de los activos totales: "))
            resultado = rotacion_activos_totales(ventas_netas, activos_totales)
            print("El resultado de la razón financiera de rotación de activos totales es:", resultado)
            print(SEPARADOR)
        elif opcion == 7:
            total_pasivos = float(input("Introduzca el valor del total de pasivos: "))
            activos_totales = float(input("Introduzca el valor de los activos totales: "))
            resultado = razon_endeudamiento(total_pasivos, activos_totales)
            print("El resultado de la razón financiera de razón de endeudamiento es:", resultado)
            print(SEPARADOR)
        elif opcion == 8:
            pasivos_totales = float(input("Introduzca el valor del total de pasivos: "))
            capital_en_acciones_comunes = float(input("Introduzca el valor del capital en acciones comunes: "))
            resultado = razon_cargos_interes_fijos(pasivos_totales, capital_en_acciones_comunes)
            print("El resultado de la razón financiera de razón de deuda-capital patrimonial es:", resultado)
            print(SEPARADOR)
        elif opcion == 9:
            EBIT = float(input("Introduzca el valor del EBIT: "))
            gastos_interes = float(input("Introduzca el valor de los gastos por intereses: "))
            resultado = razon_cargos_interes_fijos(EBIT, gastos_interes)
            print("El resultado de la razón financiera de razón de cargos de interés fijos es:", resultado)
            print(SEPARADOR)
        elif opcion == 10:
            EBIT = float(input("Introduzca el valor del EBIT: "))
            pagos_fijos = float(input("Introduzca el valor de los pagos fijos: "))
            resultado = razon_cobertura_pagos_fijos(EBIT, pagos_fijos)
            print("El resultado de la razón financiera de razón de cobertura de pagos fijos es:", resultado)
            print(SEPARADOR)
        elif opcion == 11:
            ventas = float(input("Introduzca el valor de las ventas: "))
            costo_venta = float(input("Introduzca el costo de venta: "))
            resultado = margen_utilidad_bruta(ventas, costo_venta)
            print("El resultado de la razón financiera de margen de utilidad bruta es:", resultado)
            print(SEPARADOR)
        elif opcion == 12:
            utilidades_operativas = float(input("Introduzca el valor de las utilidades operativas: "))
            ventas = float(input("Introduzca el valor de las ventas: "))
            resultado = margen_utilidad_operativa(utilidades_operativas, ventas)
            print("El resultado de la razón financiera de margen de utilidad operativa es:", resultado)
            print(SEPARADOR)
        elif opcion == 13:
            utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
            ventas_netas = float(input("Introduzca el valor de las ventas netas: "))
            resultado = margen_utilidad_neta(utilidad_neta, ventas_netas)
            print("El resultado de la razón financiera de margen de utilidad neta es:", resultado)
            print(SEPARADOR)
        elif opcion == 14:
            utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
            acciones_emitidas = float(input("Introduzca el valor de las acciones emitidas: "))
            resultado = ganancias_por_accion(utilidad_neta, acciones_emitidas)
            print("El resultado de la razón financiera de ganancias por acción es:", resultado)
            print(SEPARADOR)
        elif opcion == 15:
            utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
            activos_totales = float(input("Introduzca el valor de los activos totales: "))
            resultado = rendimiento_sobre_activos_totales(utilidad_neta, activos_totales)
            print("El resultado de la razón financiera de rendimiento sobre los activos totales es:", resultado)
            print(SEPARADOR)
        elif opcion == 16:
            utilidad_neta = float(input("Introduzca el valor de la utilidad neta: "))
            patrimonio = float(input("Introduzca el valor del patrimonio: "))
            resultado = rendimiento_sobre_patrimonio(utilidad_neta, patrimonio)
            print("El resultado de la razón financiera de rendimiento sobre el patrimonio es:", resultado)
            print(SEPARADOR)
        else:
            print("¡Opción no válida!")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

def seleccionar_opcion():
    print("¿Qué necesita calcular?")
    print("1.-Una técnica de evaluación de proyectos de inversión")
    print("2.-Una razón financiera")
    opcion = input("Ingrese el número 1 o 2 para mostrar las opciones: ")
    if opcion == "1":
        mostrar_opciones_tecnicas_inversion()
    elif opcion == "2":
        mostrar_opciones_razon_financiera()
    else:
        print("Opción no válida.")

def mostrar_opciones_tecnicas_inversion():
    print("Introduzca el número de la técnica desea calcular:")
    print("//////////////////////////Opciones//////////////////////////")
    print("1. Calcular el periodo de recuperación para ingresos mixtos")
    print("2. Calcular el Valor Presente Neto (VPN)")
    print("3. Calcular el periodo de recuperación para una anualidad")
    print(SEPARADOR)
    opcion = input("¿Qué técnica necesita calcular?: ")
    ejecutar_opcion_tecnica_inversion(opcion)

def ejecutar_opcion_tecnica_inversion(opcion):
    try:
        opcion = int(opcion)
        if opcion == 1:
            calcular_periodo_recuperacion_mixto()
        elif opcion == 2:
            calcular_vpn()
        elif opcion == 3:
            calcular_periodo_recuperacion_anualidad()
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

def calcular_periodo_recuperacion_anualidad():
    try:
        inversion_inicial = float(input("Ingrese la inversión inicial: "))
        flujo_efectivo_anual = float(input("Ingrese el flujo de efectivo anual: "))
        periodo_recuperacion = inversion_inicial / flujo_efectivo_anual
        print("El periodo de recuperación es:",(periodo_recuperacion), "años")
    except ValueError:
        print("Error: Por favor, ingrese números válidos.")

def calcular_periodo_recuperacion_mixto():
    def calcular_periodo_recuperacion(inversion_inicial, ingresos_anuales):
        total_ingresos = 0.0
        periodo = 0

        for ingreso in ingresos_anuales:
            total_ingresos += ingreso
            periodo += 1

            if total_ingresos >= inversion_inicial:
                ingreso_restante = total_ingresos - inversion_inicial
                periodo -= (ingreso_restante / ingresos_anuales[-1])
                return periodo

        return "El período de recuperación no se alcanzó después de todos los ingresos."

    inversion_inicial = float(input("Ingrese la inversión inicial: "))
    ingresos_anuales = []

    numero_anos = int(input("Ingrese el número de años: "))
    for i in range(1, numero_anos + 1):
        ingreso = float(input(f"Ingrese los ingresos del año {i}: "))
        ingresos_anuales.append(ingreso)

    periodo_recuperacion = calcular_periodo_recuperacion(inversion_inicial, ingresos_anuales)
    if isinstance(periodo_recuperacion, int) or isinstance(periodo_recuperacion, float):
        print("El período de recuperación es:",(periodo_recuperacion), "años")
    else:
        print(periodo_recuperacion)

def calcular_vpn():
    cf0 = float(input("Ingrese la inversión inicial: "))
    k = float(input("Ingrese la tasa de descuento(en decimal): "))
    num_cf = int(input("Ingrese el número de flujos de efectivo: "))

    cf_list = []
    for i in range(num_cf):
        cf = float(input(f"Ingrese el flujo de efectivo para el periodo {i+1}: "))
        cf_list.append(cf)

    vpn = -cf0
    for i in range(num_cf):
        vpn += (cf_list[i] / ((1 + k) ** (i+1)))
    print("El Valor Presente Neto (VPN) es:",vpn)

SEPARADOR = "//" * 30
seleccionar_opcion()