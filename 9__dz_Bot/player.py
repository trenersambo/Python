"""Модуль игрока"""
from aiogram import types
import game
import bot
import emoji
import text


async def player_turn(message: types.Message):
    """Ход игрока"""
    name = message.from_user.full_name
    await message.answer(f'{name}, твой ход! Сколько конфет возьмешь?')


async def player_game(message: types.Message, take: str, name: str):
    """Обработка хода игрока"""
    if take.isdigit():
        take = int(take)
        if (game.get_total() - take) < 0:
            await message.answer(f'{name}, хочет взять - {take} {text.declension_sweets(take)[0]},'
                                 f' но на столе всего {game.get_total()}.\n'
                                 f'Возьми поменьше, не жадничай{emoji.emojize("😃")}')
        elif take <= 0 or take > 28:
            await message.answer(f'{name}, можно брать не менее 1 и '
                                 f'не более 28{emoji.emojize("👆")}')
        elif 1 <= take <= 28:
            game.take_sweets(take)
            if await game.check_win(message, 'player', take):
                return
            if take <= 5:
                await message.answer(f'{name} берет всего {take} '
                                     f'{text.declension_sweets(take)[0]}.'
                                     f'\nЧто так мало? Бери больше,'
                                     f' не скромничай{emoji.emojize("😋")}\n\n'
                                     f'На столе осталось {game.get_total()} '
                                     f'{text.declension_sweets(game.get_total())[1]}. '
                                     f'Ходит бот!')
                await bot.bot_turn(message)
            elif take >= 24:
                await message.answer(f'{name} берет аж {take} {text.declension_sweets(take)[0]}.'
                                     f'\nМного сладкого вредно{emoji.emojize("😏")}\n'
                                     f'\nНа столе осталось {game.get_total()} '
                                     f'{text.declension_sweets(game.get_total())[1]}. Ходит бот!')
                await bot.bot_turn(message)
            else:
                await message.answer(f'{name} берет {take} {text.declension_sweets(take)[0]}.'
                                     f'\nНа столе осталось {game.get_total()} '
                                     f'{text.declension_sweets(game.get_total())[1]}. Ходит бот!')
                await bot.bot_turn(message)
    else:
        await message.answer(f'Что-то тут не то! Вводи число{emoji.emojize("🤦")}')
