
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import pywavefront 

Window = None
Shader_programm = None
Vao_cubo = None

WIDTH = 800
HEIGHT = 600

Tempo_entre_frames = 0 # movimentar a camera




Cam_speed = 1.0 #velocidade da camera
Cam_yaw_speed = 30.0 #velocidade de rotação da câmera em y
Cam_pos = np.array([0.0, 0.0, 2.0]) #posicao inicial da câmera
Cam_yaw = 0.0 #ângulo de rotação da câmera em y

def redimensionaCallback(window, w, h):
    global WIDTH, HEIGHT
    WIDTH = w
    HEIGHT = h

def inicializaOpenGL():
    global Window, WIDTH, HEIGHT

    #Inicializa GLFW
    glfw.init()

    #Criação de uma janela
    Window = glfw.create_window(WIDTH, HEIGHT, "Exemplo - renderização de um triângulo", None, None)
    if not Window:
        glfw.terminate()
        exit()

    glfw.set_window_size_callback(Window, redimensionaCallback)
    glfw.make_context_current(Window)

    print("Placa de vídeo: ",OpenGL.GL.glGetString(OpenGL.GL.GL_RENDERER))
    print("Versão do OpenGL: ",OpenGL.GL.glGetString(OpenGL.GL.GL_VERSION))




    
def inicializaCubo():

    global Vao_cubo
    
    Vao_cubo = glGenVertexArrays(1)
    glBindVertexArray(Vao_cubo)

    # VBO dos vértices do quadrado
    points = [
		#face frontal
		0.5, 0.2, 0.5,#0
		0.5, -0.2, 0.5,#1
		-0.5, -0.2, 0.5,#2
		-0.5, 0.2, 0.5,#3
		0.5, 0.2, 0.5,
		-0.5, -0.2, 0.5,
		#face traseira
		0.5, 0.2, -0.5,#4
		0.5, -0.2, -0.5,#5
		-0.5, -0.2, -0.5,#6
		-0.5, 0.2, -0.5,#7
		0.5, 0.2, -0.5,
		-0.5, -0.2, -0.5,
		#face esquerda
		-0.5, -0.2, 0.5,
		-0.5, 0.2, 0.5,
		-0.5, -0.2, -0.5,
		-0.5, -0.2, -0.5,
		-0.5, 0.2, -0.5,
		-0.5, 0.2, 0.5,
		#face direita
		0.5, -0.2, 0.5,
		0.5, 0.2, 0.5,
		0.5, -0.2, -0.5,
		0.5, -0.2, -0.5,
		0.5, 0.2, -0.5,
		0.5, 0.2, 0.5,
		#face baixo
		-0.5, -0.2, 0.5,
		0.5, -0.2, 0.5,
		0.5, -0.2, -0.5,
		0.5, -0.2, -0.5,
		-0.5, -0.2, -0.5,
		-0.5, -0.2, 0.5,
		#face cima
		-0.5, 0.2, 0.5,
		0.5, 0.2, 0.5,
		0.5, 0.2, -0.5,
		0.5, 0.2, -0.5,
		-0.5, 0.2, -0.5,
		-0.5, 0.2, 0.5,
	]
    points = np.array(points, dtype=np.float32)
    pvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, pvbo)
    glBufferData(GL_ARRAY_BUFFER, points, GL_STATIC_DRAW)
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)


    # VBO das cores
    normais = [
		#face frontal - vermelha
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0,
		0.0, 0.0, 1.0,
		#face trazeira - verde
		0.0, 0.0, -1.0,
		0.0, 0.0, -1.0,
		0.0, 0.0, -1.0,
		0.0, 0.0, -1.0,
		0.0, 0.0, -1.0,
		0.0, 0.0, -1.0,
		#face esquerda - azul
		-1.0, 0.0, 0.0,
		-1.0, 0.0, 0.0,
		-1.0, 0.0, 0.0,
		-1.0, 0.0, 0.0,
		-1.0, 0.0, 0.0,
		-1.0, 0.0, 0.0,
		#face direita - ciano
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		1.0, 0.0, 0.0,
		#face baixo - magenta
		0.0, -1.0, 0.0,
		0.0, -1.0, 0.0,
		0.0, -1.0, 0.0,
		0.0, -1.0, 0.0,
		0.0, -1.0, 0.0,
		0.0, -1.0, 0.0,
		#face cima - verde
		0.0, 1.0, 0.0,
		0.0, 1.0, 0.0,
		0.0, 1.0, 0.0,
		0.0, 1.0, 0.0,
		0.0, 1.0, 0.0,
		0.0, 1.0, 0.0,
	]
    normais = np.array(normais, dtype=np.float32)
    nvbo = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, nvbo)
    glBufferData(GL_ARRAY_BUFFER, normais, GL_STATIC_DRAW)
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)

def inicializaShaders():
    global Shader_programm
   
    vertex_shader = """
        #version 400
        layout(location = 0) in vec3 vertex_posicao; //vértices do objeto vindas do modelo do objeto (PYTHON)
        layout(location = 1) in vec3 vertex_normal; //normais do objeto vindas do modelo do objeto (PYTHON)
        out vec3 vertex_posicao_cam, vertex_normal_cam;
        uniform mat4 transform, view, proj;
        void main () {
            vertex_posicao_cam = vec3 (view * transform * vec4 (vertex_posicao, 1.0)); //posição do objeto em relação a CÂMERA
            vertex_normal_cam = vec3 (view *  transform * vec4 (vertex_normal, 0.0)); //normais do objeto em relação a CÂMERA
            gl_Position = proj * view * transform * vec4 (vertex_posicao, 1.0);
        }
    """
    vs = OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER)
    if not glGetShaderiv(vs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(vs, 512, None)
        print("Erro no vertex shader:\n", infoLog)

   
    # Especificação do Vertex Shader:
    fragment_shader = """
        #version 400
		in vec3 vertex_posicao_cam, vertex_normal_cam; //variáveis vindas do VERTEX SHADER
        
        //propriedades de uma luz pontual vindas do PYTHON
        uniform vec3 luz_posicao;
        uniform vec3 Ls;// luz especular
		uniform vec3 Ld;// luz difusa
		uniform vec3 La;// luz ambiente

        //propriedades de reflexão da superficie do objeto vindas do PYTHON
		uniform vec3 Ks;//reflexão especular
		uniform vec3 Kd;//reflexão difusa
		uniform vec3 Ka;//reflexão ambiente
        uniform float especular_exp;//expoente especular
        
        uniform mat4 view; //matriz da câmera vinda do PYTHON
		out vec4 frag_colour;

        //variáveis globais que são utilizadas tanto na intensidade difusa quanto especular, para não precisar recalcular duas vezes
        vec3 luz_posicao_cam, luz_vetor_cam, luz_vetor_cam_normalizada, vertex_normal_cam_normalizada;

        vec3 intensidadeAmbiente(){
            /*
            Cálculo de Intensidade de Luz Ambiente (Ia)
            O cálculo da intensidade de luz ambiente é o mais simples:
            basta multiplicar a cor da luz ambiente pela refletância de luz ambiente da superfície
            */
            vec3 Ia = La * Ka;
            return Ia;
        }

        vec3 intensidadeDifusa(){
            /*
            Cálculo de Intensidade de Luz Difusa (Id)
            Para calcularmos a intensidade de luz difusa, precisamos, primeiramente, 
            calcular a posição da luz em relação a câmera (luz_posicao_cam)
            */
            luz_posicao_cam = vec3 (view * vec4 (luz_posicao, 1.0));//posicao da luz em relação a câmera

            /*A posição da luz (luz_posicao_cam) calculada acima representa um vetor que sai da origem (0,0,0) e
		aponta para a luz. Para a luz difusa, precisamos calcular um vetor que saia de cada vértice do objeto
		(vertex_posicao_cam) e aponte para essa luz. Para isso, basta calcularmos a diferença entre luz_posicao_cam
		e vertex_posicao_cam.*/
            luz_vetor_cam = luz_posicao_cam - vertex_posicao_cam;//vetor apontando para a luz em relação a posicao do vértice 

            /*Por fim, normalizamos o vetor da luz em relação ao vértice do objeto e calculamos o cosseno do angulo
		entre o mesmo e a normal da superficie utilizando o produto escalar*/
            luz_vetor_cam_normalizada = normalize(luz_vetor_cam);//vetor da luz normalizada
            vertex_normal_cam_normalizada = normalize(vertex_normal_cam);
            float cosseno_difusa = dot(vertex_normal_cam_normalizada,luz_vetor_cam_normalizada);//cosseno do angulo entre o vetor da luz e a normal da superficie
            
            vec3 Id = Ld * Kd * cosseno_difusa;

            return Id;

        }

        vec3 intensidadeEspecular(){
            /*
            Cálculo de Intensidade de Luz Especular (Is)
            Para o cálculo da intensidade de luz especular, precisamos primeiramente calcular o vetor que representa 
            a luz refletida em relação a normal da superfície */
            vec3 luz_reflexao_vetor_cam = reflect(-luz_vetor_cam_normalizada, vertex_normal_cam_normalizada);
            /*Como a intensidade de luz especular depende da posição da câmera, definimos um vetor que sai da superficie
		    do objeto e aponta para a camera, e então normalizamos, pois utilizaremos ele no cálculo do produto escalar*/
            vec3 superficie_camera_vetor = normalize(-vertex_posicao_cam);
            /*E então calculamos o ângulo entre o vetor de reflexão da luz e o vetor em relação a posicao do observador*/
            float cosseno_especular = dot(luz_reflexao_vetor_cam, superficie_camera_vetor);
            cosseno_especular = max(cosseno_especular, 0.0);//se o cosseno der negativo, atribui 0 para ele
            /*Na intensidade especular, precisamos elevar o cosseno calculado acima ao expoente especular*/
            float fator_especular = pow (cosseno_especular, especular_exp);
            /*E, por fim, calculamos a intensidade de luz especular refletida (Is) */

            vec3 Is = Ls * Ks * fator_especular;

            return Is;
        }
		void main () {

            vec3 Ia = intensidadeAmbiente();

            vec3 Id = intensidadeDifusa();

            vec3 Is = intensidadeEspecular();

            /*A cor final do fragmento é a soma das 3 componentes de iluminação*/
		    frag_colour = vec4 (Ia+Id+Is,1.0);
		}
    """
    

    fs = OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER)
    if not glGetShaderiv(fs, GL_COMPILE_STATUS):
        infoLog = glGetShaderInfoLog(fs, 512, None)
        print("Erro no fragment shader:\n", infoLog)

    # Especificação do Shader Programm:
    Shader_programm = OpenGL.GL.shaders.compileProgram(vs, fs)
    if not glGetProgramiv(Shader_programm, GL_LINK_STATUS):
        infoLog = glGetProgramInfoLog(Shader_programm, 512, None)
        print("Erro na linkagem do shader:\n", infoLog)

    glDeleteShader(vs)
    glDeleteShader(fs)

def transformacaoGenerica(Tx, Ty, Tz, Sx, Sy, Sz, Rx, Ry, Rz):
    #matriz de translação
    translacao = np.array([
        [1.0, 0.0, 0.0, Tx], 
        [0.0, 1.0, 0.0, Ty], 
        [0.0, 0.0, 1.0, Tz], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    #matriz de rotação em torno do eixo X
    angulo = np.radians(Rx)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoX = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, cos, -sen, 0.0],
        [0.0, sen, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de rotação em torno do eixo Y
    angulo = np.radians(Ry)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoY = np.array([
        [cos, 0.0, sen, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sen, 0.0, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #matriz de rotação em torno do eixo Z
    angulo = np.radians(Rz)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoZ = np.array([
        [cos, -sen, 0.0, 0.0],
        [sen, cos, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    #combinação das 3 rotação
    rotacao = rotacaoZ.dot(rotacaoY.dot(rotacaoX))

    #matriz de escala
    escala = np.array([
        [Sx, 0.0, 0.0, 0.0], 
        [0.0, Sy, 0.0, 0.0], 
        [0.0, 0.0, Sz, 0.0], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)

    transformacaoFinal = translacao.dot(rotacao.dot(escala))
    
    
    transformLoc = glGetUniformLocation(Shader_programm, "transform")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, transformacaoFinal)

def especificaMatrizVisualizacao():


    #posicao da camera
    translacaoCamera = np.array([
        [1.0, 0.0, 0.0, -Cam_pos[0]], 
        [0.0, 1.0, 0.0, -Cam_pos[1]], 
        [0.0, 0.0, 1.0, -Cam_pos[2]], 
        [0.0, 0.0, 0.0, 1.0]], np.float32)
    
    #orientacao da camera (rotação em y)
    angulo = np.radians(-Cam_yaw)
    cos, sen = np.cos(angulo), np.sin(angulo)
    rotacaoCamera = np.array([
        [cos, 0.0, sen, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [-sen, 0.0, cos, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ])

    visualizacao = rotacaoCamera.dot(translacaoCamera)

    transformLoc = glGetUniformLocation(Shader_programm, "view")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, visualizacao)

def especificaMatrizProjecao():
    #Especificação da matriz de projeção perspectiva.
    znear = 0.1 #recorte z-near
    zfar = 100.0 #recorte z-far
    fov = np.radians(67.0) #campo de visão
    aspecto = WIDTH/HEIGHT #aspecto

    a = 1/(np.tan(fov/2)*aspecto)
    b = 1/(np.tan(fov/2))
    c = (zfar + znear) / (znear - zfar)
    d = (2*znear*zfar) / (znear - zfar)
    projecao = np.array([
        [a,   0.0, 0.0,  0.0],
        [0.0, b,   0.0,  0.0],
        [0.0, 0.0, c,    d],
        [0.0, 0.0, -1.0, 1.0]
    ])

    transformLoc = glGetUniformLocation(Shader_programm, "proj")
    glUniformMatrix4fv(transformLoc, 1, GL_TRUE, projecao)

def inicializaCamera():
    especificaMatrizVisualizacao() #posição da câmera e orientação da câmera (rotação)
    especificaMatrizProjecao() #perspectiva ou paralela

def trataTeclado():
    global Cam_pos, Cam_yaw, Cam_yaw_speed, Tempo_entre_frames
    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_ESCAPE)):
            glfw.set_window_should_close(Window, True)

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_A)):
        Cam_pos[0] -= Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_D)):
        Cam_pos[0] += Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_UP)):
        Cam_pos[1] += Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_PAGE_DOWN)):
        Cam_pos[1] -= Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_W)):
        Cam_pos[2] -= Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_S)):
        Cam_pos[2] += Cam_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_LEFT)):
        Cam_yaw += Cam_yaw_speed * Tempo_entre_frames

    if (glfw.PRESS == glfw.get_key(Window, glfw.KEY_RIGHT)):
        Cam_yaw -= Cam_yaw_speed * Tempo_entre_frames

def especificaMaterialCubo(KaR, KaG, KaB, KdR, KdG, KdB, KsR, KsG, KsB, n):
    global Shader_programm
    #Coeficiente de reflexão ambiente
    Ka = np.array([KaR, KaG, KaB])#reflete luz ambiente
    Ka_loc = glGetUniformLocation(Shader_programm, "Ka")
    glUniform3fv(Ka_loc, 1, Ka)

    #Coeficiente de reflexão difusa
    Kd = np.array([KdR, KdG, KdB])#reflete luz difusa
    Kd_loc = glGetUniformLocation(Shader_programm, "Kd")
    glUniform3fv(Kd_loc, 1, Kd)

    #Coeficiente de reflexão especular
    Ks = np.array([KsR, KsG, KsB])#reflete luz especular
    Ks_loc = glGetUniformLocation(Shader_programm, "Ks")
    glUniform3fv(Ks_loc, 1, Ks)

    #expoente expecular
    especular_exp = n
    especular_exp_loc = glGetUniformLocation(Shader_programm, "especular_exp")
    glUniform1f(especular_exp_loc, especular_exp)

def especificaLuz():
    global Shader_programm
    #posição da luz
    luz_posicao = np.array([0.0, 0.0, 2.0])
    luz_posicaoloc = glGetUniformLocation(Shader_programm, "luz_posicao")
    glUniform3fv(luz_posicaoloc, 1, luz_posicao)

    #Fonte de luz ambiente
    La = np.array([0.2, 0.2, 0.2]) #cinza bem escuro
    La_loc = glGetUniformLocation(Shader_programm, "La")
    glUniform3fv(La_loc, 1, La)

    #Fonte de luz difusa
    Ld = np.array([0.7, 0.7, 0.7]) #cinza bem claro
    Ld_loc = glGetUniformLocation(Shader_programm, "Ld")
    glUniform3fv(Ld_loc, 1, Ld)
    
    #Fonte de luz especular
    Ls = np.array([1.0, 1.0, 1.0]) #luz branca
    Ls_loc = glGetUniformLocation(Shader_programm, "Ls")
    glUniform3fv(Ls_loc, 1, Ls)

def inicializaRenderizacao():
    global Window, Shader_programm, Vao_cubo, WIDTH, HEIGHT, Tempo_entre_frames

    tempo_anterior = glfw.get_time()

    #Ativação do teste de profundidade
    glEnable(GL_DEPTH_TEST)

    while not glfw.window_should_close(Window):
        #calcula quantos segundos se passaram entre um frame e outro
        tempo_frame_atual = glfw.get_time()
        Tempo_entre_frames = tempo_frame_atual - tempo_anterior
        tempo_anterior = tempo_frame_atual

        

        glClearColor(0.2, 0.3, 0.3, 1.0)
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #limpa o buffer de cores e de profundidade
        
        glViewport(0, 0, WIDTH, HEIGHT)

        glUseProgram(Shader_programm)

        especificaLuz()

        trataTeclado()

        inicializaCamera()

        glBindVertexArray(Vao_cubo) #modelo do cubo

                            # Tx    Ty    Tz   Sx   Sy   Sz  Rx   Ry   Rz


        especificaMaterialCubo(0.2, 0.2, 0.2, 225/255, 225/255, 225/255, 0.3, 0.3, 0.3, 32) #branco

        transformacaoGenerica(-0.0, -1.3, -1.15, 0.2, 0.4, 0.2, 0.0, 0.0, 0.0) #topete ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-1.22, -1.25, -1.15, 0.25, 0.4, 0.35, 0.0, 0.0, 0.0) #topete ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-0.6, -1.5, -1.2, 1.0, 1.0, 0.6, 0.0, 0.0, 0.0) #cabeça ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-0.6, -1.5, -1.2, 1.0, 1.0, 0.6, 0.0, 0.0, 0.0) #corpo da ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)


        especificaMaterialCubo(0.2, 0.2, 0.2, 0/255, 0/255, 0/255, 0.3, 0.3, 0.3, 32) #preto

        transformacaoGenerica(-1.25, -1.5, -1.2, 0.5, 0.8, 0.3, 0.0, 0.0, 0.0) #cabeça ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-0.2, -1.75, -1.0, 0.1, 0.3, 0.1, 0.0, 0.0, 0.0) #pés da ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-0.2, -1.75, -1.4, 0.1, 0.3, 0.1, 0.0, 0.0, 0.0) #pés da ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-1.0, -1.75, -1.4, 0.1, 0.3, 0.1, 0.0, 0.0, 0.0) #pés da ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-1.0, -1.75, -1.0, 0.1, 0.3, 0.1, 0.0, 0.0, 0.0) #pés da ovelha
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-3.3, -1.15, -3.6, 0.1, 3.25, 0.1, 0.0, 0.0, 0.0) #viga area direita
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-6.7, -1.15, -3.6, 0.1, 3.25, 0.1, 0.0, 0.0, 0.0) #viga area esquerda
        glDrawArrays(GL_TRIANGLES, 0, 36)

        especificaMaterialCubo(0.2, 0.2, 0.2, 128/255, 128/255, 128/255, 0.3, 0.3, 0.3, 32)
        transformacaoGenerica(-5.0, -0.25, -6.0, 3.5, 1.5, 4.9, 0.0, 0.0, 0.0) #parte de cima da casa
        glDrawArrays(GL_TRIANGLES, 0, 36)

        especificaMaterialCubo(0.2, 0.2, 0.2, 225/255, 193/255, 193/255, 0.3, 0.3, 0.3, 32)
        transformacaoGenerica(-4.0, -1.15, -5.0, 1.4, 3.0, 0.05, 0.0, 0.0, 0.0) #parede da frente/direita
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-6.0, -1.15, -5.0, 1.4, 3.0, 0.05, 0.0, 0.0, 0.0) #parede da frente/esquerda
        glDrawArrays(GL_TRIANGLES, 0, 36)
        
        transformacaoGenerica(-3.3, -1.15, -6.7, 3.5, 3.0, 0.05, 0.0, 90.0, 0.0) #parede da direita casa
        glDrawArrays(GL_TRIANGLES, 0, 36)     

        transformacaoGenerica(-6.7, -1.15, -6.7, 3.5, 3.0, 0.05, 0.0, 90.0, 0.0) #parde da esquerda casa
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-5.0, -1.15, -8.4, 3.5, 3.0, 0.05, 0.0, 0.0, 0.0) #parede de tras, casa
        glDrawArrays(GL_TRIANGLES, 0, 36)

        especificaMaterialCubo(0.2, 0.2, 0.2, 0/255, 128/255, 64/255, 0.3, 0.3, 0.3, 32)
        transformacaoGenerica(2.3, -0.2, -4.9, 1.5, 2.5, 1.5, 0.0, 0.0, 0.0) #parte de cima arvore esquerda
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-1.0, -0.2, -2.8, 1.5, 2.5, 1.5, 0.0, 0.0, 0.0) #parte de cima arvore direita
        glDrawArrays(GL_TRIANGLES, 0, 36)

        especificaMaterialCubo(0.2, 0.2, 0.2, 102/255, 51/255, 0/255, 0.3, 0.3, 0.3, 32)
        transformacaoGenerica(2.4, -1.15, -5.0, 0.5, 3.0, 0.5, 0.0, 0.0, 0.0) #tronco arvore direita
        glDrawArrays(GL_TRIANGLES, 0, 36)

        transformacaoGenerica(-1.0, -1.15, -3.0, 0.5, 3.0, 0.5, 0.0, 0.0, 0.0) #tronco arvore esquerda
        glDrawArrays(GL_TRIANGLES, 0, 36)


        especificaMaterialCubo(0.2, 0.2, 0.2, 0/255, 221/255, 0/255, 0.3, 0.3, 0.3, 32)
        transformacaoGenerica(-1.0, -2.0, -5.0, 15.0, 1.0, 10.0, 0.0, 0.0, 0.0) #chao
        glDrawArrays(GL_TRIANGLES, 0, 36)

        glfw.poll_events()

        glfw.swap_buffers(Window)
        
        trataTeclado()
    
    glfw.terminate()

# Função principal
def main():
    inicializaOpenGL()
    inicializaCubo()
    
   
    inicializaShaders()
    inicializaRenderizacao()


if __name__ == "__main__":
    main()