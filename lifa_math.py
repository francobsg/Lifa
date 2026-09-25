import sympy as sp

def resolver_matematica(expresion: str):
    """
    Resuelve expresiones matemáticas o despeja ecuaciones simples.
    """
    try:
        # Reemplazamos símbolos comunes de texto a sintaxis de Python/Sympy
        expresion = expresion.replace("^", "**").replace("=", "-")
        
        # Convertimos el texto a una expresión simbólica
        expr_simbolica = sp.sympify(expresion)
        
        # Intentamos resolverla (si es una ecuación igualada a 0) o evaluarla
        if expr_simbolica.free_symbols:
            # Si tiene variables como 'x', intentamos despejarla
            solucion = sp.solve(expr_simbolica)
            resultado = f"El resultado para la variable es: {solucion}"
        else:
            # Si son solo números, calculamos el valor exacto
            resultado = f"El resultado es: {sp.N(expr_simbolica, 4)}" # 4 decimales max
            
        return {
            "status": "success",
            "expresion_original": expresion,
            "mensaje": resultado
        }
    except Exception as e:
        return {"status": "error", "mensaje": "No pude resolver esa expresión. Asegúrate de usar números y variables claras (ej. 'x**2 - 4 = 0')."}

# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    print("=== PROBANDO MÓDULO MATEMÁTICO ===")
    print(resolver_matematica("x^2 - 4 = 0")["mensaje"])
    print(resolver_matematica("150 * 0.15")["mensaje"])