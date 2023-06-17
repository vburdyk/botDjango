import requests
from aiogram import Bot, Dispatcher, types, executor

BOT_TOKEN = "***********************************"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['catalog'])
async def catalog_command(message: types.Message):
    api_url = 'https://9add-91-245-117-166.ngrok-free.app/api/v1/products/'

    response = requests.get(api_url)
    products = response.json()

    if not products:
        await message.reply("There is no products in catalog!")
        return

    products_text = '\n'.join([f"{product['title']}: {product['price']}$" for product in products])

    await message.reply(f"Catalog of products:\n  {products_text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
