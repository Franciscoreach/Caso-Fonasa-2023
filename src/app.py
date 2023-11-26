#Importando Librerias
from flask import Flask
from flask import render_template, redirect, request, Response, session, url_for
from datetime import datetime

from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__, template_folder='templates')


app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='fonasa_bd'
app.config['MYSQL_CURSORCLASS']='DictCursor'
mysql=MySQL(app)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/perfil')
def perfil():
    return render_template("perfil.html")

@app.route('/nosotros')
def nosotros():
    return render_template("nosotros.html")

@app.route('/ubicanos')
def ubicanos():
    return render_template("ubicanos.html")


@app.route('/ingresopaciente')
def Ingresar_Paciente():
    cursor = mysql.connection.cursor()
    #cursor.execute("Select * FROM")
    return render_template("IngresoPaciente.html")

@app.route('/ingreso-pacienteNino')
def Ingresar_PacienteNino():
    return render_template('IngresoPacienteNino.html')


#Metodo Agregar Paciente Niño
@app.route('/ingreso-pacienteNinoADD', methods =['POST'])
def Ingresar_PacienteNinoADD():
    noHistoriaClinica = request.form['noHistoriaClinica']
    nombre = request.form['nombre']
    edad = request.form['edad']
    estatura = request.form['estatura']
    peso = request.form['peso'] 

    if noHistoriaClinica and nombre and edad and estatura and peso:
        if (int(edad)<=5 and int(edad)>=1):
            relacionPesoEstatura = int(peso) + int(estatura) + 3
            riesgo = (int(edad) * int(relacionPesoEstatura))/100
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO pninno (noHistoriaClinica,nombre,edad,estatura,peso,relacionPesoEstatura,riesgo) VALUES (%s, %s ,%s, %s ,%s,%s, %s)"
            dataN = (noHistoriaClinica, nombre, edad, estatura, peso, relacionPesoEstatura, riesgo)
            cursor.execute(sql, dataN)
            mysql.connection.commit()

            cursor2 = mysql.connection.cursor()
            prioridad = int(peso) + int(estatura) + 3
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad, prioridad, riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataP = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataP)
            mysql.connection.commit()

        if (int(edad)<=12 and int(edad)>=6):
            relacionPesoEstatura = int(peso) + int(estatura) + 2
            riesgo = (int(edad) * int(relacionPesoEstatura))/100
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO pninno (noHistoriaClinica,nombre,edad,estatura,peso,relacionPesoEstatura,riesgo) VALUES (%s, %s ,%s, %s ,%s,%s, %s)"
            dataN = (noHistoriaClinica, nombre, edad, estatura, peso, relacionPesoEstatura, riesgo)
            cursor.execute(sql, dataN)
            mysql.connection.commit()

            cursor2 = mysql.connection.cursor()
            prioridad = int(peso) + int(estatura) + 2
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad, prioridad, riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataP = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataP)
            mysql.connection.commit()

        if (int(edad)<=15 and int(edad)>=13):
            relacionPesoEstatura = int(peso) + int(estatura) + 1
            riesgo = (int(edad) * int(relacionPesoEstatura))/100
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO pninno (noHistoriaClinica,nombre,edad,estatura,peso,relacionPesoEstatura,riesgo) VALUES (%s, %s ,%s, %s ,%s,%s, %s)"
            dataN = (noHistoriaClinica, nombre, edad, estatura, peso, relacionPesoEstatura, riesgo)
            cursor.execute(sql, dataN)
            mysql.connection.commit()

            cursor2 = mysql.connection.cursor()
            prioridad = int(peso) + int(estatura) + 1
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad, prioridad, riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataP = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataP)
            mysql.connection.commit()

    return redirect(url_for('Listado_Pacientes_General'))




#----------------------------------------------------------------------------------------------------

@app.route('/ingreso-pacienteJoven')
def Ingresar_PacienteJoven():
    return render_template('IngresoPacienteJoven.html')

#Función Agregar Paciente Joven
@app.route('/ingreso-pacienteJovenADD', methods =['POST'])
def Ingresar_PacienteJovenADD():
    noHistoriaClinica = request.form['noHistoriaClinica']
    nombre = request.form['nombre']
    edad = request.form['edad']
    anosFumando = request.form['anosFumando']

    if noHistoriaClinica and nombre and edad and anosFumando:
        if  (int(edad)>= 16 and int(edad)<=40) and int(anosFumando)>0:
            fumador = 1 #Ingresa como boolean a la base de datos 1 = True
            prioridad = ((int(anosFumando)/4) + 3)
            riesgo = (int(edad) * int(prioridad))/100
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO pjoven (noHistoriaClinica,nombre,edad,fumador,prioridad,riesgo) VALUES (%s, %s ,%s, %s ,%s, %s)"
            dataP = (noHistoriaClinica, nombre, edad,fumador,prioridad,riesgo)
            cursor.execute(sql, dataP)
            mysql.connection.commit()

            cursor2 = mysql.connection.cursor()
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad,prioridad,riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataPa = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataPa)
            mysql.connection.commit()

        if  (int(edad)>= 16 and int(edad)<=40) and int(anosFumando)<=0:
            fumador = 0 #Ingresa como boolean a la base de datos 1 = True
            prioridad = 2
            riesgo = (int(edad) * int(prioridad))/100
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO pjoven (noHistoriaClinica,nombre,edad,fumador,prioridad,riesgo) VALUES (%s, %s ,%s, %s ,%s, %s)"
            dataP = (noHistoriaClinica, nombre, edad,fumador,prioridad,riesgo)
            cursor.execute(sql, dataP)
            mysql.connection.commit()

            cursor2 = mysql.connection.cursor()
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad,prioridad,riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataPa = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataPa)
            mysql.connection.commit()

    return redirect(url_for('Listado_Pacientes_General'))   


#----------------------------------------------------------------------------------------------------

#Función Agregar Paciente Anciano
@app.route('/ingreso-pacienteAnciano')
def Ingresar_PacienteAnciano():
    return render_template('IngresoPacienteAnciano.html')


#Función Agregar Paciente Anciano
@app.route('/ingreso-pacienteAncianoADD', methods =['POST'])
def Ingresar_PacienteAncianoADD():
    noHistoriaClinica = request.form['noHistoriaClinica']
    nombre = request.form['nombre']
    edad = request.form['edad']
    poseeDieta = request.form['poseeDieta']


    if noHistoriaClinica and nombre and edad and poseeDieta:

        if  int(edad)>=41 and poseeDieta == "Si":
            tieneDieta = 1 #Ingresa como boolean a la base de datos 1 = True
            prioridad = ((int(edad)/20) + 4)
            riesgo = ((int(edad) * int(prioridad))/100)+5.3
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO panciano (noHistoriaClinica,nombre,edad,tieneDieta,prioridad,riesgo) VALUES (%s, %s ,%s, %s ,%s,%s)"
            dataA = (noHistoriaClinica, nombre, edad, tieneDieta,prioridad,riesgo)
            cursor.execute(sql, dataA)
            mysql.connection.commit()
        
            cursor2 = mysql.connection.cursor()
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad,prioridad,riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataAn = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataAn)
            mysql.connection.commit()

        if  int(edad)>=41 and poseeDieta == "No":
            tieneDieta = 1 #Ingresa como boolean a la base de datos 1 = True
            prioridad = (int(edad)/30)+3
            riesgo = ((int(edad) * int(prioridad))/100)+5.3
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO panciano (noHistoriaClinica,nombre,edad,tieneDieta,prioridad,riesgo) VALUES (%s, %s ,%s, %s ,%s,%s)"
            dataA = (noHistoriaClinica, nombre, edad, tieneDieta,prioridad,riesgo)
            cursor.execute(sql, dataA)
            mysql.connection.commit()
        
            cursor2 = mysql.connection.cursor()
            sql2 = "INSERT INTO paciente (noHistoriaClinica,nombre,edad,prioridad,riesgo) VALUES (%s, %s ,%s, %s, %s)"
            dataAn = (noHistoriaClinica, nombre, edad, prioridad, riesgo)
            cursor2.execute(sql2, dataAn)
            mysql.connection.commit()


    return redirect(url_for('Listado_Pacientes_General'))  


#Función de Login
@app.route('/acceso-login', methods =["GET","POST"])
def acceso_login():
    if request.method == 'POST' and 'username' in request.form and 'password':
        _username = request.form['username']
        _password = request.form['password']

        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM usuario WHERE username = %s AND password = %s',(_username,_password,))
        account = cur.fetchone()
        if account:
            session['logueado'] = True
            session['id'] = account['id']
            return render_template('perfil.html')

        else:
            return render_template("login.html", mensaje="El usuario ingresado es incorrecto")


#Lectura de los datos del paciente para la consulta 
@app.route('/lista-pacientesGeneral')
def Listado_Pacientes_General():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM paciente ORDER BY prioridad DESC")
    dataPaciente = cursor.fetchall()
    #total = cursor.rowcount
    return render_template("listaPacienteGeneral.html", dataP = dataPaciente)

#Agregar una Consulta
@app.route('/ingreso-consultaADD', methods =['POST'])
def Ingresar_ConsultaADD():
    noHistoriaClinica = request.form['noHistoriaClinica']
    nombrePaciente = request.form['nombrePaciente']
    edad = request.form['edad']
    prioridad = request.form['prioridad']
    riesgo = request.form['riesgo'] 
    nombreEsp = request.form['nombreEsp'] 

    #Ingreso a consulta de Pediatria para Niños
    if noHistoriaClinica and nombrePaciente and edad and prioridad and riesgo and nombreEsp:
        if int(prioridad)<=4 and (int(edad)<=15 and int(edad)>=1):
            tipoConsulta = "Pedriatria"
            estado = "Desocupado"
            fechaConsulta = datetime.now()
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO consulta_paciente (noHistoriaClinica,nombrePaciente,edad,prioridad,riesgo,nombreEsp,fechaConsulta ,tipoConsulta,estado) VALUES ( %s ,%s, %s, %s ,%s,%s, %s, %s,%s)"
            dataPaci = (noHistoriaClinica,nombrePaciente,edad,prioridad,riesgo, nombreEsp,fechaConsulta ,tipoConsulta,estado)
            cursor.execute(sql, dataPaci)
            mysql.connection.commit()

    #Ingreso a Consulta CGI / Jovenes y Ancianos
        if (int(edad)>=16 and int(edad)<=100) and int(prioridad)<=4:
            tipoConsulta = "CGI"
            estado = "Desocupado"
            fechaConsulta = datetime.now()
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO consulta_paciente (noHistoriaClinica,nombrePaciente,edad,prioridad,riesgo,nombreEsp,fechaConsulta ,tipoConsulta,estado) VALUES ( %s ,%s, %s, %s ,%s,%s, %s, %s,%s)"
            dataPaci = (noHistoriaClinica,nombrePaciente,edad,prioridad,riesgo, nombreEsp,fechaConsulta ,tipoConsulta,estado)
            cursor.execute(sql, dataPaci)
            mysql.connection.commit()
        
    #Independiente de la edad se ingresa a Urgencia
        if  int(prioridad)>4:
            tipoConsulta = "Urgencia"
            estado = "Desocupado"
            fechaConsulta = datetime.now()
            cursor = mysql.connection.cursor()
            sql = "INSERT INTO consulta_paciente (noHistoriaClinica,nombrePaciente,edad,prioridad,riesgo,nombreEsp,fechaConsulta ,tipoConsulta,estado) VALUES ( %s ,%s, %s, %s ,%s,%s, %s, %s,%s)"
            dataPaci = (noHistoriaClinica,nombrePaciente,edad,prioridad,riesgo, nombreEsp,fechaConsulta ,tipoConsulta,estado)
            cursor.execute(sql, dataPaci)
            mysql.connection.commit()

    return redirect(url_for('Optimizar_Atencion'))

#Lectura de los pacientes para ser Atendidos 
@app.route('/lista-pacientesConsulta')
def Optimizar_Atencion():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM consulta_paciente ORDER BY prioridad DESC,fechaConsulta ASC, edad DESC")
    dataConsulta = cursor.fetchall()
    #total = cursor.rowcount
    return render_template("listaPacienteConsulta.html", dataP = dataConsulta)


#Editar Datos - Generar consulta
@app.route('/edit/<string:idConsulta>', methods=['POST'])
def Atender_Paciente(idConsulta):
        nombrePaciente = request.form['nombrePaciente']
        edad = request.form['edad']

        if nombrePaciente and edad:
            estado = "Ocupado"
            cursor = mysql.connection.cursor()
            sql = "UPDATE consulta_paciente SET nombrePaciente = %s, edad = %s,estado= %s  WHERE idConsulta = %s"
            dataU = (nombrePaciente, edad, estado, idConsulta)
            cursor.execute(sql, dataU)
            mysql.connection.commit()
            
        return redirect(url_for('Optimizar_Atencion'))


#Liberar Consultas
@app.route('/editEstadoConsulta', methods=['POST'])
def Liberar_Consultas():
    dataT = mysql.connection.cursor()
    dataT.execute ("SELECT * FROM consulta_paciente WHERE estado ='Ocupado'")
    dataUp = dataT.fetchall()

    if dataUp:
        cursor = mysql.connection.cursor()
        sql = "UPDATE consulta_paciente SET estado = 'Desocupado'"
        cursor.execute(sql)
        mysql.connection.commit()

    return redirect(url_for('Optimizar_Atencion'))

#Atender todas las Consultas
@app.route('/editEstadoConsultaD', methods=['POST'])
def Todas_Consultas():
    dataT = mysql.connection.cursor()
    dataT.execute ("SELECT * FROM consulta_paciente WHERE estado ='Desocupado'")
    dataUp = dataT.fetchall()
    
    if dataUp:
        cursor = mysql.connection.cursor()
        sql = "UPDATE consulta_paciente SET estado = 'Ocupado'"
        cursor.execute(sql)
        mysql.connection.commit()

    return redirect(url_for('Optimizar_Atencion'))
            


#Listado de los pacientes con Mayor Riesgo
@app.route('/lista-pacientesRiesgo')
def Listar_Pacientes_Mayor_Riesgo():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM paciente ORDER BY riesgo DESC")
    dataRiesgo = cursor.fetchall()
    #total = cursor.rowcount
    return render_template("listaPacientesRiesgo.html", dataR = dataRiesgo)


#Listado de Pacientes Fumadores Urgentes
@app.route('/lista-pacientesFumadores')
def Listar_Pacientes_Fumadores_Urgentes():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM pjoven WHERE fumador=1 ORDER BY prioridad DESC")
    dataConsulta = cursor.fetchall()
    #total = cursor.rowcount
    return render_template("listaPacientesFumadores.html", dataP = dataConsulta)

#Paciente más Anciano
@app.route('/lista-pacienteAnciano')
def Paciente_Mas_Anciano():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM panciano WHERE edad=(SELECT MAX(edad) FROM paciente)")
    dataEdad = cursor.fetchall()
    #total = cursor.rowcount

    return render_template("listaPacienteAnciano.html", dataR = dataEdad)



#Consulta con mas Pacientes Atendido Pediatria - CGI - Urgencia
@app.route('/lista-masConsulta')
def Consulta_mas_Pacientes_Atendidos():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT tipoConsulta, COUNT(*) AS cantidad FROM consulta_paciente GROUP BY tipoConsulta HAVING COUNT(*) ORDER BY cantidad DESC")
    dataEdad = cursor.fetchall()
    #total = cursor.rowcount

    return render_template("listaMasConsulta.html", dataR = dataEdad)



if __name__ == '__main__':
    app.secret_key='8mQ&g*1GdXrT"kX'
    app.run(debug=True,port=5000, threaded=True)


