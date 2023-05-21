from tkinter import *

janela = Tk()
janela.title("Projeto Conscientizador DIV/DEV/1M")
janela.geometry()

largura = 1200
altura = 700
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
janela.resizable(True,True)
janela.state("zoomed")

def home():
    titulo = Label(janela, text="\n\nProjeto Conscientizador", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nSejam bem-vindos!\n\n Separamos alguns assuntos relacionados aos ambientes de uso coletivo na Proz\n para que possamos tornar nossa convivência ainda mais agradável. Nosso objetivo\n é discutir assuntos pertinentes ao nosso convívio afim de torná-lo ainda melhor.\n\n", font=("Arial 25"))
    label1.pack()
    
    def iniciar_click():
        titulo.destroy()
        label1.destroy()
        iniciar.destroy()
        barulho()

    iniciar = Button(janela, width=10, text="Iniciar", font=("Arial 25 bold"), command=iniciar_click)
    iniciar.pack()

def barulho():
    titulo = Label(janela, text="\n1. Barulho", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nVocês se incomodam com barulhos de conversas\n alheias, fora da sala, durante o horário de aula?\n\n", font=("Arial 25"))
    label1.pack()

    def concordo_click():
        titulo["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
        sugestao1 = Entry(janela, width=80)
        sugestao1.pack()
        concordo.destroy()
        discordo.destroy()
        label1.destroy()

        def sugerir_click():
            titulo["text"]="\n\n\n\nObrigado pela sua sugestão!\n\n"
            sugerir.destroy()
            concordo.destroy()
            discordo.destroy()
            sugestao1.destroy()

            def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    banheiro()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        sugerir = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir_click)
        sugerir.pack()

        
    def discordo_click():
        concordo.destroy()
        discordo.destroy()
        titulo["text"]="\n1. Barulho"
        label1["text"]="\n\nQuanto aos outros alunos, o barulho pode incomodá-los durante o\nhorário de aula, em ocasiões de provas ou atividades avaliativas?\n\n"

        def concordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            label1["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
            sugestao1 = Entry(janela, width=80)
            sugestao1.pack()

            def sugerir1_click():
                titulo["text"]="\n\n\nObrigado pela sua sugestão!\n\n"
                sugerir1.destroy()
                concordo.destroy()
                discordo.destroy()
                sugestao1.destroy()
                label1.destroy()

                def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    banheiro()

                proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
                proximo.pack()

            sugerir1 = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir1_click)
            sugerir1.pack()  
        
        def discordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            titulo["text"]="\n1. Barulho"
            label1["text"]="\n\nPara evitar esse tipo de situação no futuro, podemos pensar em algumas\n atitudes: Respeitar o horário de aula não conversando alto nos corredores\n ou próximo às salas de aula. Ao atender uma ligação, dirigir-se para um\n ambiente mais adequeado. Exemplos: Refeitório, Entrada da Unidade, etc.\n\n"

            def proximo_click():
                titulo.destroy()
                label1.destroy()
                proximo.destroy()
                banheiro()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        concordo1 = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo1_click)
        concordo1.pack()
        discordo1 = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo1_click)
        discordo1.pack()

    concordo = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo_click)
    concordo.pack()
    discordo = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo_click)
    discordo.pack()
    

def banheiro():
    titulo = Label(janela, text="\n2. Banheiro", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nVocês se incomodam com a higienização do banheiro por parte dos seus usuários?\n(Quanto a utilização dos alunos somente.)\n\n", font=("Arial 25"))
    label1.pack()

    def concordo_click():
        titulo["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
        sugestao1 = Entry(janela, width=80)
        sugestao1.pack()
        concordo.destroy()
        discordo.destroy()
        label1.destroy()

        def sugerir_click():
            titulo["text"]="\n\n\n\nObrigado pela sua sugestão!\n\n"
            sugerir.destroy()
            concordo.destroy()
            discordo.destroy()
            sugestao1.destroy()

            def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    plataforma()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        sugerir = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir_click)
        sugerir.pack()

        
    def discordo_click():
        concordo.destroy()
        discordo.destroy()
        titulo["text"]="\n2. Banheiro"
        label1["text"]="\n\nOs alunos estão mantendo os banheiros sempre higienizados?\n\n"

        def discordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            label1["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
            sugestao1 = Entry(janela, width=80)
            sugestao1.pack()

            def sugerir1_click():
                titulo["text"]="\n\n\nObrigado pela sua sugestão!\n\n"
                sugerir1.destroy()
                concordo.destroy()
                discordo.destroy()
                sugestao1.destroy()
                label1.destroy()

                def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    plataforma()

                proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
                proximo.pack()

            sugerir1 = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir1_click)
            sugerir1.pack()
        
        def concordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            titulo["text"]="\n2. Banheiro"
            label1["text"]="\n\nPara evitar esse tipo de situação no futuro, podemos pensar em algumas\n atitudes: Jogar o papel no lixo, secar as mãos corretamente, não deixando\n cair respingos de água no chão, deixar sempre o vaso sanitário limpo para a\n próxima pessoa, utilizar a quantidade correta de sabão, evitando o desperdício.\n\n"

            def proximo_click():
                titulo.destroy()
                label1.destroy()
                proximo.destroy()
                plataforma()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        concordo1 = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo1_click)
        concordo1.pack()
        discordo1 = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo1_click)
        discordo1.pack()

    concordo = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo_click)
    concordo.pack()
    discordo = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo_click)
    discordo.pack()

def plataforma():
    titulo = Label(janela, text="\n3. Plataforma JoyClass", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nA plataforma JoyClass é intuitiva?\n De fácil utilização?\n\n", font=("Arial 25"))
    label1.pack()

    def discordo_click():
        titulo["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
        sugestao1 = Entry(janela, width=80)
        sugestao1.pack()
        concordo.destroy()
        discordo.destroy()
        label1.destroy()

        def sugerir_click():
            titulo["text"]="\n\n\n\nObrigado pela sua sugestão!\n\n"
            sugerir.destroy()
            concordo.destroy()
            discordo.destroy()
            sugestao1.destroy()

            def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    apostila()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        sugerir = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir_click)
        sugerir.pack()

        
    def concordo_click():
        concordo.destroy()
        discordo.destroy()
        titulo["text"]="\n3. Plataforma JoyClass"
        label1["text"]="\n\nAlguma melhoria poderia ser implementada na plataforma JoyClass?\n\n"

        def concordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            label1["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
            sugestao1 = Entry(janela, width=80)
            sugestao1.pack()

            def sugerir1_click():
                titulo["text"]="\n\n\nObrigado pela sua sugestão!\n\n"
                sugerir1.destroy()
                concordo.destroy()
                discordo.destroy()
                sugestao1.destroy()
                label1.destroy()

                def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    apostila()

                proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
                proximo.pack()

            sugerir1 = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir1_click)
            sugerir1.pack()
        
        def discordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            titulo["text"]="\n3. Plataforma JoyClass"
            label1["text"]="\n\nCaso vocês encontrem dificuldades em acessar a plataforma,\n podem nos procurar ou acionar a Coordenação da PROZ.\n\n"

            def proximo_click():
                titulo.destroy()
                label1.destroy()
                proximo.destroy()
                apostila()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        concordo1 = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo1_click)
        concordo1.pack()
        discordo1 = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo1_click)
        discordo1.pack()

    concordo = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo_click)
    concordo.pack()
    discordo = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo_click)
    discordo.pack()

def apostila():
    titulo = Label(janela, text="\n4. Apostila", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nO conteúdo da apostila é adequado de acordo com o curso?\n\n", font=("Arial 25"))
    label1.pack()

    def discordo_click():
        titulo["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
        sugestao1 = Entry(janela, width=80)
        sugestao1.pack()
        concordo.destroy()
        discordo.destroy()
        label1.destroy()

        def sugerir_click():
            titulo["text"]="\n\n\n\nObrigado pela sua sugestão!\n\n"
            sugerir.destroy()
            concordo.destroy()
            discordo.destroy()
            sugestao1.destroy()

            def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    comunicacao()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        sugerir = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir_click)
        sugerir.pack()

        
    def concordo_click():
        concordo.destroy()
        discordo.destroy()
        titulo["text"]="\n4. Apostila"
        label1["text"]="\n\nAlguma melhoria poderia ser implementada\n nas apostilas para módulos futuros?\n\n"

        def concordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            label1["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
            sugestao1 = Entry(janela, width=80)
            sugestao1.pack()

            def sugerir1_click():
                titulo["text"]="\n\n\nObrigado pela sua sugestão!\n\n"
                sugerir1.destroy()
                concordo.destroy()
                discordo.destroy()
                sugestao1.destroy()
                label1.destroy()

                def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    comunicacao()

                proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
                proximo.pack()

            sugerir1 = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir1_click)
            sugerir1.pack()
        
        def discordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            titulo["text"]="\n4. Apostila"
            label1["text"]="\n\nCaso futuramente surja alguma dificuldade em entendimento do material, informações\n errôneas ou falta de aprofundamento em determinado tema, procure a Coordenação da PROZ.\n\n"

            def proximo_click():
                titulo.destroy()
                label1.destroy()
                proximo.destroy()
                comunicacao()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        concordo1 = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo1_click)
        concordo1.pack()
        discordo1 = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo1_click)
        discordo1.pack()

    concordo = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo_click)
    concordo.pack()
    discordo = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo_click)
    discordo.pack()
        
def comunicacao():
    titulo = Label(janela, text="\n5. Comunicaçao da Coordenação", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nAs informações repassadas pela Coordenação da PROZ aos\n alunos são transmitidas de forma clara e em tempo hábil?\n\n", font=("Arial 25"))
    label1.pack()

    def discordo_click():
        titulo["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
        sugestao1 = Entry(janela, width=80)
        sugestao1.pack()
        concordo.destroy()
        discordo.destroy()
        label1.destroy()

        def sugerir_click():
            titulo["text"]="\n\n\n\nObrigado pela sua sugestão!\n\n"
            sugerir.destroy()
            concordo.destroy()
            discordo.destroy()
            sugestao1.destroy()

            def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    conduta()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        sugerir = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir_click)
        sugerir.pack()

        
    def concordo_click():
        concordo.destroy()
        discordo.destroy()
        titulo["text"]="\n5. Comunicaçao da Coordenação"
        label1["text"]="\n\nAlguma melhoria poderia ser implementada na transmissão de informações\n vindas da matriz até chegar aos alunos da nossa unidade?\n\n"

        def concordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            label1["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
            sugestao1 = Entry(janela, width=80)
            sugestao1.pack()

            def sugerir1_click():
                titulo["text"]="\n\n\nObrigado pela sua sugestão!\n\n"
                sugerir1.destroy()
                concordo.destroy()
                discordo.destroy()
                sugestao1.destroy()
                label1.destroy()

                def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    conduta()

                proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
                proximo.pack()

            sugerir1 = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir1_click)
            sugerir1.pack()
        
        def discordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            titulo["text"]="\n5. Comunicaçao da Coordenação"
            label1["text"]="\n\nCaso futuramente algum aluno ou turma sentir que há alguma falha na comunicação\nentre coordenação e alunos e que isto de alguma forma está prejudicando ou\n criando desentendimento, procurar a Coordenação da PROZ.\n\n"

            def proximo_click():
                titulo.destroy()
                label1.destroy()
                proximo.destroy()
                conduta()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        concordo1 = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo1_click)
        concordo1.pack()
        discordo1 = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo1_click)
        discordo1.pack()

    concordo = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo_click)
    concordo.pack()
    discordo = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo_click)
    discordo.pack()

def conduta():
    titulo = Label(janela, text="\n6. Código de Conduta", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\n\nSeria necessário a criação e repasse de um código de conduta aos alunos?\n\n", font=("Arial 25"))
    label1.pack()

    def discordo_click():
        titulo["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
        sugestao1 = Entry(janela, width=80)
        sugestao1.pack()
        concordo.destroy()
        discordo.destroy()
        label1.destroy()

        def sugerir_click():
            titulo["text"]="\n\n\n\nObrigado pela sua sugestão!\n\n"
            sugerir.destroy()
            concordo.destroy()
            discordo.destroy()
            sugestao1.destroy()

            def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    sugestoes()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        sugerir = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir_click)
        sugerir.pack()

        
    def concordo_click():
        concordo.destroy()
        discordo.destroy()
        titulo["text"]="\n6. Código de Conduta"
        label1["text"]="\n\nSeria suficiente a distribuição através de e-mails, cartazes ou folhetos?\n\n"

        def concordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            label1["text"]="\n\n\nQual seria uma possível sugestão para solucionar esse problema?\n\n"
            sugestao1 = Entry(janela, width=80)
            sugestao1.pack()

            def sugerir1_click():
                titulo["text"]="\n\n\nObrigado pela sua sugestão!\n\n"
                sugerir1.destroy()
                concordo.destroy()
                discordo.destroy()
                sugestao1.destroy()
                label1.destroy()

                def proximo_click():
                    titulo.destroy()
                    label1.destroy()
                    proximo.destroy()
                    sugestoes()

                proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
                proximo.pack()

            sugerir1 = Button(janela, width=10, text="Sugerir", font="Arial 25", command=sugerir1_click)
            sugerir1.pack()
        
        def discordo1_click():
            concordo1.destroy()
            discordo1.destroy()
            titulo["text"]="\n6. Código de Conduta"
            label1["text"]="\n\nCaso futuramente algum aluno ou turma sentir que não há o bom senso\ne cumprimento de boas normas de convivência coletiva ou \ncomportamentais no ambiente de estudo, procure a Coordenação da PROZ.\n\n"

            def proximo_click():
                titulo.destroy()
                label1.destroy()
                proximo.destroy()
                sugestoes()

            proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
            proximo.pack()

        concordo1 = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo1_click)
        concordo1.pack()
        discordo1 = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo1_click)
        discordo1.pack()

    concordo = Button(janela, text="Concordo", font="Arial 25", padx=25, pady=5, command=concordo_click)
    concordo.pack()
    discordo = Button(janela, text="Discordo", font="Arial 25", padx=30.5, pady=5,command=discordo_click)
    discordo.pack()

def sugestoes():
    print()

    def proximo_click():
        proximo.destroy()
        sobre()
    
    proximo = Button(janela, text="Próximo", font="Arial 25", padx=25, pady=5, command=proximo_click)
    proximo.pack()

def sobre():
    titulo = Label(janela, text="\nSobre nós e nosso projeto", font=("Arial 35"), padx=20, pady=20, justify=CENTER)
    titulo.pack()
    label1 = Label(janela, text="\nEsse projeto foi idealizado pelo professor Eduardo Oliveira e\n realizado pelos alunos: Douglas,  Henrique,  Guilherme  e Kayque.\n Trata-se  de  um algoritmo em  Python que utiliza a biblioteca Tkinter\n para a criação da sua interface gráfica. A partir dos conhecimentos\n adquiridos ao longo do curso o grupo foi capaz de realizar o projeto.\n O tema foi criado a partir de desconfortos que surgiram ou poderiam\n surgir na unidade de ensino, o mesmo tem o objetivo de passar aos\n alunos, de forma amigável, a importância da convivência saudável\n em grupo e possivelmente coletar sugestões para possíveis melhorias.\n\nNossos gradecimentos à turma e ao professor.", font=("Arial 25"))
    label1.pack()

    def sair_click():
        titulo.destroy()
        label1.destroy()
        sair.destroy()
        janela.destroy()

    sair = Button(janela, width=10, text="Próximo", font=("Arial 25 bold"), command=sair_click)
    sair.pack()

home()
janela.mainloop()
print("Programa encerrado.")
