"""Configura el repositorio del Grupo 4 en GitHub con la CLI `gh`.

Uso (desde la raíz del repositorio, con `gh auth login` hecho):

    python scripts/configurar_github.py            # solo muestra lo que haría
    python scripts/configurar_github.py --aplicar  # lo ejecuta

Crea las etiquetas, los hitos (H0 y H1), las incidencias de
docs/H0/tablero-inicial.csv y la protección de la rama main.
Antes de usarlo, rellenad USUARIOS con los nombres de usuario de GitHub.
Es opcional: todo se puede hacer a mano desde la web de GitHub.
"""

import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path

USUARIOS = {
    "José Luis Martínez Fernández": "",  # usuario de GitHub del Director
    "Antonio Jesús Cejudo Valero": "",  # usuario de GitHub del Analista
    "Antonio Chacón Durán": "",  # usuario de GitHub del Desarrollador
}

ETIQUETAS = {
    "analisis": "1D76DB",
    "diseno": "5319E7",
    "documentacion": "0E8A16",
    "gestion": "FBCA04",
    "repositorio": "B48A55",
    "calidad": "D93F0B",
}

HITOS = {
    "H0": ("H0 · Propuesta validada", "2026-11-20T23:59:00Z"),
    "H1": ("H1 · Diseño aprobado", "2026-12-14T23:59:00Z"),
}

APLICAR = "--aplicar" in sys.argv


def ejecutar(cmd):
    print("$ " + " ".join(cmd))
    if APLICAR:
        subprocess.run(cmd, check=True)


def main():
    raiz = Path(__file__).resolve().parent.parent
    for nombre, color in ETIQUETAS.items():
        ejecutar(["gh", "label", "create", nombre, "--color", color, "--force"])

    for titulo, fecha in HITOS.values():
        ejecutar(["gh", "api", "repos/{owner}/{repo}/milestones",
                  "-f", f"title={titulo}", "-f", f"due_on={fecha}"])

    with open(raiz / "docs" / "H0" / "tablero-inicial.csv", encoding="utf-8") as f:
        for fila in csv.DictReader(f):
            cmd = ["gh", "issue", "create",
                   "--title", fila["titulo"],
                   "--body", fila["descripcion"],
                   "--label", fila["etiqueta"],
                   "--milestone", HITOS[fila["hito"]][0]]
            usuario = USUARIOS.get(fila["responsable"], "")
            if usuario:
                cmd += ["--assignee", usuario]
            ejecutar(cmd)

    proteccion = {
        "required_status_checks": None,
        "enforce_admins": True,
        "required_pull_request_reviews": {"required_approving_review_count": 1},
        "restrictions": None,
    }
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as tmp:
        json.dump(proteccion, tmp)
    ejecutar(["gh", "api", "-X", "PUT", "repos/{owner}/{repo}/branches/main/protection",
              "--input", tmp.name])

    if not APLICAR:
        print("\nModo de prueba: no se ha cambiado nada. Añade --aplicar para ejecutarlo.")


if __name__ == "__main__":
    main()
