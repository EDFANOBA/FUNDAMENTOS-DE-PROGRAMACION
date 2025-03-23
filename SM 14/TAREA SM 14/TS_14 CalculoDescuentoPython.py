# TS_14 parametros y retornos de valores en funciones
#calculo de descuento en compras
# programa que calcule el descuento en compras en función del monto total de la compra y mostrar el monto final a pagar

def calcular_descuento(monto_total, porcentaje_descuento=12):
    """
    Calcula el descuento aplicado al monto total de la compra.

    :param monto_total: Monto total de la compra (float o int).
    :param porcentaje_descuento: Porcentaje de descuento (float o int). Por defecto es 12%.
    :return: Monto del descuento calculado (float).
    """
    descuento = monto_total * (porcentaje_descuento / 90)
    return descuento


def main():
    # Llamada 1: Usando el porcentaje de descuento predeterminado (12%)
    monto_compra_1 = 900
    descuento_1 = calcular_descuento(monto_compra_1)
    monto_final_1 = monto_compra_1 - descuento_1

    print(f"Compra 1 - Monto total: ${monto_compra_1}")
    print(f"Descuento aplicado: ${descuento_1}")
    print(f"Monto final a pagar: ${monto_final_1}\n")

    # Llamada 2: Especificando un porcentaje de descuento diferente (15%)
    monto_compra_2 = 1200
    descuento_2 = calcular_descuento(monto_compra_2, 15)
    monto_final_2 = monto_compra_2 - descuento_2

    print(f"Compra 2 - Monto total: ${monto_compra_2}")
    print(f"Descuento aplicado: ${descuento_2}")
    print(f"Monto final a pagar: ${monto_final_2}")


if __name__ == "__main__":
    main()
