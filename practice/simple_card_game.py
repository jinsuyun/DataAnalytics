import random

def draw_a_card(card_list):
    '''
    전체 카드의 리스트를 argument로 받음
    카드 리스트에서 임의의 카드 한장을 뽑고 이를 리스트에서 지움
    random.randint() 함수 활용, list 내장함수 pop() 활용
    :return: 뽑은 카드 값
    '''
    random_index = random.randint(0, len(card_list) - 1)  # 56장의 카드에서 랜덤하게 1장을 뽑음
    a_card = card_list.pop(random_index)

    return a_card

def get_score(card_list,owner):
    '''
    가지고 있는 카드들의 리스트를 argument로 받음
    카드 소유주를 나타내는 문자열을 argument로 받음
    합계 점수를 계산, sum() 함수 활용
    현재 보유중인 카드 리스트를 출력
    점수 합산 결과를 카드 소유주가 누구인지와 함께 출력 (print)
    :return: 계산된 합계 점수
    '''
    value_sum=sum(card_list)
    print(card_list)
    print("score of %s: %d" %(owner,value_sum))
    return value_sum


def print_result(my_score,dealer_score):
    '''
    나의 점수와 딜러의 점수를 arguments로 받음
    대소 비교를 통해 결과를 출력 (print)
    :return: None
    '''
    if my_score>dealer_score:
        print("Win")
    elif dealer_score>my_score:
        print("Lose")
    else :
        print("Draw")

    pass

cards = list(range(1, 14)) * 4 #카드 56장 생성 1~14까지 하트, 클로버, 다이아, 스페이스
my_cards, dealer_cards = [], []#나의 리스트와 딜러의 카드 리스트 생성

for i in range(2):
    my_cards.append(draw_a_card(cards))#카드를 드로우한다
    dealer_cards.append(draw_a_card(cards))#딜러의 카드를 드로우한다

my_sum = get_score(my_cards, 'me')
dealer_sum = get_score(dealer_cards, 'dealer')

print_result(my_sum, dealer_sum)


