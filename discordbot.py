import discord
import random
import time
import asyncio
import discord.ext
from discord.ext import commands
import os
import traceback
import random
from googlesearch import search
from googletrans import Translator

bot = commands.Bot(command_prefix="mu:", help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =706416588160499796
ModeFlag = 0
translator = Translator()




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
    
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはよう！')
 # 挨拶する非同期関数を実行

@bot.command()
async def help(ctx):#コマンドを定義するときの関数は必ずContextという引数が渡される。つまり引数を最低一つだけでも書いておかないと動かないので注意
    embed = discord.Embed(title="ヘルプ", description="このヘルプコマンドにはプレフィックスを書いていないため、\n実行には全て`mu:コマンド名`とする必要があります。",color=0x4169e1)
    #↑ここのテキストは自分で修正よろしく
    embed.add_field(name="**help**", value="このコマンドです。",inline=False)
    embed.add_field(name="**about**", value="botについてや、botの招待リンク、サポートサーバーを確認できます。",inline=False)
    embed.add_field(name="**newinfo**", value="新着情報を確認します。",inline=False)
    embed.add_field(name="**コマンド無し**", value="「mumeinosato-global」というチャンネルを作成するとグローバルチャットに参加できます。",inline=False)
    embed.add_field(name="**game**", value="このbotでできるゲーム一覧を表示します。",inline=False)
    embed.add_field(name="**tool**", value="便利ツール一覧を表示します。",inline=False)
    embed.add_field(name="**servermanagement**", value="サーバー運営に役立つコマンド一覧を表示します。", inline=False)
    embed.add_field(name="**partner**", value="提携しているもの一覧を表示します。",inline=False)
    embed.add_field(name="**myinformation 〔パスワード〕**", value="登録内容を表示します。（パスワードを持っている場合のみアクセスできます。)",inline=False)
    await ctx.send(embed=embed)#Contextにはいろいろな情報が入っており、そこから様々な関数、情報にアクセスできる。ctx.sendがその一つ

@bot.command()
async def about(ctx):
    embed = discord.Embed(title="このbotについて...", description="Mumeinosato bot/ むめいのさと　ぼっと",color=0x4169e1)
    embed.add_field(name="製作者", value="Mumeinosato#7252 \n[無名の里](https://www.youtube.com/channel/UCpb92184AP2Ffhyf7u2bD3w?view_as=subscriber) [@mumeinosato](https://mobile.twitter.com/mumeinosato)",inline=False)
    embed.add_field(name="バージョン", value="Ver.1.3.3\n提携サーバー表示版",inline=False)
    embed.add_field(name="このbotを招待", value="[こちら](https://discord.com/api/oauth2/authorize?client_id=729668738877620255&permissions=272103536&scope=bot)から招待できます",inline=False)
    embed.add_field(name="サポートサーバー", value="[こちら](https://discord.gg/csJHtxZ)から参加できます。",inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def newinfo(ctx):
    await embox("新着情報","\n**2020 9/6** 提携サーバー「partnerserver」で確認可能。　\n**2020 9/6** wiki:LINE、YouTube追加。　\n**2020 9/5**　wiki改良。\n**2020 8/13** おみくじ内容追加。　\n**2020 8/12** おみくじ機能実装。　\n**2020 7/9** 試験運用開始。\n**2020 7/9 **  BOTの稼働を開始しました。",0x4169e1,ctx.message)

@bot.command()
async def servermanagement(ctx):
    await embox("サーバー運営に役立つコマンド一覧", "\n**mesay (喋らせたい言葉)** \n埋め込みメッセージを送信します。　\n**promotionalwarning** \n宣伝チャンネル以外で宣伝した人向けに警告文を表示します",0xffff00,ctx.message)

@bot.command()
async def game(ctx):
    await embox("ゲーム一覧", "\n**omikuji** \nおみくじを引くことができます。　\n**dice** \nサイコを振ることができます。",0x4169e1,ctx.message)              
 
@bot.command()
async def tool(ctx):
    await embox("便利ツール一覧", "\n**google** \nGoogle検索をします。　\n**translation** \n翻訳をします。　\n**charactercode** \n言語を検出します。　\n**ping** \nbotのメッセージ送信速度をチェックします。",0x4169e1)

@bot.command()
async def partner(ctx):
    await embox("提携一覧", "\n**partnerserver** \n提携サーバーを表示します。",0x4169e1,ctx.message)
    
@bot.command()
async def promotionalwarning(ctx):
    await embox("宣伝チャンネルをご利用ください", "このチャンネルでは、宣伝が禁止されています。",0xff0000,ctx.message)
    
@bot.command()
async def myinformation3861(ctx):
    await embox("無名の里サービスに登録内容", "無名の里サービスの登録内容を確認できます。",0xff0000,ctx.message)
    embed = discord.Embed(title="「雑談　暇人の仲間」の提携鯖主です", description="以下のリンクから提携をキャンセルできます",color=0x4169e1)
    embed.add_field(name="提携キャンセルページ:", value="https://forms.gle/GAH6zP43H3JmPEx49")
    await ctx.send(embed=embed)    
    
@bot.command()
async def test(ctx):
    await embox("これはテストコマンドです。","特に意味はありません。",0x4169e1,ctx.message)

@bot.command()
async def emsay(ctx,*,arg):
  await ctx.send(embed=discord.Embed(description=arg))
    
@bot.command()
async def ping(ctx):
    starttime = time.time()
    msg = await ctx.send("Pingを測定しています。\nしばらくお待ちください...")
    ping = time.time() - starttime
    await msg.edit(content=f"測定結果:{round(ping * 1000)}ms")
    #float(ping * 1000)

@bot.command()
async def partnerserver(ctx):
    embed = discord.Embed(title="提携サーバー一覧", description="以下のリンクから申請できます。",color=0xff0000)
    embed.add_field(name="申請ページ:", value="https://forms.gle/53okyZb9L6MXztzq6")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="Weaの雑談サーバー", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/9ayfU9K")
    await ctx.send(embed=embed) 
    embed = discord.Embed(title="Minecraft非公式コミュニティ", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/9rHM6FP")
    await ctx.send(embed=embed) 
    embed = discord.Embed(title="Torippiiism", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/kH6uR6R")
    embed = discord.Embed(title="nakiの公開用鯖〜皆にnitroください", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/5yavTEP")
    await ctx.send(embed=embed) 
    embed = discord.Embed(title="雑談サーバー旧(新型コロッケサーバー)", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/xmJT5As")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="楽しく雑談サーバー", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/By7efDM")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="✨Eveyone's notepad✨", description="以下のリンクから参加できます ",color=0x4169e1)
    embed.add_field(name="招待リンク:", value="https://discord.gg/JtSbYWP")
    await ctx.send(embed=embed)
    embed = discord.Embed(title="雑談＆大都市マイクラ！（統合)",description="以下のリンクから参加できます ",color=0x4169e)
    embed.add_field(name="招待リンク:", value="https://discord.gg/dySMGdg")
    await ctx.send(embed=embed)
    
@bot.event
async def on_message(message):
    """
    if message.author == bot.user:
        return
    """#Bot判定は下のif文で十分。ちなみにこれは複数行コメントアウト
    if message.author.bot:
        return
    
    GLOBAL_CH_NAME = "mumeinosato-global"
    
    if message.channel.name == GLOBAL_CH_NAME:                                                          
        print("success")
        await message.delete() # 元のメッセージは削除しておく
        channels = bot.get_all_channels()
        global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]
        embed = discord.Embed(title="メッセージを送信しました",
            description=message.content, color=0x00bfff)
        embed.set_author(name=message.author.display_name,                                                                            
            icon_url=message.author.avatar_url_as(format="png"))
        embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
            icon_url=message.guild.icon_url_as(format="png"))# Embedインスタンスを生成、投稿者、投稿場所などの設定
        for channel in global_channels:# メッセージを埋め込み形式で転送
            await channel.send(embed=embed)
    
    global ModeFlag
    if message.content == '!exit':
        await message.channel.send('ﾉｼ')
        sys.exit()
    # google検索モード(次に何か入力されるとそれを検索)
    if ModeFlag == 1:
        kensaku = message.content
        ModeFlag = 0
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(kensaku, lang="jp",num_results = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break
    # google検索モードへの切り替え
    if message.content == 'mu:google':
        ModeFlag = 1
        await message.channel.send('検索するワードをチャットで発言してね')
        
    if message.content.startswith('mu:translation'):
        say = message.content
        say = say[7:]
        if say.find('-') == -1:
            str = say
            detact = translator.detect(str)
            befor_lang = detact.lang
            if befor_lang == 'ja':
                convert_string = translator.translate(str, src=befor_lang, dest='en')
                embed = discord.Embed(title='翻訳結果', color=0x4169e1)
                embed.add_field(name='翻訳前', value=str)
                embed.add_field(name='翻訳後', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
            else:
                convert_string = translator.translate(str, src=befor_lang, dest='ja')
                embed = discord.Embed(title='翻訳結果', color=0x4169e1)
                embed.add_field(name='翻訳前', value=str)
                embed.add_field(name='翻訳後', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
        else:
            trans, str = list(say.split('='))
            befor_lang, after_lang = list(trans.split('-'))
            convert_string = translator.translate(str, src=befor_lang, dest=after_lang)
            embed = discord.Embed(title='翻訳結果', color=0x4169e1)
            embed.add_field(name='翻訳前', value=str)
            embed.add_field(name='翻訳後', value=convert_string.text, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith('mu:charactercode'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語はたぶん ' + detect.lang + ' です。言語コードは、こちらから確認できます。https://ja.wikipedia.org/wiki/ISO_639-1コード一覧'
        await message.channel.send(m)    
    
    if bot.user in message.mentions:
        print(f"{message.author.name}にメンションされました")
        await message.channel.send(f"{message.author.mention} ヘルプが必要なのか？\nmu:help でヘルプを表示しろよ")
        
    elif message.content == "mu:dice":
        await embox("サイコロコマンドが実行されました",f"サイコロぐらい自分でやれよ　今回だけだぞ　分かったなしっかり覚えておけよ\n\n実行者:{message.author.name}",0x4169e1,message)
        await asyncio.sleep(2)
        x = random.randint(1,6) # 50から100の乱数をxに代入
        await embox("結果は、、",f"結果は {str(x)} だよ　分かったか",0x4169e1,message)
        return

    elif message.content == "mu:omikuji":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="おみくじ", description=f"{message.author.mention}さんの今日の運勢は！",
                              color=0x4169e1)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[運勢] ", value=random.choice(('大大吉', '大吉', '向大吉', '末大吉', '吉', '中吉', '小吉', '後吉', '吉凶未分末大吉', '吉凶相交末吉', '吉凶相半', '吉凶相央', '小凶後吉', '凶後吉', '凶後大吉', '凶', '大凶')), inline=False)
        await message.channel.send(embed=embed)
    
    elif message.content.startswith("こんにち"):
        await message.channel.send("こん")

    elif message.content.startswith("こんちゃ"):
        await message.channel.send("こん")

    elif message.content.startswith("ども"):
        await message.channel.send("どーもです")

    elif message.content.startswith("よろし"):
        await message.channel.send("よろ")

    elif message.content.startswith("ただいま"):
        await message.channel.send("おか")

    elif message.content.startswith("飯落ち"):
        await message.channel.send("いってら")

    elif message.content.startswith("落ち"):
        await message.channel.send("おつ〜")

    elif message.content.startswith("ばい"):
        await message.channel.send("ばーい")

    elif message.content.startswith("死ね"):
        await message.channel.send("そういうのよくないよ")

    elif message.content.startswith("おはよ"):
        await message.channel.send("おは")
        
    elif message.content.startswith("暇"):
        await message.channel.send("俺も暇だな〜")
        
    elif message.content.startswith("初めまして"):
        await message.channel.send("よろ〜")
        
    elif message.content.startswith("草"):
        await message.channel.send("草")
                
    elif message.content.startswith("w"):
        await message.channel.send("www")
        
    elif message.content.startswith("だろ"):
        await message.channel.send("そうだよ")
        
    elif message.content.startswith("そうだよ"):
        await message.channel.send("そうだよ")
        
    elif message.content.startswith("こんばん"):
        await message.channel.send("こんばんわんこそば")
        
    elif message.content.startswith("今何時？"):
        await message.channel.send("さて何時だろう。自分で見ろw")
        
    elif message.content.startswith("えぇっと"):
        await message.channel.send("何々？")
        
    elif message.content.startswith("ちわっす"):
        await message.channel.send("ちわっす！")
        
    elif message.content.startswith("えぇ...(困惑)"):
        await message.channel.send("困ってる？ならこのBotを使おう！(宣伝)")
        
    elif message.content.startswith("せやな"):
        await message.channel.send("https://tenor.com/view/%e7%8c%ab%e5%ae%ae%e3%81%b2%e3%81%aa%e3%81%9f-smile-virtual-youtuber-nekomiya-gif-11959563")
        
    elif message.content.startswith("そうだね"):
        await message.channel.send("そうだよ")    
                                        
    await bot.process_commands(message)#on_messageの定義内の最後にこれを入れないと定義したコマンドが動かなくなる。注意

bot.run(token)
