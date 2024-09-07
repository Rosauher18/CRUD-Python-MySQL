import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='123456',
                db='universidad',
                charset='utf8',  # Forzar el uso de utf8
                use_unicode=True  # Usar unicode para las consultas
            )
            if self.conexion.is_connected():
                print(" ")
        except Error as ex:
            print('Error al intentar la conexion: {0}'.format(ex))
    def listarCursos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")  # query de selección
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print('Error al intentar ejecutar la consulta: {0}'.format(ex))
    def registrarCurso(self, curso):
       if self.conexion.is_connected():
           try:
               cursor = self.conexion.cursor()
               sql = "INSERT INTO cursos (codigo, nombre, creditos) VALUES ('{0}', '{1}', '{2}')"
               cursor.execute(sql.format(curso[0], curso[1], curso[2]))
               self.conexion.commit()
               print("\n")
               print("Curso registrado satisfactoriamente!\n")
           except Error as ex:
            print('Error al intentar la conexion: {0}'.format(ex))
    def actualizarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE cursos SET nombre = '{0}', creditos = '{1}' WHERE codigo = '{2}'"
                cursor.execute(sql.format(curso[1], curso[2], curso[0]))
                self.conexion.commit()
                print("Curso actualizado satisfactoriamente!")
            except Error as ex:
                print('Error al intentar la conexion: {0}'.format(ex))

    def eliminarCurso(self, codigoCursoEliminar):
         if self.conexion.is_connected():
             try:
               cursor = self.conexion.cursor()
               sql = "DELETE FROM cursos WHERE codigo = '{0}'"
               cursor.execute(sql.format(codigoCursoEliminar))
               self.conexion.commit()
               print("\n")
               print("Curso eliminado exitosamente!\n")
             except Error as ex:
               print('Error al intentar la conexion: {0}'.format(ex))
    
        
