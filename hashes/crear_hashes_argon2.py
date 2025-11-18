#!/usr/bin/env python3
"""
Versión 2: misma lógica de contraseñas, pero usando executemany
para insertar todos los usuarios en un solo paso.
"""

import mysql.connector
from argon2 import PasswordHasher
from datetime import datetime

# ----------------------------
# Config Argon2id
# ----------------------------
ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=2,
    hash_len=32,
    salt_len=16
)

# ----------------------------
# Datos
# ----------------------------
rows = [
    ("user1", "Mi pez favorito, mi clado taxonomico favorito, un organulo de la celula vegetal"),
    ("user2", "cafe, libro, flor"),
    ("user3", "Apellido, DNI, numero de teléfono"),
    ("user4", "Pacopiso Marzo Cachivache"),
    ("user5", "Nala, Baskonia, Ribabellosa"),
    ("user6", "Barandiaran, Badaia, Alan"),
    ("user7", "Rueda, luz, puerta"),
    ("user8", "Julio, cerveza, fútbol."),
    ("user9", "Croqueta, fentanilo, Mariano"),
    ("user10", "Nombre de mi mascota, nombre de mi equipo de fútbol favorito, nombre de mi jugador favorito"),
    ("user11", "Baskonia, Mus, Gasteiz"),
    ("user12", "Robert, 26/04/2025, Porsche"),
    ("user13", "vitoria, 23, bocajr"),
    ("user14", "Animal,Año,NombreFamiliar"),
    ("user15", "Arrigo Opel Athletic"),
    ("user16", "Mus,Luis,Alaves"),
    ("user17", "cazador, Cuautepec, Bustamante."),
    ("user18", "Duke, Tías, Portátil"),
    ("user19", "Ordenador, letras, mascota"),
    ("user20", "Chivas, paraiso, acámbaro"),
    ("user21", "menditxo,unamuno,blackjack"),
    ("user22", "balón, poker, dinero"),
    ("user23", "Emi, rocallosas, 27/04/04"),
]

# ----------------------------
# Helpers
# ----------------------------
def split_into_three(raw_line: str):
    parts = [p.strip().strip(".") for p in raw_line.split(",")]
    parts = [p for p in parts if p != ""]
    if len(parts) == 3:
        return parts

    words = raw_line.replace(".", "").split()
    if len(words) >= 3:
        n = len(words)
        step = max(1, n // 3)
        a = " ".join(words[:step])
        b = " ".join(words[step: 2 * step])
        c = " ".join(words[2 * step:])
        return [a.strip(), b.strip(), c.strip()]

    return [raw_line, "", ""]


def make_password(parts):
    return "_".join(p.replace(" ", "") for p in parts)


def build_user_records():
    """
    Devuelve una lista de tuplas:
    (username, password_hash, created_at)
    lista lista para executemany.
    """
    records = []
    now = datetime.utcnow()
    for uid, raw in rows:
        parts = split_into_three(raw)
        password = make_password(parts)
        hashed = ph.hash(password)
        print(f"{uid}: {password} -> ARGON2ID OK")
        records.append((uid, hashed, now))
    return records

# ----------------------------
# Main
# ----------------------------
def main():
    # Conexión con context manager
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ciberseguridad"
    )

    cursor = conn.cursor()

    records = build_user_records()

    cursor.executemany(
    """
    INSERT IGNORE INTO users_argon2 (username, password_hash, created_at)
    VALUES (%s, %s, %s)
    """,
    records
)

    conn.commit()
    cursor.close()
    conn.close()
    print("\nTerminado (v2). Hashes Argon2id guardados en users_argon2.")


if __name__ == "__main__":
    main()