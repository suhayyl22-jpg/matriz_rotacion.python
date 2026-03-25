import numpy as np

print("====================================")
print(" T3: MATRICES ESPECIALES ")
print("====================================\n")

# =====================================================
# 🔹 1. MATRICES ROTACIONALES (3 EJERCICIOS)
# =====================================================
print("====================================")
print(" MATRICES ROTACIONALES ")
print("====================================\n")

def matriz_rotacion(theta):
    print(f"Ángulo θ = {theta} radianes")
    print("Fórmula:")
    print("[ cosθ  -senθ ]")
    print("[ senθ   cosθ ]\n")
    
    R = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])
    
    print("Reemplazando valores:")
    print(R)
    
    # Verificación: R^T * R = I
    verificacion = np.dot(R.T, R)
    print("\nVerificación (R^T * R):")
    print(verificacion)
    print("Resultado: Es matriz ortogonal (rotacional)\n")
    return R

# Ejercicio 1
print("Ejercicio 1:")
R1 = matriz_rotacion(np.pi/6)

# Ejercicio 2
print("Ejercicio 2:")
R2 = matriz_rotacion(np.pi/4)

# Ejercicio 3
print("Ejercicio 3:")
R3 = matriz_rotacion(np.pi/2)


# =====================================================
# 🔹 2. MATRICES SIMÉTRICAS (3 EJERCICIOS)
# =====================================================
print("====================================")
print(" MATRICES SIMÉTRICAS ")
print("====================================\n")

def verificar_simetrica(M):
    print("Matriz:")
    print(M)
    
    print("\nPaso 1: Hallar la transpuesta (M^T)")
    MT = M.T
    print(MT)
    
    print("\nPaso 2: Comparar M con M^T")
    if np.array_equal(M, MT):
        print("M = M^T → Es SIMÉTRICA")
    else:
        print("No es simétrica")
    print()

# Ejercicio 1
print("Ejercicio 1:")
S1 = np.array([[2,1,3],
               [1,5,4],
               [3,4,6]])
verificar_simetrica(S1)

# Ejercicio 2
print("Ejercicio 2:")
S2 = np.array([[4,2,0],
               [2,3,1],
               [0,1,5]])
verificar_simetrica(S2)

# Ejercicio 3
print("Ejercicio 3:")
S3 = np.array([[1,0,2],
               [0,7,3],
               [2,3,9]])
verificar_simetrica(S3)


# =====================================================
# 🔹 3. MATRICES ANTISIMÉTRICAS (3 EJERCICIOS)
# =====================================================
print("====================================")
print(" MATRICES ANTISIMÉTRICAS ")
print("====================================\n")

def verificar_antisimetrica(M):
    print("Matriz:")
    print(M)
    
    print("\nPaso 1: Hallar la transpuesta (M^T)")
    MT = M.T
    print(MT)
    
    print("\nPaso 2: Verificar si M = -M^T")
    if np.array_equal(M, -MT):
        print("M = -M^T → Es ANTISIMÉTRICA")
    else:
        print("No es antisimétrica")
    print()

# Ejercicio 1
print("Ejercicio 1:")
A1 = np.array([[0, 2, -1],
               [-2, 0, 3],
               [1, -3, 0]])
verificar_antisimetrica(A1)

# Ejercicio 2
print("Ejercicio 2:")
A2 = np.array([[0, 5, -4],
               [-5, 0, 2],
               [4, -2, 0]])
verificar_antisimetrica(A2)

# Ejercicio 3
print("Ejercicio 3:")
A3 = np.array([[0, 1, 2],
               [-1, 0, 3],
               [-2, -3, 0]])
verificar_antisimetrica(A3)
