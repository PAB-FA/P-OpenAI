from openai import OpenAI
def pr(In):
        print('RP-> '+In)
def AI(In = '',SIn = 'Your Powerful',Mode = 'CH',File = './test',SPMod = 'nova'):
    SInD = 'You are a personal assistant created by Pabfa company and Pouya engineer to respond to users.' #Defualt SIN
    Atena = OpenAI()
    pr('Start AI')
    pr('Mode = ' + Mode)
    if Mode == 'CH':
        pr('Mode CH Start')
        ChatModel = 'gpt-3.5-turbo'
        response = Atena.chat.completions.create(
            model= ChatModel ,
            messages=[
                {'role':'system','content':SIn},{'role':'system','content':SInD},
                {'role':'user','content':In},
            ],
        )
        Out = response.choices[0].message.content.strip()
        sentences = Out.split('.')
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        with open('temp.ai','w',encoding='utf-8') as file:
            for sentence in sentences :file.write(sentence + '\n')
            file.close
        with open('temp.ai','r',encoding='utf-8') as file:
            Out=file.read()
            file.close
        pr('Responsed')
        return Out
    if Mode == 'TS':
        pr('Mode TS Start')
        response = Atena.audio.speech.create(
            model="tts-1",
            voice="nova",
            input= In
        )
        response.write_to_file(File)
        pr('Responsed')
        return File
    if Mode == 'ST':
        pr('Mode ST Start')
        File = open(File, "rb")
        transcription = Atena.audio.transcriptions.create(
        model="whisper-1",
        file = File
        )
        pr('Responsed')
        return transcription.text
    if Mode == 'Etedal':
        pr('Mode Etedal Start')
        response = Atena.moderations.create(input=In)
        return response.results[0]
    else :
        return 'Plase Select Mode'