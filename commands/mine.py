from main import *

@bot.command(aliases=['MINE','m','M'])
async def mine(ctx):
    await ctx.message.delete(delay=0)
    user = getUser(ctx.message.author.id)
    if user is not False:
        num1 = 0
        num2 = 0
        operator = 0
        payout = 0
        operators = ['+','-','*','/']
        difficulty = randint(1,3)
        operator = choice(operators)
        if difficulty == 1:
            num1 = randint(-10,10)
            num2 = randint(-10,10)
            payout = randint(1,5)
        elif difficulty == 2:
            num1 = randint(-100,100)
            num2 = randint(-100,100)
            payout = randint(5,10)
        else:
            num1 = randint(-1000,1000)
            num2 = randint(-1000,1000)
            payout = randint(10,20)
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        else:
            answer = num1 / num2
        if difficulty == 1:
            difficulty = "Easy"
        elif difficulty == 2:
            difficulty = "Medium"
        else:
            difficulty = "Hard"
        question = Embed(title=f"How much is {num1} {operator} {num2}", description=f"{user.name}, you have been given a {difficulty} question to solve.\nThe payout for solving the question is {payout} dollars.\nIf you make a mistake you will be penalized with the same amount of money\n\n{num1} {operator} {num2} = ?", color=0x93f5e9)
        msg = await ctx.send(embed=question)
        callback = await bot.wait_for('message', check=lambda message: message.author == ctx.message.author)
        if callback.content == str(answer):
            await msg.delete(delay=0)
            msg = await ctx.send(f'{user.name}, you correctly solved the question and got rewarded {payout} BSD.')
            await deleteMessage(msg)
            user.balance += payout
        else:
            await msg.delete(delay=0)
            msg = await ctx.send(f'{user.name}, you made mistake and got a penalty of {payout} BSD deducted.')
            await deleteMessage(msg)
            user.balance -= payout
        db.commit()
        await callback.delete(delay=5)
    else:
        msg = await ctx.send(f'You are not a part of the tycoon, {user.name}.')
        deleteMessage(msg)