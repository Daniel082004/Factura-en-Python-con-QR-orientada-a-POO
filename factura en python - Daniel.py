import datetime
from tkinter.tix import ExFileSelectBox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class supermercado:
    
    def contraseña(Self):
        x = int(input("escriba la contraseña para poder facuturar: "))
        if x == 2426:
            print("contraseña correcta, continuemos")
        else:
            print("contraseña incorrecta, lo siento")
            exit()
            
    def datos(self):
        self.cliente = str(input("Nombre del cliente: "))
        self.cedula = int(input("Escriba la cedula del cliente: "))
    

    def productos(self):
        self.nombre = str(input("Escriba el nombre del producto: "))
        self.cantidad = int(input("Escriba la cantidad de productos que va a pagar: "))
        self.precio = float(input("Escriba el precio del producto: "))
        self.cajero = str(input("Escriba el nombre del Cajero: "))


    def mostrar(self):
        
        self.subtotal = self.cantidad * self.precio
        self.total = self.subtotal + (self.subtotal * .19)
        
        print("                            Hipermercado Dani ")
        print("                               Nit: 800542 ")
        print("                      Responsable de iva.    CIIU  1081")
        print("                              Tel: 3177905980 ")
        print("                         hipermercadodani@gmail.com ")
        print("                                 Neiva-Huila ")
        print("                                    Altico ")
        print("                --------------------------------------------")
        print("                           DIAN: 127867648746")
        print("                   Vigencia hasta:        31/12/2023")
        import time
        print("                   Fecha:                ",time.strftime("%d/%m/%y"))
        print("                   Hora:                 ",time.strftime("%I:%M:%S"))
        print("                --------------------------------------------")
        print("                        CAJERO:         ",self.cajero)
        print("                        CLIENTE:        ",self.cliente)
        print("                        CEDULA:         ",self.cedula)
        print("                --------------------------------------------")
        print("                 USD   PRODUC.DESCRIPCION   PRECIO   TOTAL")
        print("                ",self.cantidad,"      ",self.nombre,"  ",self.precio," ",self.subtotal )
        print("                --------------------------------------------")
        print("                ----------- DETALLE DE VALORES -------------")
        print("                                        SUBTOTAL: ","$",self.subtotal)
        print("                                        IVA:      ","$",self.subtotal * 0.19)
        print("                                        TOTAL :   ","$",self.total)
        print("                --------------------------------------------")
        print("                ------------- FORMA DE PAGO ----------------")
        print("                                EFECTIVO")
        print("                --------------------------------------------")
        print("                         ¡GRACIAS POR TU COMPRA!")
        print("                                   QR")
        print("                             VISITANOS JORGE")
        print("                --------------------------------------------")
        print("                   FACTURA GENERADA POR SOFTWARE DFAM_2004")
        print("                   PARA MAYOR INFORMACION, CONTACTENOS AL")
        print("                   hipermercadodani@gmail.com O AL 3177907")
    
    
    def PDF(self):
        w, h = letter
        c = canvas.Canvas("Factura.pdf")
        c.drawString(235,h -50,"              Hipermercado Dani")
        c.drawString(250,h -65,"                 Nit: 800542 ")
        c.drawString(220,h -80,"       Responsable de iva.    CIIU  1081")
        c.drawString(240,h -95,"               Tel: 3177905980 ")
        c.drawString(225,h -110,"          hipermercadodani@gmail.com ")
        c.drawString(250,h -125,"                 Neiva-Huila ")
        c.drawString(258,h -140,"                   Altico ")
        c.drawString(235,h -150," ---------------------------------------------------")
        c.drawString(220,h -170,"                    DIAN: 127867648746")
        c.drawString(240,h -190,"Vigencia hasta:           31/12/2023")
        c.drawString(240,h -205,f"Fecha:                        {datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year}")
        c.drawString(240,h -220,f"Hora:                          {datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}")
        c.drawString(235,h -235," ----------------------------------------------------")
        c.drawString(260,h -250,f"      CAJERO:         {self.cajero}")
        c.drawString(260,h -265,f"      CLIENTE:        {self.cliente}")
        c.drawString(260,h -280,f"      CEDULA:         {self.cedula}")
        c.drawString(235,h -295," ----------------------------------------------------")
        c.drawString(225,h -320," USD  DESCRIPCION  PRECIO  TOTAL")
        c.drawString(235,h -335,f" {self.cantidad}     {self.nombre}   {self.precio}  {self.subtotal}")
        c.drawString(235,h -350," ----------------------------------------------------")
        c.drawString(235,h -365," ----------------------------------------------------")
        c.drawString(250,h -380,f"                     SUBTOTAL:  ${self.subtotal}")
        c.drawString(250,h -395,f"                     IVA:               ${self.subtotal * 0.19}")
        c.drawString(248,h -410,f"                     TOTAL :         ${self.total}")
        c.drawString(235,h -420," ---------------------------------------------------")
        c.drawString(235,h -435," ---------- FORMA DE PAGO --------------")
        c.drawString(242,h -452,"                  EFECTIVO")
        c.drawString(235,h -462," ---------------------------------------------------")
        c.drawString(225,h -485,"           ¡GRACIAS POR TU COMPRA!")
        c.drawImage("Qr_super.png",290, h-600, width=100, height=100)
        c.drawString(230,h-625,"               ¡VISITANOS JORGE!")
        c.drawString(230,h-645," ----------------------------------------------------")
        c.save()
             
factura=supermercado()
factura.contraseña()
factura.datos()
factura.productos()
factura.mostrar()
factura.PDF()