import asyncio
import discord
import random
import logging
from discord import app_commands

# ログの出力名を設定
logger = logging.getLogger('discoedbot')

# ログレベルの設定
logger.setLevel(20)
# ログのコンソール出力の設定
sh = logging.StreamHandler()
logger.addHandler(sh)


# ログの出力形式の設定
formatter = logging.Formatter('%(asctime)s:%(filename)s:%(lineno)d:%(levelname)s:%(message)s')
sh.setFormatter(formatter)
TOKEN = 'xxxxxx'

# 接続に必要なオブジェクトを生成

intents = discord.Intents.default()#適当に。
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="起動中"))  # ステータスメッセージを設定
    print("起動完了")
    print(f'discord.py バージョン: {discord.__version__}')  # discord.pyのバージョンを表示
    print ("にちかbot ver 1")
    await tree.sync()#スラッシュコマンドを同期
    channel_id = 1155085958216171611
    channel = client.get_channel(channel_id)
    if channel:
        await channel.send('Botが起動しました')
    while True:
      joinserver=len(client.guilds)
      servers=str(joinserver)
      await client.change_presence(activity = discord.Activity(name="/help | サーバー数: "+servers, type=discord.ActivityType.competing))

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
 


@tree.command(name="導入サーバー数",description="にちかbotの導入サーバー数が見れます")
async def guild(interaction: discord.Interaction):
    joinserver=len(client.guilds)
    servers=str(joinserver)
    await interaction.response.send_message("にちかbotの導入サーバー数:"+servers)


@tree.command(name="にちか",description="色んなメッセージを送ります")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(15)
    if ran == 0: 
        await interaction.response.send_message("#にちかは危険物")
    if ran == 1:
        await interaction.response.send_message("うんち")
    if ran == 2:
        await interaction.response.send_message("おうどん食べたい")
    if ran == 3:
        await interaction.response.send_message("私の名前はにちかボットです")
    if ran == 4:
        await interaction.response.send_message("おせちおせちおせち〇こ")
    if ran == 5:
        await interaction.response.send_message("にちかbotおおおおおおおおおおおおお")
    if ran == 6:
        await interaction.response.send_message("ここはどこ？")
    if ran == 7:
        await interaction.response.send_message("あいうえお")
    if ran == 8:
        await interaction.response.send_message("私はねぇにちかではなくにちかbotです")
    if ran == 9:
        await interaction.response.send_message("今、サンフランシスコにいる(？)")
    if ran == 10:
        await interaction.response.send_message("にちか天才")
    if ran == 11:
        await interaction.response.send_message("にちかは神様")
    if ran == 12:
        await interaction.response.send_message("暇だしゲームしよ〜")
    if ran == 13:
        await interaction.response.send_message("暇人おる？")
    if ran == 14:
        await interaction.response.send_message("にちかの家の屋根裏なう")


@tree.command(name="help",description="ヘルプコマンドです")
async def test_command(interaction: discord.Interaction):
   embed = discord.Embed(title="ヘルプ",description="にちかbotで使えるコマンド一覧です",color=0xF1C40F)
   embed.add_field(name="/導入サーバー数",value="現在にちかbotが入っているサーバー数が送信されます",inline=False)
   embed.add_field(name="/にちか",value="色んなメッセージを送ります",inline=False)
   embed.add_field(name="/返信",value="X(旧Twitter)で元々稼働してた「にちかbot」が返信してくれたものを送信します",inline=False)
   embed.add_field(name="/タイムライン返信",value="X(旧Twitter)で元々稼働してた「にちかbot」が返信してくれたものを送信します",inline=False)
   embed.add_field(name="/おふろ",value="録画してあげます♡",inline=False)
   embed.add_field(name="/学校",value="退学を促します",inline=False)
   embed.add_field(name="/教育",value="ビ〇グモーター副社長",inline=False)
   embed.add_field(name="/おみくじ",value="今日のあなたの運勢が確かめられます",inline=False)
   await interaction.response.send_message(embed=embed)


@tree.command(name="返信",description="X(旧Twitter)で元々稼働してた「にちかbot」が返信してくれたものを送信します")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(10)
    if ran == 0:
        await interaction.response.send_message("そんな無茶な！")
    if ran == 1:
        await interaction.response.send_message("えぇ.....")
    if ran == 2:
        await interaction.response.send_message("問題　にちかbotの製作者は？")
    if ran == 3:
        await interaction.response.send_message("ぁあ^～")
    if ran == 4:
        await interaction.response.send_message("リアルマネー欲しい")
    if ran == 5:
        await interaction.response.send_message("暇人.com")
    if ran == 6:
        await interaction.response.send_message("しりとりやろピカチュウのウから")
    if ran == 7:
        await interaction.response.send_message("やだ")
    if ran == 8:
        await interaction.response.send_message("ああああああああああああ")
    if ran == 9:
        await interaction.response.send_message("暇あ")


@tree.command(name="タイムライン返信",description="X(旧Twitter)で元々稼働してた「にちかbot」が返信してくれたものを送信します")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(12)
    if ran == 0:
        await interaction.response.send_message("おはようございます")
    if ran == 1:
        await interaction.response.send_message("寝たい")
    if ran == 2:
        await interaction.response.send_message("にちかて誰？")
    if ran == 3:
        await interaction.response.send_message("てめぇ....")
    if ran == 4:
        await interaction.response.send_message("にちか食べたい")
    if ran == 5:
        await interaction.response.send_message("にちかておいしいよね")
    if ran == 6:
        await interaction.response.send_message("なんだろう....")
    if ran == 7:
        await interaction.response.send_message("Twitter(現X)飽きた？")
    if ran == 8:
        await interaction.response.send_message("Q.オ〇ニーとかは？")
    if ran == 9:
        await interaction.response.send_message("俺は無実だ！！！")
    if ran == 10:
        await interaction.response.send_message("インテル入ってる")
    if ran == 11:
        await interaction.response.send_message("アル中カラカラ～")



@tree.command(name="おふろ",description="録画してあげます♡")
async def test_command(interaction: discord.Interaction):
        await interaction.response.send_message("●REC")


@tree.command(name="学校",description="退学を促します")
async def test_command(interaction: discord.Interaction):
        await interaction.response.send_message("退学したらええんちゃう")



@tree.command(name="教育",description="ビ〇グモーター副社長")
async def test_command(interaction: discord.Interaction):
        await interaction.response.send_message("教育教育教育教育教育教育教育教育教育教育教育教育教育教育教育教育死刑死刑死刑死刑死刑死刑死刑死刑死刑死刑死刑教育教育教育教育教育教育教育教育教育教育教育教育教育教育教育")






@tree.command(name="おみくじ",description="あなたの運勢が確かめられます")
async def test_command(interaction: discord.Interaction):
    ran = random.randrange(5)
    if ran == 0:
        await interaction.response.send_message("おみくじ結果: 大吉")
    if ran == 1:
        await interaction.response.send_message("おみくじ結果: 中吉")
    if ran == 2:
        await interaction.response.send_message("おみくじ結果: 小吉")
    if ran == 3:
        await interaction.response.send_message("おみくじ結果: 凶")
    if ran == 4:
        await interaction.response.send_message("おみくじ結果: 大凶 背後に気をつけてください")







            
@client.event
async def on_guild_join(guild):
    channel = guild.text_channels
    logger.info('サーバーに追加されました。')

    for txch in channel:
        try:
            embed = discord.Embed(title="にちかbotだお！", description="このbotは元ネタ『にちか』の許可の上作成しました。発言することはX(旧Twitter)で稼働してたにちかbotのセリフです(一部ありません)。ヘルプコマンド 【/help】\n[サポートサーバー](https://discord.gg/WDYtz2czfd)\n[ホームページ](https://kudaken.com/nichika/) \n[仕様](https://kudaken.com/nichika/about.html)\n※このbotは一部下ネタを発言します。苦手な人はご注意ください。", color=0xE67E22)
            await txch.send(embed=embed)
        except discord.errors.Forbidden:
            continue
        else:
            break

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)