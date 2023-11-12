import time
from simulaciones import *
with st.sidebar:
    st.image("UPC.png")
    selected = option_menu("Menu principal", ["Inicio", 'Simulación A - Velocidad terminal',
                                              'Simulación B - Campo eléctrico', 'Simulación C - Interferencia de ondas',
                                              'Simulación D - Refracción de la luz'],
        icons=['house', 'droplet-half', 'lightning-fill', 'soundwave', 'search'], menu_icon="cast", default_index=0)
if selected == "Inicio":
    st.title("Trabajo Final del curso Física para Ciencias de la Computación")
    st.write(r'''
    El trabajo que presentamos en este informe representa una etapa importante en la evolución de los programas que 
    hemos desarrollado durante el curso de Física para Ciencias de la Computacion. A lo largo de esta experiencia 
    educativa, hemos trabajado para comprender y modelar diversos fenómenos físicos, desde los conceptos de Mecánica de
     fluidos hasta temas de Óptica. En este Trabajo final, estamos buscando consolidar y ampliar nuestros conocimientos 
     mediante la implementación de programas más completos y sin los errores señalados durante el ciclo académico.
    Nuestros programas previos tenían un objetivo claro: representar visualmente fenómenos físicos en función de 
    condiciones iniciales específicas. Utilizando gráficos en un plano XY, hemos logrado mostrar de manera efectiva el 
    comportamiento de estos fenómenos físicos, lo que ha resultado ser una herramienta valiosa para comprender y 
    comunicar principios fundamentales de la física. En este Trabajo final, aspiramos a mejorar nuestras simulaciones y
    análisis. No solo queremos mostrar los resultados de los fenómenos, sino también profundizar un poco más en el 
    proceso del modelado, las aproximaciones matemáticas y los métodos de resolución que empleamos. Además, la principal
    novedad respecto a nuestros trabajos anteriores es brindar la posibilidad de variar algunos de los parámetros a placer
    para obtener nuevas conclusiones. Por ejemplo, para la primera simulación al incrementar el radio de la esfera, la velocidad
    terminal es mayor y la esfera demora un mayor tiempo en alcanzarla y esto puede dar pie a nuevos análisis. Además, 
    se agregaron tablas comparativas, imagenes, gifs, entre otros recursos para lograr dar a entender mejor los fenómenos físicos estudiados.
    '''
    )
    st.image("fis.jpg")
if selected == "Simulación A - Velocidad terminal":
    st.header("Cálculo de la velocidad terminal en un fluido real")
    menu_sec('A')
if selected == "Simulación B - Campo eléctrico":
    st.header("Cálculo de la intensidad de campo eléctico generada por una barra cargada de longitud infinita")
    menu_sec('B')
if selected == "Simulación C - Interferencia de ondas":
    st.header("Representación de la interferencia de dos ondas y cálculo de la frecuencia de pulso")
    menu_sec('C')
if selected == "Simulación D - Refracción de la luz":
    st.header("Verificación de la Ley de Snell en refracción de la luz")
    menu_sec('D')



