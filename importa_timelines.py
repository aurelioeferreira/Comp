import os
#Esse módulo importa para um projeto do DaVinci Resolve timelines no formato fcpxml ainda não importadas neste projeto.
#vai
arquivos = []
extensao = ".fcpxml" #precisa ser fcpxml, pois timelines xml não foram importadas (versão 18.5 estável do DaVinci)
pasta = r"D:\Curso Python programação e machine learning para iniciantes\Gravações"
for file in os.listdir(pasta):
    if file.endswith(extensao):
        print(file)
        arquivos.append(file)

resolve = app.GetResolve() #Pega objeto Resolve. Precisa que DaVinci Resolve esteja aberto. app é um objeto interno do DaVinci.
projectManager = resolve.GetProjectManager()
projeto = projectManager.GetCurrentProject()
mediapool = projeto.GetMediaPool()

timeline_count = projeto.GetTimelineCount() 
timelines = []
for i in range(timeline_count):
	timelines.append(projeto.GetTimelineByIndex(i+1))        

for arquivo in arquivos:
    ja_tem = False #já tem esse arquivo importado como uma timeline no projeto?
    for timeline in timelines:
         if str(timeline) in str(arquivo):
              ja_tem = True
              break
    if not ja_tem: #se não tem ainda essa timeline, importe no projeto.
        caminhoArquivo = rf"{pasta}\{arquivo}"
        timeline = mediapool.ImportTimelineFromFile(caminhoArquivo, {"timelineName": arquivo.removesuffix(extensao)})