import os
import discord
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = 1471159197856043019

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} untuk mode scraping.')
    channel = client.get_channel(CHANNEL_ID)
    
    if channel is None:
        try:
            channel = await client.fetch_channel(CHANNEL_ID)
        except Exception as e:
            print(f"Error mengambil channel: {e}")
            await client.close()
            return
            
    if channel:
        print(f"Mulai menyalin teks dari channel: {channel.name}...")
        messages_text = []
        # Mengambil maksimal 200 pesan dari yang paling awal
        async for msg in channel.history(limit=200, oldest_first=True):
            if msg.content.strip():
                # Membersihkan pesan dari hal-hal yang tidak perlu jika memungkinkan,
                # tapi kita ambil raw text-nya saja dulu
                messages_text.append(f"{msg.content}")
        
        with open('data/data_stresteam.txt', 'w', encoding='utf-8') as f:
            f.write("=== SUMBER PENGETAHUAN SERVER STRESTEAM ===\n")
            f.write("Berikut adalah informasi resmi tentang server Stresteam:\n\n")
            f.write("\n---\n".join(messages_text))
            
        print("Selesai! Data telah ditulis ke data/data_stresteam.txt")
    else:
        print("Channel tidak ditemukan atau bot tidak punya akses ke channel tersebut.")
        
    await client.close()

if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
