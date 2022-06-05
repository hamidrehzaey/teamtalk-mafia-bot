#!/usr/bin/python3
# -*- coding: utf-8 -*-

import teamtalk, random, os, configparser, sys, threading, win32gui, win32con, ctypes, winsound
ctypes.windll.kernel32.SetConsoleTitleW("teamtalk mafia bot-v2.0")
t = teamtalk.TeamTalkServer()

newRoles = []
god_role_list = []
players = []

numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]

full_mafia =["پدر خوانده", "دکتر لِکتِر", "مافیای ساده1", "مافیای ساده2", 'دزد', 'ناتاشا', 'شهروند ', 'ناتو', 'حرفه ای مافیا', 'تروریست', 'مذاکره‌کننده', 'سم ', 'داروساز', 'شب خسب', 'بازجو', 'خرابکار', 'یاکوزا', 'افسونگر', 'گروگانگیر', 'آمپول زن', 'مرد قهرمان', ]
p_mafia = []
r_mafia = []
send_to_mafia_players = []

normal_votelists = set()
normal_voteUserList = set()

card_name = ["شلیک نهایی", "مسیر سبز", "بیخوابی", "دروغ سیزده", "ذهن زیبا", "فرش قرمز"]
card_number = ['1', '2', '3', '4', '5', '6']

hidden_main_votelists = []
hidden_votelists = set()
hidden_voteUserList = set()
hidden_vote_list_result = []

timeUserList = set()

@t.subscribe("messagedeliver")
def roles(server, params):
	global role_content
	if params["type"] != teamtalk.USER_MSG:
		return

	hwnd = win32gui.GetForegroundWindow()
	win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

	role_content = params["content"]
	role_user = t.get_user(params["srcuserid"])
	nickname = role_user["nickname"]
	if role_user.get('chanid') == int(chanid):
		if nickname == " god" and role_content == 'b' or nickname == " god" and role_content == 'ذ':
			t.broadcast_message('مافیا بازها بیایید بازی.')
		if nickname == " god" and role_content == "شروع" or nickname == " god" and role_content == "start":
			t.channel_message('به بازی شبهای مافیا خوش اومدید.')
			channel_users = t.get_users_in_channel(int(chanid))
			for user in channel_users:
				new_user = user['nickname']
				for number in numbers:
					if number in new_user:
						players.append(new_user)
						players.sort()
			if len(players) < 8:
				t.channel_message('تعداد بازیکنها کمتر از 8 نفر میباشد.')
			else:
				t.channel_message(f"{len(players)} نفر در این بازی شرکت دارند.")
				t.user_message(" god", '12 نقش استاندارد در لیست وجود دارد.\nآیا مایل هستید نقش جدیدی را به لیست نقش ها اضافه کنید؟\nبله یا خیر نوشته و بفرستید.')

				@t.subscribe('messagedeliver')
				def role_question(server, params):
					if params['type'] != teamtalk.USER_MSG:
						return

					role_question_content = params['content']
					role_question_user = t.get_user(params["srcuserid"])
					nickname = role_question_user["nickname"]
					if role_question_user.get('chanid') == int(chanid):
						if nickname == " god" and role_question_content == "بله":
							t.user_message(' god', 'نقش ها رو با گذاشتن ویرگول یا کاما  بینشون وارد کنید.\nتوجه داشته باشید اگه نقشهای وارد شده بدون ویرگول یا کاما باشند یک نقش حساب خواهند شد.')

							@t.subscribe("messagedeliver")
							def add_role(server, params):
								if params['type'] != teamtalk.USER_MSG:
									return
								add_role_content = params['content']

								extra_list_roles = ["پدر خوانده", "دکتر لِکتِر", "مافیای ساده1", "مافیای ساده2", "دکتر", "روانپزشک", "اِسنایپِر یا حرفه ای", "کارآگاه", "شهردار", "جان سخت", "شهروند ساده1", "شهروند ساده2"]

								if not add_role_content == "بله" and not add_role_content == "نقش":
									for i in add_role_content.split(','):
										extra_list_roles .append(i)

									if len(extra_list_roles) == len(players):
										t.user_message(' god', 'با ارسال کلمه نقش، نقش ها را برای همه ارسال کنید. ')

										@t.subscribe("messagedeliver")
										def unconstant_role_sending(server, params):
											if params['type'] != teamtalk.USER_MSG:
												return
											unconstant_role_content = params['content']
											unconstant_role_user = t.get_user(params["srcuserid"])
											nickname = unconstant_role_user["nickname"]
											if unconstant_role_user.get('chanid') == int(chanid):
												if nickname == " god" and unconstant_role_content == "نقش":
#													انتخاب نقش به صورت رَندُم
													for i in range(0, len(extra_list_roles)):
#														حذف نقش انتخاب شده از لیست اصلی برای جلوگیری از تکرار
														rand = random.choice(extra_list_roles)
														newRoles.append(rand)
														extra_list_roles.remove(rand)

													for i in range(0, len(players)):
														t.user_message(players[i], f"{players[i]} در نقش {newRoles[i]}")
														godlist = f"{players[i]} در نقش {newRoles[i]}"
														god_role_list.append(godlist)
													t.user_message(" god", '\n'.join(god_role_list[0:3]))
													t.user_message(" god", '\n'.join(god_role_list[3:6]))
													t.user_message(" god", '\n'.join(god_role_list[6:9]))
													t.user_message(" god", '\n'.join(god_role_list[9:12]))
													t.user_message(" god", '\n'.join(god_role_list[12:15]))
													if len(players) >= 16:
														t.user_message(" god", '\n'.join(god_role_list[15:18]))
													if len(players) >= 19:
														t.user_message(" god", '\n'.join(god_role_list[18:21]))
													if len(players) >= 22:
														t.user_message(" god", '\n'.join(god_role_list[21:25]))
													t.channel_message('پایان ارسال نقش')
													t.change_status(0, 'پایان ارسال نقش')
													t.user_message(" god", 'با ارسال کلمه مافیا مافیاها رو بهم معرفی کنید.')

													@t.subscribe("messagedeliver")
													def mafia_role_sending(server, params):
														if params['type'] != teamtalk.USER_MSG:
															return
														mafia_role_content = params['content']
														mafia_role_user = t.get_user(params["srcuserid"])
														nickname = mafia_role_user["nickname"]
														if mafia_role_user.get('chanid') == int(chanid):
															if nickname == " god" and mafia_role_content == "مافیا":
																#ارسال نقش های مافیا به مافیاها
																doovr = 0
																for i in  newRoles:
																	if i in full_mafia:
																		r_mafia.append(i)
																		p_mafia.append(players[doovr])
																	doovr += 1

																len_p_mafia = len(p_mafia)
																dict1 = {

																}

																tupl_list = []

																for i in range(0, len_p_mafia):
																	list0 = []
																	list0.append(p_mafia[i])
																	list0.append(r_mafia[i])
																	tp = tuple(list0)
																	tupl_list.append(tp)
																	list0.clear

																for p in p_mafia:
																	dict1[p] = []
																	for r in tupl_list:
																		if p in r:
																			continue
																		dict1[p].append(r)

																for key, value in dict1.items():
																	for i in range(0, len_p_mafia - 1):
																		m_role = f"{value[i][0]} در نقش {value[i][1]}"
																		send_to_mafia_players.append(m_role)
																	t.user_message(key, '\n'.join(send_to_mafia_players))
																	send_to_mafia_players.clear()
																	newRoles.clear()
																	players.clear()
																	t.channel_message('مافیا ها بهم معرفی شدند.')
																	t.change_status(0, 'مافیا ها بهم معرفی شدند.')

											else:
												@t.subscribe("messagedeliver")
												def errorContent(server, params):
													if params['type'] != teamtalk.USER_MSG:
														return
													error_content = params['content']
													error_user = t.get_user(params["srcuserid"])
													nickname = error_user["nickname"]
													if error_user.get('chanid') == int(chanid):
														if nickname == " god" and not error_content == "مافیا":
															t.user_message(' god', 'تعداد نقشها با تعداد بازی کنها یکی نیست')
														else:
															pass

						if nickname == " god" and role_question_content == "خیر":
							if len(players) >= 13:
								t.user_message(' god', 'تعداد بازیکنها بیشتر از ۱۲ نفر میباشد.')
							else:
								list_roles = ["پدر خوانده", "دکتر لِکتِر", "مافیای ساده1", "مافیای ساده2", "دکتر", "روانپزشک", "اِسنایپِر یا حرفه ای", "کارآگاه", "شهردار", "جان سخت", "شهروند ساده1", "شهروند ساده2"]
								new_roles =[]
								t.user_message(' god', 'با ارسال کلمه نقش، نقش ها را برای همه ارسال کنید. ')

								@t.subscribe("messagedeliver")
								def constant_role_sending(server, params):
									if params['type'] != teamtalk.USER_MSG:
										return
									constant_role_content = params['content']
									try:
										if len(players) < 12:
											list_roles.remove('شهروند ساده2')
											if len(players) < 11:
												list_roles.remove("مافیای ساده2")
												if len(players) < 10:
													list_roles.remove("شهروند ساده1")
													if len(players) < 9:
														list_roles.remove("مافیای ساده1")
									except:
										pass
									constant_role_user = t.get_user(params["srcuserid"])
									nickname = constant_role_user["nickname"]
									if constant_role_user.get('chanid') == int(chanid):
										if nickname == " god" and constant_role_content == "نقش":
#											انتخاب نقش به صورت رَندُم
											for i in range(0, len(list_roles)):
#												حذف نقش انتخاب شده از لیست اصلی برای جلوگیری از تکرار
												rand = random.choice(list_roles)
												new_roles.append(rand)
												list_roles.remove(rand)

											for i in range(0, len(players)):
												t.user_message(players[i], f"{players[i]} در نقش {new_roles[i]}")
												godlist = f"{players[i]} در نقش {new_roles[i]}"
												god_role_list.append(godlist)
											t.user_message(" god", '\n'.join(god_role_list[0:3]))
											t.user_message(" god", '\n'.join(god_role_list[3:6]))
											t.user_message(" god", '\n'.join(god_role_list[6:9]))
											if len(players) >= 10:
												t.user_message(" god", '\n'.join(god_role_list[9:12]))
											t.channel_message('پایان ارسال نقش')
											t.change_status(0, 'پایان ارسال نقش')
											t.user_message(" god", 'با ارسال کلمه مافیا مافیاها رو بهم معرفی کنید.')

											@t.subscribe("messagedeliver")
											def mafia_role_sending(server, params):
												if params['type'] != teamtalk.USER_MSG:
													return
												mafia_role_content = params['content']
												mafia_role_user = t.get_user(params["srcuserid"])
												nickname = mafia_role_user["nickname"]
												if mafia_role_user.get('chanid') == int(chanid):
													if nickname == " god" and mafia_role_content == "مافیا":
														#ارسال نقش های مافیا به مافیاها
														doovr = 0
														for i in  new_roles:
															if i in full_mafia:
																r_mafia.append(i)
																p_mafia.append(players[doovr])
															doovr += 1

														len_p_mafia = len(p_mafia)
														dict1 = {

														}

														tupl_list = []

														for i in range(0, len_p_mafia):
															list0 = []
															list0.append(p_mafia[i])
															list0.append(r_mafia[i])
															tp = tuple(list0)
															tupl_list.append(tp)
															list0.clear

														for p in p_mafia:
															dict1[p] = []
															for r in tupl_list:
																if p in r:
																	continue
																dict1[p].append(r)

														for key, value in dict1.items():
															for i in range(0, len_p_mafia - 1):
																m_role = f"{value[i][0]} در نقش {value[i][1]}"
																send_to_mafia_players.append(m_role)
															t.user_message(key, '\n'.join(send_to_mafia_players))
															send_to_mafia_players.clear()
															new_roles.clear()
															players.clear()
														t.channel_message('مافیا ها بهم معرفی شدند.')
														t.change_status(0, 'مافیا ها بهم معرفی شدند.')

			@t.subscribe('messagedeliver')
			def roles_list(server, params):
				if params["type"] != teamtalk.USER_MSG:
					return
				roles_list_content = params["content"]
				roles_list_user = t.get_user(params["srcuserid"])
				nickname = roles_list_user["nickname"]
				if roles_list_user.get('chanid') == int(chanid):
					if nickname == " god" and role_content == "rl" or nickname == " god" and role_content == "قم":
						if '\n'.join(god_role_list) == '':
							t.user_message(' god', 'هنوز نقشها تعیین نشده')
						else:
							t.user_message(' god', '\n'.join(god_role_list))

	else:
		t.user_message(role_user, "بیرون از کانال نمیتوانید پیام بدهید.")

@t.subscribe("messagedeliver")
def end(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	end_content = params["content"]
	end_user = t.get_user(params["srcuserid"])
	nickname = end_user["nickname"]
	if end_user.get('chanid') == int(chanid):
		if nickname == " god" and end_content == "f" or nickname == " god" and end_content == "ب":
			t.channel_message('با تشکر از شما بخاطر بازی\nبازی تموم شد.\nبرم واسه بازی بعدی بیام.')
			os.execl(sys.executable, sys.executable, *sys.argv)

@t.subscribe("messagedeliver")
def normal_time(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	def normal_time_end_message():
		normal_time.thread_run = False
		t.channel_message(f"پایان زمان صحبت بازیکن {''.join(timeUserList)} 60 ثانیه")
		t.change_status(0, f"پایان زمان صحبت بازیکن {''.join(timeUserList)} 60 ثانیه")

	normal_time_content = params["content"].lower()
	normal_time_users = t.get_users_in_channel(int(chanid))
	normal_time_user = t.get_user(params['srcuserid'])
	if normal_time_user.get('chanid') == int(chanid):
		for normalUserNumber in numbers:
			if " god" in normal_time_user['nickname'] and not normal_time.thread_run and normal_time_content == f"t {normalUserNumber}" or " god" in normal_time_user['nickname'] and not normal_time.thread_run and normal_time_content == f"ف {normalUserNumber}" or " god" in normal_time_user['nickname'] and not normal_time.thread_run and normal_time_content == f"t{normalUserNumber}" or " god" in normal_time_user['nickname'] and not normal_time.thread_run and normal_time_content == f"ف{normalUserNumber}":
				timeUserList.clear()
				for normal_user in normal_time_users:
					normalUser = normal_user['nickname']
					if normalUserNumber in normalUser:
						t.channel_message(f"شروع زمان صحبت برای {normalUser} 60 ثانیه")
						t.change_status(0, f"شروع زمان صحبت برای {normalUser} 60 ثانیه")
						timeUserList.add(normalUser)

						normal_time.thread = threading.Timer(60, normal_time_end_message)
						normal_time.thread.daemon = True
						normal_time.thread.start()
						normal_time.thread_run = True

			elif " god" in normal_time_user['nickname'] and normal_time.thread_run and normal_time_content == f"t {normalUserNumber}" or " god" in normal_time_user['nickname'] and normal_time.thread_run and normal_time_content == f"ف {normalUserNumber}" or " god" in normal_time_user['nickname'] and normal_time.thread_run and normal_time_content == f"t{normalUserNumber}" or " god" in normal_time_user['nickname'] and normal_time.thread_run and normal_time_content == f"ف{normalUserNumber}":
				t.user_message(' god', '60 ثانیه هنوز تموم نشده\nمیتونی tc بزنی تا لغو بشه')

		if " god" in normal_time_user['nickname'] and normal_time.thread_run and normal_time_content == 'tc' or " god" in normal_time_user['nickname'] and normal_time.thread_run and normal_time_content == 'فز':
			normal_time.thread.cancel()
			normal_time.thread_run = False
			t.channel_message(f"لغو زمان صحبت بازیکن {''.join(timeUserList)} 60 ثانیه")
			t.change_status(0, f"لغو زمان صحبت بازیکن {''.join(timeUserList)} 60 ثانیه")

		elif " god" in normal_time_user['nickname'] and not normal_time.thread_run and normal_time_content == 'tc' or " god" in normal_time_user['nickname'] and not normal_time.thread_run and normal_time_content == 'فز':
			t.user_message(' god', '60 ثانیه فعال نیست.')

normal_time.thread = 't'
normal_time.thread_run = False

@t.subscribe("messagedeliver")
def challenge_time(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	def challenge_time_end_message():
		challenge_time.thread_run = False
		t.channel_message(f"پایان زمان چالش بازیکن {''.join(timeUserList)} 30 ثانیه")
		t.change_status(0, f"پایان زمان چالش بازیکن {''.join(timeUserList)} 30 ثانیه")

	challenge_time_content = params["content"].lower()
	challenge_time_users = t.get_users_in_channel(int(chanid))
	challenge_time_user = t.get_user(params['srcuserid'])
	if challenge_time_user.get('chanid') == int(chanid):
		for normalUserNumber in numbers:
			if " god" in challenge_time_user['nickname'] and not challenge_time.thread_run and challenge_time_content == f"ch {normalUserNumber}" or " god" in challenge_time_user['nickname'] and not challenge_time.thread_run and challenge_time_content == f"زا {normalUserNumber}" or " god" in challenge_time_user['nickname'] and not challenge_time.thread_run and challenge_time_content == f"ch{normalUserNumber}" or " god" in challenge_time_user['nickname'] and not challenge_time.thread_run and challenge_time_content == f"زا{normalUserNumber}":
				timeUserList.clear()
				for normal_user in challenge_time_users:
					normalUser = normal_user['nickname']
					if normalUserNumber in normalUser:
						t.channel_message(f"شروع زمان چالش برای {normalUser} 30 ثانیه")
						t.change_status(0, f"شروع زمان چالش برای {normalUser} 30 ثانیه")
						timeUserList.add(normalUser)

						challenge_time.thread = threading.Timer(30, challenge_time_end_message)
						challenge_time.thread.daemon = True
						challenge_time.thread.start()
						challenge_time.thread_run = True

			elif " god" in challenge_time_user['nickname'] and challenge_time.thread_run and challenge_time_content == f"ch {normalUserNumber}" or " god" in challenge_time_user['nickname'] and challenge_time.thread_run and challenge_time_content == f"زا {normalUserNumber}" or " god" in challenge_time_user['nickname'] and challenge_time.thread_run and challenge_time_content == f"ch{normalUserNumber}" or " god" in challenge_time_user['nickname'] and challenge_time.thread_run and challenge_time_content == f"زا{normalUserNumber}":
				t.user_message(' god', '30 ثانیه هنوز تموم نشده\nمیتونی cc بزنی تا لغو بشه')

		if " god" in challenge_time_user['nickname'] and challenge_time.thread_run and challenge_time_content == "cc" or " god" in challenge_time_user['nickname'] and challenge_time.thread_run and challenge_time_content == "زز":
			challenge_time.thread.cancel()
			challenge_time.thread_run = False
			t.channel_message(f"لغو زمان چالش بازیکن {''.join(timeUserList)} 30 ثانیه.")
			t.change_status(0, f"لغو زمان چالش بازیکن {''.join(timeUserList)} 30 ثانیه.")

		elif " god" in challenge_time_user['nickname'] and not challenge_time.thread_run and challenge_time_content == "cc" or " god" in challenge_time_user['nickname'] and not challenge_time.thread_run and challenge_time_content == "زز":
			t.user_message(' god', '30 ثانیه فعال نیست.')

challenge_time.thread = 'cht'
challenge_time.thread_run = False

@t.subscribe("messagedeliver")
def defense_time(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	def defense_time_end_message():
		defense_time.thread_run = False
		t.channel_message(f"پایان زمان دفاع بازیکن {''.join(timeUserList)} 90 ثانیه.")
		t.change_status(0, f"پایان زمان دفاع بازیکن {''.join(timeUserList)} 90 ثانیه.")

	defense_time_content = params["content"].lower()
	defense_time_users = t.get_users_in_channel(int(chanid))
	defense_time_user = t.get_user(params['srcuserid'])
	if defense_time_user.get('chanid') == int(chanid):
		for normalUserNumber in numbers:
			if " god" in defense_time_user['nickname'] and not defense_time.thread_run and defense_time_content == f"d {normalUserNumber}" or " god" in defense_time_user['nickname'] and not defense_time.thread_run and defense_time_content == f"ی {normalUserNumber}" or " god" in defense_time_user['nickname'] and not defense_time.thread_run and defense_time_content == f"d{normalUserNumber}" or " god" in defense_time_user['nickname'] and not defense_time.thread_run and defense_time_content == f"ی{normalUserNumber}":
				timeUserList.clear()
				for normal_user in defense_time_users:
					normalUser = normal_user['nickname']
					if normalUserNumber in normalUser:
						t.channel_message(f"شروع زمان دفاع برای {normalUser} 90 ثانیه.")
						t.change_status(0, f"شروع زمان دفاع برای {normalUser} 90 ثانیه.")
						timeUserList.add(normalUser)

						defense_time.thread = threading.Timer(90, defense_time_end_message)
						defense_time.thread.daemon = True
						defense_time.thread.start()
						defense_time.thread_run = True

			elif " god" in defense_time_user['nickname'] and defense_time.thread_run and defense_time_content == f"d {normalUserNumber}" or " god" in defense_time_user['nickname'] and defense_time.thread_run and defense_time_content == f"ی {normalUserNumber}" or " god" in defense_time_user['nickname'] and defense_time.thread_run and defense_time_content == f"d{normalUserNumber}" or " god" in defense_time_user['nickname'] and defense_time.thread_run and defense_time_content == f"ی{normalUserNumber}":
				t.user_message(' god', '90 ثانیه هنوز تموم نشده\nمیتونی dc بزنی تا لغو بشه')

		if " god" in defense_time_user['nickname'] and defense_time.thread_run and defense_time_content == "dc" or " god" in defense_time_user['nickname'] and defense_time.thread_run and defense_time_content == "یز":
			defense_time.thread.cancel()
			defense_time.thread_run = False
			t.channel_message(f"لغو زمان دفاع بازیکن {''.join(timeUserList)} 90 ثانیه.")
			t.change_status(0, f"لغو زمان دفاع بازیکن {''.join(timeUserList)} 90 ثانیه.")

		elif  " god" in defense_time_user['nickname'] and not defense_time.thread_run and defense_time_content == "dc" or " god" in defense_time_user['nickname'] and not defense_time.thread_run and defense_time_content == "یز":
			t.user_message(' god', '90 ثانیه فعال نیست.')

defense_time.thread = 'd'
defense_time.thread_run = False

@t.subscribe("messagedeliver")
def normal_vote(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	def normal_vote_end_message():
		normal_vote.thread_run = False
		if len(normal_votelists) == 0:
			t.channel_message(f"{''.join(normal_voteUserList)} {len(normal_votelists)} رأی.")
			t.user_message(' god', f"{''.join(normal_voteUserList)} {len(normal_votelists)} رأی.")
			t.change_status(0, f"{''.join(normal_voteUserList)} {len(normal_votelists)} رأی.")
		else:
			t.channel_message(f"{''.join(normal_voteUserList)} {len(normal_votelists)} رأی.\nآرا: {' '.join(normal_votelists)}")
			t.user_message(' god', f"{''.join(normal_voteUserList)} {len(normal_votelists)} رأی.\nآرا: {' '.join(normal_votelists)}")
			t.change_status(0, f"{''.join(normal_voteUserList)} {len(normal_votelists)} رأی.\nآرا: {' '.join(normal_votelists)}")

	normal_vote_content = params["content"].lower()
	normal_vote_users = t.get_users_in_channel(int(chanid))
	normal_vote_user = t.get_user(params['srcuserid'])
	if normal_vote_user.get('chanid') == int(chanid):
		for normalVoteUserNumber in numbers:
			if "god" in normal_vote_user['nickname'] and not normal_vote.thread_run and normal_vote_content == f"v {normalVoteUserNumber}" or "god" in normal_vote_user['nickname'] and not normal_vote.thread_run and normal_vote_content == f"ر {normalVoteUserNumber}" or "god" in normal_vote_user['nickname'] and not normal_vote.thread_run and normal_vote_content == f"v{normalVoteUserNumber}" or "god" in normal_vote_user['nickname'] and not normal_vote.thread_run and normal_vote_content == f"ر{normalVoteUserNumber}":
				normal_votelists.clear()
				normal_voteUserList.clear()
				for vote_user in normal_vote_users:
					voteUser = vote_user['nickname']
					if normalVoteUserNumber in voteUser:
						t.channel_message(f"شروع رأی گیری {voteUser}")
						t.change_status(0, f"شروع رأی گیری {voteUser}")
						normal_voteUserList.add(voteUser)

						normal_vote.thread = threading.Timer(4, normal_vote_end_message)
						normal_vote.thread.daemon = True
						normal_vote.thread.start()
						normal_vote.thread_run = True

				@t.subscribe("messagedeliver")
				def vote(server, params):
					if params["type"] != teamtalk.CHANNEL_MSG:
						return

					hwnd = win32gui.GetForegroundWindow()
					win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

					channel_user = t.get_user(params['srcuserid'])
					new_user = channel_user['nickname']
					if new_user:
						for vote_user_number in numbers:
							if vote_user_number in new_user:
								normal_votelists.add(new_user)

normal_vote.thread = 'nv'
normal_vote.thread_run = False

@t.subscribe("messagedeliver")
def hidden_vote(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	def hidden_vote_end_message():
		hidden_vote.thread = False
		if len(hidden_votelists) == 0:
			t.user_message(' god', f"{''.join(hidden_voteUserList)} {len(hidden_votelists)} رأی.")
			t.channel_message(f"پایان رأی مخفی {''.join(hidden_voteUserList)}")
			t.change_status(0, f"پایان رأی مخفی {''.join(hidden_voteUserList)}")
			god_vote_list = f"{''.join(hidden_voteUserList)} {len(hidden_votelists)} رأی."
			hidden_vote_list_result.append(''.join(god_vote_list))
		else:
			t.user_message(' god', f"{''.join(hidden_voteUserList)} {len(hidden_votelists)} رأی.\nآرآ: {''.join(hidden_votelists)}")
			t.channel_message(f"پایان رأی مخفی {''.join(hidden_voteUserList)}")
			t.change_status(0, f"پایان رأی مخفی {''.join(hidden_voteUserList)}")
			god_vote_list = f"{''.join(hidden_voteUserList)} {len(hidden_votelists)} رأی."
			hidden_vote_list_result.append(''.join(god_vote_list))

	hidden_vote_content = params["content"].lower()
	hidden_vote_users = t.get_users_in_channel(int(chanid))
	hidden_vote_user = t.get_user(params['srcuserid'])
	if hidden_vote_user.get('chanid') == int(chanid):
		if "god" in hidden_vote_user['nickname'] and hidden_vote_content == "مخفی":
			t.user_message(' god', 'شماره بازیکنهایی که اومدن تو رأی مخفی با گذاشتن فاصله بینشون وارد کنید\nاین کار رو واسه اینکه به هم دیگه نتونن رأی بِدَن انجام میدی.\nبعدش شماره نفر اول رو وارد بکن و بهمین ترتیب ادامه بده.')

		if "god" in hidden_vote_user['nickname'] and hidden_vote_content:
			for i in hidden_vote_content.split():
				if i == "start":
					continue
				if  i == "مخفی":
					continue
				if  i == "h":
					continue
				hidden_main_votelists.append(i)

		for voteUserNumber in numbers:
			if "god" in hidden_vote_user['nickname'] and hidden_vote_content == voteUserNumber:
				hidden_votelists.clear()
				hidden_voteUserList.clear()
				for vote_user in hidden_vote_users:
					voteUser = vote_user['nickname']
					if voteUserNumber in voteUser:
						t.channel_message(f"شروع رأی مخفی {voteUser}")
						t.change_status(0, f"شروع رأی مخفی {voteUser}")
						hidden_voteUserList.add(voteUser)
						hidden_main_votelists.append(voteUser)

						hidden_vote.thread = threading.Timer(6, hidden_vote_end_message)
						hidden_vote.thread.daemon = True
						hidden_vote.thread.start()
						hidden_vote.thread_run = True

				@t.subscribe("messagedeliver")
				def hidden_vote_collection(server, params):
					if params["type"] != teamtalk.USER_MSG:
						return
					channel_user = t.get_user(params['srcuserid'])
					new_user = channel_user['nickname']
					if new_user:
						for vote_user_number in numbers:
							if vote_user_number in new_user:
								if not new_user in hidden_main_votelists:
									hidden_votelists.add(new_user)
									hidden_main_votelists.append(new_user)

		if "god" in hidden_vote_user['nickname'] and hidden_vote_content == "hv" or "god" in hidden_vote_user['nickname'] and hidden_vote_content == "ار":
			t.channel_message('\n'.join(hidden_vote_list_result))
			t.change_status(0, '\n'.join(hidden_vote_list_result))
			hidden_main_votelists.clear()

hidden_vote.thread = 'hv'
hidden_vote.thread_run = False

def card_selection():
	#با یه حلقه تمام کارتها را بصورت رندوم به لیست کارتهای جدید اضافه میکنیم
	for i in range(0, len(card_name)):
		rand_card = random.choice(card_name)
		#برای جلوگیری از تکرار کارت انتخاب شده تصادفی رو از لیست حذف میکنیم
		card_name.remove(rand_card)
		return rand_card

@t.subscribe("messagedeliver")
def card(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	card_content = params["content"]
	card_user = t.get_user(params["srcuserid"])
	nickname = card_user["nickname"]
	if card_user.get('chanid') == int(chanid):
		if nickname == " god" and card_content == 'c' or nickname == " god" and card_content == 'ز':
			t.user_message(' god', 'شماره کارت را داخل کانال وارد کنید')

			@t.subscribe('messagedeliver')
			def Card_list(server, params):
				if params['type'] != teamtalk.USER_MSG:
					return
				card_list_content = params["content"]
				card_list_user = t.get_user(params["srcuserid"])
				nickname = card_list_user["nickname"]
				if card_list_user.get('chanid') == int(chanid):
					if nickname == " god" and card_list_content == "cl" or nickname == " god" and card_list_content == "زم":
						t.channel_message(f"کارتهای مانده {' '.join(card_number)}")
						t.channel_message(f"نام کارتها {' '.join(card_name)}")

			@t.subscribe('messagedeliver')
			def Card_number(server, params):
				if params['type'] != teamtalk.CHANNEL_MSG:
					return
				card_number_content = params["content"]
				card_user = t.get_user(params["srcuserid"])
				nickname = card_user["nickname"]
				if card_user.get('chanid') == int(chanid):
					if len(card_number_content) == 1:
						for cardNumberList in card_number:
							if cardNumberList in card_number_content:
								if nickname == ' god':
									t.channel_message(f' کارت انتخاب شده: {card_selection()}')
									card_number.remove(cardNumberList)

@t.subscribe("messagedeliver")
def help(server, params):
	if params["type"] != teamtalk.USER_MSG:
		return
	help_content = params["content"]
	help_user = t.get_user(params["srcuserid"])
	nickname = help_user["nickname"]
	if help_user.get('chanid') == int(chanid):
		if help_content == "help" or help_content == "راهنما":
			t.user_message(help_user, 'نویسندگان ربات: روهان کمالیان, فرهاد محمدی, یلدا حسنپور, حمید رضائی\nگاد بازی باید اول اسمش فاصله بزنه و بعد کلمه god رو بنویسه\nstart/شروع: شروع نقشدهی\nrl/قم: ارسال نقشها به گاد.\nf/ب: پایان بازی و راه اندازی مجدد ربات\nb/ذ: ارسال broadcast در صورت فعال بودن برای id\nc/ز: شروع کارتهای بازی\ncl/زم: ارسال لیست کارتها در کانال\nv/ر شماره بازیکن: شروع رأی گیری معمولی.')
			t.user_message(help_user, 'مخفی: شروع رأی گیری مخفی.\nhv/ار: ارسال نتیجه ی رأی گیری مخفی در کانال.\nt/ف شماره بازیکن: شروع زمان صحبت معمولی.\ntc/فز: لغو زمان صحبت معمولی.\nch/زا شماره بازیکن: شروع زمان چالش.\ncc/زز: لغو زمان چالش.\nd/ی شماره بازیکن: شروع زمان دفاع.\ndc/یز: لغو زمان دفاع.\nhelp/راهنما: راهنمای ربات.')

def Login():
	global chanid
	if not os.path.exists('config.ini'):
		hostAddress = input('آدرس سِروِر را وارد کنید.')
		tcpport = input('tcp پورت سِروِر را وارد کنید')
		channelID = input('id کانال را وارد نمایید.')
		username = input('نام کاربری را وارد کنید')
		password = input('رمز عبور را وارد کنید')
		nickname = input('اسم مستعار یا nickname را وارد کنید')
		client_name = input('نام سِروِر را وارد کنید.')
		config_file = f"""
[options]
hostAddress = {hostAddress}
tcpport = {tcpport}
channel_id = {channelID}
username = {username}
password = {password}
nickname = {nickname}
clientName = {client_name}
"""

		file_creation = open('config.ini', 'x', encoding = 'utf-8-sig')
		file_creation .write(config_file)
		print('فایل کانفیگ با موفقیت ساخته شد برنامه را با زدن اینتر بسته و مجددا راه اندازی نمایید.')
		input()
	else:
		try:
			config = configparser.ConfigParser()
			loaded = config.read('config.ini', encoding = 'utf-8-sig')
			host = config['options']['hostAddress']
			tcp = config['options']['tcpport']
			chanid = config['options']['channel_id']
			username = config['options']['username']
			password = config['options']['password']
			nickname = config['options']['nickname']
			clientName = config['options']['clientName']
			t.set_connection_info(host, tcp)
			t.connect()
			t.login(nickname, username, password, clientName)
			t.join(int(chanid))
			t.change_status(0, 'با ارسال کلمه help راهنمای ربات رو میتونید بخونید.')
			print('برنامه در حال اجرا میباشد.\r\nورژن 2.0')
			try:
				t.handle_messages(timeout = 1)
			except teamtalk.TeamTalkError:
				if role_content == 'b' or role_content == 'ذ':
					t.user_message(' god', 'امکان broadcast برای این id فعال نیست pv رو ببند دوباره باز کن.')
					Login()
				else:
					t.user_message(' god', 'ببخش که خطا میدم باید برم بیام اما حافظم پاک نشده فقط باید pv رو ببندی دوباره باز بکنی.')
					Login()
			except TypeError:
				t.user_message(' god', 'ببخش که خطا میدم باید برم بیام اما حافظم پاک نشده فقط باید pv رو ببندی دوباره باز بکنی.')
				Login()
			except UnicodeDecodeError: 
				t.user_message(' god', 'ببخش که خطا میدم باید برم بیام اما حافظم پاک نشده فقط باید pv رو ببندی دوباره باز بکنی.')
				Login()
		except KeyError:
			print('مشکلی در فایل کانفیگ وجود دارد فایل کانفیگ را پاک کرده برنامه را مجددا راه اندازی نمایید.')
			input()

Login()