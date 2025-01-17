#importando o flet
import flet as ft

#função principal que vai rodar o site ou aplicativo
def main(pagina):

    #titulo
    titulo = ft.Text("Chat de Texto")

    #função para o chat funcionar

    def enviar_mensagem_tunel(mensagem):
        
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    #campo enviar mensagem
    campo_enviar_mensagem = ft.TextField(label="digite sua mensagem")

    #função para enviar mensagem

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = (f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

    #botao enviar mensagem
    botao_enviar_mensagem = ft.ElevatedButton("enviar mensagem", on_click=enviar_mensagem)

    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar_mensagem])

    #criando o site

    chat = ft.Column()

    #Função para Entrar no Chat

    def entrar_nochat(evento):
        print("oi")

        #echar o popup
        popup.open = False
        #remover o titulo
        pagina.remove(titulo)
        #remover o botao
        pagina.remove(botao)

        #carregar o chat
        pagina.add(chat)

        #carregar o campo enviar mensagem
        pagina.add(linha_enviar)

        #ostrar quando alguem entra no chat
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} Entrou no chat"
        pagina.pubsub.send_all(mensagem)
       

        #atualizar a pagina
        pagina.update()


    #popup

    titulo_popup = ft.Text("Bem vindo ao Chat")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup = ft.ElevatedButton("entrar no chat", on_click=entrar_nochat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    #função para abrir o popup ao apertar o botão
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()


    #botão
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(titulo)
    pagina.add(botao)
    




#executar a função com o flet
ft.app(main, view=ft.WEB_BROWSER)