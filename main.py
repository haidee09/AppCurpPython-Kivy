from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import string
import random
class CGridLayout(GridLayout):
    def inicializar(self,apepaterno,apematerno,nombre,anio):
        self.apePat=apepaterno.upper()
        self.apeMat=apematerno.upper()
        self.nom=nombre.upper()
        self.curp=""
        self.nombrepila=""
        self.listanombres=[]
        self.mesesnombres=["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"]
        self.mesesnum=["01","02","03","04","05","06","07","08","09","10","11","12"]
        self.vocales=['A','E','I','O','U']
        self.consonantes=['B','C','D','F','G','H','J','K','L','M','N','Ñ','P','Q','R','S','T','V','W','X','Y','Z']
        self.mesfinal=""
        self.anio=anio.upper()
        self.calcular()
        self.s=""

    def getValueSpinnerDia(self, spinnner, text):
        """
        Se obtiene el valor de spinner dia
        """
        dia1=text
        self.dia=dia1

    def getValueSpinnerMes(self, spinner, text):
        """
        Se obtiene el valor de spinner mes
        """
        mes1=text
        self.mes=mes1

    def getValueSpinnerEntidad(self, spinner, text):
        """
        Se obtiene el valor de spinner entidad
        """
        entidad1=text
        self.entidad=entidad1

    def getValueCheckbox(self, value):
        """
        Se obtiene el valor de checkbox sexo
        """
        sex=value
        self.s=sex

    def calcular(self):

        #DIVIDIR EL NOMBRE , PARA GUARDAR EN UNA LISTA LOS NOMBRES:
        self.listanombres=self.nom.split(" ")
        print(self.listanombres)

        #ADJUNTAR PRIMERA LETRA DEL PRIMER APELLIDO
        self.curp +=self.apePat[0:1]

        #ENCONTRAR PRIMERA VOCAL DEL PRIMER APELLIDO

        j=1
        primervocal=False
        while j<len(self.apePat) and primervocal==False:
            vocal = self.apePat[j]
            for v in self.vocales:
                if v == vocal:
                    primervocal=True
            j+=1
        self.curp += vocal
        #ADJUNTAMOS LA INICIAL DEL SEGUNDO APELLIDO
        self.curp += self.apeMat[0:1]

        #ADJUNTAMOS LA INICIAL DEL NOMBRE
        #CONDICIONES PARTICULARES PARA SABER QUE NOMBRE TOMAR
        i=0
        bandera=False
        while i<len(self.listanombres) and bandera==False:
            #Si el unico nombre es JOSE
            if self.listanombres[i]=="JOSE" and ((self.listanombres[i+1]=="" or self.listanombres[i+1]==None) and (self.listanombres[i+2]=="" or self.listanombres[i+2]==None) and (self.listanombres[i+3]=="" or self.listanombres[i+3]==None)):
                self.nombrepila=self.listanombres[i]
            #Si el primer nombres es Jose y hay mas nombres, que tome el segundo
            elif self.listanombres[i]=="JOSE" and self.listanombres[i+1]!="":
                self.nombrepila = self.listanombres[i+1]
            #Analizar si MARIA es el unico nombre si es asi, se toma el nombre de Maria
            elif self.listanombres[i]=="MARIA" and ((self.listanombres[i+1]=="" or self.listanombres[i+1]==None) and (self.listanombres[i+2]=="" or self.listanombres[i+2]==None) and (self.listanombres[i+3]=="" or self.listanombres[i+3]==None)):
                self.nombrepila=self.listanombres[i]
            #Analizar si en el nombre se encuentra el nombre de MARIA DE LOS, si es asi, toma el cuarto nombre
            elif self.listanombres[i]=="MARIA" and self.listanombres[i+1]=="DE" and self.listanombres[i+2]=="LOS":
                self.nombrepila = self.listanombres[i+3]
            #Analizar si en el nombre se encuentra el nombre de MARIA DE LA, si es asi, toma el cuarto nombre
            elif self.listanombres[i]=="MARIA" and self.listanombres[i+1]=="DE" and self.listanombres[i+2]=="LA":
                self.nombrepila = self.listanombres[i+3]
            #Analizar si en el nombre aparece el nombre de MARIA DEL entonces toma el tercer nombre
            elif self.listanombres[i]=="MARIA" and self.listanombres[i+1]=="DEL":
                self.nombrepila = self.listanombres[i+2]
            #Analizar si en el nombre aparece MARIA DE, entonces toma el tercer nombre, siempre y cuando en este no aparezcan los nombres LA, LOS
            elif self.listanombres[i]=="MARIA" and self.listanombres[i+1]=="DE" and self.listanombres[i+2]!="LA" and self.listanombres[i+2]!="LOS":
                self.nombrepila = self.listanombres[i+3]
            #Analizar si tiene mas de 2 nombres y el primero es MARIA, entonces toma el segundo
            elif self.listanombres[i]=="MARIA" and self.listanombres[i+1]=="DE" and self.listanombres[i+2]!="DEL":
                self.nombrepila = self.listanombres[i+1]
            else:
                bandera=True
            i+=1

        if bandera:
            self.nombrepila = self.listanombres[0]
        #ADJUNTAR NOMBRE DE PILA AL CURP UNA VEZ ANALIZADAS LAS CONDICIONES
        self.curp += self.nombrepila[0:1]

        #ADJUNTAMOS el AÑO, MES ,DIA DE NACIMIENTO
        #----------------------AÑO--------------
        self.curp += self.anio[2:]
        #--------------------MES-----------------------------
        for m in range(0,len(self.mesesnombres)):
            if self.mesesnombres[m]==self.mes:
                pos=m
        self.mesfinal=self.mesesnum[pos]
        self.curp += self.mesfinal
        #---------------------DIA----------------------
        self.curp += self.dia

        #ADJUNTAMOS EL SEXO DE LA PERSONA , H -HOMBRE, M-MUJER

        self.curp += self.s

        #ADJUTAMOS  LA CLAVE DELA ENTIDAD FEDERATIVA DE nacimiento
        estado={
            'AGUASCALIENTES':'AS', 'BAJA CALIFORNIA':'BC', 'BAJA CALIFORNIA SUR':'BS','CAMPECHE':'CC',
            'COAHUILA DE ZARAGOZA':'CL','COLIMA':'CM','CHIAPAS':'CS','CHIHUAHUA':'CH','DISTRITO FEDERAL':'DF',
            'DURANGO':'DG','GUANAJUATO':'GT','GUERRERO':'GR','HIDALGO':'HG','JALISCO':'JC','ESTADO DE MEXICO':'MC',
            'MICHOACAN DE OCAMPO':'MN','MORELOS':'MS','NAYARIT':'NT','NUEVO LEON':'NL','OAXACA':'OC','PUEBLA':'PL',
            'QUERETARO DE ARTEAGA':'QT','QUINTANA ROO':'QR','SAN LUIS POTOSI':'PT','SINALOA':'SL','SONORA':'SR',
            'TABASCO':'TC','TAMAULIPAS':'TS','TLAXCALA':'TL','VERAZCRUZ':'VZ','YUCATAN':'YN','ZACATECAS':'ZS',
            'EXTRANEJERO':'NE'
        }
        self.curp += estado[self.entidad]

        #Primera consonante interna (no inicial) del primer apellido.
        j=1
        primerconsonante=False
        while j<len(self.apePat) and primerconsonante==False:
            consonante = self.apePat[j]
            for c in self.consonantes:
                if c == consonante:
                    primerconsonante=True
            j+=1
        #if consonante=='Ñ':
        #    self.curp += 'X'
        #else:
        self.curp += consonante

        #Primera consonante interna (no inicial) del segundo apellido.
        j=1
        segunda_consonante=False
        while j<len(self.apeMat) and segunda_consonante==False:
            consonante2 = self.apeMat[j]
            for c in self.consonantes:
                if c == consonante2:
                    segunda_consonante=True
            j+=1
        #if consonante2=='Ñ':
        #    self.curp += 'X'
        #else:
        self.curp += consonante2

        #Primer consonante no inicial del nombre de pila
        j=1
        consonantenombre=False
        while j<len(self.nombrepila) and consonantenombre==False:
            consonantenom = self.nombrepila[j]
            for c in self.consonantes:
                if c == consonantenom:
                    consonantenombre=True
            j+=1
        #if consonantenom=='Ñ':
        #    self.curp += 'X'
        #else:
        self.curp += consonantenom

        #ULTIMOS DOS DIGITOS dígito del 0-9 para fechas de nacimiento hasta el año 1999 y A-Z para fechas de nacimiento a partir del 2000.
        #------Primer digito al azar--------
        def id_generator(size=1, chars=string.ascii_uppercase):#+ string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        if(int(self.anio)<2000):
            digito1=random.randrange(10)
        else:
            digito1=id_generator(1)

        self.curp += str(digito1)

        #------Segundo digito al azar--------
        digito2=random.randrange(10)
        self.curp += str(digito2)

        #VERIFICAR AL FINAL SI EXISTE UN A Ñ EN EL CURP SI ES ASI CAMBIARLA
        curptem=list(self.curp)
        for i in range(0,len(curptem)):
            if curptem[i]=="Ñ":
                self.curp[i:i+1]="X"
        #SE NECESITA HACER CONVERTIR CURP DE CADENA A LISTA ASÍ SE ELIMINARIAN LAS CONDICIONES DESPUES DE ENCONTRAR CADA CONSONANTE

        #VERIFICAR LO DE LAS PALABRAS ALTISONANTES
        inconvenientes = ['BACA', 'LOCO', 'BUEI', 'BUEY', 'MAME', 'CACA', 'MAMO',
            'CACO', 'MEAR', 'CAGA', 'MEAS', 'CAGO', 'MEON', 'CAKA', 'MIAR', 'CAKO', 'MION',
            'COGE', 'MOCO', 'COGI', 'MOKO', 'COJA', 'MULA', 'COJE', 'MULO', 'COJI', 'NACA',
            'COJO', 'NACO', 'COLA', 'PEDA', 'CULO', 'PEDO', 'FALO', 'PENE', 'FETO', 'PIPI',
            'GETA', 'PITO', 'GUEI', 'POPO', 'GUEY', 'PUTA', 'JETA', 'PUTO', 'JOTO', 'QULO',
            'KACA', 'RATA', 'KACO', 'ROBA', 'KAGA', 'ROBE', 'KAGO', 'ROBO', 'KAKA', 'RUIN',
            'KAKO', 'SENO', 'KOGE', 'TETA', 'KOGI', 'VACA', 'KOJA', 'VAGA', 'KOJE', 'VAGO',
            'KOJI', 'VAKA', 'KOJO', 'VUEI', 'KOLA', 'VUEY', 'KULO', 'WUEI', 'LILO', 'WUEY',
            'LOCA']
        if self.curp[:4] in inconvenientes:
            self.curp=self.curp[:1] + 'X' + self.curp[2:]

        #ENVIO DE CURP AL TEXTINPUT
        self.display.text=self.curp

class CurpApp(App):
    def build(self):
        return CGridLayout()

CurpApp().run()
