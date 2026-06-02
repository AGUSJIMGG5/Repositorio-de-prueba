import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def ayuda(ctx):
    await ctx.send(f'Para usar este bot puedes usar los siguientes comandos:\n$hello\n$tips\n$consecuencias\n$tips2\n$consecuencias2\n$tips3\n$consecuencias3')

@bot.command()
async def tips(ctx):
    listatips = [
        "Recicla papel, plástico y vidrio.",
        "Usa menos bolsas plásticas.",
        "Apaga luces y aparatos que no uses.",
        "No tires basura en calles o ríos.",
        "Reutiliza objetos antes de botarlos.",
        "Evita quemar basura.",
        "Ahorra agua en casa." ]
    
    await ctx.send(random.choice(listatips))

@bot.command()
async def consecuencias(ctx):
    listacontaminacion = [
        "El calentamiento global aumenta.",
        "La contaminacion empeora enfermedades en el aire.",
        "Los animales marinos son dañados por los plasticos.",
        "Los bosques y ecosistemas se destruyen.",
        "El agua contaminada afecta a personas y animales inocentes.",
        "El cambio climatico empeora.",
        "Puede provocar escasez de agua limpia."
    ]

    await ctx.send(random.choice(listacontaminacion))

@bot.command()
async def tips2(ctx):
    tips2texto = (
        "Uso del transporte público y utilización del coche privado solo cuando sea completamente necesario. Alternativamente, se puede compartir coches privados entre varias personas. Cuantos menos coches, menos emisiones."
        "Elegir, a la hora de comprar el coche, un modelo de bajo consumo energético."
        "Llevar a revisión de manera anual el coche para comprobar que el vehículo no contamina más de lo permitido. Un coche en buen estado siempre contaminará menos."
        "Por descontado, todo desplazamiento que se pueda realizar en bicicleta o andando es menos contaminante que cualquier coche."
        "Reciclar no solo disminuye la cantidad de basura que hay en el planeta, también ayuda a mantener la calidad del aire: se aprovechan los recursos y de esa manera se reduce considerablemente los procesos de fabricación que generan gases nocivos para la atmósfera."
    )

    await ctx.send(tips2texto)

    imagen = discord.File("imagenes3/tips.jpg")
    await ctx.send(file=imagen)

@bot.command()
async def consecuencias2(ctx):
    contaminacion2 = (
        "La contaminación del aire es el principal riesgo ambiental.  "
        "También influyen otros factores como los contaminantes del agua de consumo, la contaminación interior (por ejemplo, la exposición pasiva al humo del tabaco) o de compuestos orgánicos y sustancias químicas.  "
        "En 2016 cerca de 7 millones de muertes prematuras fueron consecuencia de la contaminación, según la Organización Mundial de la Salud (OMS). Estas muertes fueron resultado sobre todo de enfermedades respiratorias y cardiovasculares como consecuencia de la polución del aire. "
        "La exposición a la contaminación atmosférica tiene consecuencias muy variadas: enfermedades cardíacas, cáncer de pulmón, mayor riesgo de enfermedades cerebrales y respiratorias… "
        "Los principales afectados por la contaminación son los niños, las personas mayores y las mujeres embarazadas, así como trabajadores (exposición ocupacional por el tipo de trabajo que se realiza) y los enfermos crónicos. "
    )

    await ctx.send(contaminacion2)

    imagen = discord.File("imagenes3/contaminacion.jpg")
    await ctx.send(file=imagen)

@bot.command()
async def consecuencias3(ctx):
    consecuencias3texto = (
        "Puede existir diferentes tipos de contaminación en el propio hogar. "
         "El uso de combustibles fósiles es la principal causa de contaminación del aire. "
         "En los últimos años, de forma anual, 1,3 millones de personas pierden la vida por efectos secundarios de la contaminación. "
         "Las personas que residen en ciudades son más propensas a padecer enfermedades cardíacas, problemas respiratorios y alergias."
    )

    await ctx.send(consecuencias3texto)
    await ctx.send("https://cdn0.ecologiaverde.com/es/posts/5/8/2/contaminacion_del_suelo_causas_consecuencias_y_soluciones_285_1200.jpg")

@bot.command()
async def tips3(ctx):
    tips3texto = (
        "Usar espráis que sean respetuosos con el medio ambiente y no generen gases invernadero."
         "Cuidar las zonas verdes de las ciudades: muchas o pocas, funcionan como el pulmón de oxígeno de los núcleos urbanos. No generan tanto oxígeno como en el campo, pero pueden ayudar a absorber CO2."
         "En casa, utiliza bombillas de bajo consumo: con ello lograrás tener la misma luz a través del uso de energía eficiente."
         "No derroches agua: en Fundación Aquae tenemos varios consejos al respecto que lo explican ampliamente, pero resumiendo: ducharse y no bañarse, tener un sistema de doble descarga en la cisterna del baño o cerrar los grifos cuando no estés usando el agua."
         "Consumir productos sostenibles y reducir la carne en la dieta son dos formas de evitar la sobreproducción de alimentos y, por tanto, de reducir las emisiones."
    )

    await ctx.send(tips3texto)
    await ctx.send("https://cdn.prod.website-files.com/69df751c27fd89a1aa9d21d8/69fbb4315c605c72d9f575ee_Banner-EvitarContaminacion.jpeg")


bot.run("")