import os
from dotenv import load_dotenv
from telethon import TelegramClient, events, errors
import asyncio
import time
from datetime import datetime

# Memuat variabel dari file .env
load_dotenv()

# Mengambil variabel dari environment dan memastikan semuanya ada
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
phone_number = os.getenv('PHONE_NUMBER')
sender_id = os.getenv('SENDER_ID')
grup_id = os.getenv('GRUP_ID')

# Cek apakah semua variabel lingkungan sudah diatur
if not all([api_id, api_hash, phone_number, sender_id, grup_id]):
    raise ValueError("Pastikan semua variabel lingkungan API_ID, API_HASH, PHONE_NUMBER, SENDER_ID, dan GRUP_ID sudah diatur di file .env")

# Konversi sender_id dan grup_id ke integer
sender_id = int(sender_id)
grup_id = int(grup_id)

# Membuat klien Telethon
client = TelegramClient('sesi-login', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    # Mendapatkan ID chat dan teks pesan
    chat_id = event.chat_id
    message_text = event.message.message
    incoming_time = datetime.now()

    # Menampilkan ID pengirim dan pesan yang diterima di konsol jika ID pengirim sesuai
    if event.sender_id == sender_id:
        print(f"Pesan diterima dari {sender_id}: {message_text}")
        
        # Membalas pesan, aktifkkan jika ingin membalas pesan.... 
        send_time = datetime.now()
        # Menghitung selisih waktu dalam milidetik
        time_diff = (send_time - incoming_time).total_seconds() * 1000
        await event.reply(f"Selisih waktu (milidetik): {time_diff:.3f} ms")
        
        # Meneruskan pesan ke grup
        try:
            await client.forward_messages(grup_id, event.message)
            print(f"Pesan diteruskan ke grup dengan ID: {grup_id}")
        except errors.ChatAdminRequiredError:
            print("Bot tidak memiliki izin untuk meneruskan pesan ke grup tersebut.")

async def main():
    while True:
        try:
            await client.start(phone_number)
            print("Bot sudah berjalan dan menunggu pesan...")
            await client.run_until_disconnected()
        except (errors.ConnectionError, errors.TimeoutError):
            print("Koneksi terputus. Mencoba untuk menghubungkan kembali...")
            await client.disconnect()
            await asyncio.sleep(5)  # Tunggu 5 detik sebelum mencoba menghubungkan kembali

with client:
    client.loop.run_until_complete(main())
