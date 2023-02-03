from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())


@bot.event
async def on_ready():
  print('다음으로 로그인합니다: ')
  print(bot.user.name)
  print('connection was succesful')
  await bot.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name="치오야 도움말"),
                            status=discord.Status.idle)


@bot.command(aliases=[
  '되돌리기', '되', '나가', '정지', '반복', '지금음악', '지금노래', '지음', '지노', '일시정지', '핑', '재생',
  '재', '목록', '리스트', '플레이리스트', '제거', '제', '다시재생', '재게', '저장', '세이브', '검색', '찾기',
  '서버목록', '셔플', '랜덤', '스킵', '넘기기', '볼륨'
])
async def 공지(ctx):
  await ctx.send('')


TOKEN = os.environ['token']
Authorization = os.environ['Auth']
URL = os.environ['URL']

Ping = PingPong(URL, Authorization)
Ping2 = PingPong(URL, Authorization)


@bot.command(aliases=['개발자', '제작자', '만든놈'])
async def 크레딧(ctx):
  embed = discord.Embed(title="크레딧", description="이 봇을 만든놈", color=0xd4b886)
  embed.add_field(name="노예주인", value="아몬드#1734", inline=False)
  embed.add_field(name="코딩노예", value="SPAEER#7411", inline=False)
  embed.set_footer(text="PingPongTool 사용")
  await ctx.reply(embed=embed)


@bot.command(aliases=['도움말', '헬프', '도움'])
async def help1(ctx):
  embed = discord.Embed(title="", description="", color=0xd4b886)
  embed.add_field(name="`치오야 배워 [알려줄 말] [뜻]`",
                  value="`저에게 단어를 알려줄 수 있어요!`",
                  inline=False)
  embed.add_field(name="`치오야 음악도움말`", value="`음악 기능의 도움말!`", inline=False)
  embed.add_field(name="`치오야 미니게임도움말`",
                  value="`미니게임 명령어를 알려드려요!`",
                  inline=False)
  embed.add_field(name="`치오야 관리도움말`",
                  value="`서버 관리 명령어를 알려드려요!`",
                  inline=False)
  embed.add_field(name="`치오야 개발자`",
                  value="`아무도 안 궁금해 하는 치오의 개발자를 알려드려요!`",
                  inline=False)
  embed.set_footer(text="Chio")
  await ctx.reply('<@{}>'.format(ctx.message.author.id), embed=embed)


@bot.command(aliases=["음악도움말", "도움말음악"])
async def 도움말2(ctx):
  embed = discord.Embed(title="", description="", color=0xd4b886)
  embed.add_field(name="`음악 기능은 / 명령어도 있어요!",
                  value="`/를 입력해보세요`",
                  inline=False)
  embed.add_field(name="`치오야 재생(이름,URL)",
                  value="`음악을 재생해요.(같은 명령어 : 재)`",
                  inline=False)
  embed.add_field(name="`치오야 검색(이름)`",
                  value="`음악을 검색해서 재생해요.(같은 명령어 : 찾기)`",
                  inline=False)
  embed.add_field(name="`치오야 목록`",
                  value="`플레이리스트를 확인해요.(같은 명령어 : 리스트,플레이리스트`",
                  inline=False)
  embed.add_field(name="`치오야 스킵`",
                  value="`음악을 스킵해요.(같은 명령어 : 넘기기)`",
                  inline=False)
  embed.add_field(name="`치오야 일시정지`", value="`음악을 일시정지해요`", inline=False)
  embed.add_field(name="`치오야 다시재생`",
                  value="`음악을 다시 재생해요 (같은 명령어 : 재개 `",
                  inline=False)
  embed.add_field(name="`치오야 반복`", value="`음악을 반복해요`", inline=False)
  embed.add_field(name="`치오야 지금음악`",
                  value="`지금 재생중인 음악을 확인해요(같은 명령어 : 지음)`",
                  inline=False)
  embed.add_field(name="`치오야 제거`", value="`플레이리스트에 있는 음악을 제거해요`", inline=False)
  embed.add_field(name="`치오야 들어와`",
                  value="`치오가 음성 채널에 접속해요(같은 명령어 : 제)`",
                  inline=False)
  embed.add_field(name="`치오야 나가`",
                  value="`치오가 음성 채널을 나가요(같은 명렁어 : 정지)`",
                  inline=False)
  embed.add_field(name="`치오야 저장`",
                  value="`현재 음악을 저장해서 DM으로 보내드려요.(같은 명령어 : 세이브)`",
                  inline=False)
  embed.add_field(name="`치오야 되돌리기`",
                  value="`음악을 이전으로 되돌려요`(같은 명령어 : 되",
                  inline=False)
  embed.add_field(name="`치오야 셔플`",
                  value="`음악을 섞어요.(같은 명령어 : 랜덤)`",
                  inline=False)
  embed.add_field(name="`치오야 서버목록`",
                  value="`치오가 들어와 있는 서버를 확인해요`",
                  inline=False)
  embed.add_field(name="`치오야 볼륨`", value="`볼륨을 설정해요.`", inline=False)
  embed.set_footer(text="Chio")
  await ctx.reply('<@{}>'.format(ctx.message.author.id), embed=embed)


@bot.command(aliases=["미니게임도움말", "도움말미니게임"])
async def 도움말3(ctx):
  embed = discord.Embed(title="", description="", color=0xd4b886)
  embed.add_field(name="`치오야 돈 줘`", value="`돈줘 벅벅(쿨타임 1분)`", inline=False)
  embed.add_field(name="`치오야 슬롯 [베팅할 돈]`",
                  value="`모은 돈을 사용해 도박을 할 수 있어요!`",
                  inline=False)
  embed.add_field(name="`치오야 컬러 [베팅할 돈]`",
                  value="`모은 돈을 사용해 컬러라는 미니게임을 할 수 있어요!`",
                  inline=False)
  embed.add_field(name="`치오야 트럼프`", value="`아직 미완성..!`", inline=False)
  embed.set_footer(text="Chio")
  await ctx.reply('<@{}>'.format(ctx.message.author.id), embed=embed)


@bot.command(aliases=["관리도움말", "도움말관리"])
async def 도움말4(ctx):
  embed = discord.Embed(title="", description="", color=0xd4b886)
  embed.add_field(name="`치오야 킥 [유저#태그]`", value="`해당 유저를 추방해요!`", inline=False)
  embed.add_field(name="`치오야 밴 [유저#태그]`",
                  value="`해당 유저를 서버에서 차단해요!`",
                  inline=False)
  embed.add_field(name="`치오야 언밴 [유저#태그]`",
                  value="`해당 유저의 차단을 풀어요!`",
                  inline=False)
  embed.add_field(name="`치오야 지워 [삭제할값]`",
                  value="`서버의 채팅을 삭제해요!`",
                  inline=False)
  embed.set_footer(text="Chio")
  await ctx.reply('<@{}>'.format(ctx.message.author.id), embed=embed)


@bot.command(aliases=["삭제", "청소"])
async def 지워(ctx, *, amount):
  i = (ctx.message.author.guild_permissions.administrator)

  if i is True:
    if int(amount) > 100:
      await ctx.reply('100개 이상의 메시지는 지울 수 없어요!')
    else:
      await ctx.channel.purge(limit=int(amount) + 1)
      msg = await ctx.channel.reply('<@{}>, '.format(ctx.message.author.id) +
                                   amount + '개의 메시지를 삭제했습니다!')
      await asyncio.sleep(4)
      await msg.delete()

  if i is False:
    await ctx.channel.reply('<@{}>, '.format(ctx.message.author.id) +
                           '권한이 부족해요..!')


@bot.command(aliases=["추방"])
async def 킥(ctx, *, user_name: discord.Member, reason=None):
  i = (ctx.message.author.guild_permissions.administrator)

  if i is True:
    await user_name.kick(reason=reason)
    await ctx.reply(str(user_name) + "을(를) 추방했어요!")

  if i is False:
    await ctx.channel.reply('<@{}>, '.format(ctx.message.author.id) +
                           '권한이 부족해요..!')


@킥.error
async def 킥_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply("추방할 유저를 넣어주세요!")


@bot.command(aliases=["차단"])
async def 밴(ctx, *, user_name: discord.Member):
  i = (ctx.message.author.guild_permissions.administrator)

  if i is True:
    await user_name.ban()
    await ctx.reply(str(user_name) + "을(를) 차단했어요!")

  if i is False:
    await ctx.channel.reply('<@{}>, '.format(ctx.message.author.id) +
                           '권한이 부족해요..!')


@밴.error
async def 밴_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply("차단할 유저를 넣어주세요!")


@bot.command(aliases=["밴풀기", "차단풀기", "밴풀어", "차단풀어"])
async def 언밴(ctx, *, user_name):
  i = (ctx.message.author.guild_permissions.administrator)

  if i is True:
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = user_name.split('#')
    for ban_entry in banned_users:
      user = ban_entry.user
      if (user.name, user.discriminator) == (member_name,
                                             member_discriminator):
        await ctx.guild.unban(user)
        await ctx.reply(f"{user.mention}의 차단을 풀었어요!")

  if i is False:
    await ctx.channel.reply('<@{}>, '.format(ctx.message.author.id) +
                           '권한이 부족해요..!')


@지워.error
async def 지워_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply("삭제할 값을 넣어주세요!")


@bot.command()
async def 배워(ctx, learn, *, word):
  wb = openpyxl.load_workbook("memory.xlsx")
  ws = wb.active

  for i in range(1, 10000):
    if ws["A" + str(i)].value == "." or ws["A" + str(i)].value == learn:
      ws["A" + str(i)].value = learn
      ws["B" + str(i)].value = word
      await ctx.reply("추가했어요! 부적절한 단어가 있다면 삭제되거나 수정될 수도 있어요!")
      wb.save("memory.xlsx")
      break


@배워.error
async def 배워_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.reply('뭘 배울까요?')


@bot.listen()
async def on_command_error(ctx, error):
  if type(error) is commands.errors.CommandNotFound:
    data = await Ping.Pong(ctx.author.id,
                           ctx.message.content[4:],
                           NoTopic=False)
    brand = data['text'][:24]
    오류 = "오류 "
    if data['text'] == "몰?루" or data['text'] == 오류:
      res = ctx.message.content[4:]
      wb = openpyxl.load_workbook("memory.xlsx")
      ws = wb.active

      for i in range(1, 10000):
        val = ws["A" + str(i)].value
        if val == res:
          await ctx.reply(ws["B" + str(i)].value)
          break
      if val == res:
        pass
      else:
        if data['text'] == "몰?루" or data['text'] == 오류:
          response = random.choice(
            ["?", "..네에?", "뭐라구요?", "네?", "몰루?", "으응..", "으음...?"])
          await ctx.reply(response)
    elif brand != "아무말에도 곧잘 대답하는 이 봇은 핑퐁 빌더":
      await ctx.reply(data['text'])
      if data['image']:
        await ctx.reply(data['image'])
    else:
      data2 = await Ping2.Pong(ctx.author.id,
                               ctx.message.content[4:],
                               NoTopic=False)
      await ctx.reply(data2['text'])
      if data2['image']:
        await ctx.reply(data2['image'])


token = os.environ['token']
PREFIX = os.environ['PREFIX']
bot.run(token)
