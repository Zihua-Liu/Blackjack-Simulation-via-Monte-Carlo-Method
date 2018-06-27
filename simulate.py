import numpy as np
import random

def sum_cards(hand):
	aces = False
	aces_locs = []
	sum_ = 0

	if len(hand) == 2:
		sum_ = hand[0] + hand[1]
		return sum_

	for k in range(len(hand)):
		if hand[k] == 11:
			aces = True
			aces_locs.append(k)

	if aces == False:
		for i in hand:
			sum_ = sum_ + i
		return sum_

	not_aces = []
	for card in hand:
		if card != 11:
			not_aces.append(card)
	sum_ = sum(not_aces)

	if sum_ > 10:
		for i in aces_locs:
			sum_ = sum_ + 1
		return sum_

	if sum_ <= 9 and len(aces_locs) > 1:
		sum_ = sum_ + 11
		for i in range(len(aces_locs)):
			sum_ = sum_ + 1
		return sum_

	if sum_ == 10 and len(aces_locs) == 1:
		sum_ = sum_ + 11
		return sum_
	else:
		for i in range(len(aces_locs)):
			sum_ = sum_ + 1
		return sum_

def player_h(p_hand, cards, i, p_stand):
	ncards = len(cards)
	stand = False

	while stand != True:
		current = sum_cards(p_hand)

		if i == ncards - 1:
			stand = True
		elif current < p_stand:
			i = i + 1
			p_hand.append(cards[i])
		else:
			stand = True

	return [current, i]

def dealer_h(d_hand, cards, i):
	ncards = len(cards)
	stand = False

	while stand != True:
		current = sum_cards(d_hand)

		if i == ncards - 1:
			stand = True
		elif current <= 16:
			i = i + 1
			d_hand.append(cards[i])
		else:
			stand = True
	return [current, i]

def play_bj(cards, bet, p_stand):
	ncards = len(cards)

	i = -1

	winings = 0

	while i < ncards - 1:
		if i < ncards - 4:
			i = i + bet
			p_hand = [cards[i - 1], cards[i]]

			i = i + bet
			d_hand = [cards[i - 1], cards[i]]

		else:
			return winings

		p_res = player_h(p_hand, cards, i, p_stand)

		i = p_res[1]

		if p_res[0] <= 21:
			d_res = dealer_h(d_hand, cards, i)

			i = d_res[1]

		if p_res[0] > 21:
			winings = winings - bet
		elif d_res[0] > 21:
			winings = winings + bet
		elif p_res[0] > d_res[0]:
			winings = winings + bet
		elif p_res[0] < d_res[0]:
			winings = winings - bet
	return winings

if __name__ == "__main__":
	
	N = 12
	bet = 2
	p_stand = [16]
	deck = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
	deck = deck.repeat(4)
	two_d = deck.repeat(2)
	res = []
	"""
	for i in range(N):
		s_decks = two_d
		random.shuffle(s_decks)
		res.append(play_bj(s_decks, bet, p_stand))
	print("Average Winnings per Hand = " + str(np.array(res).mean()))
	"""
	iters = 1000
	"""
	res2 = []
	for k in range(iters):
		for i in range(N):
			s_decks = two_d
			random.shuffle(s_decks)
			res.append(play_bj(s_decks, bet, p_stand))
		res2.append(np.array(res).mean())
	"""

	playw = []
	p_stand = [11]
	res = []
	res2 = []
	for z in range(10):
		res4 = []
		for k in range(iters):
			print("Standing by " + str(11 + z) + " simulating round " + str(k))
			for i in range(N):
				s_decks = two_d
				random.shuffle(s_decks)
				res.append(play_bj(s_decks, bet, p_stand))
			res4.append(np.array(res).mean())
		playw.append(np.array(res4).mean())
		p_stand[0] = p_stand[0] + 1
	
	print("------------------------------------------------------------")
	for i in range(len(playw)):
		print("The average loss of standing by " + str(11 + i) + " is " + str(playw[i]))












































