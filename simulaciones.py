import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from scipy.constants import pi, g
from streamlit_option_menu import option_menu
import pandas as pd
from numpy import cos
from scipy.signal import find_peaks
from matplotlib.animation import FuncAnimation
import streamlit.components.v1 as components
from numpy import sqrt
import matplotlib.ticker as ticker
from matplotlib.ticker import FuncFormatter
def menu_sec(tipo_sim):
    selected_2 = option_menu(
        menu_title=None,
        options=["Planteamiento general del problema y solución", "Ejecución de la simulación del fenómeno físico"],
        icons=["file-earmark-text", "lightbulb"],
        default_index=0,
        orientation="horizontal"
    )
    if selected_2 == "Planteamiento general del problema y solución":
        prob(tipo_sim)
    if selected_2 == "Ejecución de la simulación del fenómeno físico":
        mostrar_sim(tipo_sim)


def prob(tipo_sim):
    if tipo_sim == 'A':
        st.subheader("Contexto y objetivo de la simulación")
        st.write("Para el presente trabajo se debe simular el movimiento de una esfera de vidrio al dejarla caer sobre "
                 "un fluido viscoso, en este caso la glicerina. Luego de soltar la esfera, esta se desplazará hacia "
                 "abajo por su "
                 "gravedad pero el fluido mostrara una oposición a dicho movimiento a través de la fuerza de empuje "
                 "según el principio de Arquimedes y también una fuerza de arrastre por la propiedad viscosa del líquido."
                 " La teoría dice que, con el paso del tiempo, la velocidad de la esfera se irá acercando hacia una "
                 "velocidad límite llamada 'velocidad terminal'. El objetivo es comprobar si este comportamiento "
                 "ocurre y además calcular dicha velocidad límite.")
        st.subheader("Problema propuesto")
        st.write("Al realizar el análisis de fuerzas para la esfera según la Segunda ley de Newton se puede establecer:")
        st.image("term_1.png")
        st.latex(r'''
            \sum_{} \vec{F} = m \cdot \vec{a}
            \newline
            m \cdot \vec{g} + \vec{E} + \vec{F_v} = m \cdot \vec{a}
            ''')
        st.write("La fricción del líquido, según la Ley de Stokes, depende de la velocidad. Así que es conveniente "
                 "representar la aceleracion como la derivada de la velocidad respecto al tiempo para obtener una "
                 "ecuacion diferencial en función de la velocidad.")
        st.latex(r'''
            -m \cdot g + \rho_L \cdot g \cdot V_e + 6 \pi \cdot R_e \cdot \eta \cdot v = -m \cdot \frac{dv}{dt} 
            \newline
            \frac{dv}{dt} = g \cdot ( 1 - \frac{\rho_L}{\rho_e} ) - \frac{6 \pi \cdot R_e \cdot \eta}{m} \cdot v
            ''')
        st.write("Se le solicita a usted como estudiante, encontrar el valor de las velocidades a lo largo del tiempo"
                 " y plasmarlos en una grafica. A partir de ello concluya si la velocidad tiende a algún valor límite"
                 " y hállelo. Luego compárelo con el siguiente valor teórico con su porcentaje de error asociado.")
        st.latex(r'''
                    v_t = \frac{2}{9} \cdot \frac{R_e^2 \cdot g}{\eta} \cdot ( \rho_e - \rho_L )
                    ''')
        st.write("Considere los siguientes parametros:")
        st.image("term_2.png")
        with st.expander("Análisis del problema y planteamiento general de la solución propuesta"):
            st.write("Antes de empezar la solución del problema, hay que considerar que la velocidad en el instante "
                     "t=0 es 0. Esto se debe a que la esfera se suelta sin ninguna velocidad inicial. La ecuacion "
                     "diferencial nos permite relacionar la derivada de la velocidad y la velocidad. Por lo tanto, se"
                     " puede lograr una aproximación interesante con el método de las diferencias finitas. La idea de "
                     "esto es considerar puntos finitos muy cercanos entre sí, por ejemplo puntos en el eje x separados "
                     "0.0001. Aproximadamente, la derivada en un punto (x0,y0), puede hallarse como la pendiente entre los "
                     "puntos (x0,y0) y (x1,y1) debido a que son puntos muy cercanos. Es decir, si tenemos la pendiente y el punto"
                     " inicial (x0,y0) podemos hallar aproximadamente y1.")
            st.image("term_4.jpg")


            st.write("Por lo cual nuestro programa consta de 2 funciones principales que ayudaran al cálculo. "
                     "La primera función permite calcular la derivada de la velocidad "
                     "en funcion de una velocidad pasada como parámetro, esto puede lograrse directamente gracias a la "
                     "ecuación diferencial. La segunda función permite hallar la velocidad en un tiempo t en función "
                     "de la velocidad anterior que es pasada como parámetro ya que esto es posible a partir de la velocidad "
                     "inicial, la pendiente entre los puntos y la distancia horizontal h que separa los puntos. Gracias"
                     " a estas funciones es posible hallar de forma secuencial cada una de las velocidades y mostrarlas"
                     " en un grafico de pyplot. El conjunto de tiempos finitos elegidos son numeros del 0 al 8 separados"
                     " por un h=0.0001.")
            st.write("Implementacion de funciones que logran solucionar el problema:")
            st.image("term_3.png")
    if tipo_sim == 'B':
        st.write("Problema sobre campo electrico")
    if tipo_sim == 'C':
        st.subheader("Contexto y objetivo de la simulación")
        st.write("Para el presente trabajo se debe simular desplazamiento en el eje 'y' del efecto producido por dos "
                 "ondas mecánicas. Cuando dos ondas mecánicas ocupan un mismo lugar en el espacio, estas se superponen"
                 " y ocurre el fenómeno de interferencia. El efecto resultante es la suma de los valores obtenidos por"
                 " cada onda por separado. Al estar desfasadas entre sí, esta interferencia para distintos instantes "
                 "de tiempo puede ser constructiva (se amplifica el efecto si el desfase es mínimo) o destructiva ("
                 "se contrarrestan entre sí en caso haya un gran desfase). El objetivo es estudiar cómo se manifiesta "
                 "la interferencia dadas dos funciones de onda.")
        st.subheader("Problema propuesto")
        st.write("Se tienen dos ondas mecánicas que se viajan en la dirección +x definidas por dos funciones de onda:")
        st.latex(r'''
            y_1 (x,t)= A \ cos( k_1 \cdot x - \omega_1 \cdot t + \delta_1)\newline 
            y_2 (x,t)= A \ cos( k_2 \cdot x - \omega_2 \cdot t + \delta_2) 
                ''')
        st.write("Considere un punto fijo x para ambas ondas en el que estas se superponen y generan una interferencia. "
                 "Lo que ocurrirá es que en cierto intervalo de tiempo la interferencia se manifiesta de varios puntos "
                 "de interferencias constructivas, luego aparecen algunas interferencias destructivas. Y a lo largo "
                 "del tiempo se sigue esta secuencia. La función genera picos muy altos, a los que llamamos pulsos, y "
                 "luego la función genera puntos cercanos a 0 que gráficamente separan a estos pulsos entre sí. "
                 "Teniendo en cuenta esto, se le solicita a usted como estudiante que muestre en un solo gráfico dos "
                 "funciones de onda, y luego en otro gráfico muestre cómo se manifiesta la interferencia a lo largo "
                 "del tiempo. Se deben mostrar los pulsos generados y calcule de forma gráfica la frecuencia con la "
                 "que aparecen dichos pulsos. Puede compararlo con el siguiente modelo teórico:")
        st.image("inter_2.png")
        st.latex("f_{pulso}=|f_1-f_2|")
        st.write("Considere los siguientes parámetros:")
        st.image("inter_3.jpg")
        with st.expander("Análisis del problema y planteamiento general de la solución propuesta"):
            st.write("Antes de empezar, podemos dividir el problema en dos partes. La primera consiste en mostrar"
                     " de forma gráfica las dos funciones de onda y también la interferencia (en la que solo se deben "
                     "sumar ambos valores). Esto lo podemos hacer simplemente con una función que retorne el valor de"
                     " cada función de onda y ya.")
            st.image("inter_4.jpg")
            st.write("Nuestra atención estará en la segunda parte del problema que supone un reto un poco más complejo."
                     " Esta consiste en calcular la frecuencia de pulsos de forma gráfica. Menciono que es un problema "
                     "más complicado debido a que incluso cometimos un error en la simulación enviada anteriormente. A "
                     "nivel de resultado no hubo problema pero fue un error de conceptos, en la que incluso tuvimos que"
                     " volver a preguntarnos realmente qué es un pulso o cómo funciona este fenómeno. Así que "
                     "detallaremos un poco más cómo funciona la generación de pulsos para así evitar el siguiente "
                     "problema que tuvimos. Originalmente, la solución que propusimos fue buscar el valor más alto de "
                     "la función y buscar cada cuánto tiempo se repite, aparentemente suena bastante coherente y fácil."
                     " Pero esto solo sirve para ciertos parámetros, en los que la función tiene un periodo de pocos "
                     "segundos. En estos casos los pulsos son exactamente iguales y se puede realizar dicho proceso. Sin"
                     " embargo al variar los parámetros pasó esto:")
            st.image("inter_1.png")
            st.write("¿Cómo es posible hallar cada cuánto se repite cierto punto si ni siquiera los pulsos siguen el "
                     "mismo patrón?, ¿Es un error en la generación del gráfico o es normal en los pulsos?, ¿Qué es un "
                     "pulso?. Para no quedarnos con estas dudas desarrollaremos un poco más el modelo teórico al "
                     "considerar un valor constante para x.")
            st.latex(r'''
                        y_{int} (t)= A \ cos( k_1 \cdot x - \omega_1 \cdot t + \delta_1) + A \ cos( k_2 \cdot x 
                        - \omega_2 \cdot t + \delta_2) \newline
                        y_{int} (t)= 2A \ cos(\frac{\omega_1 - \omega_2}{2} \cdot t + \frac{k_2 - k_1}{2} \cdot x + 
                        \frac{\delta_2  - \delta_1}{2}) \cdot \newline cos(\frac{\omega_1 + \omega_2}{2} \cdot t + 
                        \frac{k_1 + k_2}{2} \cdot x + \frac{\delta_1  + \delta_2}{2})
                            ''')
            st.write("Podemos ver el resultado de la interferencia como el producto de dos resultados, el 2Acos() "
                     "multiplicado por el segundo cos(). Pero notamos que el primer coseno tiene una frecuencia pequeña"
                     " a comparación del segundo coseno. Esto es relevante porque el coseno con menor frecuencia es "
                     "el que va a determinar los pulsos. Esto de forma intuitiva lo podemos entender así: Cuando la "
                     "función más lenta alcanza un pico, en las cercanías a este pico cuando lo multiplicas por los "
                     "valores del segundo coseno vas a tener puntos variados pero en determinados momentos ambos cosenos"
                     " alcanzan valores altos. Por lo tanto, aproximadamente aquí se forman los picos del pulso. "
                     "Y cuando la función más lenta toma el valor de 0, por más que el segundo coseno toma valores "
                     "variados por su alta frecuencia, al multiplicar los valores el resultado va a ser cercano a 0 "
                     "durante cierto tramo.")
            st.image("inter_5.jpg")
            st.write("Por lo tanto, la generación de pulsos es influenciada principalmente por el primer coseno, en el"
                     " que su frecuencia es f1-f2. Pero, ¿en qué ayuda realizar este análisis si lo queremos resolver "
                     "de forma gráfica? El primer motivo es que responde las preguntas anteriores. Los pulsos no tienen por qué"
                     " ser iguales, simplemente el pico de uno de los factores pues aproximadamente se relaciona con "
                     "puntos altos de la interferencia. No podemos determinar de forma sencilla el pico más alto porque "
                     "los valores en concreto dependen del producto de ambos cosenos. Pasa algo parecido para los tiempos"
                     " en el que el primer coseno es cercano a 0. Como este va lento, la interferencia se queda cerca"
                     " a 0 por un intervalo de tiempo notorio. El segundo motivo es que con esto podemos concluir que "
                     "la grafica de la interferencia va a ser irregular aunque conozcamos que hay tramos de tendencia alta y"
                     " de tendencia 0. Por lo que es una tarea bastante compleja determinar a nivel gráfico la "
                     "frecuencia de pulsos con una precisión abrumadora. La única solución que encontramos fue usar"
                     " una herramienta de la librería scipy para cálculo de picos, que detecta picos según cierto valor mínimo y "
                     "busca picos que estén separados cierta distancia. Jugando un poco con estos dos parámetros aproximadamente"
                     " podemos hacernos una idea de qué tan separados están los picos. La precisión en algunos casos "
                     "no es muy buena pero es lo que se pudo hacer. Además, solo consideramos frecuencias con diferencia"
                     " mayor a 2 Hz para poder ver más de un pico en la gráfica y este método funcione bien.")
    if tipo_sim == 'D':
        st.subheader("Contexto y objetivo de la simulación")
        st.write("Para el presente trabajo se debe simular la trayectoria que seguirá un haz de luz al cambiar de medio"
                 " dado un punto de partida y un punto de llegada. Según el principio de Fermat, la trayectoria seguida"
                 " debe minimizar el tiempo del recorrido. Por lo tanto, la luz seguirá una trayectoria recta hasta "
                 "llegar a la interfase y luego seguirá otra trayectoria recta hasta el punto de llegada. Así que debemos"
                 " averiguar dónde la luz intersectará a la interfase para obtener la trayectoria y verificar si se cumple"
                 " la ley de Snell. La ley de Snell relaciona los ángulos de incidencia y de refracción con el índice de "
                 "refracción de los dos medios."
                 )
        st.subheader("Problema propuesto")
        st.write("Considere un punto de partida P1(x1,y1) y un punto de llegada P2(x2,y2). Desde P1 parte un haz de luz"
                 " de tal forma que llegue a P2. El principio de Fermat dice que la trayectoria será de tal forma que"
                 " minimice el tiempo de la trayectoria. Sabemos que la luz viaja a distintas velocidades en distintos"
                 " medios. Por lo tanto, tiene sentido pensar que la trayectoria no será solo una línea recta. Esto"
                 " es porque al pasar más tiempo en el medio en el que la luz es más veloz le permitirá alcanzar mayores"
                 " distancias en menos tiempo pero aun así no se puede desviar mucho de una trayectoria recta para no"
                 " tener que recorrer un camino más largo. Por lo tanto, se le solicita que halle la trayectoria que"
                 " permita minimizar el tiempo")
        st.image("luz_1.jpg")
        st.latex(r'''
                    t=t_1+t_2
                    \newline
                    t=d_1/v_1+d_2/v_2
                    \newline
                    t=\frac{\sqrt{(x_1-x)^2+y_1^2}}{v_1} + \frac{\sqrt{(x-x_2)^2+y_2^2}}{v_2}
                        ''')
        st.write(
            "Para hallar la distancia que minimice la función tiempo es posible hallar la derivada e igualarla a 0. De"
            " este proceso se puede obtener la ley de Snell. Se le solicita que muestre en una gráfica cómo varía el"
            " tiempo al variar los valores de x. Y también, verificar si se cumple la ley de Snell para la trayectoria"
            " relacionada con el menor tiempo. La ley de Snell consiste en la siguiente relación:")
        st.latex(r"n1 \cdot sen(\theta_{inc})=n2 \cdot sen(\theta_{ref})")
        st.write("Considere los siguientes parámetros:")
        st.image("luz_2.jpg")
        with st.expander("Análisis del problema y planteamiento general de la solución propuesta"):
            st.write("Al ver el problema, una primera reacción puede ser simplemente crear una función que sea la derivada"
                     " del tiempo, igualarla a 0, obtener el valor de x de forma exacta y verificar si cumple la ley de Snell."
                     " Este procedimiento disminuiría el margen de error. Pero implementar esto ha sido imposible para"
                     " el equipo porque la ecuación obtenida es muy complicada de resolver incluso aplicando herramientas"
                     " como Symbolab.")
            st.latex(r"dt/dx=\frac{x-x_1}{v_1 \cdot \sqrt{(x_1-x)^2+y_1^2}} - \frac{x_2-x}{v_2 \cdot \sqrt{(x-x_2)^2+y_2^2}}")
            st.latex(r"\frac{x-x_1}{v_1 \cdot \sqrt{(x_1-x)^2+y_1^2}} - \frac{x_2-x}{v_2 \cdot \sqrt{(x-x_2)^2+y_2^2}} =0")
            st.latex(r"\frac{x-x_1}{v_1 \cdot \sqrt{(x_1-x)^2+y_1^2}}=\frac{x_2-x}{v_2 \cdot \sqrt{(x-x_2)^2+y_2^2}}")
            st.write("Al estar el x tambien en las raíces cuadradas, es muy dificil resolver la ecuación. Talvez una opción"
                     " sería elevar al cuadrado un par de veces, obtener una ecuación polinomial de cuarto grado y con"
                     " alguna herramienta de Numpy tener la raíz real y positiva. Talvez no sea imposible pero es un camino"
                     " muy incómodo. De la relación lo máximo que podemos sacar es la ley de Snell.")
            st.latex(r"sen(\theta_{inc})=\frac{x-x_1}{\sqrt{(x-x_1)^2+y_1^2}}")
            st.latex(r"sen(\theta_{ref})=\frac{x_2-x}{\sqrt{(x_2-x)^2+y_2^2}}")
            st.latex(r"\frac{x-x_1}{\frac{c}{n_1} \cdot \sqrt{(x_1-x)^2+y_1^2}}=\frac{x_2-x}{\frac{c}{n_2} \cdot \sqrt{(x-x_2)^2+y_2^2}}")
            st.latex(r"sen(\theta_{inc}) \cdot n_1 = sen(\theta_{ref}) \cdot n_2")
            st.write("Así que ni modo. Solo queda usar el mismo método que aplicamos en todas las simulaciones anteriores: "
                     "Definir un conjunto de puntos en el eje x muy cercanos y evaluar la función para todos los puntos. "
                     "Para este caso hemos considerado puntos del 1 al 10 separados 0.001. La función usada fue:")
            st.image("luz_3.jpg")
            st.write("Y pues eso es todo, hallamos el mínimo con un min(array) y luego obtenemos la posición en la que ocurre. "
                     "La explicación anterior no tiene mucho que ver con esto pero pues en este caso la solución es "
                     "muy simple y no viene mal sobreanalizar el problema en vez de dejar vacío este apartado. "
                     "Además, usamos el valor mínimo obtenido para trazar en un plano XY cómo se vería la trayectoria. "
                     "Y con este valor también podemos hallar los ángulos de incidencia y refracción"
                     " según la expresión usada arriba para poder verificar si cumple la relación de la ley de Snell.")



def mostrar_sim(tipo_sim):
    if tipo_sim == 'A':
        st.subheader("Simulacion")
        # DEFINICION DE VARIABLES
        # Radio de la esfera (m) que se sumerge en el liquido
        rad_esf = st.slider(
            'Seleccione el radio de la esfera sumergida en m',
            0.0100, 0.0500, step=0.0001, value=0.0255, format="%f")
        # Volumen de la esfera (m3)
        vol_esf = 4 / 3 * pi * np.power(rad_esf, 3)
        # Densidad de la esfera (kg/m3)
        dens_esf = st.slider(
            'Seleccione la densidad de la esfera sumergida en kg/m3',
            3000, 4000, step=1, value=3250)
        # Masa de la esfera (kg), dens=m/v
        masa_esf = dens_esf * vol_esf
        # Densidad del liquido (kg/m3), para este caso la glicerina
        dens_glic = 1.26 * 1000
        # Viscosidad de la glicerina (Pa/s)
        visc = 1.40
        # Diferencia entre los puntos del eje del tiempo h
        h = 0.0001
        # Valor teorico de la velocidad terminal
        val_teor = 2 / 9 * rad_esf * rad_esf * g * (dens_esf - dens_glic) / visc

        # Funcion que calcula la derivada en funcion de la velocidad (Sale de la ecuacion diferencial)
        def derivada_v(v):
            return g * (1 - dens_glic / dens_esf) - v * 6 * pi * rad_esf * visc / masa_esf

        #Funcion que aproxima la velocidad segun el punto anterior (Metodo de diferencias finitas, usa la derivada)
        def obtener_velocidad(v_anterior):
            nueva_velocidad = v_anterior + h * derivada_v(v_anterior)
            return nueva_velocidad

        # Se crea el array de tiempos, se consideraran tiempos separados por 0.00001, se usaran funciones especiales
        # de numpy como np.linspace
        inicio = 0.00000
        final = 8.00000
        paso = h
        num_elementos = int((final - inicio) / paso) + 1

        array_tiempos = np.linspace(inicio, final, num_elementos)
        array_tiempos = np.round(array_tiempos, decimals=4)
        # Se crea el array de velocidades, inicializando su primer elemento en 0 y luego obtener los siguientes valores
        array_velocidades = np.zeros(num_elementos)
        array_velocidades[0] = 0.0
        #Para el segundo elemento en adelante, hallamos el termino en funcion del anterior gracias a las funciones
        for i in range(1, num_elementos):
            array_velocidades[i] = obtener_velocidad(array_velocidades[i - 1])

        # Se crean los datos en los ejes a partir de los calculos
        x = array_tiempos
        y = array_velocidades

        # Ajustar una línea recta (polinomio de grado 1) a los últimos 100 puntos (Para mostrar la tendencia a un valor)
        degree = 1
        coeffs = np.polyfit(x[-100:], y[-100:], degree)
        polynomial = np.poly1d(coeffs)

        # Crear puntos para la línea ajustada, osea para mostrar el grafico
        x_fit = x
        y_fit = polynomial(x_fit)

        # Como se menciono anteriormente,se eligira el ultimo valor de la velocidad para obtener la tendencia
        # Asi que este es el valor experimental
        y_tend = y[-1]

        # BLOQUE QUE NOMAS ES PARA EL GRAFICO
        plt.figure(figsize=(10, 6))
        # Graficar los puntos de la relacion entre x, y
        plt.plot(x, y, color='red', label='Velocidad de la esfera en glicerina')
        # Configurar el formato para 2 decimales en el eje x
        plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))

        # Configurar el formato para 3 decimales en el eje y
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))

        plt.plot(x_fit, y_fit, '--', color='green', label='Tendencia de los ultimos 100 puntos')
        plt.xlabel('Tiempo(s)')
        plt.ylabel('Velocidad(m/s)')
        plt.title('Grafica Velocidad vs Tiempo')
        plt.legend()
        st.pyplot(plt)
        st.subheader("Comparacion de valores")
        df = pd.DataFrame({'Valor experimental': [y_tend], 'Valor teorico': [val_teor], '% de error': [100*(val_teor-y_tend)/val_teor]})
        st.dataframe(df.style.format("{:.9f}"), hide_index=True)
        st.subheader("Representacion grafica de la velocidad terminal")
        st.image("terminal.gif")

    if tipo_sim == 'B':
        st.write("hola")
    if tipo_sim == 'C':
        st.subheader("Simulacion")
        # Parametros
        A = st.slider(
            'Seleccione la amplitud de ambas ondas en m',
            2.00, 4.00, step=0.01, value=3.45)
        v = 340.0  # v=f*λ
        pos_x = st.slider(
            'Seleccione la posicion x en m que se tendrá como referencia',
            2.00, 3.50, step=0.01, value=3.20)
        fas_1 = 0.0
        fas_2 = pi / 3
        frec_1 = st.slider(
            'Seleccione la frecuencia para la onda 1 en Hz',
            20.0, 26.0, step=0.1, value=25.6)
        frec_2 = st.slider(
            'Seleccione la frecuencia para la onda 2 en Hz',
            28.0, 36.0, step=0.1, value=28.8)
        k1 = 2 * pi / (v / frec_1)
        k2 = 2 * pi / (v / frec_2)
        w1 = 2 * pi * frec_1
        w2 = 2 * pi * frec_2

        # Funcion de onda para el x seleccionado
        def f_onda_1(t):
            return A * cos(k1 * pos_x - w1 * t + fas_1)

        def f_onda_2(t):
            return A * cos(k2 * pos_x - w2 * t + fas_2)

        st.latex("y_1 (t)=" + str(A) + "\ cos(" + str(round(k1*pos_x, 3)) + "-" + str(round(w1, 3)) + r"\cdot t)\newline "
                "y_2 (t)=" + str(A) + "\ cos(" + str(round(k2 * pos_x, 3)) + "-" + str(round(w2, 3)) + r"\cdot t + \frac{\pi}{3})\newline "
                 "y_{resultante}=y_1+y_2")
        #BLOQUE DE GRAFICOS DE AMBAS FUNCIONES DE ONDA
        # Vectorizacion para pasarle arrays como parametro y retorne otro array
        vect_1 = np.vectorize(f_onda_1)
        vect_2 = np.vectorize(f_onda_2)
        # Graficas de ambas ondas para un x determinado a lo largo del tiempo:
        arr_t = np.linspace(0.0, 1.0, 10001)
        arr_y = vect_1(arr_t)
        arr_y2 = vect_2(arr_t)
        plt.figure(figsize=(20, 6))
        plt.title('Grafica y vs t para ambas ondas')
        plt.xlabel("Tiempo (s)")
        plt.ylabel("y (m)")
        # Configurar el formato para 2 decimales en el eje x
        plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        # Configurar el formato para 2 decimales en el eje y
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        plt.plot(arr_t, arr_y, color='darkred')
        plt.plot(arr_t, arr_y2, color='darkblue')
        plt.plot(arr_t, arr_t - arr_t, color='black')
        plt.legend(["Funcion de onda y1", "Funcion de onda y2"], loc="lower right")
        st.pyplot(plt)
        plt.figure(figsize=(20, 6))
        plt.title('Grafica y vs t para la interferencia de las ondas')
        plt.xlabel("Tiempo (s)")
        plt.ylabel("y (m)")
        # Configurar el formato para 2 decimales en el eje x
        plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        # Configurar el formato para 2 decimales en el eje y
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        plt.plot(arr_t, arr_y + arr_y2, color='darkred')
        plt.plot(arr_t, arr_t - arr_t, color='black')
        plt.legend(["Interferencia de las ondas"], loc="lower right")
        st.pyplot(plt)
        plt.gcf().clear()
        st.subheader("Cálculo de la frecuencia de pulsos a partir de la gráfica generada")
        # BLOQUE DEL CALCULO DE PICOS
        senal_combinada = arr_y + arr_y2
        # Encuentra picos en la señal con SciPy
        # Le damos que encuentre puntos que sean aproximadamente altos, y que estén separados una distancia considerable
        picos, _ = find_peaks(senal_combinada, height=0.9*max(senal_combinada), distance=int(7000/((frec_2-frec_1))))

        # Grafica la señal y marca los picos
        plt.plot(arr_t, arr_t - arr_t, color='black')
        plt.plot(arr_t, senal_combinada)
        plt.plot(picos*0.0001, senal_combinada[picos], 'red')  # Marca los picos en rojo
        plt.title('Deteccion de picos para la hallar la frecuencia de pulsos')
        plt.xlabel("Tiempo (s)")
        plt.ylabel("y (m)")
        # Configurar el formato para 2 decimales en el eje x
        plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        # Configurar el formato para 2 decimales en el eje y
        plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        st.pyplot(plt)

        # Cálculo de la frecuencia basada en los picos encontrados
        periodo = (picos[1]-picos[0])*0.0001
        frec_int = 1 / periodo
        df = pd.DataFrame({'Valor experimental': [frec_int], 'Valor teorico': [frec_2-frec_1],
                           '% de error': [100 * (abs(frec_int-(frec_2-frec_1))) / (frec_2-frec_1)]})
        st.dataframe(df.style.format("{:.3f}"), hide_index=True)
        st.subheader("Animación del efecto de los pulsos")
        # BLOQUE DE ANIMACION (osea no tiene mucho que ver con la simulacion)
        def plot_pulso(i):
            x = arr_t[:(i+1)*500]
            y = senal_combinada[:(i+1)*500]
            plt.cla()  # Limpia el gráfico anterior
            plt.xlim(0, 1)

            plt.plot(x, y, color='darkred')
            plt.title('Efecto de los pulsos')
            plt.xlabel("Tiempo (s)")
            plt.ylabel("y (m)")
            plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))


        # Crear el gráfico inicial
        fig, ax = plt.subplots(figsize=(7, 4))
        plot_pulso(0)

        ani = FuncAnimation(fig, plot_pulso, frames=range(20), repeat=True, interval=300)

        components.html(ani.to_jshtml(), height=1000)

    if tipo_sim == 'D':
        st.subheader("Simulacion")
        # Parametros
        option_1 = st.selectbox(
            'Seleccione el medio desde el que parte la luz',
            ('Aire (n=1.00)', 'Agua (n=1.33)', 'Etanol (n=1.36)'))
        if option_1 == 'Aire (n=1.00)':
            n1=1.00
        if option_1 == 'Agua (n=1.33)':
            n1=1.33
        if option_1 == 'Etanol (n=1.36)':
            n1=1.36
        option_2 = st.selectbox(
            'Seleccione el medio hacia el que viajará la luz',
            ('Vidrio Pyrex (n=1.47)', 'Acrílico (n=1.50)', 'Benceno (n=1.50)', 'Diamante (n=2.42)'))
        if option_2 == 'Vidrio Pyrex (n=1.47)':
            n2 = 1.47
        if option_2 == 'Acrílico (n=1.50)':
            n2 = 1.50
        if option_2 == 'Benceno (n=1.50)':
            n2 = 1.50
        if option_2 == 'Diamante (n=2.42)':
            n2 = 2.42
        x1 = st.slider('Ingrese el valor de x1:', 1, 10, 2, 1)
        y1 = st.slider('Ingrese el valor de y1:', 1, 10, 6, 1)
        x2 = st.slider('Ingrese el valor de x2:', 1, 10, 6, 1)
        y2 = st.slider('Ingrese el valor de y2:', -10, -1, -7, 1)
        c=300000000
        v1=c/n1
        v2=c/n2
        # BLOQUE SOBRE LA TRAYECTORIA SEGUIDA
        st.subheader("Representación de la trayectoria de la luz")
        # Funcion que haya el tiempo total de trayectoria si la luz cayera en algun x. Debemos minimzar esta funcion
        def tiempo_trayectoria(x):
            return sqrt((x1 - x) ** 2 + y1 ** 2) / v1 + sqrt((x2 - x) ** 2 + y2 ** 2) / v2
        # BLOQUE DE GRAFICOS 1
        f_vect = np.vectorize(tiempo_trayectoria)
        arr_x = np.arange(0, 10, 0.001)
        arr_t = f_vect(arr_x)
        indice_minimo = np.argmin(arr_t)
        x_interf = arr_x[indice_minimo]
        sin2 = abs(x2 - x_interf) / sqrt((x2 - x_interf) ** 2 + y2 ** 2)
        sin1 = abs(x_interf - x1) / sqrt((x1 - x_interf) ** 2 + y1 ** 2)
        ang_2 = np.degrees(np.arcsin(sin2))
        ang_1 = np.degrees(np.arcsin(sin1))
        plt.title("Trayectoria que sigue la luz")
        plt.xlabel("Posicion x (m)")
        plt.ylabel("Posicion y (m)")
        ax = plt.gca()  # Obtener el eje actual
        ax.set_xlim(0, 10)  # Establecer límites en el eje X
        ax.set_ylim(-10, 10)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(base=1))  # Configurar el salto en el eje X a 1
        ax.yaxis.set_major_locator(ticker.MultipleLocator(base=2))
        plt.annotate("x=" + str(x_interf), xy=(x_interf, 0), xytext=(x_interf + 1, 0 + 1),
                     arrowprops=dict(arrowstyle='->'))
        x = np.linspace(x1, x_interf, 5)
        y = np.linspace(y1, 0, 5)
        plt.plot(x, y)
        # BLOQUE DE PUES SOLO PARA MOSTRAR FLECHITAS EN LAS LINEAS (Sí, es mucho texto solo para eso)
        ds = 0.6

        # number of line segments per interval
        Ns = np.round(np.sqrt((x[1:] - x[:-1]) ** 2 + (y[1:] - y[:-1]) ** 2) / ds).astype(int)

        # sub-divide intervals w.r.t. Ns
        subdiv = lambda x, Ns=Ns: np.concatenate([np.linspace(x[ii], x[ii + 1], Ns[ii]) for ii, _ in enumerate(x[:-1])])
        x, y = subdiv(x), subdiv(y)

        plt.quiver(x[:-1], y[:-1], x[1:] - x[:-1], y[1:] - y[:-1], scale_units='xy', angles='xy', scale=1, width=.004,
                   headlength=4, headwidth=4, color='C0')

        x = np.linspace(x_interf, x2, 5)
        y = np.linspace(0, y2, 5)
        plt.plot(x, y)
        # length of line segment
        ds = 0.6

        # number of line segments per interval
        Ns = np.round(np.sqrt((x[1:] - x[:-1]) ** 2 + (y[1:] - y[:-1]) ** 2) / ds).astype(int)

        # sub-divide intervals w.r.t. Ns
        subdiv = lambda x, Ns=Ns: np.concatenate([np.linspace(x[ii], x[ii + 1], Ns[ii]) for ii, _ in enumerate(x[:-1])])

        x, y = subdiv(x), subdiv(y)

        plt.quiver(x[:-1], y[:-1], x[1:] - x[:-1], y[1:] - y[:-1], scale_units='xy', angles='xy', scale=1, width=.004,
                   headlength=4, headwidth=4, color='C1')
        plt.plot([x_interf, x_interf], [y2, y1], linestyle='--')
        plt.plot([x1, x2], [0, 0], linestyle='--')
        # Definir la región que deseas rellenar
        x_fill = np.arange(0, 11)
        y_fill = np.full(11, 10)  # Seleccionar valores de y >= 0
        # Rellenar la mitad superior con un color
        plt.fill_between(x_fill, y_fill, color='royalblue', alpha=0.6)
        # Definir la región que deseas rellenar
        x_fill = np.arange(0, 11)
        y_fill = np.full(11, -10)

        # Rellenar la mitad superior con un color
        plt.fill_between(x_fill, y_fill, color='cyan', alpha=0.2)
        plt.text(10, 0.3, option_1.split()[0], fontsize=9, ha='right')
        plt.text(10, -0.7, option_2.split()[0], fontsize=9, ha='right')
        st.pyplot(plt)
        st.subheader("Tiempo de trayectoria según la intersección en la inerfase")
        # BLOQUE DEL SEGUNDO GRAFICO, EL DE Tiempo vs X
        plt.close()
        plt.title("Gráfica Tiempo vs x")
        plt.xlabel("Distancia x en la que la luz intersecta a la interfase (m)")
        plt.ylabel("Tiempo (s)")
        plt.plot(arr_x, arr_t)
        # Establecer el formato de los ticks en el eje x a dos decimales
        plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:.2f}"))
        st.pyplot(plt)
        # TABLA DE RESULTADOS
        st.subheader("Tabla de resultados")
        df = pd.DataFrame({'X que minimiza el tiempo': [str(x_interf)], 'Angulo de incidencia (i)': [str(round(ang_1, 6)) + '°'],
                           'Angulo de refraccion (r)': [str(round(ang_2, 6)) + '°'], 'Sen(i)/Sen(r)':[str(sin1/sin2)], 'n2/n1':[str(n2/n1)],
                           '% de error': [f'{float(100 * (abs((n2/n1) - (sin1/sin2)) / (n2/n1))):.9f}%']})
        df = df.T
        df.columns=["Valor obtenido"]
        st.dataframe(df)
