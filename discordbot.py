import discord
import random
import time
import asyncio
import discord.ext
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix="mu:", help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(f"ヘルプは mu:help | 導入サーバー数: {len(bot.guilds)}"))
    
    #status=discord.Status.idle で退席状態に
    
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
   

async def embox(title,description,color,message):
      embed = discord.Embed(title=title,description=description,color=color)
      await message.channel.send(embed=embed)

@bot.command()
async def help(ctx):#コマンドを定義するときの関数は必ずContextという引数が渡される。つまり引数を最低一つだけでも書いておかないと動かないので注意
    embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`コマンド名`とする必要があります。煽ってきたりします。(先に言っておく)",color=0x77aa27)
    #↑ここのテキストは自分で修正よろしく
    embed.add_field(name="help", value="このコマンドです。",inline=False)
    embed.add_field(name="newinfo", value="新着情報を確認します。",inline=False)
    embed.add_field(name="wiki", value="開発者が知っていること、関係することについてwiki形式で見ることができます。",inline=False)
    embed.add_field(name="dice", value="サイコロを振ることができます。\n(現在エラーのため使用できません)",inline=False)
    embed.add_field(name="ping", value="BOTのメッセージ送信速度をチェックします。",inline=False)
    embed.add_field(name="about", value="botについてや、botの招待リンクを確認できます。",inline=False)
    embed.add_field(name="serverintroduction", value="開発者が運営しているサーバーについて表示できます。",inline=False)
    await ctx.send(embed=embed)#Contextにはいろいろな情報が入っており、そこから様々な関数、情報にアクセスできる。ctx.sendがその一つ

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="このbotについて...", description="Mumeinosato bot/ むめいのさと　ぼっと",color=0x77aa27)
    embed.add_field(name="製作者", value="Mumeinosato#7252",inline=True)
    embed.add_field(name="バージョン", value="Ver.1α\nテスト試験版",inline=False)
    embed.add_field(name="このbotを招待", value="[こちら](https://discord.com/api/oauth2/authorize?client_id=729668738877620255&permissions=272103536&scope=bot)から招待できます",inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def serverintroduction(ctx):
    embed = discord.Embed(title="開発者のサーバーについて...", description="以下のリンクから参加できます。",color=0x77aa27)
    embed.add_field(name="招待リンク:", value="https://discord.gg/nFtHPAZ")
    await ctx.send(embed=embed)

@bot.command()
async def newinfo(ctx):
    await embox("新着情報","\n**2020 6/24** コマンドフレームワークへ移行しました。\n**2020 5/15** 一般公開を開始しました。\n**2020 5/14** help等のコマンドを3つ実装しました。\n**2020 5/2 **  BOTの稼働を開始しました。",0x77aa27,ctx.message)

@bot.command()
async def test(ctx):
    await embox("これはテストコマンドです。","特に意味はありません。",0x77aa27,ctx.message)

@bot.command()
async def dice(ctx):
    embed = discord.Embed(title="サイコロコマンドが実行されました", description="何が出るかな？！何が出るかな？！",color=0x77aa27)
    embed.set_footer(title="{ctx.author.name} さんによる実行")
    await asyncio.sleep(1) # time.sleepはBotの動作を止める原因になるので厳禁!!!代わりにasyncio.sleep()を使おう
    x = random.randint(1,6) 
    await embox("結果は、、",f"結果は {x} でした！",0x77aa27,ctx.message)#{}の中ではstr型じゃ無くてもよい

@bot.command()
async def ping(ctx):
    starttime = time.time()
    msg = await ctx.send("測定中です...しばらくお待ちください。")
    ping = time.time() - starttime
    await msg.edit(content=f"結果:{round(ping * 1000)}ms")
    #float(ping * 1000)

@bot.command()
async def wiki(ctx, *,arg:str=""):
    """
    コマンドには引数を指定できる。
    例えばこの場合は「tb:wiki Switch」と送信すると引数argに"Switch"が渡される。
    ちなみに引数が無いときは空の文字列が自動で入るようになっているけどここの説明は難しいので省略
    """
    if not arg:#こうしておくと、文字列が空であるとき(つまりこの場合は引数が渡されなかったとき)にifの中が実行される
        embed = discord.Embed(title="WeaのWikiへようこそ！", description="開発者が知っていることや関係することについてwiki形式で紹介します。\n(実行は全て`wiki 単語名`というように行ってください。)",color=0x77aa27)
        embed.add_field(name="現在登録されているもの:", value="アスファルト 9: Legends\nNintendo Switch\nTJAPlayer3")
        await ctx.send(embed=embed)

    elif arg == "アスファルト 9: Legends":#スペースまで一字一句一致してないとifの中が実行されないので変えた方がいいかも
        await embox("アスファルト 9: Legends","アスファルト 9: Legends とは、\nゲームロフトが開発した\niOS、Android、Windows、Nintendo Switch、MacOS で\nプレイできるカーアクションレースゲームのこと。\nアスファルトシリーズ13作目(ナンバリングでは9作目)で、\n実在する車(マシン)を操作し、様々なロケーションでレースを行う。",0x77aa27,ctx.message)
    
    elif arg == "Nintendo Switch":
        await embox("Nintendo Switch","Nintendo Switch とは、\n任天堂が開発・販売をしている、\n据え置き型ゲーム機のこと。",0x77aa27,ctx.message)

    elif arg == "TJAPlayer3":
        await embox("TJAPlayer3","TJAPlayer3 とは、\nWindows向けの太鼓の達人エミュレーターの一つ。\n現在は配布を終了している。(Waybackmachineというツールを使用すればDL可)\n.tja 形式の譜面データと音源ファイルを用意することでプレイ可能。",0x77aa27,ctx.message)

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        # もし、送信者がbotなら無視する
        return
    GLOBAL_CH_NAME = "hoge-global" # グローバルチャットのチャンネル名

    if message.channel.name == GLOBAL_CH_NAME:
        # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する

        await message.delete() # 元のメッセージは削除しておく

        channels = client.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        # channelsはbotの取得できるチャンネルのイテレーター
        # global_channelsは hoge-global の名前を持つチャンネルのリスト

        embed = discord.Embed(title="hoge-global",
            description=message.content, color=0x00bfff)

        embed.set_author(name=message.author.display_name, 
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))
        # Embedインスタンスを生成、投稿者、投稿場所などの設定

        for channel in global_channels:
            # メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
    
            
@bot.event
async def on_message(message):
    """
    if message.author == bot.user:
        return
    """#Bot判定は下のif文で十分。ちなみにこれは複数行コメントアウト
    if message.author.bot:
        return

    if bot.user in message.mentions:
        print(f"{message.author.name}にメンションされました")
        await message.channel.send(f"{message.author.mention}ヘルプが必要なのか？\nmu:help でヘルプを表示しろよ")

    elif message.content.startswith("こんにち"):
        await message.channel.send("こん")

    elif message.content.startswith("こんちゃ"):
        await message.channel.send("こん")

    elif message.content.startswith("ども"):
        await message.channel.send("どうーもです")

    elif message.content.startswith("よろし"):
        await message.channel.send("よろ〜")

    elif message.content.startswith("ただいま"):
        await message.channel.send("おか")

    elif message.content.startswith("飯落ち"):
        await message.channel.send("いってら")

    elif message.content.startswith("落ち"):
        await message.channel.send("お疲れ～")

    elif message.content.startswith("ばい"):
        await message.channel.send("ばーい")

    elif message.content.startswith("死ね"):
        await message.channel.send("そうゆうのよくないよ〜")

    elif message.content.startswith("おはよ"):
        await message.channel.send("おは")
        
    elif message.content.startswith("暇"):
        await message.channel.send("俺も暇だな〜")

    await bot.process_commands(message)#on_messageの定義内の最後にこれを入れないと定義したコマンドが動かなくなる。注意

bot.run(token)
