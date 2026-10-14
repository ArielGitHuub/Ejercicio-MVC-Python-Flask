from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
import os

app = Flask(__name__, template_folder='template')

# Configuración de base de datos
app.config['SECRET_KEY'] = 'super_clave_segura_2026'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///sistema_bonos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ==========================================
# MODELOS (La "M" de MVC)
# ==========================================
class Vendedor(db.Model):
    __tablename__ = 'vendedores'
    id_vendedor = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(120))
    apellidos = db.Column(db.String(120))
    facturas = db.relationship('Factura', backref='vendedor')

class Factura(db.Model):
    __tablename__ = 'facturas'
    id_factura = db.Column(db.Integer, primary_key=True)
    vendedor_id = db.Column(db.Integer, db.ForeignKey('vendedores.id_vendedor'))
    total_facturado = db.Column(db.Float)
    fecha_emision = db.Column(db.Date)

# Lógica de Negocio
def calcular_comision(monto_total):
    if monto_total >= 1500:
        return monto_total * 0.18
    elif monto_total >= 1000:
        return monto_total * 0.15
    elif monto_total >= 750:
        return monto_total * 0.10
    elif monto_total >= 400:
        return monto_total * 0.05
    return 0.0

def cargar_datos_iniciales():
    if Vendedor.query.count() == 0:
        equipo = [
            Vendedor(nombres="Juan", apellidos="Pérez"),
            Vendedor(nombres="Ana", apellidos="Martínez"),
            Vendedor(nombres="Carlos", apellidos="Gómez"),
            Vendedor(nombres="Lucía", apellidos="Sánchez"),
            Vendedor(nombres="Pedro", apellidos="Ramírez")
        ]
        db.session.add_all(equipo)
        db.session.commit()

    if Factura.query.count() == 0:
        ventas_demo = [
            Factura(vendedor_id=1, total_facturado=200.0, fecha_emision=datetime(2026, 5, 12)),
            Factura(vendedor_id=1, total_facturado=850.0, fecha_emision=datetime(2026, 6, 18)),
            Factura(vendedor_id=2, total_facturado=350.0, fecha_emision=datetime(2026, 7, 5)),
            Factura(vendedor_id=2, total_facturado=450.0, fecha_emision=datetime(2026, 8, 22)),
            Factura(vendedor_id=3, total_facturado=120.0, fecha_emision=datetime(2026, 5, 30)),
            Factura(vendedor_id=3, total_facturado=90.0,  fecha_emision=datetime(2026, 9, 14)),
            Factura(vendedor_id=4, total_facturado=500.0, fecha_emision=datetime(2026, 10, 2)),
            Factura(vendedor_id=4, total_facturado=600.0, fecha_emision=datetime(2026, 10, 10)),
            Factura(vendedor_id=5, total_facturado=300.0, fecha_emision=datetime(2026, 8, 11)),
            Factura(vendedor_id=5, total_facturado=1100.0, fecha_emision=datetime(2026, 9, 25))
        ]
        db.session.add_all(ventas_demo)
        db.session.commit()

# ==========================================
# CONTROLADORES (La "C" de MVC)
# ==========================================
@app.route('/')
def inicio():
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    return render_template('formulario_busqueda.html', max_date=fecha_hoy)

@app.route('/comisiones', methods=['POST'])
def mostrar_comisiones():
    fecha_hoy = datetime.now().strftime("%Y-%m-%d")
    f_inicio_str = request.form.get('fecha_inicio')
    f_fin_str = request.form.get('fecha_fin')
    
    try:
        fecha_inicio = datetime.strptime(f_inicio_str, "%Y-%m-%d")
        fecha_fin = datetime.strptime(f_fin_str, "%Y-%m-%d")
        fecha_limite = datetime.now()
        
        if fecha_inicio > fecha_fin:
            return render_template('formulario_busqueda.html', error="La fecha de inicio no puede ser mayor a la de fin.", max_date=fecha_hoy)
            
        if fecha_fin > fecha_limite or fecha_inicio > fecha_limite:
            return render_template('formulario_busqueda.html', error="No se permiten fechas futuras.", max_date=fecha_hoy)
            
    except ValueError:
        return render_template('formulario_busqueda.html', error="Las fechas no son válidas.", max_date=fecha_hoy)

    resultados_query = (
        db.session.query(
            Vendedor.nombres,
            Vendedor.apellidos,
            func.sum(Factura.total_facturado).label('suma_ventas')
        )
        .join(Factura)
        .filter(Factura.fecha_emision.between(fecha_inicio, fecha_fin))
        .group_by(Vendedor.id_vendedor)
        .all()
    )

    resumen = []
    for r in resultados_query:
        comision = calcular_comision(r.suma_ventas)
        resumen.append({
            "nombre": r.nombres,
            "apellido": r.apellidos,
            "total_ventas": r.suma_ventas,
            "comision": comision
        })

    return render_template('comision.html', comision=resumen, inicio=f_inicio_str, fin=f_fin_str)

# MAIN
if __name__ == '__main__':
    with app.app_context():
        # Previene el error WinError 32 al recargar
        db.drop_all()
        db.create_all()
        cargar_datos_iniciales()
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))