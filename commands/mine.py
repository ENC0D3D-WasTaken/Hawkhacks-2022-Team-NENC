from main import *

@bot.command(aliases=['MINE','m','M'])
async def mine(ctx):
    user = await getUser(ctx.message.author.id)
    if user is not False:
        await deleteMessage(ctx.message)
        name = ctx.message.author.name
        difficulty = randint(1,3)
        correct = False
        number1 = 0
        payout = 0
        number2 = 0
        operator = '+'
        answer = 0
        match difficulty:
            case 1:
                number1 = randint(-10,10)
                number2 = randint(-10,10)
                payout = randint(1,5)
            case 2:
                operator = random(['+','-'])
                number1 = randint(-100,100)
                number2 = randint(-100,100)
                payout = randint(5,10)
            case 3:
                operator = random(['+','-','*','/'])
                number1 = randint(-5000,5000)
                number2 = randint(-5000,5000)
                payout = randint(10,20)
        match operator:
            case '+':
                answer = number1 + number2
            case '-':
                answer = number1 - number2
            case '*':
                answer = number1 * number2
            case '/':
                answer = number1 / number2
        answer = round(answer,2)
        question = f'{name}, How much is {number1} {operator} {number2}?'
        questionEmbed = Embed(title=question, description=f'{name}, the question is of {difficulty} and if answered correctly will reward you with {payout} dollars, If you don\'t answer correctly you will be penalized with the same amount.', color=0x93f5e9)
        embed = await ctx.send(embed=questionEmbed)
        msg = await bot.wait_for('message', timeout=30.0, check=lambda message: message.author == ctx.message.author)
        if msg.content == str(answer):
            winmsg = Embed(title=f'Good Job!', description=f'{name}, you answered correctly and have been rewarded {payout} dollars.', color=0x93f5e9)
            win = await ctx.send(embed=winmsg)
            await deleteMessage(win)
            correct = True
            db.execute(f'UPDATE users SET balance = :bal WHERE memberId = :memberId',{'bal':user.balance + payout,'memberId':user.memberId})
        else:
            losemsg = Embed(title=f'Better Luck Next Time!', description=f'{name}, you answered incorrectly and have been penalized {payout} dollars.', color=0x93f5e9)
            lose = await ctx.send(embed=losemsg)
            db.execute(f'UPDATE users SET balance = :bal WHERE memberId = :memberId',{'bal':user.balance + payout,'memberId':user.memberId})
            await deleteMessage(lose)
        try:
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
            db.commit()
    else:
        msg = await ctx.send(f'You are not registered, {ctx.message.author.name}.')
        await deleteMessage(msg)