from flask import Flask, send_file, request
import pandas as pd
import random
import io

app = Flask(__name__)

# Ruta principal para verificar que el servidor funciona
@app.route("/")
def home():
    return "Servidor UPSS funcionando correctamente"

def generar_dato():
    tipos = ["Ecógrafo","Rayos X","Tomógrafo","Resonancia","Densitómetro","Fluoroscopía"]
    incidentes = ["No enciende","Artefactos","Sobrecalentamiento","Error software","Fuga eléctrica","Ruido anormal"]
    riesgos = ["Bajo","Medio","Alto"]
    soporte = ["Disponible","Limitado","No disponible"]
    componentes = ["Fuente de poder","Transductor","Detector","Software","Cableado"]
    tipo_falla = ["Mecánica","Eléctrica","Electrónica","Software"]

    return {
        "Codigo": f"EQ-{random.randint(100,999)}",
        "Nombre": random.choice(tipos),
        "Fecha Adquisicion": f"20{random.randint(10,25)}-{random.randint(1,12)}-{random.randint(1,28)}",
        "Frecuencia Uso": random.randint(1,100),
        "Fallas Año": random.randint(0,10),
        "Frecuencia Fallas": random.randint(0,5),
        "Downtime": random.randint(0,200),
        "Tipo Equipo": random.choice(tipos),
        "Eficiencia Clinica": random.randint(50,100),
        "Obsolescencia": random.randint(1,10),
        "Costos": random.randint(10000,500000),
        "Mantenimiento": random.randint(1,12),
        "Riesgo Paciente": random.choice(riesgos),
        "Dificultad Centro": random.randint(1,5),
        "Disponibilidad Soporte": random.choice(soporte),
        "Ubicacion": "UPSS Diagnóstico por Imágenes",
        "Costo Reparaciones": random.randint(0,20000),
        "Uptime (hrs)": random.randint(1000,4000),
        "Downtime (hrs)": random.randint(0,200),
        "Costo Soles": random.randint(500,5000),
        "Incidente": random.choice(incidentes),
        "Severidad": random.choice(riesgos),
        "Componente Afectado": random.choice(componentes),
        "Tipo Falla": random.choice(tipo_falla)
    }

@app.route("/generar_csv")
def generar_csv():
    cantidad = int(request.args.get("cantidad", 1000))
    filas = [generar_dato() for _ in range(cantidad)]
    df = pd.DataFrame(filas)

    output = io.BytesIO()
    df.to_csv(output, index=False, encoding="utf-8")
    output.seek(0)

    return send_file(
        output,
        mimetype="text/csv",
        as_attachment=True,
        download_name=f"dataset_upss_{cantidad}.csv"
    )

# Render / Gunicorn NO usa this run block
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

